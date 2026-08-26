---
title: "Spec Driven Development (SDD)"
ring: adopt
quadrant: methods-and-patterns
featured: true
---

We follow an agentic-first way of working, and Spec Driven Development (SDD) is how we make that work in practice. Rather than prompting an agent straight into code, we first write down an explicit specification — expected behaviour, business rules and failure scenarios — which the agent then implements and verifies against.

The specification is the handover artifact that matters: it gives the agent as well as human stakeholders a concrete contract to work within and to review before code is generated.

We encourage combining SDD with [Domain Driven Design](/methods-and-patterns/domain-driven-design): DDD supplies the shared language and domain boundaries, SDD turns that understanding into verifiable requirements. Together they keep agentic coding tools like [Claude Code](/tools/claude-code) pointed at the right problem, not just generating code fast.

Where scenarios are best captured collaboratively with business stakeholders, [BDD](/methods-and-patterns/bdd) remains a good source of input for a spec.
