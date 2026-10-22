# How to use the INFO Technology Radar

## What's new in this version (22 October 2026)
This version replaces the previous edition of 23 April 2026. It bundles all updates we made to the radar during
August and September 2026. The main themes are a stronger preference for European, open and sovereign solutions,
an agentic-first way of working, and our open source Data & AI stack.

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

## Introduction
The [INFO](https://info.nl) Tech Radar contains a high-level list of preferred technologies that we like to use for the solutions that we build for our clients. 
It also contains technologies that we would like to trial as well as technologies that we want to put on hold.
The INFO Tech Radar was built using the [AOE People Tech Radar generator](https://github.com/AOEpeople/techradar), 
and we continue to be inspired by the [ThoughtWorks Technology Radar](https://www.thoughtworks.com/radar)

## Purpose of the INFO Technology Radar
The purpose of the INFO technology radar is:
- To give focus on our INFO technology innovation strategy.
- To help make technology decisions for our client teams.
- To give guidance in the career growth paths of our technical employees
- To share our technology strategy with our (potential new) clients and potential new employees.

## Who maintains the INFO Technology Radar?
This is the responsibility of the tech and design radar working group at INFO. 
We will try our best to involve all relevant people at INFO where we can and try to make the radar shared by all of us. 
Everyone at INFO can contribute to the technology radar.

## How to use the INFO Technology Radar?
The INFO tech radar contains a list of current preferred technologies for new technical solutions in our teams,
as well as technologies that we would like to trial.
Read and use it when defining your team's technology vision for new solutions or major changes.
There may be perfectly valid reasons to deviate from the INFO Tech Radar in our teams. 
We do ask our teams to always discuss such deviations.

Note that our tech radar is not a complete list of our preferred technologies.
To keep it manageable, we only include technologies that we think are currently relevant to our teams.

### Quadrants
We group the items on the tech radar in four quadrants:

- Languages & Frameworks: programming languages and software frameworks
- Tools: software products such as content management systems as well as software development tools
- Techniques: architectural techniques, elements of our software development process, best practices, and such
- Platforms: things that we build software on top of such as cloud-native platforms

### Rings
Every quadrant is divided into three rings:

- Adopt: We can clearly recommend this technology. We have used it for a longer period of time in many teams, and it has proven to be stable and useful.
- Trial: We have tried it, or want to try it, and find it promising. We recommend having a closer look at the technology in this ring, especially when you face a specific need for it in your project. The goal of items here is to look at them more closely, with the goal to bring them to the 'adopt' ring.
- Hold: This category is a bit special. Unlike the others, we recommend stopping doing or using something. That does not mean that they are bad, and it often might be ok to use them in existing projects. But we move things here if we think we shouldn't do them any more because we see better options or alternatives now.

### Design-related choices
This tech radar does not cover design tools and choices. For those, see the [INFO Design radar](https://infonl.atlassian.net/wiki/spaces/exp/pages/966688781/INFO+Design+radar).
Currently only accessible to INFO employees, but publicly available in the future.

