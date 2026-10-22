---
title: "Event-driven Architecture"
ring: adopt
quadrant: methods-and-patterns
featured: true
---

Event-driven architecture is less a technology choice than a way of thinking about systems. Rather than components calling each other to make things happen, they publish facts about what has happened, and other components decide for themselves what to do with them.

We use this approach, and we use it deliberately. It is not free: asynchronous flows are harder to follow than a call stack, delivery is typically at-least-once so consumers have to be idempotent, eventual consistency has to be a decision rather than a surprise, and debugging spans several components, which means tracing has to be in place from the start rather than added once something goes wrong.

As with any architecture, the right answer is the one that fits the problem. Event-driven is one of the approaches we reach for, not a default we apply everywhere.
