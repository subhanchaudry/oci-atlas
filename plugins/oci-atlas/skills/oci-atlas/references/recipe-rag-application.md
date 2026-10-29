# Recipe: retrieval over governed enterprise data

Reviewed: 2026-10-29 · Basis: documentation-based suggested pattern; no live ingestion or inference.

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

## Sources

- [OCI enterprise GenAI architecture](https://docs.oracle.com/en/solutions/oci-genai-enterprise/index.html)
- [Generative AI Agents retrieval and tools](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/overview.htm)
- [Data Platform permissions](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/permissions-model.html)
- [Current Generative AI interfaces](https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm)
