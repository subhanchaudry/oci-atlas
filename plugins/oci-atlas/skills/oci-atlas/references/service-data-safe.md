# Data Safe targets, assessments, auditing, and masking

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Choose the database-security task

Data Safe provides supported database-security capabilities such as security/user assessment, discovery, activity auditing, masking and SQL Firewall management. Identify the specific feature and target database first. Registering a database does not prove that every feature is configured, all sensitive data was found, or a security recommendation was remediated.

Separate assessment/discovery from operations that change database behavior or data. A request to inspect sensitive-column metadata is not permission to run a masking job against production. Masking changes values and needs an explicitly selected suitable copy, preservation intent and application-data checks.

## Target and access model

A Data Safe target references the actual Oracle database/PDB plus its supported connection/authentication setup. Depending on placement, connectivity can use a supported private endpoint or on-premises connector. A registered but inactive target can still lack a working connector or database login.

OCI IAM controls access to Data Safe resources; target-database service accounts/roles authorize the selected database operations. Network reachability, database grants and human Data Safe permissions are separate. A CDB and its PDBs can have different registration/feature scope; do not infer complete estate coverage from one visible target.

## Working sequence

Navigate to **Data Safe → Target databases** and the requested feature. Inspect current Data Safe API/CLI help for management operations and the feature's documented database prerequisites. Keep credentials and sensitive discovery/audit output inside appropriate handling flows.

1. Identify the exact target, database/version/location, selected feature and existing registration. Read its connection and readiness state.
2. Resolve the supported network path from Data Safe and the necessary feature-specific database grants. Inspect private endpoint/connector requirements rather than assuming the operator's SQL connection proves service access.
3. Run the requested bounded assessment, discovery or audit query. Capture the evaluated target, time and relevant findings without exporting sensitive rows unnecessarily.
4. Distinguish observed configuration from a recommendation and from an actual correction. Correlate with the database owner's intended policy.
5. For requested masking, work on the approved database copy, review the sensitive-data model and masking policy, perform supported prechecks and inspect the effect on related data/application integrity.
6. For audit/security-policy changes, verify scope and the resulting database/application behavior independently from the management request.

## Diagnose and maintain

For a failed assessment or collection job, inspect target readiness, grants, listener/TLS, connector/endpoint health and feature-specific errors. OCI Audit and database activity auditing answer different questions. A lack of collected audit records can reflect configuration or retention, not an absence of database activity.

Review automatic registration policies and shared connectors before changing them; a policy can affect additional PDBs. Before deregistration or removing an endpoint, enumerate dependent targets, reports and collection/retention needs. Deleting Data Safe metadata and deleting the database are different operations. Use [Base Database](service-base-database.md), [Autonomous Database](service-autonomous-database.md), and [hybrid connectivity](service-hybrid-connectivity.md) for the underlying resource and network boundaries.

## Sources

- [Data Safe capabilities and feature entry points](https://docs.oracle.com/en-us/iaas/data-safe/index.html)
- [Target registration](https://docs.oracle.com/en-us/iaas/data-safe/doc/target-database-registration.html)
- [Target connectivity choices](https://docs.oracle.com/en-us/iaas/data-safe/doc/connectivity-options-target-databases.html)
- [Masking workflow and data-change implications](https://docs.oracle.com/en-us/iaas/data-safe/doc/data-masking-overview.html)
