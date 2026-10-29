# Search with OpenSearch clusters and semantic retrieval

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Choose the search workload

Search with OpenSearch manages supported OpenSearch clusters for application search and related retrieval. Select it when its index/query model, operational features and available integrations fit the application. It is distinct from OCI Resource Search, Logging Search, and Oracle AI Vector Search; these do not share a universal query language or permission model.

Resolve text, vector or hybrid search requirements and existing data ownership. A RAG application does not automatically require a new search cluster if its current governed database/platform already supplies suitable retrieval. Check managed-service version/plugin support before assuming a feature from an upstream OpenSearch tutorial is available.

## Resource relationships and access

The OCI cluster resource represents the managed environment. OpenSearch indexes, mappings, documents, roles and queries are data-plane objects. Node/storage configuration, endpoint/network access, backups and application-level index permissions require distinct attention.

Management IAM access is not proof an application can read every index or administer OpenSearch security. Resolve the supported cluster authentication model, private connection path, TLS and index-level authorization. A Console-visible endpoint is not automatically reachable from a laptop or another managed runtime.

## Working sequence

Navigate to **Search with OpenSearch** and inspect the current service management API/CLI plus the cluster's supported OpenSearch client interface. Preserve existing infrastructure and index ownership.

1. Read cluster version/topology, endpoints, health, capacity and configured access. Identify authoritative data sources and existing indexes before creating new ones.
2. Define mappings/analyzers or vector fields appropriate to the chosen version. Record embedding/model/dimension and document/access metadata where semantic retrieval is used.
3. Establish ingestion with bounded authorized records and inspect per-record outcomes. A request-level response can contain individual indexing failures.
4. Query from the intended application identity and network. Inspect returned document IDs, relevant filters and representative relevance.
5. Observe cluster/index health, storage, shards, ingest/query workload and errors before resizing.
6. Integrate any model/agent consumer with the actual supported retrieval contract and record index/model/query revisions.

## Diagnose and change

Separate OCI provisioning/work-request state from OpenSearch health and data-query behavior. For failed access, inspect routing, TLS and the selected data identity/role. For missing results, inspect mapping, index/alias, filters, ingestion errors and visibility rather than immediately scaling nodes.

Plan index/mapping changes with the required reindexing and application alias/consumer transition. A model or vector-dimension change can require rebuilding data; don't update only the query model. Define how source deletion or revoked access reaches the index.

Inspect supported backup/restore and resize procedures before operational changes. Before cleanup, distinguish a rebuildable index from authoritative source data and a shared cluster from an application-owned one. Removing an ingestion definition does not necessarily remove indexed content or storage charges. Use [AI Vector Search](service-ai-vector-search.md) for database-local alternatives and [the RAG recipe](recipe-rag-application.md) for retrieval/application boundaries.

## Sources

- [Managed OpenSearch concepts](https://docs.oracle.com/en-us/iaas/Content/search-opensearch/Concepts/ociopensearch.htm)
- [Cluster connectivity and ingestion interface](https://docs.oracle.com/en-us/iaas/Content/search-opensearch/Tasks/ingestingociopensearchdata.htm)
- [Semantic-search integration](https://docs.oracle.com/en-us/iaas/Content/search-opensearch/Concepts/semanticsearch.htm)
- [Cluster backup, resize, and lifecycle entry points](https://docs.oracle.com/en-us/iaas/Content/search-opensearch/home.htm)
