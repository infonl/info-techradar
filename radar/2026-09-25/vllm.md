---
title: "vLLM"
ring: assess
quadrant: platforms-and-operations
featured: true
---

[vLLM](https://docs.vllm.ai/) is an open source, high-throughput inference engine for serving open-weight language models on your own GPUs, with an OpenAI-compatible API.

Self-hosting is the most sovereign end of our model strategy: prompts and data never leave infrastructure we control. We are gaining experience with it by serving open-weight models behind our [LiteLLM](/platforms-and-operations/litellm) gateway, where they sit next to hosted models via [OpenRouter](/platforms-and-operations/openrouter).

### Considerations

- **GPU cost and operations:** GPUs are expensive and scarce, and serving models is real operational work (drivers, scheduling, upgrades, capacity). It only pays off with sustained load or strict data requirements.
- **Model quality:** Open-weight models are closing the gap, but for many tasks the best hosted models are still ahead. Measure on your own use case before committing.
