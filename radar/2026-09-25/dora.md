---
title: "DORA Metrics"
ring: trial
quadrant: methods-and-patterns
featured: false
---

[DORA metrics](https://dora.dev/guides/dora-metrics-four-keys/) measure how teams deliver software: deployment frequency, lead time for changes, change failure rate and time to restore service.

What has changed is how we deliver. In the agentic way of working we now prefer, AI agents write, and increasingly merge, a large share of our code. As Rick Pollick argues in [DORA Metrics in the Agentic Era](https://rickpollick.com/blog/dora-metrics-agentic-era), the classic four metrics assume each commit and deploy costs human effort. Once agents do much of the work, that assumption breaks:

- **Deployment frequency** goes up with trivial changes and stops being a signal of value delivered.
- **Lead time for changes** can shrink through revert churn without anything new reaching production.
- **Change failure rate** tends to rise, with many small, agent-generated failures that never show up as major incidents.
- **Time to restore** matters more than ever.

The article suggests keeping the four keys and adding a second layer, such as outcome latency (from human intent to verified customer value), reviewer load, rework ratio, and segmenting change failure rate by human, agent-assisted and agent-authored changes.

We are moving DORA metrics back to Trial to work out how to use them in our agentic way of working: which of the classic metrics still mean something, which extra metrics we need, and how to measure them without just rewarding throughput.
