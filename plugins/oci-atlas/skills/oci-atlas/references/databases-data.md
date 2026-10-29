# Databases and data services

Reviewed: 2026-10-29 · Basis: documentation review; examples are not live-tested.

## Choose by workload and operating responsibility

| Need | Starting point | Clarify |
| --- | --- | --- |
| Managed Oracle database with automated administration | Autonomous Database | Workload/deployment option, SQL access, scaling and network model |
| More Oracle DB system administration control | Base Database Service | Version, edition, licensing, HA, backups and customer responsibilities |
| Exadata capabilities | Exadata Database Service offering | Required features, deployment model, capacity and cost |
| MySQL application compatibility | MySQL HeatWave | DB system, HA, replication and optional analytics capabilities |
| PostgreSQL application compatibility | OCI Database with PostgreSQL | Supported version/extensions, topology and migration constraints |

Start with the application's database compatibility, data scale, RPO/RTO, connectivity and operating model. Do not choose a different database solely to bypass a network error. Newer docs may use **Autonomous AI Database**, **Lakehouse**, or **Transaction Processing** labels; map customer ATP/ADW terminology to current deployment/workload choices and CLI fields rather than guessing renamed identifiers.

## Autonomous Database relationships and connectivity

Management operations create/scale/configure a database resource. SQL sessions require a database account or a specifically configured authentication mechanism. OCI IAM access to the resource is not automatically SQL privilege on its tables.

For private access, resolve the database hostname from the real application network, verify routing and NSGs, then use the advertised TLS/mTLS connection method. Obtain the actual connect descriptor and port. Wallet requirements depend on the chosen connection mode/client; do not assume every connection requires a wallet or that a downloaded wallet creates network access. Keep wallet contents and DB passwords out of chat and version control.

Use the [database connectivity recipe](recipe-database-connectivity.md) when the task spans application networking and SQL. For lifecycle changes, inspect backup/retention and restore implications, then verify the new service state. Restoring or deleting a database needs exact target and data-retention intent, not just its display name.

## Data engineering services are different objects

- **Data Integration:** a workspace holds design artifacts/data assets; data flows define transformations. Wrap work in tasks, publish tasks into an application, then run the published runtime artifact. A saved design is not an executed pipeline.
- **Data Flow:** an OCI service for running Spark applications. An application describes reusable code/dependencies/runtime settings; a run is an execution. It is distinct from a Data Integration artifact named a “data flow.” Diagnose code, runtime compatibility, access to artifacts/data, and network dependencies separately.
- **Streaming:** streams and stream pools support producers and consumers. Capture partitioning, retention, consumer behavior and endpoint/authentication needs before proposing a pipeline. Do not describe a stream as permanent database storage.
- **AI Data Platform:** consider it for governed shared data, Spark and workflow orchestration. Keep its workspace/catalog access and network context separate from Data Science compute. Use the current owning service docs for exact configuration instead of transferring another product's SQL or pipeline semantics.

## Navigate and work

Console search: **Autonomous Database**, the chosen DB service, **Data Integration**, **Data Flow**, or **Streaming**. CLI roots to inspect: `oci db`, `oci mysql`, `oci psql`, `oci data-integration`, `oci data-flow`, and `oci streaming`. Confirm availability in installed help.

Read-only discovery, using [selected context variables](access-and-tools.md):

```bash
oci db autonomous-database list --compartment-id "$ATLAS_COMPARTMENT_ID" --all \
  --profile "$ATLAS_PROFILE" --auth "$ATLAS_AUTH" --region "$ATLAS_REGION"
```

For an ingestion job, inspect source/target identities, data asset connections, schema mappings, network/DNS and data privileges. Publish/run the correct artifact, observe its run status/logs, and verify bounded row counts or output objects. A successful orchestration status alone doesn't establish data correctness. For schema changes, inspect downstream dependencies before updating a mapping or deleting artifacts.

## Canonical engine and lifecycle guides

Start with [service selection](service-selection.md), then load only the chosen engine: [Autonomous Database](service-autonomous-database.md), [Base Database](service-base-database.md), [Exadata](service-exadata.md), [MySQL HeatWave](service-mysql-heatwave.md), [OCI Database with PostgreSQL](service-postgresql.md), or [NoSQL Database](service-nosql.md). [OCI Cache](service-oci-cache.md) addresses cached application state; define the durable source and failure behavior. [Data Safe](service-data-safe.md) adds supported database-security controls and distinct target access.

For moves and ongoing changes, use [Database Migration](service-database-migration.md), [GoldenGate](service-goldengate.md), and the [cutover recipe](recipe-database-migration.md). Replication, database HA, and [application DR](service-full-stack-dr.md) solve different dependencies. A current replica can contain the same accidental deletion as its source.

For transport, distinguish [Queue](service-queue.md) work distribution, [Streaming](service-streaming.md) event logs, and [Streaming with Apache Kafka](service-streaming-kafka.md) managed Kafka clusters. Streaming's Kafka-compatible interface is a separate service interface. [Oracle Integration](service-oracle-integration.md) handles application/business integrations; [Data Integration](service-data-integration.md) handles data tasks. [Analytics Cloud](service-analytics-cloud.md) supplies analytics delivery rather than replacing an ingestion engine.

## Sources

- [Base Database Service](https://docs.oracle.com/en/cloud/paas/base-database/about/index.html)
- [Autonomous Database list command](https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/db/autonomous-database/list.html)
- [Autonomous Database private connectivity](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/private-endpoints-autonomous.html)
- [MySQL HeatWave](https://docs.oracle.com/en-us/iaas/mysql-database/home.htm)
- [OCI Database with PostgreSQL](https://docs.oracle.com/en-us/iaas/Content/postgresql/home.htm)
- [Data Integration concepts and runtime](https://docs.oracle.com/en-us/iaas/Content/data-integration/using/overview.htm)
- [Data Flow applications and runs](https://docs.oracle.com/en-us/iaas/Content/data-flow/using/concepts.htm)
- [Streaming overview](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streamingoverview.htm)
- [AI Data Platform and Data Science architecture](https://docs.oracle.com/en/solutions/ai-data-platform-data-science-workloads/)
