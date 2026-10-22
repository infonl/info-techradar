---
title: "LLM Tracing and Evals"
ring: trial
quadrant: methods-and-patterns
featured: true
---

LLM applications fail differently from ordinary code: the same input can give a different answer tomorrow, after a model or prompt change. Two practices make that visible:

- **Tracing:** record every model and tool call of an agent or pipeline, with prompts, responses, latency and cost, so a bad answer can be traced back to the step that caused it. Where possible this goes through [OpenTelemetry](/methods-and-patterns/opentelemetry), like the rest of our observability.

- **Evals:** run a fixed set of representative inputs against the application and score the outputs, automatically and in CI, so a prompt or model change is tested before it ships, just like code.

The capability matters more than the tool, and the right tool differs per project. We currently use [Langfuse](https://langfuse.com/) for tracing, prompt management and evals. It is open core: the core is MIT licensed and can be self-hosted, but some enterprise features are under a commercial license, and the company is owned by ClickHouse.

For new agents we prefer building with [Apache Burr](https://burr.apache.org/), which models an application as an explicit state machine and ships a self-hosted UI to trace and debug every step. It is open source and incubating at the Apache Software Foundation, so tracing comes with the framework instead of from a separate vendor.
