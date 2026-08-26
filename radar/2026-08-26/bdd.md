---
title: "BDD"
ring: adopt
quadrant: methods-and-patterns
featured: true
---

Behaviour-Driven Development (BDD) is a collaborative approach to software development that bridges the communication gap between business and IT. It keeps teams focused on the behaviour that matters to the people using the software, described from their perspective rather than from the implementation's.

The value of BDD is in the conversation. Writing scenarios together with business stakeholders surfaces disagreement about requirements early, while it is still cheap to resolve. The automated tests that follow are a by-product of that shared understanding, not the point of it.

We write those scenarios in Gherkin, whose Given/When/Then structure is deliberately close to natural language. A scenario stays readable for non-technical stakeholders while remaining precise enough to execute.

BDD is not a one-size-fits-all solution. It works best when the team is genuinely committed to the collaborative approach and when complex business rules need to be understood by everyone involved. Where the requirements are simple, or where the only readers are engineers, the ceremony costs more than it returns.

The concrete handover from BDD is the Gherkin feature file: a Given/When/Then scenario that doubles as executable specification and living documentation, versioned alongside the code it describes. That is exactly the artifact [Spec Driven Development](/methods-and-patterns/spec-driven-development) wants as input — a well-written scenario already reads like part of a spec an agent can implement and verify against.

BDD's Given/When/Then vocabulary works best when it is grounded in a shared domain language, which is where [Domain Driven Design](/methods-and-patterns/domain-driven-design) comes in: DDD's ubiquitous language keeps a scenario's terms consistent with the terms used in the model and the code.
