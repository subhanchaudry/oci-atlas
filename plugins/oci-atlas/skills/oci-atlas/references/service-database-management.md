# Database Management diagnostics, jobs, and privileges

Reviewed: 2026-11-17

## Choose the operational task

Database Management provides database fleet monitoring, performance diagnosis and supported management operations. Choose [Ops Insights](service-ops-insights.md) for historical capacity and fleet SQL analysis, [Data Safe](service-data-safe.md) for database-security assessments, or [Database Tools](service-database-tools.md) for client/MCP access. These services can share targets without sharing authorization or lifecycle.

## Target and access model

Resolve the database deployment type, database/CDB/PDB scope, version and management option. Basic and Full management have different feature coverage; use the feature-support matrix for the actual target. External databases require their supported registration and connectivity path. OCI access to a managed-database resource does not grant database credentials or permission to execute administrative SQL.

The unified onboarding flow can enable Database Management, Ops Insights, or both for supported resources. It gathers connection and credential configuration together, but the selected services still need their own permissions and supported target configuration. Record which services were enabled.

## Working pattern

1. Open **Database Management**, select the compartment and database, and inspect onboarding, collection status, connection health and management option.
2. Establish an incident time window and workload context. Use database metrics and Performance Hub to locate the relevant workload rather than treating a fleet average as the failing SQL statement.
3. Inspect **Privilege analysis** for supported databases. Compare used/unused grants against a representative capture period before proposing changes; an unused privilege in a short observation window is not automatically safe to revoke.
4. For requested SQL jobs, select the target database or database group, inspect the template and parameters, and confirm the executing credentials. Oracle-defined job templates are starting points, not preauthorization to change a fleet.
5. Inspect per-target job outcomes and verify the intended database result. For custom monitoring, test a Metric Extension Template before publishing and applying it.

## Operating record

Record target coverage, collection gaps, diagnostic window, job revision, credentials by reference, and unresolved actions. Database Management can also monitor supported GoldenGate deployments; that monitoring does not replace replication checkpoint inspection. Account for the selected management option, database licensing prerequisites and related collection resources. Before disabling management, identify alerts, jobs and diagnostic consumers; disabling monitoring does not stop the database.

## Sources

- [Diagnostics and Management target support](https://docs.oracle.com/en-us/iaas/database-management/doc/database-management-oracle-databases.html)
- [Unified onboarding](https://docs.oracle.com/en-us/iaas/releasenotes/operations-insights/unified-onboarding-dbm-opsi.htm)
- [Privilege analysis](https://docs.oracle.com/en-us/iaas/releasenotes/database-management/privilege-analysis.htm)
- [Database Management releases](https://docs.oracle.com/en-us/iaas/releasenotes/services/database-management/)
