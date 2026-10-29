# NoSQL tables, key design, and capacity

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Select the data model deliberately

Oracle NoSQL Database Cloud Service supports managed table access for key-oriented and supported query workloads. Choose from the application's access patterns, required consistency, data shape and scale. It is not an automatic drop-in replacement for an arbitrary relational schema or an in-memory cache.

Identify fixed-schema, JSON collection or hybrid table requirements from the current service documentation. Flexible JSON content does not remove the need for a well-designed primary/shard key, index strategy or capacity plan. Keep the cloud service and a self-managed Oracle NoSQL deployment's setup/interfaces distinct.

## Resource relationships and prerequisites

A table has a primary key, shard-key design, data/schema and configured limits or supported capacity mode. Secondary indexes, expiration behavior and regional/global table options have their own constraints. Key design affects distribution and future changes; verify which fields are immutable before importing a large dataset.

Resolve tenancy/compartment, data region/endpoint, intended SDK/client and runtime identity. Table administration and application reads/writes are different operations and permissions. A client reaching an endpoint does not establish authorization for the selected table. Don't infer cross-region consistency or conflict handling from the phrase “global table.”

## Working pattern

Use Console **NoSQL Database** and inspect current `oci nosql --help` plus the supported application SDK. The management CLI and a data SDK need not expose identical operations. Read the actual service endpoint instead of constructing one from the tenancy name.

1. Document the dominant reads/writes and required row identity. Choose a key that distributes the expected traffic, rather than a convenient field with extreme skew.
2. Inspect an existing table's schema, indexes, capacity, retention and ownership before creating another copy.
3. For a requested create/change, use the current table/schema contract and configured capacity mode. Check what requires table recreation or a data migration.
4. Run a bounded authorized write/read using the application principal and intended key/query. Validate returned structure and the chosen consistency behavior.
5. Inspect throttling, observed read/write usage, query/index behavior and hot keys before increasing all capacity.
6. For global/replicated data, inspect supported regions, initialization, write ownership and conflict behavior before distributing application writers.

## Lifecycle and common mistakes

An index being created does not guarantee every expected query uses it. A successful table-management operation does not establish application read/write access. Retrying a write requires the application's key/version/idempotency contract; avoid inventing exactly-once business effects from a successful transport response.

Changing a primary/shard-key design can require a new table and coordinated data movement. Expiring a row and deleting the entire table are different scopes. Before cleanup, identify applications, regional replicas, indexes and any export/retention requirement. Keep the authoritative data source clear if a table is a derived materialization. Use [service selection](service-selection.md) for comparison with PostgreSQL/MySQL/Autonomous and [OCI Cache](service-oci-cache.md) for transient cache semantics.

## Sources

- [NoSQL cloud concepts](https://docs.oracle.com/en/cloud/paas/nosql-cloud/dtddt/cloud-concepts.html)
- [Table schema, primary keys, and shard keys](https://docs.oracle.com/en/cloud/paas/nosql-cloud/dtddt/designing-a-table-in-oracle-nosql-database-cloud-service.html)
- [SDKs, global tables, IAM, and capacity task entry points](https://docs.oracle.com/en/cloud/paas/nosql-cloud/index.html)
