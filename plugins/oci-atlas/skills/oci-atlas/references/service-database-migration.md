# Database Migration resources, evaluation, and cutover

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested planning and operational workflow.

## Choose migration scope and method

Database Migration coordinates supported database movement to OCI. Resolve source/target engines, versions, editions, character sets, data volume, acceptable downtime and application dependencies before selecting a method. Do not promise that an arbitrary heterogeneous pair is supported or that “online” means no application interruption.

A migration changes the application's authoritative database location. Ongoing replication serves a different operating contract, and disaster recovery protects a service against failure. The same underlying technology can participate in several patterns without making their readiness or cutover steps interchangeable.

## Resource relationships and prerequisites

Source/target connection resources identify databases and the supported connectivity/credential configuration. A migration specifies the movement behavior; migration jobs execute/evaluate the defined work and expose phase/status details. Inspect the current service's supported workflow, including its use of underlying database migration/replication tools, rather than manually mixing steps from unrelated tutorials.

Resolve operator IAM, service/runtime access, database grants, network reachability and required dependent objects. Temporary staging/storage or supporting replication resources can have independent cost and retention. Read prerequisites for the selected migration type; do not universally request privileged host access when that workflow does not require it.

## Working sequence

Use Console **Database migrations** and the current Database Migration CLI/API reference. Begin with the existing migration definition and data owners, not a blind new migration job.

1. Inventory source/target compatibility, schemas, unsupported objects/features, write ownership and downstream applications. Identify the chosen acceptance criteria.
2. Configure supported connections and required database/network prerequisites. Establish source and target access from the execution service's context.
3. Run the supported evaluation/validation phase before data movement. Inspect actionable errors and method-specific requirements rather than treating evaluation success as completed migration.
4. Execute the requested initial copy and, where applicable, change capture/apply. Observe phases, lag, failures and committed target data.
5. Before a separately requested cutover, coordinate application writers/jobs, confirm the final synchronization point, and agree the supported rollback/return conditions.
6. Transition application connections and verify schema, representative data invariants, authentication and a bounded business operation. Record the target and observed outcome.

## Failure and cleanup

For job failure, identify the earliest failed phase and resource state before retrying. A completed bulk copy can coexist with a broken incremental stream; a small lag is not proof every object or application dependency is migrated. Inspect source log retention and target apply errors before advancing a cutover.

Preserve the original database and required recovery resources according to the chosen retention intent. Do not delete source data simply because a migration job is successful, or describe a consumer connection update as proof that all writers switched. Enumerate temporary storage, connections, jobs and replication resources before removing them. Use [GoldenGate](service-goldengate.md) for ongoing CDC concepts and the [migration recipe](recipe-database-migration.md) for the cross-service/application sequence.

## Sources

- [Database Migration service and supported approach](https://docs.oracle.com/en-us/iaas/database-migration/doc/oracle-cloud-infrastructure-database-migration.html)
- [Connections, migrations, and job terminology](https://docs.oracle.com/en-us/iaas/database-migration/doc/database-migration-terminology.html)
- [Preparation and taskflows](https://docs.oracle.com/en-us/iaas/database-migration/doc/getting-started.html)
- [Migration overview and underlying tool boundaries](https://docs.oracle.com/en-us/iaas/database-migration/doc/overview.html)
