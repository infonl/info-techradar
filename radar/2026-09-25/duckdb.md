---
title: "DuckDB"
ring: adopt
quadrant: tools
featured: true
---

[DuckDB](https://duckdb.org/) is an in-process analytical database: a single library, no server, that runs fast SQL over Parquet, CSV and [Apache Iceberg](/platforms-and-operations/apache-iceberg) tables, locally or straight from object storage.

We use it both during development and in production, as the query engine and serving layer on top of our lakehouse. There it replaced a separate distributed query engine that was more infrastructure than our data volumes justified.

### Why DuckDB?

- **Fast without a cluster:** For the data sizes most projects actually have, a single process on a decent machine outperforms a distributed setup, at a fraction of the operational cost.

- **Everywhere:** The same engine runs in a notebook, a test, an ETL job and an API, which makes analysis and pipelines easy to reproduce.

- **Open formats:** It reads and writes open formats directly, so it composes with the rest of the stack instead of owning the data.

### Considerations

- **Single node:** DuckDB scales up, not out. For datasets that do not fit on one machine, a distributed engine or [Databricks](/tools/databricks) is still the better fit.
- **Concurrency:** Only one process can write to a database file at a time. Plan the serving layer for read-mostly workloads.
