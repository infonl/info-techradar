---
title: "OpenRouter"
ring: adopt
quadrant: platforms-and-operations
featured: true
---

[OpenRouter](https://openrouter.ai/) is a hosted LLM router: one API and one bill for hundreds of models from all major providers. We already use it in our Data & AI work, typically as an upstream behind our own [LiteLLM](/platforms-and-operations/litellm) gateway.

Trying a different model is a matter of changing its name, which keeps us from committing to a single model provider too early. API keys can carry their own credit limit, so a project or experiment cannot run up an unbounded bill.

OpenRouter is a US company. Even when a request ends up at an EU-hosted model, it passes through a service outside EU jurisdiction, and its EU in-region routing for enterprise customers does not change that. For clients with digital sovereignty requirements we are assessing [EU LLM Routers](/platforms-and-operations/eu-llm-routers) as an alternative.
