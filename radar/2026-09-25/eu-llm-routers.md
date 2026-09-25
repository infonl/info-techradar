---
title: "EU LLM Routers"
ring: assess
quadrant: platforms-and-operations
featured: true
---

EU LLM routers offer what [OpenRouter](/platforms-and-operations/openrouter) offers (one API for many models, switching models without code changes), but they are operated by European companies, with the option to keep routing and inference in the EU. They are the router counterpart of the [European Sovereign Cloud](/platforms-and-operations/european-sovereign-cloud).

We like the router approach because it keeps us independent of any single model provider. What we are missing is an EU-based router for clients who cannot send their data through a US service. We are assessing two candidates:

- **[Eden AI](https://www.edenai.co/)** (Lyon, France): unified API for LLMs plus OCR, speech, translation and vision models. An EU company that offers a standard data processing agreement.

- **[EUrouter](https://www.eurouter.ai/)**: routes to 100+ models hosted on European infrastructure (Scaleway, OVHcloud, Mistral AI and others), optionally restricted to a single country. It has an OpenAI-compatible API and positions itself as a drop-in OpenRouter replacement.

Both would slot in behind our [LiteLLM](/platforms-and-operations/litellm) gateway as just another upstream, so trying them costs little.

### What we look at

- **Jurisdiction:** EU-registered entity, EU-hosted routing and inference, and a data processing agreement.
- **Model coverage:** Does it offer the models we actually use, including open-weight ones?
- **Budgets and key management:** On par with what OpenRouter offers today.
- **Price and reliability:** Markup over direct provider pricing, uptime and fallback behaviour.
