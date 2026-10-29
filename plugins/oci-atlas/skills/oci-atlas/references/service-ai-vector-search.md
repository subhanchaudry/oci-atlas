# Oracle AI Vector Search and retrieval design

Reviewed: 2026-10-29 · Basis: Oracle documentation review; illustrative SQL, no live schema changes.

## Select a retrieval capability, not a new database by default

Oracle AI Vector Search stores and searches embeddings alongside supported application data in Oracle AI Database. Consider it when existing Oracle data, SQL filtering and governance make database-local retrieval useful. Compare [OpenSearch](service-opensearch.md) for a search-centric index and the chosen agent/platform's managed retrieval when that already meets the task.

Confirm actual database version, compatibility setting, deployment and supported vector features. The presence of an Autonomous Database OCID does not establish that every vector function, index option or SDK interface is available. SQL access, vector object privileges and model/network dependencies remain separate from OCI database-management IAM.

## Data and index relationships

Track authoritative document/row ID, content version, chunk metadata, embedding model/version, vector dimensions and distance metric. Query vectors and stored vectors must use a compatible embedding contract. Similar dimensionality alone does not make two models' vector spaces interchangeable.

An approximate index trades retrieval behavior and resource use against the chosen search requirements. HNSW and IVF have different structures and configuration. Use current SQL/index documentation rather than copying one service/SDK's automatic-index defaults into every Oracle database.

Illustrative **schema write**, only after the target schema and version are selected:

```sql
CREATE TABLE atlas_vectors (
  doc_id NUMBER PRIMARY KEY,
  body CLOB,
  embedding VECTOR
);
```

This skeleton does not choose an embedding model, authorization filter or production index configuration.

## Working pattern

Use the database's supported SQL client, documented SDK or advertised REST interface. A control-plane CLI create/update does not load vector rows or create a SQL index.

1. Resolve source ownership, relevant data permissions and expected question/query behavior. Reuse a suitable existing schema/store where possible.
2. Choose chunking, embedding generation and provenance. For in-database model execution or external model calls, verify supported model format, network privileges and credential handling.
3. Load a bounded authorized sample with source/version and access metadata. Inspect null/error handling and vector compatibility before bulk ingestion.
4. Establish a baseline similarity query with the required relational/access filters. Choose index/search configuration from the observed dataset/workload and current feature support.
5. Inspect representative retrieved records, identifiers and authorization boundaries before integrating answer generation.
6. Record the embedding/index/query contract and the source-to-index update/deletion procedure.

## Common mistakes and lifecycle

A populated vector column does not prove useful retrieval; a fast query does not establish relevance or permitted access. Preserve tenant/document filters in the actual retrieval query/application, not only in a prompt. Re-embedding or changing distance/index choices can require coordinated data and query updates.

Keep authoritative source data separate from rebuildable embeddings/indexes. For deletion or revoked access, remove/update retrieval material through the intended propagation path. Do not drop a shared schema to reset one index. Use the [RAG recipe](recipe-rag-application.md) to connect retrieval, source authorization and grounded application responses.

## Sources

- [Vector data, compatibility, and embeddings](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/overview-ai-vector-search.html)
- [Vector index structures and SQL contract](https://docs.oracle.com/en/database/oracle/oracle-database/26/sqlrf/create-vector-index.html)
- [Database vector access paths and SDK boundaries](https://docs.oracle.com/en/cloud/paas/autonomous-database/vcapi/concepts/oracle-ai-database-vector-search.html)
