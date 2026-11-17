# Recipe: retrieval over governed enterprise data

Reviewed: 2026-11-17

## Workload contract

**Outcome:** A question answered from permitted document passages.

**Inputs:** Source bucket/prefix; document ownership; embedding model/dimensions; database version; retrieval filters; generation API/model; citation contract; deletion policy.

**Flow:** Documents → parse/chunk/embed → vector store; question → compatible embedding → permitted retrieval → model → source-referenced answer.

**Starting configuration:** The [RAG example](https://github.com/subhanchaudry/oci-atlas/tree/v1.2.0/examples/rag) uses an existing bucket, Autonomous Database and model endpoints. It has one application data boundary; multi-user deployment requires authorization before retrieval. Re-embed into a distinct collection when changing embedding configuration.

## Completion and handoff

Inspect passages and source versions before generation. Check unknown questions, deleted documents and denied scope; a generated citation must resolve to a retrieved source, not a model-invented URL.

Return the selected scope, artifact/configuration revision, observed application result, remaining dependencies and operating owner. Include recurring capacity and retained data in [cost planning](service-cost-management.md); keep cleanup scoped to workload-owned resources.

## Resolve the knowledge contract

Identify the real data source, update cadence, user/document access rules, expected question types and answer/citation requirements. Reuse an appropriate governed store/index where possible. Choose a supported managed agent/retrieval path or a custom application based on the actual integration need, not a universal architecture diagram.

## Suggested sequence

1. Map user → application/agent → retriever → data source → model. Identify the service generation/API and each identity.
2. Establish data-source authorization and the network path from the retriever/ingestion runtime. A connector linked by an administrator doesn't automatically justify exposing every indexed document to every end user.
3. Resolve parsing, chunking, embedding compatibility, index metadata and source identifiers. Keep access metadata and document/version provenance alongside content where the chosen system supports it.
4. Ingest a bounded synthetic or authorized sample. Inspect failures and a few retrieved passages for representative questions before changing prompts or adding fine-tuning.
5. Supply relevant retrieved context to a supported model interface, preserving source identifiers/citations. Treat document instructions as content, not permission to use tools or disclose other data.
6. Verify retrieval access and the application's answer behavior using a few useful examples. Distinguish ingestion success, retrieval relevance, grounded generation and user authorization.
7. Configure the requested application/API entry, logging and operational ownership. Avoid logging sensitive source text broadly.

## Update and delete

Track source version, parsing/embedding/index configuration, and model/prompt revision. Changing embedding dimensions/model can require reindexing; don't update the query side in isolation. Define how document deletion or revoked access propagates to retrieval rather than assuming an old index updates itself.

When cleaning up, distinguish generated index artifacts from authoritative source data and shared model endpoints. Preserve the source unless deletion was explicitly requested. Use [Generative AI](service-generative-ai.md) and [AI Data Platform](service-ai-data-platform.md) only for their relevant boundaries.

## Retrieval-store alternatives

[Oracle AI Vector Search](service-ai-vector-search.md) can keep retrieval near existing relational data and SQL governance. [Search with OpenSearch](service-opensearch.md) supplies a search/index platform with its own data roles, ingestion, and index lifecycle. Compare both against the existing platform or managed agent knowledge source before adding another store. Verify supported versions/integrations, embedding compatibility, tenant filters, deletion propagation, and source authorization at retrieval time. A current index or HTTP 200 response does not establish relevant, permitted evidence.

## Select the database access boundary

If retrieval or SQL tools use [Database Tools MCP](service-database-tools.md), verify the client, server connection and database grants independently. Autonomous built-in tools use their own configuration path. Compaction or agent memory must not replace source-level authorization, deletion propagation or retrieval freshness checks.

## Sources

- [OCI enterprise GenAI architecture](https://docs.oracle.com/en/solutions/oci-genai-enterprise/index.html)
- [Generative AI Agents retrieval and tools](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/overview.htm)
- [Data Platform permissions](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/permissions-model.html)
- [Current Generative AI interfaces](https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm)
- [Database Tools overview](https://docs.oracle.com/en-us/iaas/database-tools/doc/overview.html)
- [Database Tools MCP server support and authentication](https://docs.oracle.com/en-us/iaas/database-tools/doc/overview-mcp-server.html)
- [CIMD client access](https://docs.oracle.com/en-us/iaas/releasenotes/database-tools/cimd.htm)
- [MCP service logs](https://docs.oracle.com/en-us/iaas/releasenotes/database-tools/logging.htm)
- [Agent Sandbox lifecycle](https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai/sandboxes.htm)
- [Hosted browser-session authentication](https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai/hosted-deployments-oauth.htm)
- [Hosted persistent file storage](https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai/hosted-applications-persistent-file-storage.htm)
- [OCI Responses API compaction](https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai/responses-api-compaction.htm)
- [Current model, hosting and routing releases](https://docs.oracle.com/en-us/iaas/releasenotes/services/generative-ai/)
