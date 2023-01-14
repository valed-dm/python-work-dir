# Using redis-py: Redis in Python
# Now that you’ve mastered some basics of Redis, it’s time to jump into redis-py, the Python client that lets you talk to Redis from a user-friendly Python API.

# Remove ads
# First Steps
# redis-py is a well-established Python client library that lets you talk to a Redis server directly through Python calls:

# $ python -m pip install redis
# Next, make sure that your Redis server is still up and running in the background. You can check with pgrep redis-server, and if you come up empty-handed, then restart a local server with redis-server /etc/redis/6379.conf.

# Now, let’s get into the Python-centric part of things. Here’s the “hello world” of redis-py:

import random
import datetime
import redis

r = redis.Redis(db=0)

print(r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"}))
print(r.get("Bahamas"))  # is Python’s bytes type, not str
r.mset({"100": "200"})
print(r.get("100"))  # is Python’s bytes type, not str
print(r.get("100").decode("utf-8"))

# This also means that HGETALL becomes r.hgetall(), PING becomes r.ping(), and so on.
# There are a few exceptions, but the rule holds for the large majority of commands.

# Redis, used in Line 15, is the central class of the package and the workhorse
# by which you execute (almost) any Redis command. The TCP socket connection and reuse
# is done for you behind the scenes, and you call Redis commands
# using methods on the class instance r.

print(80*"-")
print(r.__dict__.keys())
# print(r.__dict__.values())
print(r.__dict__['connection_pool'])
print("connection", r.__dict__['connection'])
# for el in r.__dict__['response_callbacks']:
#     print(el)
print(80*"-")
# The db parameter is the database number.
# You can manage multiple databases in Redis at once, and each is identified by an integer.
# The max number of databases is 16 by default.

# When you run just redis-cli from the command line, this starts you at database 0.
# Use the -n flag to start a new database, as in redis-cli -n 5.


# Allowed Key Types

# One thing that’s worth knowing is that redis-py requires that you pass it keys
# that are bytes, str, int, or float. (It will convert the last 3 of these types to bytes
# before sending them off to the server.)

# Consider a case where you want to use calendar dates as keys:

today = datetime.date.today()
visitors = {"dan", "jon", "alex"}
# r.sadd(today, *visitors)

#       Traceback (most recent call last):
#       ...
#       redis.exceptions.DataError: Invalid input of type: 'date'.
#       Convert to a byte, string or number first.


# You’ll need to explicitly convert the Python date object to str, which you can do with .isoformat():

stoday = today.isoformat()  # Python 3.7+, or use str(today)
print(stoday)
r.sadd(stoday, *visitors)  # sadd: set-add
# {b'dan', b'alex', b'jon'} Returns all the members of the set value stored at key.
print(r.smembers(stoday))
for el in r.smembers(stoday):
    print(el.decode('utf-8'), end=" ")
# Redis SCARD command is used to return the number of elements stored in a set.
print(f"\n{r.scard(today.isoformat())}")

# To recap, Redis itself only allows strings as keys.
# redis-py is a bit more liberal in what Python types it will accept,
# although it ultimately converts everything to bytes before sending them off to a Redis server.

print(80*"-")
# a random number with 4 bits
print(random.getrandbits(4))
# a random number with 16 bits
print(random.getrandbits(16))
print(random.getrandbits(32))

print(80*"-")

print(r.keys())

vis = list()
for key in r.keys():
    vis.append([key.decode('utf-8'), r.type(key).decode('utf-8')])
    if r.type(key).decode('utf-8') == "string":
        print(r.get(key.decode('utf-8')))
    elif r.type(key).decode('utf-8') == "set":
        print(r.smembers(key.decode('utf-8')))

print(vis)
