# Recipe: database migration, replication, and application cutover

Reviewed: 2026-11-17

## Workload contract

**Outcome:** Application writers move to a compatible target.

**Inputs:** Source/target versions/features; data volume/change rate; method; grants/network; staging; synchronization boundary; writer-stop and rollback conditions.

**Flow:** Source → initial load → supported change capture/apply → writer drain → target connection → application.

**Starting configuration:** Keep source and retained logs until the agreed acceptance point. Budget overlapping environments and temporary replication resources. After target-only writes, rollback requires an explicit data reconciliation plan.

## Completion and handoff

Reconcile key data invariants and object coverage; confirm new writes and scheduled jobs use the target. Record failed or excluded objects rather than hiding them behind a successful job.

Return the selected scope, artifact/configuration revision, observed application result, remaining dependencies and operating owner. Include recurring capacity and retained data in [cost planning](service-cost-management.md); keep cleanup scoped to workload-owned resources.

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

## Keep VM relocation and upgrades distinct

Use [Cloud Migrations](service-cloud-migrations.md) for whole-guest relocation; preserve the database-consistency and client-cutover work in this recipe. For an existing managed service, [HeatWave blue/green](service-mysql-heatwave.md) or [PostgreSQL major upgrades](service-postgresql.md) may address an upgrade need without becoming a general cross-engine migration solution.

## Sources

- [Database Migration scope and underlying workflow](https://docs.oracle.com/en-us/iaas/database-migration/doc/overview.html)
- [Migration preparation](https://docs.oracle.com/en-us/iaas/database-migration/doc/getting-started.html)
- [GoldenGate source-target support](https://docs.oracle.com/en/cloud/paas/goldengate-service/ocigg/whats-supported.html)
- [Data Guard roles and transitions](https://docs.oracle.com/en-us/iaas/Content/Database/Tasks/usingdataguard.htm)
- [Custom application migration architecture](https://docs.oracle.com/en/solutions/migrate-oracle-db-custom-apps/considerations-moving-cloud1.html)
- [Cloud Migrations resource model and workflow](https://docs.oracle.com/en-us/iaas/Content/cloud-migration/cloud-migration-overview.htm)
- [Supported AWS Arm migrations](https://docs.oracle.com/en-us/iaas/releasenotes/cloud-migration/ocm_aws_arm_migration.htm)
- [HeatWave blue/green deployment](https://docs.oracle.com/en-us/iaas/releasenotes/mysql-database/heatwave-blue-green-deployments.htm)
- [PostgreSQL in-place major upgrades](https://docs.oracle.com/en-us/iaas/releasenotes/postgresql/inplace-upgrade.htm)
- [PostgreSQL recovery and moving-instance enhancements](https://docs.oracle.com/en-us/iaas/releasenotes/disaster-recovery/oct-2026.htm)
