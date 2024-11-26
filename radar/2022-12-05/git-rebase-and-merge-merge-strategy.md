---
title: "Rebase and merge as Git merge strategy"
ring: adopt
quadrant: methods-and-patterns
featured: true
---

In the context of maintaining repositories using Git we prefer a rebase and merge Git merge strategy (rebase + merge --no-ff) so that the Git history in our codebases is linear. 

Git’s default strategy is to merge commits in chronological order, however having an overview of the sequence in which changes to the codebase were made is often more useful in understanding how the codebase evolved over time. This is the reason why we prefer a rebase + merge strategy.

Generally all our Git repo's in <a href="github.html">GitHub</a> should be configured to support this merge strategy.

We also strongly encourage to squash commits when merging a feature branch onto the main branch in order to keep the Git log clean. There is typically no need to keep the history of individual commits in a feature branch in our view.