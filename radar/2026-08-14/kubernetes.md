---
title: "Kubernetes"
ring: adopt
quadrant: tools
featured: true
---

Adopting [Kubernetes](https://kubernetes.io/) starts with something more basic: we containerise the stack. Containers are how we run software during development and how we ship it to every environment beyond that, which keeps what a developer runs locally close to what actually goes to production.

How much orchestration a solution needs on top of that varies, and we work across the whole range:

- **Self-hosted Kubernetes**, where a client needs full control over the cluster or has to run on their own infrastructure.
- **Managed Kubernetes**, where most of our solutions land. The declarative model and the ecosystem around it, without the burden of operating the control plane ourselves.
- **Serverless containers on managed platforms**, where a solution does not need a cluster at all and the platform scales containers directly.

A mature managed Kubernetes offering is one of our criteria when assessing [European Sovereign Cloud](/platforms-and-operations/european-sovereign-cloud) providers, because it is a large part of what keeps workloads portable between them.
