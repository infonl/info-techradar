---
title: "OpenBao"
ring: trial
quadrant: platforms-and-operations
featured: true
---

[OpenBao](https://openbao.org/) is the open source fork of HashiCorp Vault, created after HashiCorp moved Vault to the Business Source License, just as [OpenTofu](/tools/opentofu) was forked from Terraform. It is a Linux Foundation project licensed under MPL 2.0.

We run it in production in one of our projects as the central secrets store for applications on [Kubernetes](/tools/kubernetes). The External Secrets Operator syncs secrets from OpenBao into the cluster, so no secret lives in Git or in deployment manifests, and secrets can be rotated in one place.

### Considerations

- **Critical infrastructure:** Everything depends on the secrets store being available and its unseal keys being safe. Plan high availability, backups and the unseal procedure before going to production.
