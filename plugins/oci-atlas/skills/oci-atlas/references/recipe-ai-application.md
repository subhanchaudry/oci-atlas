# Recipe: choose and deploy an AI application

Reviewed: 2026-11-17

## Workload contract

**Outcome:** An application task completed through the selected AI API.

**Inputs:** Task/input/output; data location/classification; model or agent interface; caller identity; endpoint; expected load and latency; tool permissions.

**Flow:** Client → application → model/agent → optional permitted data/tool → response.

**Starting configuration:** Use on-demand inference when it fits. Dedicated capacity, GPU serving and managed agent orchestration require a stated capability need. Use [managed agents](service-generative-ai-agents.md) for its resource lifecycle.

## Completion and handoff

A synthetic request follows the selected API schema; response parsing, authorization and failure handling work independently of answer quality. Inspect evidence relevance and tool effects separately.

Return the selected scope, artifact/configuration revision, observed application result, remaining dependencies and operating owner. Include recurring capacity and retained data in [cost planning](service-cost-management.md); keep cleanup scoped to workload-owned resources.

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

## Infrastructure and retrieval alternatives

For custom accelerated infrastructure, load [GPU/HPC](service-gpu-hpc.md) and [Lustre](service-lustre.md) only when the runtime and I/O requirements justify them. For retrieval, compare [database-native AI Vector Search](service-ai-vector-search.md), [OpenSearch](service-opensearch.md), and existing managed knowledge sources through the [RAG recipe](recipe-rag-application.md). For a container backend that does not need Kubernetes, inspect [Container Instances](service-container-instances.md).

## Choose execution and state deliberately

Use [Agent Sandbox](service-generative-ai.md) when bounded managed code execution fits; define timeouts, network access and exported results. Hosted application persistence has a documented single-replica constraint. For an [AIDP agent](service-ai-data-platform.md), distinguish the deployed revision, caller authorization, runtime identity and downstream credentials. Keep preview-dependent credential setup outside a GA-only architecture.

## Sources

- [OCI enterprise GenAI architecture: layers and design considerations](https://docs.oracle.com/en/solutions/oci-genai-enterprise/index.html)
- [Current Generative AI capabilities and API entry points](https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm)
- [Generative AI Agents tools and retrieval](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/overview.htm)
- [Data Science managed ML resources](https://docs.oracle.com/en-us/iaas/Content/data-science/using/overview.htm)
- [Agent Sandbox lifecycle](https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai/sandboxes.htm)
- [Hosted browser-session authentication](https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai/hosted-deployments-oauth.htm)
- [Hosted persistent file storage](https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai/hosted-applications-persistent-file-storage.htm)
- [OCI Responses API compaction](https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai/responses-api-compaction.htm)
- [Current model, hosting and routing releases](https://docs.oracle.com/en-us/iaas/releasenotes/services/generative-ai/)
- [AIDP dated feature history and preview labels](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidwn/index.html)
- [AIDP deployed agents and runtime identity](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/agent-flow-deployment.html)
- [AI compute autoscaling](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/ai-compute.html)
- [Agent memory and retention](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/agent-memory.html)
