---
title: "Valkey / Redis"
ring: adopt
quadrant: platforms-and-operations
featured: true
---

We use an in-memory key-value data store for specific cases such as a custom cache or queue management solution. In those cases a relational database would be overkill and not a good fit.

For new solutions we prefer [Valkey](https://valkey.io/). Valkey is the Linux Foundation fork created after Redis moved away from an open source licence, and we think it is now the better of the two: development has been more active, the performance work has gone further, and its governance is genuinely open. It is API-compatible with Redis, so existing clients, libraries and tooling continue to work, and several cloud providers now offer it as their default.

[Redis](https://redis.io/) remains a solid choice and we are happy to use it where a client prefers or requires it, or where it is already running.
