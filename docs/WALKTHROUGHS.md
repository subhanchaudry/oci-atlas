# Application architecture walkthroughs

The [packaged walkthroughs](../plugins/oci-atlas/skills/oci-atlas/references/walkthroughs.md) connect three customer goals to OCI service choices, data paths, identities and operating responsibilities:

- A small containerized API with an HTTPS entry point.
- A private application connected to Autonomous Database.
- Retrieval-augmented generation over application documents.

For additional workloads, use [workload selection](../plugins/oci-atlas/skills/oci-atlas/references/workload-selection.md). For source code and configuration, use the [private API and RAG examples](../examples/README.md).

The v1.2 walkthrough updates connect registry caches, separate database MCP services, and Enterprise AI hosting to these designs. They do not change the runnable examples or establish that those examples were deployed with the new services. See [what changed](WHATS-NEW-1.2.md) and the [validation scope](VALIDATION-1.2.md).
