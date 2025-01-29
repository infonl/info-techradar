---
title: "Docker Developer Environments"
ring: assess
quadrant: tools
featured: true
---

[Docker Development Environments](https://docs.docker.com/desktop/features/dev-environments) is still in preview, but the idea is that the whole code base,
including development setup for coding in [Visual Studio Code](/tools/visual-studio-code). It can be a single container, or a
compose based set of containers that make up a whole project. Any changes made in the code can be
pushed as a new snapshot image to a docker repository, from where an other developer can continue in
the same state.
