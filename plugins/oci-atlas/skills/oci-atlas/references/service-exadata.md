# Exadata deployment choices and resource operations

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Resolve the Exadata offering first

Exadata is a family of deployment and operating models, not one interchangeable provisioning API. Identify Dedicated Infrastructure, Exascale Infrastructure, Cloud@Customer or an Autonomous deployment before selecting object names, network requirements or maintenance procedures. A multicloud Database@ offering has its own provider/control-plane workflow; don't apply an OCI-native create command to a different portal's resource model.

Choose the offering from workload capabilities, capacity/elasticity, administration responsibility and existing estate. Exadata is not automatically required because an application uses Oracle SQL. Compare [Base Database](service-base-database.md) and [Autonomous Database](service-autonomous-database.md) when their supported features satisfy the requirement.

## Resource relationships and responsibilities

For Dedicated Infrastructure, distinguish physical infrastructure allocation, cloud VM clusters, database software homes and the databases/PDBs using them. Oracle infrastructure maintenance and customer-managed database/guest operations have different scopes. A healthy infrastructure resource is not proof that each database or application service is healthy.

For Exascale, identify the VM cluster and Exascale storage-vault model. Do not assume its storage allocation and scaling behave like dedicated storage servers. Database version can change the underlying storage architecture and supported operations. Inspect the actual resource type and current documentation before reusing a scaling or backup example.

## Prerequisites and working sequence

Use the selected **Exadata Database Service** Console entry and its current `oci db`/API resource schema. Resolve region capacity, edition/license context, network/subnet requirements, DNS, keys, backup targets and administrator/SQL access separately.

1. Inventory the current infrastructure or storage vault, VM cluster, DB homes, databases and application owners. Identify shared capacity and maintenance schedules.
2. Select the exact provisioning or resize target. Compute, local resources, database storage and shared infrastructure capacity are different limits.
3. Inspect dependencies and supported change behavior. A request to expand one database should not silently replace a shared cluster or change every consumer's configuration.
4. Submit the bounded operation through its owning workflow and observe work-request/resource state.
5. Verify database service availability, the intended capacity change and a relevant application connection/query. For restore or role changes, inspect the protection mechanism and recovery point.
6. Record retained capacity, software/maintenance state and any guest/database actions still required.

## Diagnose, maintain, and remove

Separate allocation shortage, cluster/guest health, database-open state, listener/service configuration and SQL authorization. Increasing a VM cluster's compute does not necessarily resolve a database-storage limit or a bad query plan. Check current billing semantics before promising that stopping a VM/cluster stops charges.

Coordinate service-supported maintenance with the application's availability design and the actual infrastructure/database owner. Before cleanup, enumerate databases, homes, clusters, shared vault/infrastructure and protection dependencies. Remove only the requested layer and preserve retained backups/data. A successful database deletion does not imply dedicated infrastructure or other billable capacity was removed. Use [Full Stack DR](service-full-stack-dr.md) for cross-layer recovery planning rather than treating infrastructure redundancy as complete DR.

## Sources

- [Dedicated Infrastructure deployment and administration](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/index.html)
- [Dedicated Infrastructure technical architecture](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/exacs-tech-arch.html)
- [Exascale VM clusters, storage vaults, and version differences](https://docs.oracle.com/en/engineered-systems/exadata-database-exascale/exdxs/overview-exadb-xs-service.html)
- [Exascale cluster management and scaling](https://docs.oracle.com/en/engineered-systems/exadata-database-exascale/exdxs/manage-vm-clusters.html)
