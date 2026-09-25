---
title: "OpenTofu"
ring: adopt
quadrant: tools
featured: true
---

[OpenTofu](https://opentofu.org/) is the open source fork of Terraform, created after HashiCorp moved Terraform to the Business Source License in 2023. It is a CNCF project under the Linux Foundation, licensed under MPL 2.0 and compatible with the existing Terraform providers and modules.

OpenTofu is our default tool for [Infrastructure as Code](/methods-and-patterns/infrastructure-as-code). We use it in preference to provider-specific templating such as CloudFormation or ARM templates, and in preference to Terraform itself.

### Why OpenTofu?

- **One tool for every cloud:** The same workflow and language provision [AWS](/platforms-and-operations/aws), [Azure](/platforms-and-operations/azure) and European providers alike. Good provider support is one of our selection criteria for a [European Sovereign Cloud](/platforms-and-operations/european-sovereign-cloud), and it is what makes moving between clouds realistic.

- **Open license and governance:** An open license and vendor-neutral governance mean the tool at the core of our infrastructure cannot be relicensed from under us.

- **Drop-in for Terraform:** Existing Terraform code, providers and modules work, so migrating from Terraform 1.5 or older is usually a matter of swapping the binary.

- **Built-in state encryption:** State files often contain secrets. OpenTofu can encrypt them client-side, while Terraform relies on the backend to encrypt state at rest.
