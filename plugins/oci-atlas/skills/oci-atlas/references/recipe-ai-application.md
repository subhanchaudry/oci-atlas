# Recipe: choose and deploy an AI application

Reviewed: 2026-10-29 · Basis: documentation-based suggested pattern; not a live-tested application.

## Start from the task

Determine whether the application needs text generation, document processing, retrieval over governed knowledge, structured-data queries, or predictive ML. Resolve data-location/access constraints and the relevant latency/throughput/cost needs. Prefer an available managed capability when it fits; choose a custom model server or GPU workload for a concrete requirement.

## Suggested working sequence

1. **Choose the service and API.** Discover the currently available model or model artifact and supported endpoint in the intended region. Distinguish OCI Generative AI/Enterprise AI agent features, the separately documented Generative AI Agents service, and Data Science model deployments.
2. **Map the application path.** Client → application/API layer → model or agent endpoint → optional retrieval/data/tool layer. Pick Functions, Compute or OKE based on the actual runtime requirements. Avoid deploying every component from a reference architecture by default.
3. **Resolve identities and data access.** Identify the end user, application principal, retrieval principal and tool caller. Enforce document/row access at retrieval or source boundaries, not merely by telling the model what it may reveal. Store secrets through the chosen secret-management mechanism.
4. **Add only necessary context.** For RAG, choose the source and ingestion path, then the retrieval/index strategy. For structured data, use the relevant documented tool or bounded query interface; don't assume a generic SQL tool has identical behavior across OCI products.
5. **Deploy a small vertical slice.** Establish network/IAM prerequisites, deploy the application and configure the chosen endpoint. Start with a bounded synthetic input. Introduce dedicated hosting only when selected and its capacity/cost constraints are understood.
6. **Verify the requested outcome.** Inspect the actual retrieved passages/tool calls when applicable, output format and application response. Use a few representative examples appropriate to the task. A successful model API call alone doesn't establish answer quality or data isolation.
7. **Expose and observe.** Configure the intended client authentication, endpoint reachability and useful logging. Keep sensitive prompts, documents and secrets out of broad diagnostic logs.

## Operate and evolve

Record model/version or artifact digest, prompt/configuration revision and data/index version where applicable. Recheck request schemas and availability when changing models. Re-ingesting documents or changing embeddings can require index changes; don't update one side in isolation.

Before cleanup, identify application, endpoint, dedicated capacity, data-source and storage ownership. Delete only the requested resources and report retained billable capacity. Load [AI/ML](ai-ml.md), [databases/data](databases-data.md), or [applications](applications.md) only for the missing detail.

## Sources

- [OCI enterprise GenAI architecture: layers and design considerations](https://docs.oracle.com/en/solutions/oci-genai-enterprise/index.html)
- [Current Generative AI capabilities and API entry points](https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm)
- [Generative AI Agents tools and retrieval](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/overview.htm)
- [Data Science managed ML resources](https://docs.oracle.com/en-us/iaas/Content/data-science/using/overview.htm)
