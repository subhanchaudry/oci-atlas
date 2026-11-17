# Generative AI model and agent selection

Reviewed: 2026-11-17

## Resolve the product and request contract

Identify the customer's actual API/product first. Current Generative AI documentation includes Enterprise AI model and agent features, OpenAI-compatible entry points and other managed capabilities. The separately documented Generative AI Agents service has its own objects/tools. Similar labels do not establish compatible payloads, permissions or SQL semantics.

Choose the smallest appropriate layer: model inference for generation/embeddings, a supported agent service for managed tool/retrieval workflows, or a custom application when required behavior isn't supplied. Don't deploy a dedicated cluster or additional vector store simply because the request mentions an LLM.

## Inference versus hosting

| Choice | Fits | Inspect before acting |
| --- | --- | --- |
| On-demand inference | Supported hosted-model calls | Current model capability, request schema, limits and price |
| Dedicated cluster/endpoint | Selected hosting or fine-tuning requirements | Supported model/hardware, capacity, commitment and lifecycle |
| Regional routing profile | Supported on-demand model routed to target region(s) | Actual execution regions, realm and data-location requirements |
| Custom imported/served model | A specific model/runtime need | Import support, licensing, serving interface and operational cost |

Don't persist “latest” model IDs, token limits or price tables in a static recipe. Discover supported combinations for the customer's region and request. A Console-selected region can be different from the inference region when routing is involved.

## Working sequence

1. Define input/output contract, data classification and intended scale.
2. Discover model/API capability and endpoint in the selected context. Inspect current SDK/CLI schema or generated code rather than guessing a universal chat payload.
3. Resolve the application caller's authentication and model/service permissions. Use a bounded synthetic input to separate request-format issues from application data issues.
4. Observe response format, token/usage information where supplied and relevant errors. A successful response is only transport/model execution evidence.
5. For RAG, inspect retrieval context and source permissions separately. For tools, inspect actual tool authorization and execution. Model instructions alone don't enforce data access.

For model changes, inspect payload compatibility, output behavior, routing and consumers before updating an application. For dedicated-resource cleanup, identify endpoint references and retained billable capacity. Use [AI application](recipe-ai-application.md) or [RAG](recipe-rag-application.md) only when the task spans services.

## Choose model calls or an agent lifecycle

Use [Generative AI Agents](service-generative-ai-agents.md) for knowledge bases, ingestion, tools, sessions and endpoints. For direct inference, record endpoint, serving mode, model identifier, request format and output contract together. Track input/output tokens and embedding volume where returned; separate dedicated capacity from request-based usage and keep client timeouts/retries bounded.

## Managed code execution and hosted applications

Agent Sandbox provides temporary isolated Linux workspaces within a Generative AI project. Resolve compute, lifetime, command timeouts and network access before execution. CLI/SDK operations cover commands, cancellation, file transfer and snapshots; the Console supports project enablement, networking and monitoring. Export required results before stopping or deleting the sandbox, and distinguish a snapshot from a guarantee of application recovery.

Hosted application authentication is a separate decision. Supported choices include OCI IAM, identity-domain bearer tokens and browser-session OAuth 2.1 with PKCE. Selecting No authentication removes platform-managed endpoint authentication; use it only for public content or a deliberately designed application authentication layer. It is not a workaround for denied access to private data.

Persistent file storage survives hosted-application restarts and redeployments. The reviewed release allows up to 50 GB and requires minimum and maximum replicas both set to one. Do not present that configuration as a multi-replica availability design. Record storage paths, retained state and cleanup ownership.

## Responses API context and model discovery

The OCI Responses API supports explicit compaction through POST /responses/compact and automatic compaction through context_management on POST /responses. It requires a Generative AI project OCID and follows the selected model's regional/serving availability. Verify what context is retained in subsequent requests; compaction is not permanent memory or an access-control boundary.

Discover the current model catalog and supported import/hardware combinations, then record the exact model, region, serving mode and request API. Model import, native fine-tuning and externally trained artifacts are distinct workflows. Routing profiles select permitted inference destinations; access from a local region does not establish local inference or universal private-endpoint support.

## Availability boundary for announced AI offerings

At the November 17, 2026 review, Cerebras inference is announced for 2027, AI Media Models is in preview, and Cost Advisor for AI has limited availability. They are excluded from this guide's GA recommendations. Check the exact feature and its dependencies rather than treating an AIWorld announcement as proof of current operational support.

## Sources

- [Current Generative AI API and product entry points](https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm)
- [Model concepts and hosting modes](https://docs.oracle.com/en-us/iaas/Content/generative-ai/concepts.htm)
- [Regional routing and CPU-only access](https://docs.oracle.com/en-us/iaas/Content/generative-ai/cpu-only-regions.htm)
- [Generative AI Agents tools](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/overview.htm)
- [Agent Sandbox lifecycle](https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai/sandboxes.htm)
- [Hosted browser-session authentication](https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai/hosted-deployments-oauth.htm)
- [Hosted persistent file storage](https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai/hosted-applications-persistent-file-storage.htm)
- [OCI Responses API compaction](https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai/responses-api-compaction.htm)
- [Current model, hosting and routing releases](https://docs.oracle.com/en-us/iaas/releasenotes/services/generative-ai/)
- [Hosted applications without platform authentication](https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai/hosted-applications-no-authentication.htm)
- [November AI availability and exclusions](https://blogs.oracle.com/ai-and-datascience/whats-new-in-ai-november-2026)
