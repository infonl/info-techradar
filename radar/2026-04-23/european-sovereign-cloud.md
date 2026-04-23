---
title: "European Sovereign Cloud"
ring: trial
quadrant: platforms-and-operations
featured: true
---

European Sovereign Cloud refers to cloud infrastructure operated by European providers, subject exclusively to EU jurisdiction, and designed to guarantee full digital sovereignty. As geopolitical tensions and extraterritorial legislation (such as the US CLOUD Act and FISA Section 702) create uncertainty around data processed by non-EU cloud providers, the need for genuinely sovereign alternatives has become a strategic priority — particularly for organisations handling sensitive data or operating in regulated sectors.

### Why European Sovereign Cloud?

- **Digital Sovereignty:** Ensures that data, infrastructure, and operations remain entirely within EU legal jurisdiction, eliminating exposure to non-EU government access requests.

- **GDPR & Schrems II Compliance:** Following the Schrems II ruling, transferring personal data to US-based providers carries inherent legal risk. European sovereign cloud providers eliminate this concern by design.

- **Regulatory Alignment:** Sectors such as government ([BIO](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cybersecurity/kaders-voor-cybersecurity/baseline-informatiebeveiliging-overheid/)), healthcare ([NEN 7510](https://www.nen.nl/nen-7510-1-2017-nl-238898)), and finance increasingly require or strongly prefer data processing within EU borders by EU-controlled entities.

- **Reducing Strategic Dependency:** Reliance on a small number of US hyperscalers (AWS, Azure, GCP) creates concentration risk. Diversifying towards European providers strengthens organisational resilience.

- **GAIA-X & European Cloud Initiatives:** The [GAIA-X](https://gaia-x.eu/) initiative promotes interoperable, transparent, and sovereign data infrastructure across Europe. Selecting providers aligned with these principles future-proofs the investment.

### Key Selection Criteria

When evaluating a European sovereign cloud provider, the following criteria are essential:

- **EU Ownership & Jurisdiction:** The provider must be an EU-registered entity with no controlling interest by non-EU parties.

- **OpenStack or Open API:** An open, standardised API — preferably [OpenStack](https://www.openstack.org/) — significantly reduces vendor lock-in. OpenStack is the de facto open standard for cloud infrastructure and enables portability across providers.

- **Managed Kubernetes:** A mature, managed Kubernetes offering is critical for modern application deployment and operations.

- **Comprehensive Service Catalogue:** Beyond compute and storage, look for managed databases, object storage, load balancers, DNS, backup services, VPN/networking, and monitoring.

- **Infrastructure as Code Compatibility:** First-class support for [Terraform](/tools/terraform) / [OpenTofu](https://opentofu.org/) providers is essential for automation and reproducibility.

- **Certifications:** ISO 27001, SOC 2, and — depending on context — NEN 7510 (healthcare) or BIO (Dutch government) compliance.

- **Data Centre Location:** Preference for Dutch or at minimum EU-based data centres with transparent information about physical locations.

### Provider Assessment

#### Cyso (Netherlands) — Shortlisted

[Cyso](https://cyso.com/) is a Dutch cloud provider offering OpenStack-based infrastructure with data centres in the Netherlands.

- **Strengths:** Dutch entity, OpenStack API (maximises portability), Kubernetes support, strong focus on managed hosting and compliance, ISO 27001 certified.
- **Considerations:** Smaller scale compared to hyperscalers; evaluate depth of managed services catalogue (databases, backups, monitoring) and support SLA.
- **Verdict:** Strong fit for sovereignty requirements. The OpenStack API is a significant advantage for avoiding lock-in. Recommended for further evaluation.

#### Scaleway (France) — Under Evaluation

[Scaleway](https://www.scaleway.com/) is a French cloud provider (part of the Iliad Group) offering a broad and modern cloud platform.

- **Strengths:** Comprehensive service catalogue (managed Kubernetes / Kapsule, managed databases, object storage, serverless, container registry), competitive pricing, strong developer experience, modern API and CLI tooling, French/EU data centres.
- **Considerations:** Does not use OpenStack — uses a proprietary (but well-documented) API, which increases provider-specific coupling. However, a Terraform provider is available, mitigating some lock-in risk. French entity, so not Dutch — but firmly within EU jurisdiction.
- **Verdict:** Excellent technical offering with a broad service catalogue. The lack of OpenStack is a trade-off against the richness of features. Good option if the team accepts a degree of API-level coupling.

#### OVHcloud (France) — Alternative

[OVHcloud](https://www.ovhcloud.com/) is one of Europe's largest cloud providers and a founding member of GAIA-X.

- **Strengths:** OpenStack-based public cloud, managed Kubernetes, extensive global data centre network (with multiple EU locations including the Netherlands), competitive pricing, ISO 27001 and HDS certified, GAIA-X member. Terraform provider available.
- **Considerations:** Mixed reputation for support quality. Some enterprise-grade managed services (e.g. advanced database options) lag behind hyperscalers. Recent data centre incidents (Strasbourg, 2021) raised questions about resilience practices — OVHcloud has since invested heavily in improvements.
- **Verdict:** Solid choice for OpenStack-based sovereign cloud. The scale of OVHcloud and GAIA-X membership are meaningful advantages.

#### STACKIT (Germany) — Alternative

[STACKIT](https://www.stackit.de/) is the cloud platform of the Schwarz Group (Lidl/Kaufmann), built on OpenStack.

- **Strengths:** German entity backed by one of Europe's largest retail groups, OpenStack-based, managed Kubernetes (SKE), managed databases (PostgreSQL, MariaDB, Redis, RabbitMQ), object storage, strong compliance posture (ISO 27001, C5), GAIA-X aligned. Terraform provider available. Notably, STACKIT has been contracted by De Nederlandsche Bank (DNB), underscoring its credibility and suitability for highly regulated financial institutions within the EU.
- **Considerations:** Relatively newer entrant to the public cloud market. The service catalogue is growing but may not yet match the breadth of Scaleway or OVHcloud. Less mature community and ecosystem.
- **Verdict:** Strong and increasingly credible choice backed by significant investment and validated by adoption in the European financial sector. OpenStack base and German sovereignty credentials make it a serious contender.

### Other Notable Providers

- **[Cleura](https://cleura.com/)** (Sweden): OpenStack-based, formerly City Network. Strong sovereignty focus, compliant cloud, EU data centres.
- **[Open Telekom Cloud](https://open-telekom-cloud.com/)** (Germany): OpenStack-based, operated by T-Systems (Deutsche Telekom). Enterprise-grade with broad service catalogue.
- **[PCextreme](https://www.pcextreme.nl/)** (Netherlands): Dutch OpenStack provider (Aurora Cloud). Smaller scale but strong Dutch sovereignty credentials.

### Recommendation

We recommend a structured proof-of-concept comparing **Cyso** and **one other provider** (Scaleway for breadth of services, or OVHcloud/STACKIT for OpenStack portability). Key evaluation dimensions should include:

1. **Kubernetes maturity:** Deploy a representative workload and assess operational experience.
2. **Terraform/OpenTofu coverage:** Validate that all required resources can be provisioned as code.
3. **Managed services depth:** Evaluate database, backup, monitoring, and networking offerings against project requirements.
4. **Support & SLA:** Test responsiveness and quality of technical support.
5. **Exit strategy:** Confirm that workloads can be migrated to an alternative OpenStack provider or back to a hyperscaler if needed.

The sovereign cloud landscape in Europe is maturing rapidly. Placing this topic on **trial** reflects that these providers warrant serious evaluation for projects where digital sovereignty is a requirement, while at the same time acknowledging that a definitive recommendation requires hands-on validation.

---
