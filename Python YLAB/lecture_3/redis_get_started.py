# https://realpython.com/python-redis/

# redis-cli config get dir
# redis-cli --version
# redis-cli info
# ls -hFG /usr/local/bin/redis-* | sort
# executable:/usr/local/opt/redis/bin/redis-server
# config_file:/usr/local/etc/redis.conf

# Getting Started

# Redis has a client-server architecture and uses a request-response model.
# This means that you (the client) connect to a Redis server through TCP connection,
# on port 6379 by default.
# You request some action (like some form of reading, writing, getting, setting, or updating),
# and the server serves you back a response.

# Enter redis-cli on your command line.
# Redis commands are case-insensitive.
# 127.0.0.1:6379> PING
# PONG

# As another sanity check, you can search for the process ID of the Redis server with pgrep:
# $ pgrep redis-server
# 26983

# To kill the server, use pkill redis-server from the command line.
# On Mac OS X, you can also use redis-cli shutdown.


# Redis as a Python Dictionary

# Redis stands for Remote Dictionary Service.

# “You mean, like a Python dictionary?” you may ask.
# Yes. Broadly speaking, there are many parallels you can draw between a Python dictionary
# (or generic hash table) and what Redis is and does:

# A Redis database holds key:value pairs and supports commands such as GET, SET, and DEL,
# as well as several hundred additional commands.

# Redis keys are always strings.

# Redis values may be a number of different data types.
# We’ll cover some of the more essential value data types in this tutorial:
# string, list, hashes, and sets.
# Some advanced types include geospatial items and the new stream type.

# Many Redis commands operate in constant O(1) time,
# just like retrieving a value from a Python dict or any hash table.


# 127.0.0.1:6379> SET Bahamas Nassau
# OK
# 127.0.0.1:6379> SET Croatia Zagreb
# OK
# 127.0.0.1:6379> GET Croatia
# "Zagreb"
# 127.0.0.1:6379> GET Japan
# (nil)

capitals = {}
capitals["Bahamas"] = "Nassau"
capitals["Croatia"] = "Zagreb"

# We use capitals.get("Japan") rather than capitals["Japan"] because Redis will return nil
# rather than an error when a key is not found, which is analogous to Python’s None.

print(capitals.get("Croatia"))
print(capitals.get("Japan"))
print(capitals)


# Redis also allows you to set and get multiple key-value pairs in one command,
# MSET and MGET, respectively:

# 127.0.0.1:6379> MSET Lebanon Beirut Norway Oslo France Paris
# OK
# 127.0.0.1:6379> MGET Lebanon Norway Bahamas
# 1) "Beirut"
# 2) "Oslo"
# 3) "Nassau"

# The closest thing in Python is with dict.update():
capitals.update({
    "Lebanon": "Beirut",
    "Norway": "Oslo",
    "France": "Paris",
})
# ['Beirut', 'Oslo', 'Nassau']
print([capitals.get(k) for k in ("Lebanon", "Norway", "Bahamas")])
for el in (capitals.__getitem__(c) for c in capitals):
    print(el)


# As a third example, the EXISTS command does what it sounds like, which is to check if a key exists:
# 127.0.0.1:6379> EXISTS Norway
# (integer) 1
# 127.0.0.1:6379> EXISTS Sweden
# (integer) 0

# Python has the in keyword to test the same thing, which routes to dict.__contains__(key):
print(capitals.keys())
print("Norway" in capitals)
print("Sweden" in capitals)


# Note:
# Redis commands: SET GET MSET MGET EXISTS

# The Python Redis client library, redis-py, that you’ll dive into shortly in this article,
# does things differently. It encapsulates an actual TCP connection to a Redis server and sends
# raw commands, as bytes serialized using the REdis Serialization Protocol (RESP), to the server.
# It then takes the raw reply and parses it back into a Python object such as bytes, int,
# or even datetime.datetime.

# Note: So far, you’ve been talking to the Redis server through the interactive redis-cli REPL.
# You can also issue commands directly, in the same way that you would pass the name of a script
# to the python executable, such as python myscript.py.

# So far, you’ve seen a few of Redis’ fundamental data types, which is a mapping of string:string.
# While this key-value pair is common in most key-value stores, Redis offers a number of other
# possible value types, which you’ll see next.


