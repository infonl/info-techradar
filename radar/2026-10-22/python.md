---
title: "Python"
ring: adopt
quadrant: languages-and-frameworks
featured: true
---

Preferred language for AI & data science because it is world-wide the leading programming language
for AI & data science by far.

We also prefer Python for scripting tasks over Shell Scripts (or other scripting languages)
when the following conditions apply:

- There is no obvious candidate for a scripting language for the task at hand in the context of the
current tech stack. E.g. a certain product may include a default scripting language within its tech
stack. This may then be a more logical candidate.
- The logic to be implemented is non-trivial, but also not overly complex. If the logic is very simple
a Shell Script is often a better choice because it is a very standard solution and Python will
quickly be overkill. If the logic is too complex then a script may not be the best solution in any
case and it will make sense to look into a proper (backend) software solution to implement the
logic.

### Tooling

- **[uv](https://docs.astral.sh/uv/)** manages Python versions, virtual environments and dependencies with a lockfile, replacing pip, pyenv and Poetry with one fast tool.
- **[Ruff](https://docs.astral.sh/ruff/)** for linting and formatting.
- **[ty](https://docs.astral.sh/ty/)** for type checking. It is still in beta, so use mypy or Pyright where it does not cover your needs yet.
