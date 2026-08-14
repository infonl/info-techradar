---
title: "Event-driven Architecture"
ring: adopt
quadrant: methods-and-patterns
featured: true
---

Event-driven architecture is less a technology choice than a way of thinking about systems. Rather than components calling each other to make things happen, they publish facts about what has happened, and other components decide for themselves what to do with them.

That inversion is the point. A producer stops needing to know who its consumers are, which means new behaviour can be added by adding a subscriber instead of by changing the thing that emits the event. Systems built this way tend to stay easier to extend as they grow.

We use this approach where the problem calls for it:

- when several parts of a system need to react to the same thing happening
- when producers and consumers should be able to evolve independently of each other
- when the sequence of what happened is itself valuable, for auditing, for replay, or for rebuilding state
- when load between components varies enough that decoupling them in time is worth something

It is not free. Asynchronous flows are harder to follow than a call stack. Delivery is typically at-least-once, so consumers have to be idempotent. Eventual consistency needs to be a deliberate decision rather than a surprise, and debugging spans several components, which means tracing has to be in place from the start rather than added once something goes wrong.

As with any architecture, the right answer is the one that fits the problem. Event-driven is one of the approaches we reach for deliberately, not a default we apply everywhere.
