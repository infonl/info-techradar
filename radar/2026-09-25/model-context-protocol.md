---
title: "Model Context Protocol (MCP)"
ring: adopt
quadrant: languages-and-frameworks
featured: true
---

The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) is an open standard for connecting AI applications to tools and data. An MCP server exposes tools, resources and prompts once, and every MCP-capable client (chat applications, agents, coding assistants such as [Claude Code](/tools/claude-code)) can use them.

We use MCP to package capabilities such as retrieval over our data as reusable servers, with our own template and conformance tests so that every server behaves the same way.

### Why MCP?

- **Build once, reuse everywhere:** A capability built as an MCP server is not tied to one application, model or vendor. That fits our aim to reuse skills and components across Data & AI projects.

- **Open standard:** Governed by the Linux Foundation's Agentic AI Foundation and supported by all major model providers, with official SDKs in the languages we use.

### Considerations

- **Security:** An MCP server acts with the permissions it is given. Treat every server as an integration with a trust boundary: scope its access, authenticate clients and be careful with third-party servers.
