# Recipe: application backup, restore, and disaster recovery

Reviewed: 2026-10-29 · Basis: documentation-based suggested pattern; no live restore or failover.

## Choose the failure and outcome

Define the business application, acceptable data loss (RPO), outage (RTO), failure scope and restoration owner. Protecting against accidental row deletion, a failed host, an availability-domain outage and a regional outage can require different mechanisms. High availability, retained backup and ongoing replication are related protections with different recovery contracts.

Inventory the actual databases, files/volumes, object artifacts, compute images/configuration, network/DNS, identities, keys, secrets and external integrations. A backup existing for one disk is not a recoverable application architecture. Identify authoritative data versus content that can be rebuilt from versioned source.

## Suggested sequence

1. **Map consistency and retention.** Resolve database-native protection, application quiescing/checkpoints and related volume/filesystem boundaries. A crash-consistent storage group is not automatically a transactionally consistent business system.
2. **Read existing protection.** Inspect actual completed backup/recovery points, retention, replication state and encryption-key access. Confirm target region/placement support and required standby capacity. Configured policy alone does not establish a usable recovery point.
3. **Select restoration or transition.** For logical loss, identify a suitable retained point and supported restore target. For a protected outage, inspect the actual database/storage roles and replication readiness. Use [Full Stack DR](service-full-stack-dr.md) when its orchestration and supported members fit.
4. **Prepare dependencies.** Recreate or verify target networking, DNS, keys, credentials, application artifacts and required external access. Restored data without its encryption key or application identity may remain unusable.
5. **Execute only the requested operation.** Distinguish an isolated recovery exercise, a planned switchover and an unplanned failover. A planning request does not authorize changing live writer ownership. Observe each operation and reconcile partial state before retrying.
6. **Verify the application.** Check the actual recovered point, database/filesystem state, application start and client endpoint. Use a bounded representative data/business invariant in addition to infrastructure lifecycle states.
7. **Reprotect and document.** Inspect the new primary/standby direction, backup schedules, retained source resources and the supported return procedure. Report measured RPO/RTO only if an actual exercise provides the evidence.

## Failure handling

For a failed recovery step, inspect the first meaningful error and committed resource/role changes. Do not restart the entire sequence blindly after a transport timeout. Coordinate traffic and application writers so the old and recovered environments do not both accept conflicting writes.

Use service-specific guidance for [Block Volume](service-block-volume.md), [File Storage](service-file-storage.md), [Base Database](service-base-database.md) and [Autonomous Database](service-autonomous-database.md). A replicated destination can contain the same unwanted change as its source, so retain appropriate independent recovery points. Do not assume a platform snapshot includes every secret, DNS record or external system.

## Cleanup

Identify exercise-only resources and the retained recovery material before removing anything. Keep shared networking, authoritative data and required keys available. Deleting a failed plan execution is different from removing launched capacity, restored disks or replicated data. Report what remains billable and which recovery dependencies still need an owner.

## Sources

- [Recovery objectives and DR resource terminology](https://docs.oracle.com/en-us/iaas/disaster-recovery/doc/disaster-recovery-terminology.html)
- [Application dependency ordering](https://docs.oracle.com/en-us/iaas/disaster-recovery/doc/dependency-mapping.html)
- [Volume groups and recovery consistency](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
- [File Storage replication boundaries](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/FSreplication.htm)
