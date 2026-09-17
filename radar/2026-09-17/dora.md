---
title: "DORA Metrics"
ring: hold
quadrant: methods-and-patterns
featured: false
---

We feel DORA metrics have become less relevant to us as a standalone framework. Their four metrics are narrow and deployment-centric, and in practice we get broader, more actionable insight from instrumenting our systems directly with [OpenTelemetry](/tools/opentelemetry) and visualizing the results in [Grafana](/tools/grafana). That combination lets us track the SRE metrics that matter to us, tailored to each system, rather than fitting our observability strategy to a fixed set of four benchmarks.

We are putting DORA metrics on hold in favor of this OpenTelemetry + Grafana approach.
