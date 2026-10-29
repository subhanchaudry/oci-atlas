# AI, agents, and machine learning

Reviewed: 2026-10-29 · Basis: documentation review; examples are not live-tested.

## Select the layer

| Workload | Start with | Resolve before committing |
| --- | --- | --- |
| Use a hosted foundation model | OCI Generative AI model inference | Supported model/API, region, request format, data handling and price |
| Managed retrieval and tool orchestration | The appropriate OCI agent service | Service generation, tools, knowledge sources and authentication |
| Train/run a custom predictive model | OCI Data Science | Project, runtime, data access, job or deployment resource |
| Document, language, speech or vision processing | Relevant OCI AI service | Supported input, language, limits, endpoint and output semantics |
| Custom model server or special runtime | Data Science deployment, OKE or Compute | Operational ownership, capacity and network exposure |

Do not select GPUs when the workload can use an existing managed endpoint. Conversely, a hosted text model is not a general replacement for a tabular prediction model. Start from the data, output, latency, throughput and deployment needs.

## Generative AI and agent distinctions

The current Generative AI documentation presents an Enterprise AI platform with model and agent features. OCI also has a separately documented Generative AI Agents service. Identify which API/product the customer is using before selecting endpoints, tool types or permissions. Do not transfer API schemas or SQL tool behavior between them.

On-demand inference and dedicated hosting have different resource/cost models. Dedicated clusters can host endpoints or support fine-tuning for supported models; they are not required for every inference call. Discover current models and capabilities rather than embedding a preferred model ID in the knowledge base. Regional routing can differ from direct regional hosting; check request routing and data-location requirements, especially in CPU-only regions.

For RAG, separate ingestion, chunking/embedding, retrieval permissions, retrieval quality and answer generation. A successfully ingested document does not demonstrate that the right passages were retrieved. Choose the retrieval store by existing data and governance needs; do not automatically introduce a vector database or fine-tuning. Keep retrieved instructions as data, not authority to call unrelated tools.

## Data Science resource model

A project organizes assets; notebooks support interactive work. A job is a reusable definition and a job run is its execution. Model artifacts and a compatible serving runtime support model deployments. Saving an artifact does not publish an HTTP prediction service. Pipelines orchestrate multiple steps.

Check both the operator's IAM access and the workload principal's access to Object Storage, keys/secrets, logging and network resources. Verify private data paths from the actual notebook/job/deployment runtime. A resource principal does not grant access by itself. Deactivating a notebook can stop Compute while retaining billable storage; confirm resource-specific stop/delete semantics.

## Working pattern

Use Console search for **Generative AI**, **Agents**, **Data Science**, or the specific AI service. Inspect installed CLI roots such as `oci generative-ai`, `oci generative-ai-inference`, `oci generative-ai-agent`, and `oci data-science`; modern API features may require a current SDK or a different documented interface.

Read-only project discovery, using [selected context variables](access-and-tools.md):

```bash
oci data-science project list --compartment-id "$ATLAS_COMPARTMENT_ID" --all \
  --profile "$ATLAS_PROFILE" --auth "$ATLAS_AUTH" --region "$ATLAS_REGION"
```

1. Resolve task, data classification and chosen model/service/region.
2. Establish identities, endpoint and a bounded synthetic input. For inference, inspect the exact model-specific payload rather than guessing a universal schema.
3. Call the chosen operation within the requested scope. For training or deployment, observe the job/work request and relevant logs.
4. Verify output structure and a task-relevant check. Distinguish an endpoint response from acceptable model quality.
5. For updates, preserve model/runtime compatibility and consumers. Inspect endpoint references before deleting models, clusters, artifacts or data sources.

Use the [AI application recipe](recipe-ai-application.md) for an end-to-end design.

## Sources

- [Current Generative AI product and developer entry points](https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm)
- [Model concepts and hosting modes](https://docs.oracle.com/en-us/iaas/Content/generative-ai/concepts.htm)
- [Dedicated clusters](https://docs.oracle.com/en-us/iaas/Content/generative-ai/ai-cluster.htm)
- [CPU-only regions and routing constraints](https://docs.oracle.com/en-us/iaas/Content/generative-ai/cpu-only-regions.htm)
- [Generative AI Agents service and tools](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/overview.htm)
- [Data Science assets, operations and pricing model](https://docs.oracle.com/en-us/iaas/Content/data-science/using/overview.htm)
- [Data Science project list command](https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/data-science/project/list.html)
- [Data Science job definitions and use cases](https://docs.oracle.com/en-us/iaas/Content/data-science/using/jobs-about.htm)
- [Data Scientist's OCI guide](https://docs.oracle.com/en-us/iaas/Content/GSG/Reference/getting-started-as-data-scientist.htm)
