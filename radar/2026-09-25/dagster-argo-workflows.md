---
title: "Dagster / Argo Workflows"
ring: trial
quadrant: tools
featured: true
---

Batch work such as data ingestion, ETL and model pipelines needs an orchestrator: something that schedules jobs, runs steps in the right order, retries failures and shows what happened. We use two orchestrators, because they solve different problems.

- **[Dagster](https://dagster.io/)** for data pipelines in Python. Dagster models pipelines as data assets (tables, files, models) rather than as tasks, which gives lineage, partitions and backfills without extra tooling. It fits data platforms where the question is "is this dataset up to date and where did it come from?", for example on our [Apache Iceberg](/platforms-and-operations/apache-iceberg) lakehouse. The core is open source, with a commercial cloud offering next to it.

- **[Argo Workflows](https://argoproj.github.io/workflows/)** for container batch jobs on [Kubernetes](/tools/kubernetes). Every step is a container, so steps can be written in any language, and workflows are Kubernetes resources that are deployed through Git with [Argo CD](/tools/argocd). It is a graduated CNCF project.

Rule of thumb: when the pipeline is about datasets and their freshness, use Dagster. When it is about running containers in order on a cluster you already operate, use Argo Workflows.
