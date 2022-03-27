# Cache_eguna

## Intro

A cache is a **high-speed data storage** layer which stores a subset of data, so that future requests for that data are served up faster. Caching allows you to efficiently reuse previously retrieved or computed data. The data in a cache is generally stored in **fast access hardware** such as RAM. A cache typicalli stores a subset of data **trainsiently**. 

## Types of Caching 

There are a few types that stand out from the rest. 

### In-memory Caching

Cached data is stored directly in RAM, which is assumed to be faster than the typical storing system where the original data is located.
The most common implementation of this type of caching is based on key-value databases. The key is represented by a unique value, while the value by the cached data. 

### Database Caching

Each DB usually comes with some level of caching. By caching the resul of last queries executed, the database can provide the data previously cached immediately. The most popular approach is based on usinhg a hash table storing key-value pair. 

### Web Caching

#### Web Client Caching

Stored on clients. The first time a browser loads a web page, it stored the page resources, such as test, iamges, stylesheets, scripts, and media files. The next time the same page is hit, the browser can look in the cache fro resources that were previously cached and retrieve them. 

#### Web Server Caching

Aimed at storing resources server-side for reuse. Avoids servers from getting overloaded, reducing the work to be done, and improve the page delivery speed.

### CDN Caching

CDN (Content Delivery Network) is aimed at caching content, such as web pages, stylesheets, scripts, and media files, in proxy servers. It can be seen as a system of gateways between the user and the origin server, storing its resources. When the user requires a resource, a proxy server intercepts it and checks if it has a copy. If not present, the request is forwarded to the origin server. These proxy servers are placed in vast number of locations worldwide, and user requests are dynamically routed to the nearest one. 



## Local vs External Caching

In this repo we will focus on server side caching. **Local caches**, commonly implemented in process memory, can provide significant improvements with minimal work. Local caches are often the first approach implemented and evaluated once the need for caching is identified. They are low-risk to integrate into an existing service. Often implemented as an **in-memory hash table** that is managed through application logic. An **external cache** stored cached data in a separate fleet, for example using Redis. Cache coherence issues are recuded because the external cache holds the value by all servers in the fleet. Further, external caches provide more available storage space than in-memory caches. 

## Challenges

### Local Cache Problems

- **Cache Coherence Problem**: For local caches, they will be idrrefent per server and lead to inconsistend data. 

- **Cold Start Problem**: Since each server is starting up with no cache, there can be an increase in the number of requests to the downstream dependencies. 

### External Cache Problems

- System complexity increase: Since there is an additional fleet to monitor, manage and scale. 
- Cache system down: Code to deal with cache fleet unavailability, cache node failure, or cache put(get faiulres must be added. 

## Important Considerations

- Cache size
- Cache eviction: Move data out of the cache when it hits capacity. For example, least recenlt used (LRU) strategy.
- Cache expiry: Policy of determining how long we can retrain the data in the cache. 
- Downstream service unavailability: Cache service should be able to safeguard the cache. 
- Security: Security of sentivie ort customer data that's beign cached. Data must be encrypted, and security should be provided while transmitting data to and from the cache. 


