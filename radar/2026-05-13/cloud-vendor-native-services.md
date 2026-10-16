---
title: "Cloud Vendor Native Services"
ring: adopt
quadrant: platforms-and-operations
featured: true
---

In the context of a cloud-native infrastructure for new client solutions, we generally prefer cloud-vendor native services (specific to [AWS](/platforms-and-operations/aws/) or [Azure](/platforms-and-operations/azure/)) over cloud-vendor agnostic alternatives, to use more functionality and integrate better with the rest of the cloud vendor's ecosystem, accepting an increased vendor lock-in, because native services typically expose capabilities that the abstracted alternatives flatten away.

### Why native over agnostic?

- **More functionality:** vendor-agnostic abstractions tend to surface a lowest-common-denominator feature set.
- **Better integration:** native services line up with vendor IAM, observability and networking out of the box.
- **Vendor lock-in is already partial:** many services we use have no agnostic equivalent — accepting native services elsewhere doesn't dramatically change the lock-in posture.

### Considerations at INFO

- Applies to new client solutions; existing solutions are not migrated for the sake of this preference.
- Deviation is fine when an agnostic open-market standard is a genuinely better fit, or when the client requires it.
- Specific refinements override this default — see [PostgreSQL](/platforms-and-operations/postgresql/), where we explicitly prefer the open standard over cloud-native relational alternatives.
- Cross-team skill transfer is harder when services are vendor-specific; the broader concepts (containers, queues, object storage) still translate.

For new INFO cloud solutions, native services are the default unless a vendor-agnostic option clearly wins on the specifics.
