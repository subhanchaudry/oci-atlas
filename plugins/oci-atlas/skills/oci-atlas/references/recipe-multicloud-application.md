# Recipe: Connect a multicloud application to Oracle data

Reviewed: 2026-11-17

## Outcome and inputs

Plan application and database access across cloud ownership boundaries.

**Inputs:** Application cloud/region, database deployment product, latency target, data location, address ranges, connection owners, SQL identity and recovery requirements.

**Flow:** Application in another cloud → selected supported interconnect/private path → database endpoint; DNS, identity and return routing remain explicit.

## Starting architecture

First distinguish a database running in OCI from an Oracle Database@ partner-cloud offering. They have different provisioning, networking and commercial boundaries. Do not treat a private interconnect as automatic availability in every region pair.

## Implementation sequence

Select a documented topology and current eligible locations. Map routes, DNS forwarding, TLS and SQL grants from the application runtime. Keep OCI management identity separate from partner-cloud IAM and database authentication. Measure representative application round trips before committing to a chatty remote data path.

Before changing resources, establish the selected identity, region, compartment and existing configuration owner. Provision dependencies before consumers, then observe resource state and the application result separately.

## Configure the first application path

1. Identify the product and both execution locations before selecting connectivity. A database in OCI, Oracle Database@Azure and another provider's managed database have different control planes and network ownership.
2. Inventory nonoverlapping address ranges, private DNS suffixes, return routes, firewall owners and application connection pools. Record who owns incident triage on each side.
3. Establish the supported regional connection and resolver forwarding before deploying a database-dependent application. Use [hybrid connectivity](service-hybrid-connectivity.md) and [DNS](service-dns.md); keep identity federation separate from SQL authentication.
4. From one actual application instance, resolve the database name, complete TLS and a bounded SQL query, then measure representative transactions including connection reuse. Keep latency assumptions explicit until observed.
5. Exercise reconnect behavior after a connection interruption. Document how copied data is reconciled and which database is authoritative before redirecting writers.

Optional production choices include redundant links, regional recovery and data replication. Evaluate data residency, egress charges, licensing and the selected region pair separately from application functionality.

## Application checks

Resolve the intended private endpoint and complete an application query from the partner cloud; a circuit-up state is not proof of SQL or latency requirements.

## Updates, recovery, and cleanup

Record egress, interconnect and database cost assumptions separately. Plan circuit/region loss, connection-pool recovery and writer ownership. Preserve provider-managed resources and shared connections when removing one application.

Use [cost management](service-cost-management.md) to record runtime, retained storage, traffic and shared-service costs. Use [workload selection](workload-selection.md) for alternatives and [support handoff](troubleshoot-support-handoff.md) for unresolved service boundaries.

## Preserve address and migration boundaries

For overlapping IPv4 networks, consult [DRG NAT](service-vcn-routing.md) and verify translation, DNS and return paths across both owners. If the task is relocating supported AWS guests, use [Cloud Migrations](service-cloud-migrations.md); cross-cloud application access alone does not require moving the database or changing its authoritative writer.

## Sources

- [Autonomous Database on Azure reference architecture](https://docs.oracle.com/en/solutions/deploy-autonomous-database-db-at-azure/index.html)
- [Hybrid connectivity](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm)
- [Oracle Interconnect for Azure](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm)
- [IPv4 NAT on DRG attachments](https://docs.oracle.com/en-us/iaas/releasenotes/network/nat-drg.htm)
- [Cloud Migrations resource model and workflow](https://docs.oracle.com/en-us/iaas/Content/cloud-migration/cloud-migration-overview.htm)
- [Supported AWS Arm migrations](https://docs.oracle.com/en-us/iaas/releasenotes/cloud-migration/ocm_aws_arm_migration.htm)
