---
title: "TypeScript stack and tooling"
ring: adopt
quadrant: languages-and-frameworks
featured: true
---

We prefer [TypeScript](https://www.typescriptlang.org/) over JavaScript for frontends and backends alike. One typed language across the stack lets engineers move between projects, and it gives coding agents a type checker that catches their mistakes before a reviewer has to.

Within TypeScript these are our preferred choices for new projects. They are defaults, not rules: deviate when a project has good reasons, and discuss it in the team.

- **[Next.js](https://nextjs.org/) or [TanStack Start](https://tanstack.com/start)** as the full-stack framework. Next.js is our established choice and remains a good fit, especially for content-heavy public sites. For new application-like products we increasingly use TanStack Start (1.0 since October 2026): built on Vite, with type-safe routing and server functions.

- **Contract-first typed APIs.** Define the API contract in code and publish it as OpenAPI, with [oRPC](https://orpc.unnoq.com/) or ts-rest, in line with our preference for REST over [GraphQL](/languages-and-frameworks/graphql). [tRPC](https://trpc.io/) is fine when client and server live in the same TypeScript monorepo and the API has no other consumers.

- **[Drizzle ORM](https://orm.drizzle.team/)** for data access. It stays close to SQL, is fully typed and generates plain SQL migrations. Our newer projects use it; older projects on Prisma do not need to migrate.

- **[better-auth](https://www.better-auth.com/)** for authentication inside an application. When several applications share users or a central identity provider is needed, use [Keycloak](/platforms-and-operations/keycloak).

- **[Tailwind CSS](https://tailwindcss.com/) with [shadcn/ui](https://ui.shadcn.com/)** for styling and components. shadcn/ui builds on Radix primitives and gives us accessible components we own as source code instead of as a dependency.

- **[Zod](https://zod.dev/)** for schemas and validation. One schema validates input at runtime and provides the static type, shared between client, server and API contracts.

- **[Bun](https://bun.sh/) and [Biome](https://biomejs.dev/)** in our newer templates. Bun installs, runs TypeScript and tests without extra tooling; Biome replaces ESLint plus Prettier with one fast tool. Node.js (LTS) and ESLint with Prettier remain common in our projects and are fine.

Beyond that we use the usual building blocks: React, Vite, Vitest, Turborepo and [Playwright](/tools/playwright), with [TanStack Query](/languages-and-frameworks/tanstack-query) for server state and [React Native](/languages-and-frameworks/react-native) for mobile.
