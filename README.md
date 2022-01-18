# Blockfire

Blockfire is a decentralised storage platform.

Just like S3 or Snowflake you upload your file though the web interface or via the API. However unlike the traditional services the Blockfire than distributes the data across the Blockfire network nodes. Using this mechanism the data is stored in an ultra secure environment for very cheap and without any downtime. The Blockfire network also copies the files across multiple locations across its network and thus the system also works like a CDN enabling low latency connections.

The system is essantially a CDN network built on top of a blockchain enabling higher capacity for lower cost.

The Blockfire network is the world's first decentralised hosting service. The service has a central server only to store and distribute the data so the server acts only as a node balancer.

- Warning: The Project is not yet complete

# How does it work

Blockfire has a central center which distributes the data to its network nodes.

The network nodes are miners that run the Blockfire client.
- Definition: Mining is the process of providing your SSD or HDD as a service to the Blockfire network.

Blockfire uses the network storage providers' local storage to store the data.

The subject network nodes are connected to the central server through a HTTP Socket connection and periodically communicate with the central server.

When the Blockfire server receives the data it uses the socket connections command the relevant network nodes to stream the data directly to the target. Thus allowing Blockfire to be able to work with extremely low bandwith. The connections are identified using a unique identifier key.

Files are encoded and split into smaller pieces and distributed across the network allowing no single network node to have an entire file making it impossible to decrypt.
