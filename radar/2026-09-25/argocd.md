---
title: "Argo CD"
ring: trial
quadrant: tools
featured: false
---

[Argo CD](https://argo-cd.readthedocs.io/) is a GitOps continuous delivery tool for [Kubernetes](/tools/kubernetes). The desired state of a cluster lives in Git, and Argo CD continuously reconciles what is running against that declared state.

We are trialling it as the deployment counterpart to our [Infrastructure as Code](/methods-and-patterns/infrastructure-as-code) approach: where [OpenTofu](/tools/opentofu) provisions the infrastructure, Argo CD keeps the workloads on it in sync with Git.

### Why trial Argo CD?

- **Git as the single source of truth:** Deployments are driven by what is committed, which makes changes reviewable through [GitHub](/tools/github) and trivial to roll back.

- **Continuous reconciliation:** Drift between the cluster and the declared state is detected and corrected automatically, so what runs matches what is described.

- **No deployment pipelines to maintain:** Argo CD pulls from Git and applies changes itself, so we no longer need to build and maintain bespoke provisioning pipelines and deployment logic in our CI/CD setup.

- **Visibility:** A dashboard shows sync and health status per application, making the state of each environment easy to inspect.
