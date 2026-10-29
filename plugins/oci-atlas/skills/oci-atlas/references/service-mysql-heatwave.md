# MySQL HeatWave systems, access, and availability

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Choose the MySQL workload layer

Use MySQL HeatWave for a supported managed MySQL workload. Resolve transactional requirements, compatible MySQL version, storage, application drivers and availability needs first. HeatWave query acceleration, Lakehouse, ML and GenAI capabilities are additional choices with their own configuration; a basic DB-system request does not require enabling every capability.

Do not select a different engine simply to fix private connectivity. Compare a standalone system, high-availability configuration and supported read-replica/replication options by the actual application contract. Check current compatibility and eligibility rather than assuming a source MySQL plugin or administrative privilege is available in a managed service.

## Resource model and identity

A DB system supplies the managed MySQL database environment and endpoints. A HeatWave cluster, read replicas, replication channels and backups serve different roles. High availability protects against supported instance failures; it does not replace backup retention or a separate cross-region recovery design.

OCI IAM permits management operations. A MySQL client uses a configured database authentication mechanism and SQL privileges. Access to inspect a DB-system OCID is not permission to query every schema. Establish the source of the application connection and the actual private endpoint, not only the operator's browser location.

## Prerequisites and working sequence

Navigate to **MySQL HeatWave** and inspect `oci mysql --help`. Resolve the selected compartment/region, subnet/NSGs, sizing, maintenance/backup policy, administrator credential flow and ownership. Use the actual connection details with a compatible MySQL client.

1. Read the existing DB system, endpoint, configured availability and replication state. Identify application users and dependent workloads before provisioning a replacement.
2. Select a supported configuration with the intended storage and protection choices. Check source/target requirements when importing or replicating data.
3. Observe resource/work-request state, then establish a bounded authenticated SQL connection from the intended runtime.
4. Verify the expected schema and a representative query or application transaction. A MySQL TCP connection is not evidence of schema migration completeness.
5. For HeatWave features, inspect supported shapes/capabilities, data-loading state and the appropriate feature-specific workflow before claiming queries use the accelerator or Lakehouse.
6. Record backup, replica/channel and maintenance settings separately from the primary system's lifecycle.

## Availability and diagnosis

Managed HA, read scaling and inbound/outbound replication have different writer/reader behavior. Inspect actual endpoint and role changes during a supported switchover/failover; do not assume application connection pools or external replication metadata need no attention. Verify observed lag and replay behavior before a migration cutover.

For failures, separate network/TLS/authentication, SQL privileges, storage/capacity and replication/feature-specific errors. Avoid granting broad administrator rights to an application to fix a wrong hostname or missing schema grant.

Before deleting a DB system, replica, channel or HeatWave cluster, identify consumers, recovery retention and whether data or compute is being removed. Preserve requested backups and report retained capacity. Use [database migration](recipe-database-migration.md) for cutover sequencing and [hybrid access](recipe-hybrid-private-access.md) for on-premises clients.

## Sources

- [MySQL HeatWave resource and feature entry points](https://docs.oracle.com/en-us/iaas/mysql-database/home.htm)
- [Managed high availability and role transitions](https://docs.oracle.com/en-us/iaas/mysql-database/doc/overview-high-availability.html)
- [Database connection workflows](https://docs.oracle.com/en-us/iaas/mysql-database/doc/connecting-db-system1.html)
