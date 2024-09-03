# System Design Patterns:

## Introduction to System Design Patterns
System design patterns are reusable solutions to common problems encountered when designing large-scale systems. These patterns provide best practices and strategies that help architects and developers build scalable, maintainable, and reliable systems. By applying these patterns, you can address specific challenges such as load balancing, data consistency, fault tolerance, and more.

Key System Design Patterns

### Load Balancer Pattern :

+ `Overview`: The load balancer pattern involves distributing incoming network or application traffic across multiple servers or instances to ensure that no single server becomes a bottleneck. It enhances system availability, reliability, and scalability.

+ `Components`:

    + `Load Balancer`: The central component that receives incoming requests and distributes them among backend servers.
    + `Backend Servers`: The servers that process the requests. These can be application servers, web servers, or database servers.

+ `Types of Load Balancing`:

    + `Round-Robin`: Distributes requests sequentially among servers.
    + `Least Connections`: Sends requests to the server with the fewest active connections.
    + `IP Hash`: Distributes requests based on the client’s IP address.
+ `Example`: A global e-commerce platform uses a load balancer to distribute incoming HTTP requests across multiple application servers. This ensures that even during peak traffic, the system can handle the load without crashing.

### Cache Pattern :

+ `Overview`: The cache pattern involves storing frequently accessed data in a temporary storage area (cache) to reduce the time it takes to retrieve that data. Caching can be implemented at various layers, including the database, application, or client side.

+ `Components`:

    + `Cache Store`: The storage mechanism for the cached data (e.g., Redis, Memcached).
    + `Cache Keys`: The unique identifiers used to retrieve cached data.
    + `Cache Eviction Policy`: The strategy for removing stale or least-used data from the cache (e.g., LRU - Least Recently Used).

+ `Types of Caching`:

    + `Write-Through`: Data is written to the cache and the database simultaneously.
    + `Write-Behind`: Data is first written to the cache and then asynchronously to the database.
    + `Read-Through`: Data is read from the cache if available, otherwise retrieved from the database and then cached.

+ `Example`: A social media platform caches user profile data and the latest posts in Redis to speed up page load times. This reduces the load on the database and improves the user experience.

### Database Sharding Pattern :

+ `Overview`: Sharding is a pattern that involves splitting a large database into smaller, more manageable pieces called shards. Each shard is hosted on a separate database server, allowing the system to scale horizontally.

+ `Components`:

    + `Shards`: Individual database instances that contain a subset of the overall data.
    + `Shard Key`: The attribute or set of attributes used to determine the shard in which a particular piece of data will be stored.
    + `Router`: A component that directs queries to the appropriate shard based on the shard key.

    Sharding Strategies:

    + `Range-Based Sharding`: Data is partitioned based on a range of values in the shard key.
    + `Hash-Based Sharding`: Data is distributed across shards based on a hash of the shard key.
    + `Geographic Sharding`: Data is partitioned based on the geographic location of users or data sources.
    + `Example`: A global online marketplace uses sharding to distribute user data across different geographic regions. Users from North America are stored in one shard, while users from Europe are stored in another. This reduces latency and improves the performance of the system.

### Circuit Breaker Pattern :

+ `Overview`: The circuit breaker pattern is used to prevent cascading failures in distributed systems. It monitors the interactions between services and temporarily stops requests to a failing service to allow it to recover.

+ `Components`:

    + `Circuit Breaker`: The component that monitors service calls and determines whether to allow or block requests.
    + `States`:
        + `Closed`: The circuit breaker allows requests to pass through.
        + `Open`: The circuit breaker blocks all requests to the failing service.
        + `Half-Open`: The circuit breaker allows a limited number of requests to test if the service has recovered.

+ `Example`: In a microservices architecture, a payment service uses a circuit breaker to prevent overloading the inventory service if it becomes slow or unresponsive. If the inventory service fails, the circuit breaker will temporarily block requests, preventing the entire system from failing.

### Event Sourcing Pattern :

