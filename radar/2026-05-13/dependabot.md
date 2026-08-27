---
title: "GitHub Dependabot"
ring: adopt
quadrant: tools
featured: true
---

[Dependabot](https://github.com/dependabot) is GitHub's built-in automated dependency update tool — it scans repositories and opens pull requests when newer versions of declared dependencies become available.

### Why Dependabot?

- **Security responsibility:** keeping libraries up to date is part of how we deliver secure software for our clients, and the volume of updates across services makes manual tracking impractical.
- **Native to our SCM:** we've standardised on [GitHub](/tools/github/), so Dependabot needs no extra infrastructure and integrates with the existing PR / CI flow.
- **Covers the languages we use:** first-class support for the [Node.js](/languages-and-frameworks/nodejs/) / [TypeScript](/languages-and-frameworks/typescript/) stack and the other ecosystems we touch.

### Considerations at INFO

- Every team is expected to have an automated dependency update process; Dependabot is our default mechanism for that on GitHub.
- The principle is "automated dependency updates," not "Dependabot specifically" — projects with a strong reason can use an alternative, but they have to actually run *something*.
- **Current Focus:** Renovate was previously our recommendation but is now on [hold](/tools/renovate/); new projects start with Dependabot.

For GitHub-hosted INFO projects, Dependabot is our default automated dependency-update tool.
