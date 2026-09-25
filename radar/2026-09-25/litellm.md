---
title: "LiteLLM"
ring: adopt
quadrant: platforms-and-operations
featured: true
---

[LiteLLM](https://www.litellm.ai/) is an open source AI gateway. It puts one OpenAI-compatible API in front of any number of model providers, both hosted routers such as [OpenRouter](/platforms-and-operations/openrouter) and self-hosted inference servers such as [vLLM](/platforms-and-operations/vllm).

We run the LiteLLM proxy ourselves as the single entry point for LLM traffic in our Data & AI projects. Applications talk to the gateway, never to a provider directly, so swapping or adding a model is a configuration change instead of a code change.

### Why LiteLLM?

- **Budgets and access control:** Every consumer gets a scoped virtual key with its own allowed models, rate limit, budget and expiry. Spend is tracked per key, so the cost of an experiment or a client is visible from day one.

- **Model independence:** We do not want to commit to one model or one vendor. The gateway lets us mix commercial models and self-hosted open-weight models behind the same API, with load balancing, retries and fallbacks between them.

- **Self-hosted:** Because we run it ourselves, keys, logs and spend data stay on our own infrastructure, and prompts only go to the upstream we route them to.

### Considerations

- **Keep the admin surface private:** The proxy holds the master key and all provider keys. Expose only the model API publicly and keep the admin UI on a private network or behind SSO.

- **Pin versions:** In March 2026 two LiteLLM releases on PyPI were [compromised in a supply chain attack](https://docs.litellm.ai/blog/security-update-march-2026). Pin exact versions or image digests and upgrade deliberately.
