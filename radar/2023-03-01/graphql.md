---
title: "GraphQL"
ring: adopt
quadrant: languages-and-frameworks
featured: true
---

[GraphQL](https://graphql.org/) is a powerful way to expose an API for frontend use.
We generally prefer [tRPC](/languages-and-frameworks/trpc) over GraphQL for frontend-backend integration but still consider GraphQL a valid alternative in cases where tRPC is not a good match.

When tRPC is not a good match we generally prefer GraphQL over REST because it increases flexibility and agility,
depending on the context (e.g. external APIs may still require REST for API clients' needs).

Beware
of [GraphQL misuse](https://www.thoughtworks.com/radar/methods-and-patterns/graphql-for-server-side-resource-aggregation)
however. A mix of GraphQL and REST is also a viable solution.
