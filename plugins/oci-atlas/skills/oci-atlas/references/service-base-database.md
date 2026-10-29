# Base Database systems, maintenance, and Data Guard

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Choose the operating model

Base Database fits an Oracle database workload requiring the service's supported DB-system administration model. Compare Autonomous Database for a different managed operating model and Exadata for the relevant infrastructure/capabilities. Identify database version, edition, licensing model, node topology and application requirements before proposing a shape or availability design.

Check current provisioning choices rather than copying an older OCPU-based or edition-specific example. Existing deployments and new provisioning can have different supported options. Do not assume RAC or Data Guard is available for every edition, shape or developer configuration. Resolve feature eligibility from the owning service documentation and the customer's approved licensing context.

## Resource relationships

Distinguish the DB system and its nodes, DB home/software version, container database, and pluggable database (PDB). Provisioning an OCI resource, logging into the host and opening a SQL session are separate operations with separate authorization. A PDB service name is not the same as a DB-system display name or compartment.

Data Guard maintains supported primary/standby database relationships using redo transport/apply. Switchover, failover and reinstatement have different source-state and recovery assumptions. Inspect the current association/group model and the actual roles; do not infer a healthy standby from the mere existence of a second DB system. Replication also does not replace retained backups.

## Prerequisites and working sequence

Use Console **Base Database Service** and inspect the applicable `oci db` family. Guest DBCLI/SQL tooling is a different interface from OCI CLI; use it only when needed and available. Resolve client/backup network paths, storage, keys, administrator credential handling and IaC ownership.

1. Read the existing system, DB home, database/PDB, maintenance state and protection configuration.
2. For a requested create/change, select currently supported version/edition and capacity. Inspect shared DB-home or node effects before changing software.
3. Observe work requests and lifecycle state. Establish the actual advertised database connect descriptor and bounded SQL access using the intended application account.
4. For backup/restore, identify the configured mechanism, retention, recovery point and source/target compatibility. Verify recovered data/application behavior separately from job success.
5. For Data Guard, inspect transport/apply state, standby readiness, network and feature eligibility before an authorized role transition.
6. Record resulting roles, endpoints, software state and any remaining maintenance or application actions.

## Operational mistakes to avoid

RAC availability and cross-region recovery address different failures. A changed primary role can require application/service routing coordination. Don't execute failover to investigate an ordinary SQL connection timeout; use [connectivity diagnosis](troubleshoot-connectivity.md) first.

Plan maintenance through the owning service workflow, including application compatibility and backup readiness. Before deleting a PDB, database, DB home or DB system, enumerate contained data and dependent consumers. Preserve the requested backups/standbys and report retained resources. Use the [migration recipe](recipe-database-migration.md) for relocation/cutover and [Full Stack DR](service-full-stack-dr.md) for application-wide orchestration.

## Sources

- [Base Database editions, versions, and provisioning model](https://docs.oracle.com/en-us/iaas/Content/Database/Concepts/overview.htm)
- [Base Database task and management interfaces](https://docs.oracle.com/en/cloud/paas/base-database/index.html)
- [Data Guard roles and prerequisites](https://docs.oracle.com/en-us/iaas/Content/Database/Tasks/usingdataguard.htm)
