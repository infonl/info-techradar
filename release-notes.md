# Release Notes

What has changed in each version of the INFO Technology Radar, newest first.

## What's new in Version #10
Compared to Version #9, this version bundles all updates we made to the radar during August and September 2026.
The main themes are a stronger preference for European, open and sovereign solutions, an agentic-first way of working, and our open source Data & AI stack.

### Rings
- The **Assess** ring has been merged into **Trial**. Items that were in Assess ([Go](/languages-and-frameworks/go), [Snyk](/tools/snyk)) are now in Trial.

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

### Moved
- [European Sovereign Cloud](/platforms-and-operations/european-sovereign-cloud) moves from Trial to **Adopt**. We now generally prefer a European sovereign cloud provider over the US hyperscalers. [AWS](/platforms-and-operations/aws) and [Azure](/platforms-and-operations/azure) remain in Adopt, with AWS our preferred US hyperscaler.
- [Databricks](/tools/databricks) moves from Trial to **Adopt**, next to the open source lakehouse we prefer for our own projects.
- [Keycloak](/platforms-and-operations/keycloak) moves from Hold back to **Adopt** as our preferred IAM solution.
- [Renovate](/tools/renovate) moves from Hold back to **Adopt**, in preference to Dependabot.
- [GraphQL](/languages-and-frameworks/graphql) moves from Adopt to **Hold**. For new projects we prefer REST.
- [GitHub Copilot](/tools/github-copilot) moves from Adopt to **Hold**. We prefer Claude Code.
- [DORA Metrics](/methods-and-patterns/dora) moves from Adopt to **Trial**, while we work out how to use them in an agentic way of working.

### Updated
- [BDD](/methods-and-patterns/bdd), [Domain Driven Design (DDD)](/methods-and-patterns/domain-driven-design) and [Event-driven Architecture](/methods-and-patterns/event-driven-architecture) have been rewritten, and BDD and DDD are now linked to Spec Driven Development.
- [GitHub](/tools/github) now mentions the European alternatives we are assessing, such as Forgejo, Codeberg and code.overheid.nl.
- [Kubernetes](/tools/kubernetes), [Valkey / Redis](/platforms-and-operations/redis) (we now prefer Valkey), [TanStack Query](/languages-and-frameworks/tanstack-query), [Grafana](/tools/grafana) and [Infrastructure as Code](/methods-and-patterns/infrastructure-as-code) have been updated.

### Removed
We reviewed all items and removed the ones that are no longer relevant to our teams: Algolia, Amazon Cognito, Amazon S3,
AWS IAM, Axiom, Backstage, Clerk, CockroachDB, Contentful, Cypress, Database as a Service, DigitalOcean, Event Sourcing,
GitHub Code Spaces, GitHub Packages, Jamstack, k6, Low-code / no-code development, NestJS, Next.js, Platform as a Service,
Prisma, Pulumi, React testing library, Rebase and merge as Git merge strategy, Render, Sanity, Serverless,
Serverless Framework, Snowflake, Storyblok, Strapi, Tailwind CSS, Terraform (replaced by OpenTofu), tRPC, Turborepo
and Vercel, as well as a number of older items that were no longer shown on the radar. Figma has moved to the
[INFO Design radar](https://infonl.atlassian.net/wiki/spaces/exp/pages/966688781/INFO+Design+radar).
