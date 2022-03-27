# Local cache

You can imprement a local in-mem caching solution in Python using a dictionary. You can save the content of a request in a dictionary, for example, using the URL as key and it's conent as the value. `caching.py' is an example of this strategy. It can be seen that the gettign article step is much faster if it is fetched from the cache. 

The problem with this strategy is that the content of the dictonary will grow indefinitely, eventually causing the application to crash.
We need an strategy to decide which articles should stay in memory and which shoul be removed (**caching algorithm**). 

## Caching algorithms

The problem with this strategy is that the content of the dictonary will grow indefinitely, eventually causing the application to crash.
We need an strategy to decide which articles should stay in memory and which shoul be removed (**caching algorithm**).

### Least Recently Used (LRU) strategy

Organize the items in order of use. Every time you access an entry, the LRU algo will move it to the top of the cache. Then, it is easy to identify the entry that's goen unused the logneds by looking at the bottom of the list.

One way to implement the LRU cache in Python is to use a combination of doubly linked list and a hash map. The head element of the doubly linked list points to he most recently used entry, and the tail to the least used entry. 

Python has included the @lru_cache decorator for implementering the LRU strategy. @lru_cache uses a dictionary behind the scenes. It caches the function's result under a key that consists of the call to the function, including the supplied arguments. These arguments have to be hashable. 

We will work with the following toy example: Imagine you want to determine all the different ways you can reach a specific stair in a staircase by hopping one, two, or three stairs at a time. How many paths are there to the fourth stair? 

To determine the different paths to the fourth stair, you can add up the four ways of reaching the third stair, the two ways of reaching the second stair, and the one way of reaching the first stair. This is called recursion. 


# Source 
- https://realpython.com/lru-cache-python/
