---
title: "OpenTelemetry"
ring: adopt
quadrant: methods-and-patterns
featured: true
---

[OpenTelemetry](https://opentelemetry.io/) (OTel) is the vendor-neutral CNCF standard for instrumenting applications: one set of APIs, SDKs and the OTLP wire protocol for traces, metrics and logs. It is the de facto standard for observability, and we use it in our projects.

### Why OpenTelemetry?

- **Instrument once:** Code is instrumented against OTel, not against a monitoring vendor. Where the data goes is decided in configuration, so switching backends does not mean touching application code.

- **Backend choice:** OTLP is accepted by [Grafana](/tools/grafana) and its stack as well as by managed offerings from European cloud providers, which keeps the observability stack as portable as the rest of our infrastructure.

- **Traces across services:** Distributed tracing is what makes a request followable through several services, queues and model calls. For [Event-driven Architecture](/methods-and-patterns/event-driven-architecture) and AI pipelines in particular, it has to be in place from the start.

- **Broad support:** Auto-instrumentation is available for the languages and frameworks we use, and a growing number of tools (including LLM gateways and agent frameworks) emit OTel natively.
