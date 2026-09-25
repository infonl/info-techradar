---
title: "DuckLake"
ring: assess
quadrant: platforms-and-operations
featured: true
---

[DuckLake](https://ducklake.select/) is an open lakehouse format from the makers of [DuckDB](/tools/duckdb). Data lives as Parquet files in object storage, like with [Apache Iceberg](/platforms-and-operations/apache-iceberg), but all metadata lives in an ordinary SQL database such as [PostgreSQL](/platforms-and-operations/postgresql) instead of in metadata files plus a separate catalog service.

That makes the stack considerably simpler: a database we already run replaces the catalog, and it supports transactions across multiple tables. We are preparing a pilot next to our Iceberg lakehouse.

The format is young, though. Engine support outside DuckDB is still limited, whereas Iceberg is supported almost everywhere, so for now Iceberg remains our default.
