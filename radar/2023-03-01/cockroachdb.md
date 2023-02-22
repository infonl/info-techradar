---
title: "CockroachDB"
ring: hold
quadrant: platforms
featured: true
---

In the space of <a href="dbaas.html">DBaaS</a> services, we have trialed <a href="https://www.cockroachlabs.com/">CockroachDB</a> to see if it could be our preferred DBaaS solution, and if so, under what circumstances it would be our preferred choice. 

We have decided to hold off on using CockroachDB for the time being because we feel it is overkill for our current needs where we typically have no need for large-scale data distribution. For now we think for most of our needs 'plain' [PostgreSQL](postgresql.md) (as a PaaS) is a better fit when it comes to relational databases.