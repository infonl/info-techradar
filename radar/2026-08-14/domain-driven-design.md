---
title: "Domain Driven Design (DDD)"
ring: adopt
quadrant: methods-and-patterns
featured: true
---

Domain-driven design (DDD) is a software design approach focusing on modelling software to match a domain according to input from that domain's experts.

Domain-driven design is predicated on the following goals:

- placing the project's primary focus on the core domain and domain logic
- basing complex designs on a model of the domain
- initiating a creative collaboration between technical and domain experts to iteratively refine a
conceptual model that addresses particular domain problems.

### Visualising the model with C4

A model is only worth something if it can be shared, so we use the [C4 model](https://c4model.com/) to visualise the architectures we design, and the C4 vocabulary to describe them.

We focus on the System Context and Container levels and use the lower-level Component and Code diagrams sparingly. Those top two levels are where the DDD concepts become visible: where the bounded contexts sit, where the boundaries between them run, and which language is used inside each.

Having used UML in the distant past and free-format diagramming since then, we found we were missing consistency in both visualising and describing our architectures. C4 gives us enough consolidation to be consistent, while still leaving enough flexibility in how we apply it.
