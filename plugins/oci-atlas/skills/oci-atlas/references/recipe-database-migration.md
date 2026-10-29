# Recipe: database migration, replication, and application cutover

Reviewed: 2026-10-29 · Basis: documentation-based suggested pattern; no live data movement or cutover.

## Define the authoritative database transition

Capture source and target engine/version/edition, schema/features, data volume, change rate, acceptable interruption and application dependencies. Select the target service for compatibility and operating responsibility, not merely because the initial connection attempt failed. Identify who controls application writers, batch jobs, integrations and connection secrets.

Choose a supported migration path. Database Migration coordinates supported movement; GoldenGate can provide supported ongoing CDC; Data Guard protects supported Oracle database primary/standby relationships. These roles do not imply interchangeable source-target support or an automatic application cutover.

## Suggested sequence

1. **Assess compatibility.** Inventory schemas, types, character sets, extensions, database jobs, external directories/integrations and unsupported objects. Verify current method support and the target service's limitations.
2. **Establish execution access.** Resolve operator/service IAM, source/target database grants, secure credentials and the actual runtime network/TLS path. Laptop access alone does not establish migration-service access.
3. **Prepare and evaluate.** Create only required target/staging/connection objects, preserving existing ownership. Run the selected tool's evaluation/precheck and address the actual failed prerequisites before starting movement.
4. **Establish initial state.** Perform the supported load/copy procedure and record its synchronization boundary. Inspect partial failures and target objects rather than assuming job-level success covers every row and schema dependency.
5. **Apply changes where supported.** Observe capture, distribution and target apply/checkpoints. Check source log retention, lag and failed objects. A low lag metric alone does not prove application readiness or full object coverage.
6. **Coordinate the requested cutover.** Identify the final writer stop/drain, synchronization point, connection/DNS/secret transition and supported rollback conditions. Do not convert a design or replication setup request into an unrequested live cutover.
7. **Verify the application.** Confirm the intended target receives new writes, relevant reads/data invariants hold, integrations/jobs use the correct database, and authentication works for the actual application identities.

## Replay and recovery boundaries

Before retrying, inspect committed source/target state and the tool's supported restart/checkpoint behavior. A timed-out step can have completed. Repositioning capture or apply can replay changes or omit data; do not reset progress merely to obtain a green status.

Define rollback with the real write history in mind. After target-only writes begin, pointing the application back to the old source is not automatically lossless. Bidirectional replication needs a deliberate conflict and ownership design. Keep migration readiness distinct from long-term backup, HA and disaster-recovery configuration.

Use [Database Migration](service-database-migration.md) for managed jobs/evaluation, [GoldenGate](service-goldengate.md) for CDC topology, and [Base Database/Data Guard](service-base-database.md) for supported physical database protection. Consult the chosen MySQL/PostgreSQL/Exadata/Autonomous guide for target-specific lifecycle and feature constraints.

## Retention and cleanup

Preserve the source, backups, logs and temporary migration artifacts according to the requested retention and acceptance intent. A successful copy does not authorize deleting the original database. Enumerate staging objects, replication deployments, connections and retained capacity before cleanup. Report the completed migration/application scope and remaining consumers or protection work without claiming measured downtime or acceptance that was not observed.

## Sources

- [Database Migration scope and underlying workflow](https://docs.oracle.com/en-us/iaas/database-migration/doc/overview.html)
- [Migration preparation](https://docs.oracle.com/en-us/iaas/database-migration/doc/getting-started.html)
- [GoldenGate source-target support](https://docs.oracle.com/en/cloud/paas/goldengate-service/ocigg/whats-supported.html)
- [Data Guard roles and transitions](https://docs.oracle.com/en-us/iaas/Content/Database/Tasks/usingdataguard.htm)