+ `Overview`: Event sourcing is a pattern where changes to the system's state are stored as a sequence of events. Instead of storing the current state, the system stores the history of events that led to the current state. This pattern is useful for systems that require an audit trail or need to rebuild state from a series of events.

+ `Components`:

    + `Event Store`: A storage system that records all events.
    + `Event Stream`: The sequence of events related to a specific entity.
    + `Event Handlers`: Components that process events to update the system's state or trigger other actions.

+ `Example`: A banking application uses event sourcing to record all transactions (deposits, withdrawals, transfers). The current balance of an account is calculated by replaying the sequence of events from the event store.

### CQRS (Command Query Responsibility Segregation) Pattern :

+ `Overview`: CQRS is a pattern where the operations that change the state of the system (commands) are separated from the operations that query the state (queries). This separation allows for optimized handling of read and write operations.

+ `Components`:

    + `Command Model`: Handles the write operations, ensuring data consistency.
    + `Query Model`: Handles the read operations, often optimized for performance.
    + `Event Bus`: A messaging system that communicates changes between the command and query models.

+ `Example`: An e-commerce platform uses CQRS to handle orders. The command model processes the creation, updating, and deletion of orders, while the query model provides fast access to order history and details.

### Saga Pattern :

+ `Overview`: The saga pattern is used to manage distributed transactions in a microservices architecture. Instead of using a traditional two-phase commit, the saga pattern breaks down a transaction into a series of smaller, independent operations. Each operation has a corresponding compensating action to undo the changes if something goes wrong.

+ `Components`:

    + `Saga Coordinator`: Manages the sequence of operations and ensures that compensating actions are taken if a step fails.
    + `Service Participants`: The individual microservices involved in the transaction.

+ `Example`: A travel booking system uses the saga pattern to coordinate bookings across multiple services (e.g., flights, hotels, car rentals). If the hotel booking fails, the saga will trigger compensating actions to cancel the flight and car rental bookings.

### Data Lake Pattern :

+ `Overview`: A data lake is a centralized repository that allows you to store structured and unstructured data at any scale. The data lake pattern is used in big data systems where the system needs to handle a wide variety of data types and formats.

+ `Components`:

    + `Raw Data Storage`: A storage system that can handle large volumes of raw data (e.g., HDFS, Amazon S3).
    + `Data Processing Engine`: Tools for processing and transforming data (e.g., Apache Spark, Hadoop).
    + `Metadata Catalog`: A system that tracks the data stored in the lake, including its schema, lineage, and access policies.

+ `Example`: A media company uses a data lake to store video files, logs, and user data. Data scientists and analysts can access and process this data using various tools without worrying about the underlying infrastructure.

### API Gateway Pattern :

+ `Overview`: The API Gateway pattern is used to provide a single entry point for a set of microservices. The API Gateway handles requests from clients, routing them to the appropriate service, and sometimes aggregating responses.

+ `Components`:

    + `API Gateway`: The component that receives client requests, routes them to the appropriate microservices, and returns the response.
    + `Microservices`: The individual services that handle specific tasks in the system.
    + `Authentication/Authorization`: The gateway can handle security concerns such as user authentication and authorization.

 +`Example`: An online retail platform uses an API Gateway to handle all client requests. The gateway routes product search requests to the search service, order requests to the order service, and handles user authentication.

### Bulkhead Pattern :

+ `Overview`: The bulkhead pattern is used to isolate different parts of a system to prevent failures in one part from cascading to others. It’s inspired by the bulkheads in a ship that prevent water from flooding the entire vessel if one compartment is breached.

+ `Components`:

    + `Isolated Pools`: Resources (threads, connections) are divided into separate pools for different parts of the system.
    + `Service Isolation`: Services are designed to operate independently, with separate resource allocations.

+ `Example`: A booking system for flights, hotels, and cars uses the bulkhead pattern to isolate these services. If the hotel service experiences a surge in traffic, it won’t affect the availability of the flight and car booking services.

resources : [[ complete-guide-to-system-design#systemdesignpatterns ](https://www.educative.io/blog/complete-guide-to-system-design#systemdesignpatterns)]