---
title: "TypeScript stack and tooling"
ring: adopt
quadrant: languages-and-frameworks
featured: true
---

We prefer [TypeScript](https://www.typescriptlang.org/) over JavaScript for frontends and backends alike. One typed language across the stack lets engineers move between projects, and it gives coding agents a type checker that catches their mistakes before a reviewer has to.

Within TypeScript we have a set of preferred building blocks. They are defaults for new projects, not rules: deviate when a project has good reasons, and discuss it in the team.

- **React** for web user interfaces. It is the library our engineers know best, which matters when reviewing agent-written code. For mobile we use [React Native](/languages-and-frameworks/react-native).

- **[Next.js](https://nextjs.org/) or [TanStack Start](https://tanstack.com/start)** as the full-stack framework. Use Next.js for content-heavy and public-facing sites where server rendering, SEO and its mature ecosystem pay off. Use TanStack Start for application-like products: it is built on Vite, has end-to-end type-safe routing and server functions, and deploys to any host. TanStack Start reached 1.0 in October 2026.

- **[Vite](https://vite.dev/)** as the build tool and dev server, directly or underneath TanStack Start. Fast feedback and a large plugin ecosystem.

- **[Tailwind CSS](https://tailwindcss.com/)** for styling, with [shadcn/ui](https://ui.shadcn.com/) on Radix primitives for accessible components we own as source code instead of as a dependency.

- **[Zod](https://zod.dev/)** for schemas and validation. One schema validates input at runtime and provides the static type, and the same schema is shared between client, server and API contracts.

- **Contract-first typed APIs.** Use [tRPC](https://trpc.io/) when client and server live in the same TypeScript monorepo. When the API has other consumers, define the contract with [oRPC](https://orpc.unnoq.com/) or ts-rest and publish it as OpenAPI. We prefer this over [GraphQL](/languages-and-frameworks/graphql).

- **[Drizzle ORM](https://orm.drizzle.team/)** for data access. It stays close to SQL, is fully typed and generates plain SQL migrations. We prefer it over Prisma.

- **[better-auth](https://www.better-auth.com/)** for authentication inside an application. When several applications share users or a central identity provider is needed, use [Keycloak](/platforms-and-operations/keycloak).

- **[TanStack Query](/languages-and-frameworks/tanstack-query)** for server state in the frontend.

- **Node.js or Bun** as runtime. Node.js (LTS) is the safe default. Our newer project templates use [Bun](https://bun.sh/), which installs, runs TypeScript and tests without extra tooling.

- **[Turborepo](https://turborepo.com/)** for monorepos: it caches and parallelises tasks across packages, so builds and CI stay fast as the repo grows.

- **[Vitest](https://vitest.dev/)** for unit and integration tests, with Jest-compatible APIs and native TypeScript and Vite support. [Playwright](/tools/playwright) for end-to-end tests.

- **[Biome](https://biomejs.dev/)** for linting and formatting in new projects: one fast tool instead of ESLint plus Prettier. ESLint and Prettier remain fine in existing projects.

For a standalone backend service we have no single preferred framework. NestJS suits teams that want structure and dependency injection, Fastify suits lean services.
