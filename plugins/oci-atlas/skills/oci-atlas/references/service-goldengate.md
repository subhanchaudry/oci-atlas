# GoldenGate deployments, connections, and change replication

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Define the replication contract

OCI GoldenGate manages supported data replication workloads. Resolve the exact source/target technology, deployment type/version and use case: continuous change data capture, migration synchronization, analytics delivery or a supported bidirectional pattern. Consult the current support matrix for both directions rather than assuming a listed technology is supported as both source and target.

Distinguish initial loading from ongoing capture/apply. A running deployment is not a configured replication pipeline; a running capture process does not prove target apply is current. Bidirectional replication requires explicit conflict/write-ownership design and is not an automatic safe default for two writable databases.

## Resource relationships

An OCI deployment supplies the selected GoldenGate environment. Connection resources describe supported endpoint/authentication/network details and must be associated as required. Within the relevant deployment interface, replication configuration includes the appropriate source capture, distribution/trail and target apply/checkpoint objects. Use the terminology and capabilities for that deployment type rather than applying Oracle-database assumptions to every connector.

OCI management access, deployment-console access and source/target database permissions are different boundaries. Runtime connectivity must originate from the deployment's supported networking path. A database administrator's laptop connection does not prove the managed replication service can reach the same endpoint.

## Prerequisites and working sequence

Navigate to **GoldenGate** and inspect current `oci goldengate --help` plus the chosen deployment's documented management interface. Resolve supported versions, source logging/retention, data types, target readiness and IAM/database credentials through secure mechanisms.

1. Read existing deployments, connections, assignments and pipeline ownership. Identify the data/schema scope and consumers before creating another stream.
2. Verify the actual source-target pairing and capture/apply prerequisites against current documentation. Inspect network/DNS/TLS from the runtime context.
3. Configure the approved connections and scoped replication objects through the owning workflow. Keep passwords and connection secrets outside committed parameter files.
4. Establish the initial-load/CDC boundary so the target begins from a consistent position. Use the service-supported procedure rather than independently starting two uncoordinated copies.
5. Observe process state, checkpoints, lag, discard/error evidence and a bounded source-to-target data check.
6. Record source position/retention, target apply state and downstream application outcome separately from OCI deployment lifecycle.

## Diagnose and maintain

For growing lag, separate source capture, distribution/network, target apply and target workload pressure. A live process can still be stalled on an object, missing privilege or unsupported transformation. Before repositioning a checkpoint, inspect replay/duplicate and data-loss consequences; don't reset progress to suppress an error.

Coordinate DDL/schema changes and maintenance using the supported connector behavior. Replication does not automatically replicate every user, job, network rule or application dependency. Before cleanup, identify processes, retained trails/checkpoints, connection reuse and the authoritative data source. Stopping a deployment does not necessarily remove retained resources or stop all charges. Use the [migration recipe](recipe-database-migration.md) for cutover and [database service guides](databases-data.md) for target management.

## Sources

- [OCI GoldenGate deployment scope](https://docs.oracle.com/en/cloud/paas/goldengate-service/ocigg/about-oracle-cloud-infrastructure-goldengate.html)
- [Source and target support matrix](https://docs.oracle.com/en/cloud/paas/goldengate-service/ocigg/whats-supported.html)
- [Connection, deployment, and replication task entry points](https://docs.oracle.com/en/cloud/paas/goldengate-service/index.html)
- [End-to-end Oracle database replication workflow](https://docs.oracle.com/en/cloud/paas/goldengate-service/ocigg/quickstarts/replicate-data-between-cloud-databases-in-the-same-region.html)
