---
title: "TanStack Query"
ring: adopt
quadrant: languages-and-frameworks
featured: true
---

[TanStack Query](https://tanstack.com/query/) _(formerly known as React Query)_ is our preferred library for managing server state in the frontends of our web applications.

It is worth being precise about what it does. It is not general-purpose state management; it is a cache for data that lives on the server. Fetching, caching, background revalidation, deduplication of in-flight requests and invalidation are all handled for you, which removes a category of hand-rolled code that used to end up in every project.

Despite the old name, TanStack Query is no longer React-specific. It is built on a framework-agnostic core with adapters for the other major frontend frameworks, so the same approach — and most of the same mental model — carries across the frontend stacks we work in.
