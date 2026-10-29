# Full Stack Disaster Recovery plans and dependencies

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested planning and operational workflow.

## Choose the recovery objective

Full Stack Disaster Recovery orchestrates supported application-stack transitions. It does not make every unmanaged component replicated or eliminate the need for backup, standby configuration and recovery ownership. Define the business service, acceptable data loss (RPO), acceptable outage (RTO) and the failure to recover from before choosing an operation.

Separate backup restoration, high availability, disaster recovery and migration. A successful volume restore is not a recovered application. An available standby database is not evidence that application endpoints, secrets, network paths and external integrations will work after transition.

## Resource relationships

DR protection groups describe the application's participating resources and roles. A DR plan contains ordered groups/steps; an execution records one operation's progress. Generated built-in steps depend on supported members and their configured relationships. User-defined behavior may be needed for application/external dependencies not represented by built-in handling.

A planned switchover and an unplanned failover have different assumptions about source availability and shutdown. A drill has its own supported behavior and cleanup. Inspect the exact plan type and current member support; do not treat all three as equivalent names for a generic failover button.

## Prerequisites and working sequence

Navigate to **Disaster recovery** and inspect the current Full Stack DR CLI/API reference. Resolve the primary/standby groups, plan/execution, region pair, service principals, secret references and existing automation ownership.

1. Inventory all application dependencies, including data replication, network/DNS, keys, credentials, images and downstream systems.
2. Read group members and each underlying service's protection/readiness. Plan creation alone does not prove replication or standby capacity exists.
3. Generate/read the applicable plan. Inspect built-in dependencies, required prechecks and bounded custom steps. Preserve documented ordering unless there is a justified, reviewed application-specific change.
4. For requested execution, establish the exact transition type, source state and application coordination. A request to explain recovery does not authorize a live failover.
5. Observe plan execution and the first meaningful failed step. Reconcile partial effects before retrying or continuing.
6. Verify database/data state, application start, endpoint/DNS behavior and a representative application transaction. Record elapsed recovery and observed recovery point only when actually measured.

## Failure and lifecycle handling

Do not restart a partially completed transition from the beginning without inspecting service roles and committed state. A step that timed out may already have changed the database role or launched capacity. Keep traffic/writer ownership explicit to avoid conflicting active applications.

After transition, inspect protection direction, retained source resources and the supported return/reprotection procedure. Failback is a separate operation with prerequisites, not a promised automatic rollback. Remove drill or standby resources only within the requested scope, accounting for shared infrastructure and retained data. Use [the application recovery recipe](recipe-backup-disaster-recovery.md) for a broader decision sequence and the owning database/storage guides for their specific protection mechanisms.

## Sources

- [Full Stack DR scope](https://docs.oracle.com/en-us/iaas/disaster-recovery/index.html)
- [Protection groups, plans, roles, and recovery objectives](https://docs.oracle.com/en-us/iaas/disaster-recovery/doc/disaster-recovery-terminology.html)
- [Dependency mapping and ordered operations](https://docs.oracle.com/en-us/iaas/disaster-recovery/doc/dependency-mapping.html)
- [Built-in groups and supported plan types](https://docs.oracle.com/en-us/iaas/disaster-recovery/doc/built-in-plan-groups.html)
