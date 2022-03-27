# External Cache: Redis

Stores the data in a separate fleet. **Redis** is a popular open source in-memory data structure store used as cache. Redis is a key-value store. The key can contain strings, hashes, lists, sets and sorted sets. Redis is written in C. Redis has three main peculiatiries:

- It holds its database entirely in memory, usign the disk only for persitence
- Rich set of data types compared to many key-value data stores
- It can replicate data to any number of slaves

## Redis Basics

### Redis Client

Redis commands are used to perfomr some operations on Redis server. To run those commands, you need a Redis client. To start a Redis
client, open the terminal and type `redis-cli`. This will connect to oyu local server. To run commands on Redis remote server, use `redis-cli -h host -p port -a password`. 

To start a Redis server, run `redis-server`.

### Redis data types

Redis supports strings (sequence of bytes), hashes (collection of key-value pairs), lists (lists of strings), sets (unordered collection of strings) and sorted sets (sets with a score parameter that determines the order).

### Redis key Commands

Redis keys commands are used for managign keys. The schema they use is `COMMAND KEY_NAME`. Some basic key commands are the following:

- `DEL key`: Deletes the key if exists
- `DUMP key`: Return a serialized version of the value stored at the specific key
- `EXISTS key`: Checks whether the key exists or not
- `EXPIRE key seconds`: Sets the expirty of the key after the specified time
- `EXPIREAT key timestamp`: Sets the expiry of the key after the specified time
- `KEYS pattern`: Finds all keys mathcing the pattern
- `MOVE key db`: Moves a key to another database
- `PERSIST key`: Removes the expiration from the key
- `PTTL key`: Gets the remainign time in keys expiry in milliseconds
- `RANDOMKEY`: Returns a random key from Redis
- `RENAME key newkey`: Changes the key name
- `RENAMENX key newkey`: Renames the key, if a new key doesn't exist
- `TYPE key`: Returns the data type of the value stored in the key

### Redis string Commands

Redis string commands are used for managing string values in Redis. Following lists some basic string commands:

- `SET key value`: Sets the value at the specific key
- `GET key`: Gets the value of a key
- `GETRANGE key start end`: Gets a substring of the string stored at the key
- `GETSET key value`: Sets the string value of a key and return its old value
- `GETBIT key offset`: Returns the bit value at the offset in the string value stored at the key
- `MGET key1 key2 ...`: Gets values of multiple keys
- `SETBIT key offset value`: Sets or clears the bit at the offset in the string value
- `SETEX key seconds value`: Sets the value with the expiry of a key
- `STRLEN key`: Gets the length of the value
- `INCR key`: Increment the interger value of a key by one
- `APPEND key value`: Appends a valeu to a key


### Redis Hashes Commands

Redis Hashes are mapts between the string fields and the string values. Following shows some basic commands related to hash:

- `HDEL key field`: Deleteres one or more hash fields
- `HEXISTS key field`: Determines whether a has field exists or not
- `HGET key field`: Gets the value of a hash field at the key
- `HGETALL key`: Gets all the fields and values stored in a hash key

### Redis Lists Commands

Redis lists are simply lists of strings, sorted by insertion order. You can add elements in the head or tail of the list. Basic commands related to lists:

- `BLPOP key1 timeout`: Removes and gets the first element in a list, or blocks until one is available
- `BRPOPLPUSH source destination timeout`: Post a value from a list, pushes it into another list and returns it; or blocks until one is available
- `LINDEX key index`: Gets an element from a list by its index
- `LINSERT key BEFORE|AFTER pivot value`: Inserts an element before or after another element in a list
- `LLEN key`: Gets the length of a list
- `LPOP key`: Remove and gets the first element in a list
- `LPUSH key value`: Prepends a value to a list, only if the list exists
- `LREM key count value`: Removes elements from a list

### Redis Sets Commands

Redis sets are unordered collection of unique strings. Basic set commands:

- `SADD key member1`: Adds one or more members to a set
- `SCARD key`: Gets the number of member in a set
- `SDIFF key1 key2`: Substracts multiple sets
- `SINTER key1 key2`: Insersects multiple sets
- `SMEMBERS key`: Gets all the members in a set
- `SPOP key`: Removes and return a random meber from a set

### Redis Sorted Sets Commands

Redis sorted sets are similar to Redis sets, with the difference that every member of the sorted set is associated with a score, that is used in order to take the sorted set ordered, from the smallest to the greatest score.  Redis sorted sets basic commands:

- `ZADD key score1 member1`: Adds one member to a sorted set, or updates its score
- `ZCARD key`: Gets the nubmer of members in a sorted set
- `ZCOUNT key min max`: Counts the mkembers in a sorted set with socres within the given values
- `ZINCRBY key increment member`: Increments the score of member in a sorted set
- `ZLEXCOUNT key min max`: Counts the num,ber of members in a sorted set between a given lexicopraphical range
- `ZRANK key member`: Determines the index of a member in a sorted set

### Redis Transactions Commands

Redis transaction allow the execution of a group of commands in a single step. All commnatds in a transaction are sequentially executed, and the transaction is atomic. Transactions are initiated by command MULTI and executed by command EXEC. 

### Redis Connection Commands

Redis connection commands are used to manage client connections with the Redis server. Basic redis connection commands are:

- `PING`: Checks whether the server is running or not
- `AUTH password`: Authenticates to the server
- `QUIT`: Closes the current connection

### Redis Server Commands

Redis server commands are used to manage Redis server.

## Redis as an LRU cache

When Redis is used as a cache, often it is handy to let it automatically evict old data as you add new data. LRU is actually only one of the supported eviction methods.

### Maxmemory configuration directive

The maxmemory configuration directive is used in order to configure Redis to use a specified amount of memory for the data set.Setting maxmemory to zero results into no memory limits. This is the default behavior for 64 bit systems, while 32 bit systems use an implicit memory limit of 3GB.


### Eviction policies

When the specified amount of memory is reached, it is possible to select among different behaviors, called **policies**. This is determined using the **maxmemory-policy** configuration directive. The following policies are available: 

- **noeviction**: Return errors when the memory limti is reached
- **allkeys-lru**: Try to remove the less frequently used key first, in order to make space for the new data
- **volatile-lru**: Try oto remove the LRU key, but only among keys that have an expire set
- **allkeys-random**: Removes keys randomly
- **volatile-random**: Removes keys randomly, but only among keys that have an expire set
- **volatile-ttl**: Remove keys with an expire set, and try to evict keys with a shorter time to live (TTL) first

Picking the right eviction policy is important depending on the access pattern of your application, however you can reconfigure the policy at runtime while the application is running, and monitor the number of cache misses and hits using the Redis INFO output in order to tune your setup.

### Evicttion process

It is important to understand that the eviction process works like this:

- A client runs a new command, resulting in more data added
- Redis checks the memory usage, and if it is greater than the maxmemory limit , it evicts keys according to the policy
- A new command is executed, and so forth




  
