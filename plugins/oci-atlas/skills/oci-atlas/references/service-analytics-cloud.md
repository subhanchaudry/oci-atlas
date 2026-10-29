# Analytics Cloud instances, data connections, and roles

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Choose the analytics layer

Oracle Analytics Cloud (OAC) provides supported analytics, visualization, semantic/reporting and related data-preparation capabilities. Use it when the requested business-consumption/modeling workflow fits. AI Data Platform supplies a different workspace/catalog/compute environment; a database or data pipeline does not automatically provision an OAC instance or publish a workbook.

Resolve the service edition/capacity, user audience, source systems, freshness and governance requirements. Check current features and connection support for the selected version rather than promising every visualization, AI capability or database connector from a general product description.

## Resource and authorization model

The OCI instance controls the managed service's capacity/network/lifecycle. Inside OAC, connections, datasets, semantic models, workbooks and catalog content have their own ownership and access. Source database credentials/roles control which data a connection can read. Identity-domain users/groups and OAC application roles are related administration layers, not the same permissions.

OCI management access does not automatically authorize every workbook or underlying table. Product roles can permit authoring or administration without establishing a source network path. A workbook shared to users must still respect the actual data/row-access model; don't assume sharing a link creates an appropriate tenant boundary.

## Prerequisites and working sequence

Use Console **Analytics Cloud** for the instance and the product's **Console**/content interfaces for application-level work. Inspect current instance API/CLI versus product REST documentation separately. Resolve the intended user's roles, connection owner, private access/gateway mechanism and data source grants.

1. Read the existing instance, version/capacity/network and application/content owner before creating a parallel environment.
2. Establish the data connection through its supported interface and secure credential handling. Verify reachability from OAC or the configured gateway/private path, not only a developer laptop.
3. Inspect source schema/data visibility and required business definitions. Choose live/query versus imported/refresh behavior from the actual supported connection and workload.
4. Build/update the intended dataset, semantic content or workbook. Preserve source identifiers, meaningful metrics and any existing access rules.
5. Verify the result with the intended user role and a bounded source-data comparison. A successful connection does not prove correct joins, freshness or report authorization.
6. Configure sharing, refresh or delivery only within the requested audience/schedule. Record content revision and the actual source/refresh time.

## Diagnose and maintain

Missing data can reflect source grants, filters, cache/refresh, mapping or the selected identity. Separate these from instance unavailability. For performance, inspect query/model behavior and source capacity before increasing instance capacity indiscriminately.

An OAC snapshot/content export does not automatically back up the authoritative source database or recreate every external credential/network dependency. Plan service changes using supported backup/restore and migration procedures. Before cleanup, enumerate shared connections, scheduled deliveries/refreshes and downstream users; deleting one workbook and deleting the instance have very different scopes. Use [database guides](databases-data.md) for source management and [Data Integration](service-data-integration.md) for upstream data movement.

## Sources

- [Analytics Cloud service and administration entry points](https://docs.oracle.com/en-us/iaas/analytics-cloud/index.html)
- [Instance creation and setup](https://docs.oracle.com/en-us/iaas/analytics-cloud/doc/create-services.html)
- [Identity accounts versus OAC application roles](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acgov/users-roles-pages-oracle-analytics-cloud-console.html)
- [Product administration, content backup, and permissions](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acabi/understanding-administration-pages.html)
