# OCI Atlas application examples

Start with an existing OCI network, database, and authenticated identity. Each example describes the resources it consumes, the configuration it owns, and how to remove its own artifacts.

| Example | Outcome | Existing services |
| --- | --- | --- |
| [Private container API](container-api/README.md) | Run a Python API on Container Instances and check private SQL access | Private subnet/NSGs, Autonomous Database, credential secret, image repository |
| [Document RAG](rag/README.md) | Ingest documents, retrieve passages, and generate source-referenced answers | Object Storage, vector-capable Autonomous Database, Generative AI endpoints, credential secret |

Use the [workload guide](../plugins/oci-atlas/skills/oci-atlas/references/workload-selection.md) to compare architectures. Examples are versioned with the plugin; use the same release tag for both. The plugin ZIP contains guidance; application source lives here.

These examples use original application code under the repository's UPL 1.0 license. Installed dependencies retain their own licenses; no third-party source is vendored. Exact dependency versions are recorded in each requirements file. Container base images use a versioned Python tag; pin your approved image digest and retain the recorded dependency versions for your organization's release process.
