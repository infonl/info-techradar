---
title: "CloudNativePG"
ring: trial
quadrant: platforms-and-operations
featured: true
---

[CloudNativePG](https://cloudnative-pg.io/) is a Kubernetes operator for [PostgreSQL](/platforms-and-operations/postgresql). It runs highly available Postgres clusters with automatic failover, and takes continuous backups to S3-compatible object storage for point-in-time recovery.

We run it in production in one of our projects, and use it where no suitable managed database is available, such as on our own hardware or on a [European Sovereign Cloud](/platforms-and-operations/european-sovereign-cloud) with a limited managed services catalogue. Clusters are declared as Kubernetes resources and deployed through Git like the rest of the platform. It is a CNCF Sandbox project.

### Considerations

- **You operate the database:** The operator automates a lot, but upgrades, backup restores and capacity are still your responsibility. Where a provider offers managed PostgreSQL that meets the requirements, that remains the simpler choice.
