# Cloud Migrations discovery, replication, and VM cutover

Reviewed: 2026-11-17

## Choose the migration boundary

Oracle Cloud Migrations moves supported VMware virtual machines and AWS EC2 instances to OCI Compute. Use it for an infrastructure relocation when guest OS and application compatibility fit. Use [Database Migration](service-database-migration.md) for a database-service migration and [Full Stack DR](service-full-stack-dr.md) for recovery orchestration. Replicating a VM disk does not establish database-consistent cutover.

## Resources and prerequisites

Discovery creates inventory assets; a migration project groups migration assets and plans. Plans describe target configurations and can support separate test and cutover launches. Replication and target launch are distinct operations. VMware uses a source-side agent; AWS discovery uses an agentless connection. Confirm source permissions, credential references, connectivity, staging storage, destination IAM, and existing infrastructure ownership before enrollment.

AWS Arm assets retain their architecture requirement. Discovery records architecture when available and uses it to filter compatible targets; it does not translate x86 binaries to Arm. Confirm the supported source OS and an available compatible image/shape in the destination region. A mixed Arm/x86 project evaluates each asset separately. Shape recommendations do not reserve capacity or raise limits.

## Working pattern

1. Find **Cloud Migrations** in the Console. Inspect the inventory, discovery freshness, source environment and workload dependencies.
2. Group assets by coordinated cutover. Compare recommended target settings with measured demand, destination networking and the application's recovery requirements.
3. Configure replication and inspect completed transfers and errors. Record the data point used for a test launch.
4. Launch a bounded test target. Validate guest boot, drivers, networking, application licensing, data access and representative transactions.
5. Before cutover, coordinate source writes, final synchronization, target validation and client/DNS transition. Define the rollback decision and authoritative writer.
6. Reconcile test targets, replication artifacts and source-retirement work. A successful launch does not authorize source deletion.

## Cost, failure, and ownership

Track source-cloud charges, data transfer, staging/replicated storage and test/final Compute separately. Record which resources the migration project owns and which belong to an application stack. Removing migration metadata must not be treated as proof that target disks or source resources were removed. For failure, distinguish stale discovery, source access, replication errors, unsupported architecture, capacity and application startup before repeating a launch.

## Sources

- [Cloud Migrations resource model and workflow](https://docs.oracle.com/en-us/iaas/Content/cloud-migration/cloud-migration-overview.htm)
- [Supported AWS Arm migrations](https://docs.oracle.com/en-us/iaas/releasenotes/cloud-migration/ocm_aws_arm_migration.htm)
