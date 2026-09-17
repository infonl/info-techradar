---
title: "OpenTelemetry"
ring: adopt
quadrant: tools
featured: true
---

[OpenTelemetry](https://opentelemetry.io/) is a vendor-neutral, open-source observability framework for generating, collecting, and exporting telemetry data — traces, metrics, and logs — from applications and infrastructure.

We use OpenTelemetry to instrument our applications and implement SRE metrics such as the ones described in this [logz.io article on EvOps and SRE metrics](https://logz.io/blog/evops-sre-metrics/). Rather than relying on external DORA-focused tooling, we standardize on OpenTelemetry for capturing these signals and Grafana for visualizing them.

### Why OpenTelemetry?

- **Vendor-Neutral:** A single instrumentation standard that avoids lock-in to any specific observability backend.
- **Unified Signal Model:** Traces, metrics, and logs are captured through one consistent set of APIs and SDKs across languages.
- **Broad Ecosystem:** Wide support across languages, frameworks, and cloud-native tooling, backed by the CNCF.
- **Pairs with [Grafana](/tools/grafana):** OpenTelemetry data is exported to Grafana for visualization, dashboarding, and alerting, giving us a complete observability pipeline from instrumentation to insight.
