# https://realpython.com/python-redis/

# Example: PyHats.com

# It’s time to break out a fuller example.
# Let’s pretend we’ve decided to start a lucrative website, PyHats.com,
# that sells outrageously overpriced hats to anyone who will buy them, and hired you to build the site.

# You’ll use Redis to handle some of the product catalog, inventorying, and bot traffic detection
# for PyHats.com.

# It’s day one for the site, and we’re going to be selling three limited-edition hats.
# Each hat gets held in a Redis hash of field-value pairs, and the hash has a key
# that is a prefixed random integer , such as hat:56854717.
# Using the -- hat: prefix -- is Redis convention for creating a sort of namespace within a Redis database:

import logging
import random
import redis

random.seed(444)
hats = {f"hat:{random.getrandbits(32)}": i for i in (
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1000,
        "npurchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "npurchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "npurchased": 0,
    })
}

# Let’s start with database 1 since we used database 0 in a previous example:

r = redis.Redis(db=1)
print(r.__dict__['connection_pool'])

# To do an initial write of this data into Redis, we can use .hset() (hash-set) with mapping=hat,
# calling it for each dictionary:
# With a pipeline, all the commands are buffered on the client side and then sent at once,
# in one fell swoop, using pipe.hset()

with r.pipeline() as pipe:
    for h_id, hat in hats.items():
        pipe.hset(h_id, mapping=hat)
        pipe.execute()

r.bgsave()  # Redis BGSAVE command saves the DB in the background.

# Let’s do a quick check that everything is there in our Redis database:

hats_keys = list()

for key in r.keys():
    k = key.decode('utf-8')
    hats_keys.append(k)
    print(k, "=\n", r.hgetall(k))

print(hats_keys)

# The first thing that we want to simulate is what happens when a user clicks Purchase.
# If the item is in stock, increase its npurchased by 1 and decrease its quantity (inventory) by 1.
# You can use .hincrby() to do this:

r.hincrby("hat:56854717", "quantity", -1)
r.hincrby("hat:56854717", "npurchased", 1)

print("\none hat sold:\n", r.hgetall("hat:56854717"))

# Note: HINCRBY still operates on a hash value that is a string, but it tries to interpret the string
# as a base-10 64-bit signed integer to execute the operation.

# This applies to other commands related to incrementing and decrementing for other data structures,
# namely INCR, INCRBY, INCRBYFLOAT, ZINCRBY, and HINCRBYFLOAT.
# You’ll get an error if the string at the value can’t be represented as an integer.


# It isn’t really that simple, though.
# Changing the quantity and npurchased in two lines of code hides the reality
# that a click, purchase, and payment entails more than this.
# We need to do a few more checks to make sure we don’t leave someone with a lighter wallet and no hat:

# Step 1: Check if the item is in stock, or otherwise raise an exception on the backend.
# Step 2: If it is in stock, then execute the transaction, decrease the quantity field, and increase the npurchased field.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Step 3: Be alert for any changes that alter the inventory in between the first two steps
# (a race condition).
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# Step 1 is relatively straightforward:
# it consists of an .hget() to check the available quantity.

# Step 2 is a little bit more involved.
# The pair of increase and decrease operations need to be executed atomically:
# either both should be completed successfully, or neither should be
# (in the case that at least one fails).

# With client-server frameworks, it’s always crucial to pay attention to atomicity
# and look out for what could go wrong in instances where multiple clients are trying
# to talk to the server at once. The answer to this in Redis is to use a transaction block,
# meaning that either both or neither of the commands get through.

# In redis-py, Pipeline is a transactional pipeline class by default.
# This means that, even though the class is actually named for something else (pipelining),
# it can be used to create a transaction block also.

# In Redis, a transaction starts with MULTI and ends with EXEC:

# 127.0.0.1:6379> MULTI
# 127.0.0.1:6379> HINCRBY 56854717 quantity -1
# 127.0.0.1:6379> HINCRBY 56854717 npurchased 1
# 127.0.0.1:6379> EXEC

# MULTI (Line 1) marks the start of the transaction, and EXEC (Line 4) marks the end.
# Everything in between is executed as one all-or-nothing buffered sequence of commands.
# This means that it will be impossible to decrement quantity (Line 2) but then have
# the balancing npurchased increment operation fail (Line 3).

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Let’s circle back to Step 3: we need to be aware of any changes that alter the inventory
# in between the first two steps.

