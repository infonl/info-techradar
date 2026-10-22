# Release Notes

What has changed in each version of the INFO Technology Radar, newest first.

## What's new in Version #10
Compared to Version #9, this version bundles all updates we made to the radar during August and September 2026.
The main themes are a stronger preference for European, open and sovereign solutions, an agentic-first way of working, and our open source Data & AI stack.

### Rings
- The **Assess** ring has been merged into **Trial**.

### New
- [Spec Driven Development (SDD)](/methods-and-patterns/spec-driven-development) (Adopt): how we make our agentic-first way of working work in practice.
- [Claude Code](/tools/claude-code) (Adopt): our preferred agentic coding tool.
- [OpenSpec](/tools/openspec) (Adopt) and [Spec-Kit](/tools/spec-kit) (Trial): tools to structure spec-driven development. Pick one per project.
- [OpenTelemetry](/methods-and-patterns/opentelemetry) (Adopt): the vendor-neutral standard we instrument our applications with.
- [OpenTofu](/tools/opentofu) (Adopt): our default tool for Infrastructure as Code, replacing Terraform.
- [Argo CD](/tools/argocd) (Trial): GitOps continuous delivery for Kubernetes.
- [Apache Iceberg](/platforms-and-operations/apache-iceberg) (Adopt) and [DuckDB](/tools/duckdb) (Adopt): the foundation of our open source lakehouse, with [DuckLake](/platforms-and-operations/ducklake) (Trial) as a simpler alternative we are piloting.
- [LiteLLM](/platforms-and-operations/litellm) (Adopt) and [OpenRouter](/platforms-and-operations/openrouter) (Adopt): our self-hosted AI gateway and the hosted LLM router behind it.
- [EU LLM Routers](/platforms-and-operations/eu-llm-routers) (Trial): European alternatives to OpenRouter for clients with sovereignty requirements.
- [vLLM](/platforms-and-operations/vllm) (Trial): self-hosted inference for open-weight models.
- [Model Context Protocol (MCP)](/languages-and-frameworks/model-context-protocol) (Adopt): the open standard we use to package AI capabilities as reusable servers.
- [LLM Tracing and Evals](/methods-and-patterns/llm-tracing-and-evals) (Trial): making the behaviour of LLM applications visible and testable.
- [Dagster / Argo Workflows](/tools/dagster-argo-workflows) (Trial): the orchestrators we use for data pipelines and container batch jobs.
- [CloudNativePG](/platforms-and-operations/cloudnativepg) (Trial): a Kubernetes operator for PostgreSQL, where no suitable managed database is available.
- [OpenBao](/platforms-and-operations/openbao) (Trial): the open source fork of HashiCorp Vault, as a central secrets store.

### Moved
- [European Sovereign Cloud](/platforms-and-operations/european-sovereign-cloud) moves from Trial to **Adopt**. We now generally prefer a European sovereign cloud provider over the US hyperscalers. [AWS](/platforms-and-operations/aws) and [Azure](/platforms-and-operations/azure) remain in Adopt, with AWS our preferred US hyperscaler.
- [Databricks](/tools/databricks) moves from Trial to **Adopt**, next to the open source lakehouse we prefer for our own projects.
- [Keycloak](/platforms-and-operations/keycloak) moves from Hold back to **Adopt** as our preferred IAM solution.
- [Renovate](/tools/renovate) moves from Hold back to **Adopt**, in preference to Dependabot.
- [GraphQL](/languages-and-frameworks/graphql) moves from Adopt to **Hold**. For new projects we prefer REST.
- [GitHub Copilot](/tools/github-copilot) moves from Adopt to **Hold**. We prefer Claude Code.
- [DORA Metrics](/methods-and-patterns/dora) moves from Adopt to **Trial**, while we work out how to use them in an agentic way of working.
- [Snyk](/tools/snyk) moves from Assess to **Adopt**.
- [Go](/languages-and-frameworks/go) moves from Assess to **Hold**. We are still interested in Go, but it does not have our focus right now.

### Updated
- [BDD](/methods-and-patterns/bdd), [Domain Driven Design (DDD)](/methods-and-patterns/domain-driven-design) and [Event-driven Architecture](/methods-and-patterns/event-driven-architecture) have been rewritten, and BDD and DDD are now linked to Spec Driven Development.
- [TypeScript stack and tooling](/languages-and-frameworks/typescript) now describes our preferred choices within TypeScript, such as Next.js or TanStack Start, contract-first typed APIs, Drizzle ORM, better-auth, Tailwind CSS with shadcn/ui, Zod, Bun and Biome. [Node.js](/languages-and-frameworks/nodejs) is now covered by it and no longer featured on its own.
- [Python](/languages-and-frameworks/python) now lists our preferred tooling (uv, Ruff and ty), and [React Native](/languages-and-frameworks/react-native) now describes how we use it with Expo.
- [Keycloak](/platforms-and-operations/keycloak) now explains when to use it and when to use better-auth or ZITADEL instead.
- [GitHub](/tools/github) now mentions the European alternatives we are assessing, such as Forgejo, Codeberg and code.overheid.nl.
- [Kubernetes](/tools/kubernetes), [Valkey / Redis](/platforms-and-operations/redis) (we now prefer Valkey), [TanStack Query](/languages-and-frameworks/tanstack-query), [Grafana](/tools/grafana), [European Sovereign Cloud](/platforms-and-operations/european-sovereign-cloud) and [Infrastructure as Code](/methods-and-patterns/infrastructure-as-code) (now including pyinfra) have been updated.

### Removed
We reviewed all items and removed the ones that are no longer relevant to our teams: Algolia, Amazon Cognito, Amazon S3,
AWS IAM, Axiom, Backstage, Clerk, CockroachDB, Contentful, Cypress, Database as a Service, DigitalOcean, Event Sourcing,
GitHub Code Spaces, GitHub Packages, Jamstack, k6, Low-code / no-code development, NestJS, Platform as a Service,
Pulumi, React testing library, Rebase and merge as Git merge strategy, Render, Sanity, Serverless,
Serverless Framework, Snowflake, Storyblok, Strapi, Terraform (replaced by OpenTofu) and Vercel, as well as a number
of older items that were no longer shown on the radar. Next.js, Prisma, Tailwind CSS, tRPC and Turborepo are no longer
separate items: where still relevant, they are covered by [TypeScript stack and tooling](/languages-and-frameworks/typescript). Figma has moved to the
[INFO Design radar](https://infonl.atlassian.net/wiki/spaces/exp/pages/966688781/INFO+Design+radar).
