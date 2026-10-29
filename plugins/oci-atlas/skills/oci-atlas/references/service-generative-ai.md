# Generative AI model and agent selection

Reviewed: 2026-10-29 · Basis: documentation review; no live inference or endpoint provisioning.

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

## Sources

- [Current Generative AI API and product entry points](https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm)
- [Model concepts and hosting modes](https://docs.oracle.com/en-us/iaas/Content/generative-ai/concepts.htm)
- [Regional routing and CPU-only access](https://docs.oracle.com/en-us/iaas/Content/generative-ai/cpu-only-regions.htm)
- [Generative AI Agents tools](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/overview.htm)
