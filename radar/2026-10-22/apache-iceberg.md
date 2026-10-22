---
title: "Apache Iceberg"
ring: adopt
quadrant: platforms-and-operations
featured: true
---

[Apache Iceberg](https://iceberg.apache.org/) is an open table format for large analytic datasets. It adds tables, ACID transactions, schema evolution and time travel on top of plain Parquet files in object storage.

Iceberg is the foundation of the open source lakehouse we prefer for our projects over [Databricks](/tools/databricks). We run it in production. Around it sit S3-compatible object storage for the files, an Iceberg REST catalog that tracks the tables, Python pipelines that write with PyIceberg, a workflow orchestrator that schedules them, and [DuckDB](/tools/duckdb) to query and serve the results.

### Why Iceberg?

- **No engine lock-in:** The same tables can be read and written by [DuckDB](/tools/duckdb), Spark, Trino, Python (PyIceberg) and Databricks. Switching engines does not mean migrating data.

- **Runs anywhere:** All it needs is object storage and a catalog, so it runs just as well on a [European Sovereign Cloud](/platforms-and-operations/european-sovereign-cloud) or on our own hardware as on a hyperscaler.

- **Safe evolution:** Schema and partition changes do not require rewriting data, and you can query a table as it was at any retained snapshot.

### Considerations

- **The catalog matters:** Iceberg needs a catalog to track table state. Pick one with the REST catalog API, so engines can be swapped without migrating metadata.
- **Maintenance:** Snapshot expiry and compaction of small files are your job, not the format's.
