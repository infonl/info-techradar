---
title: "Keycloak"
ring: adopt
quadrant: platforms-and-operations
featured: true
---

[Keycloak](https://www.keycloak.org/) is our preferred Identity and Access Management (IAM) solution for our [Common Ground](https://commonground.nl/) projects, and more generally whenever we do not want to depend on similar IAM SaaS cloud services.

It is the choice when several applications share users, or when single sign-on and identity federation are needed. For authentication inside a single application we use better-auth, as part of our [TypeScript stack and tooling](/languages-and-frameworks/typescript).

In one project we use [ZITADEL](https://zitadel.com/) as a lighter alternative: PostgreSQL-only, with multi-tenancy built in. It is open source under AGPL 3.0 since 2025, from a Swiss company. Keycloak remains our default.