# More Data Types in Python vs Redis
# Before you fire up the redis-py Python client, 
# it also helps to have a basic grasp on a few more Redis data types. 
# To be clear, all Redis keys are strings. It’s the value that can take on data types (or structures) 
# in addition to the string values used in the examples so far.

# A hash is a mapping of string:string, called field-value pairs, that sits under one top-level key:

# 127.0.0.1:6379> HSET realpython url "https://realpython.com/"
# (integer) 1
# 127.0.0.1:6379> HSET realpython github realpython
# (integer) 1
# 127.0.0.1:6379> HSET realpython fullname "Real Python"
# (integer) 1

# This sets three field-value pairs for one key, "realpython". 
# If you’re used to Python’s terminology and objects, this can be confusing. 
# A Redis hash is roughly analogous to a Python dict that is nested one level deep:

data = {
    "realpython": {
        "url": "https://realpython.com/",
        "github": "realpython",
        "fullname": "Real Python",
    }
}

# Redis’ fields are akin to the Python keys of each nested key-value pair in the inner dictionary above. 
# Redis reserves the term key for the top-level database key that holds the hash structure itself.

# Just like there’s MSET for basic string:string key-value pairs, there is also HMSET for hashes 
# to set multiple pairs within the hash value object:

# 127.0.0.1:6379> HMSET pypa url "https://www.pypa.io/" github pypa fullname "Python Packaging Authority"
# OK
# 127.0.0.1:6379> HGETALL pypa
# 1) "url"
# 2) "https://www.pypa.io/"
# 3) "github"
# 4) "pypa"
# 5) "fullname"
# 6) "Python Packaging Authority"

# 127.0.0.1:6379> HGETALL realpython
# 1) "url"
# 2) "https://realpython.com/"
# 3) "github"
# 4) "realpython"
# 5) "fullname"
# 6) "Real Python"

# Using HMSET is probably a closer parallel for the way that we assigned data to a nested dictionary above, 
# rather than setting each nested pair as is done with HSET.

# Two additional value types are lists and sets, which can take the place of a hash or string 
# as a Redis value. They are largely what they sound like, so I won’t take up your time with additional examples. 
# Hashes, lists, and sets each have some commands that are particular to that given data type, which are in some cases denoted by their initial letter:

# Hashes: Commands to operate on hashes begin with an H, such as HSET, HGET, or HMSET.

# Sets: Commands to operate on sets begin with an S, such as SCARD, which gets the number of elements at the set value corresponding to a given key.

# Lists: Commands to operate on lists begin with an L or R. Examples include LPOP and RPUSH. The L or R refers to which side of the list is operated on. A few list commands are also prefaced with a B, which means blocking. A blocking operation doesn’t let other operations interrupt it while it’s executing. For instance, BLPOP executes a blocking left-pop on a list structure.

# Note: One noteworthy feature of Redis’ list type is that it is a linked list rather than an array. 
# This means that appending is O(1) while indexing at an arbitrary index number is O(N).

# Here is a quick listing of commands that are particular to the string, hash, list, and set data types in Redis:

# Type	Commands
# Sets	
# SADD, SCARD, SDIFF, SDIFFSTORE, SINTER, SINTERSTORE, SISMEMBER, SMEMBERS, SMOVE, SPOP, 
# SRANDMEMBER, SREM, SSCAN, SUNION, SUNIONSTORE

# Hashes
# HDEL, HEXISTS, HGET, HGETALL, HINCRBY, HINCRBYFLOAT, HKEYS, HLEN, HMGET, HMSET, HSCAN, 
# HSET, HSETNX, HSTRLEN, HVALS

# Lists
# BLPOP, BRPOP, BRPOPLPUSH, LINDEX, LINSERT, LLEN, LPOP, LPUSH, LPUSHX, LRANGE, LREM, LSET, 
# LTRIM, RPOP, RPOPLPUSH, RPUSH, RPUSHX

# Strings
# APPEND, BITCOUNT, BITFIELD, BITOP, BITPOS, DECR, DECRBY, GET, GETBIT, GETRANGE, GETSET, 
# INCR, INCRBY, INCRBYFLOAT, MGET, MSET, MSETNX, PSETEX, SET, SETBIT, SETEX, SETNX, SETRANGE, STRLEN

# Since we’re going to be switching over to doing things in Python, you can now clear your toy database with FLUSHDB and quit the redis-cli REPL:

# 127.0.0.1:6379> FLUSHDB
# OK
# 127.0.0.1:6379> QUIT

