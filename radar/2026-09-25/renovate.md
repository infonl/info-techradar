---
title: "Renovate"
ring: adopt
quadrant: tools
featured: false
---

We put [Renovate](https://docs.renovatebot.com/) back on adopt. It is our preferred tool for automated dependency updates, in preference to Dependabot.

While we standardise on [GitHub](/tools/github), Renovate is platform agnostic and considerably more powerful and configurable than Dependabot.

### Why Renovate over Dependabot?

- **Platform agnostic:** The same configuration works across GitHub, GitLab, Bitbucket, Azure DevOps and self-hosted setups, so we are not locked in to a single forge.

- **More powerful and configurable:** Fine-grained control over grouping, scheduling, automerge and separate major/minor updates, with broad support for languages, package managers and monorepos.

- **Dependency dashboard:** A single overview of pending updates per repository makes it easy to keep dependencies current.