# Step 3 is the trickiest.
# Let’s say that there is one lone hat remaining in our inventory.
# In between the time that User A checks the quantity of hats remaining
# and actually processes their transaction,
# User B also checks the inventory and finds likewise that there is one hat listed in stock.
# Both users will be allowed to purchase the hat, but we have 1 hat to sell, not 2,
# so we’re on the hook and one user is out of their money.
# Not good.

# Redis has a clever answer for the dilemma in Step 3: it’s called optimistic locking,
# and is different than how typical locking works in an RDBMS such as PostgreSQL.

# Optimistic locking, in a nutshell, means that the calling function (client) does not acquire a lock,
# but rather monitors for changes in the data it is writing to during the time it would have held a lock.
# If there’s a conflict during that time, the calling function simply tries the whole process again.

# You can effect optimistic locking by using the WATCH command (.watch() in redis-py),
# which provides a check-and-set behavior.

# Let’s introduce a big chunk of code and walk through it afterwards step by step.
# You can picture buyitem() as being called any time a user clicks on a Buy Now or Purchase button.

# Its purpose is to confirm the item is in stock and take an action based on that result,
# all in a safe manner that looks out for race conditions and retries if one is detected:


logging.basicConfig()


class OutOfStockError(Exception):
    """Raised when PyHats.com is all out of today's hottest hat"""


def buyitem(r: redis.Redis, itemid: int) -> None:
    with r.pipeline() as pipe:
        error_count = 0
        while True:
            try:
                # Get available inventory, watching for changes
                # related to this itemid before the transaction
                pipe.watch(itemid)
                nleft: bytes = r.hget(itemid, "quantity")
                if nleft > b"0":
                    pipe.multi()
                    pipe.hincrby(itemid, "quantity", -1)
                    pipe.hincrby(itemid, "npurchased", 1)
                    pipe.execute()
                    break
                else:
                    # Stop watching the itemid and raise to break out
                    pipe.unwatch()
                    raise OutOfStockError(
                        f"Sorry, {itemid} is out of stock!"
                    )
            except redis.WatchError:
                # Log total num. of errors by this user to buy this item,
                # then try the same process again of WATCH/HGET/MULTI/EXEC
                error_count += 1
                logging.warning(
                    "WatchError #%d: %s; retrying",
                    error_count, itemid
                )
    return None


# One key here is in understanding the difference between client-side and server-side operations:

#       nleft = r.hget(itemid, "quantity")

# This Python assignment brings the result of r.hget() client-side.
# Conversely, methods that you call on pipe effectively buffer all of the commands into one,
# and then send them to the server in a single request:

# pipe.multi()
# pipe.hincrby(itemid, "quantity", -1)
# pipe.hincrby(itemid, "npurchased", 1)
# pipe.execute()

# No data comes back to the client side in the middle of the transactional pipeline.
# You need to call .execute() (Line 19) to get the sequence of results back all at once.

# Even though this block contains two commands, it consists of exactly one round-trip operation
# from client to server and back.

# This means that the client can’t immediately use the result of pipe.hincrby(itemid, "quantity", -1),
# from Line 20, because methods on a Pipeline return just the pipe instance itself.
# We haven’t asked anything from the server at this point.
# While normally .hincrby() returns the resulting value, you can’t immediately reference it
# on the client side until the entire transaction is completed.

# Here’s an illustration.
# Keep in mind that our starting quantity is 199 for hat 56854717 since we called .hincrby() above.
# Let’s mimic 3 purchases, which should modify the quantity and npurchased fields:

buyitem(r, "hat:56854717")
buyitem(r, "hat:56854717")
buyitem(r, "hat:56854717")
print("3 hats sold\n", r.hmget("hat:56854717", "quantity", "npurchased"))

# Now, we can fast-forward through more purchases, mimicking a stream of purchases
# until the stock depletes to zero. Again, picture these coming from a whole bunch of different clients
# rather than just one Redis instance:

# Buy remaining 196 hats for item 56854717 and deplete stock to 0
for _ in range(196):
    buyitem(r, "hat:56854717")

print("196 hats sold\n", r.hmget("hat:56854717", "quantity", "npurchased"))

buyitem(r, "hat:56854717")
# Now, when some poor user is late to the game, they should be met with an OutOfStockError
# that tells our application to render an error message page on the frontend:
