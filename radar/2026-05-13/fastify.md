---
title: "Fastify"
ring: adopt
quadrant: languages-and-frameworks
featured: true
---

[Fastify](https://www.fastify.io/) is a fast, low-overhead web framework for [Node.js](/languages-and-frameworks/nodejs/).

### Why Fastify?

- **Performance and security defaults:** built around schema-based validation and a plugin architecture that keeps the request lifecycle predictable.
- **First-class [TypeScript](/languages-and-frameworks/typescript/) support:** types ship with the framework rather than as a community add-on.
- **Familiar Express-style API:** developers coming from [Express](/languages-and-frameworks/express/) recognise the routing model without inheriting Express's middleware limitations.
- **Growing ecosystem:** high-quality plugins for auth, OpenAPI, GraphQL and the integrations we typically need.

### Considerations at INFO

- Preferred Node.js web framework when we don't have a project-specific reason to pick something else.
- We accept that Fastify is younger than Express and Koa, and that its track record is shorter — the benefits in performance, types and ergonomics outweigh that trade-off.
- **Current Focus:** new [Node.js](/languages-and-frameworks/nodejs/) services default to Fastify; existing Express services are not migrated unless there's a separate reason to touch them.

For Node.js services at INFO, Fastify is our default web framework.
