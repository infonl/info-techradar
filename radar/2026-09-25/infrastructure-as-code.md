---
title: "Infrastructure as Code"
ring: adopt
quadrant: methods-and-patterns
featured: false
---

This is such a given (also in the industry) that we no longer feature it on our tech radar.

All cloud infrastructure should be provisioned and maintained using Infrastructure as Code (IaC). We no longer use the templating services of the individual cloud providers, such as CloudFormation for [AWS](/platforms-and-operations/aws) and ARM templates for [Azure](/platforms-and-operations/azure). Instead we use [OpenTofu](/tools/opentofu) for every cloud, so the same tooling and skills carry over between providers, including a [European Sovereign Cloud](/platforms-and-operations/european-sovereign-cloud).

If possible, use policies to disable manual changes in cloud portals and force scripted modifications.
