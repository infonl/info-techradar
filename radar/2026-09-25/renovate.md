---
title: "Renovate"
ring: adopt
quadrant: tools
featured: true
---

We put [Renovate](https://docs.renovatebot.com/) back on adopt. It is our preferred tool for automated dependency updates, and we prefer it over Dependabot because it gives us more features and more flexibility.

Even though we standardise on [GitHub](/tools/github), where Dependabot is available out-of-the-box, Renovate is considerably more powerful and configurable.

### Why Renovate over Dependabot?

- **More features:** Dependency dashboard per repository, grouping of related updates, separate major/minor/patch handling, automerge rules, vulnerability alerts and broad support for languages, package managers and monorepos.

- **More flexibility:** Fine-grained control over scheduling, grouping, automerge and versioning through shareable presets, so we can define one organisation-wide configuration and override it per project where needed.

- **Platform agnostic:** The same configuration works across GitHub, GitLab, Bitbucket, Azure DevOps and self-hosted setups, so we are not locked in to a single forge.
