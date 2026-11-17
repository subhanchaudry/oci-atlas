# Recipe: Connect AIDP to a private database source

Reviewed: 2026-11-17

## Outcome and inputs

Register and query a private source from AIDP workspace compute.

**Inputs:** AIDP instance/workspace, compute/network configuration, supported source type, source credentials, schema visibility, catalog permissions and workflow owner.

**Flow:** Workspace compute → private DNS/network → source database; external catalog → permitted metadata → workflow → owned output.

## Starting architecture

Reuse the source and workspace. Register the external catalog only after confirming the source type and operation are supported. Platform administrator access does not replace OCI IAM or source SQL grants.

## Implementation sequence

Resolve the hostname from the actual workspace runtime; inspect forward/return routes, security and TLS. Establish a bounded source login, then discover only permitted schemas/tables. Grant platform object access independently. Execute a small notebook query before scheduling a workflow.

Before changing resources, establish the selected identity, region, compartment and existing configuration owner. Provision dependencies before consumers, then observe resource state and the application result separately.

## Configure the first private-source query

1. Record the exact AIDP workspace, supported external-source type, database hostname/service, TLS mode and source schema. Begin with a read-only account and one small table.
2. Establish DNS, routes and traffic rules from the workspace's execution environment. Select the documented private connection mechanism for that source; do not assume a workstation tunnel is inherited by managed compute.
3. Create the supported connection/catalog metadata with its designated credential. Separate permission to manage that metadata from permission to use it and from SQL grants on the source.
4. Inspect schema discovery and then run a bounded query from the same compute that will execute the workflow. Capture the failing stage: metadata registration, schema discovery, execution connection or SQL authorization.
5. Materialize into an explicitly owned destination only when required. Record the initial watermark and validate a second incremental run before scheduling it.

Use [AIDP](service-ai-data-platform.md), [private DNS](service-dns.md) and [database connectivity](recipe-database-connectivity.md) for the applicable configuration boundary. Optional production work includes credential rotation, schema-change handling and separate workspace/catalog roles; none is solved by merely registering a catalog.

## Application checks

Show the intended schema/table, run a bounded query, reconcile its output and inspect a scheduled execution separately from a manual run.

## Updates, recovery, and cleanup

For missing metadata, inspect source account visibility and catalog limitations before adding permissions. For timeouts, inspect runtime networking rather than the developer browser. Record workflow revision, parameters, watermark and output path; remove catalog/workflow metadata without deleting authoritative source data.

Use [cost management](service-cost-management.md) to record runtime, retained storage, traffic and shared-service costs. Use [workload selection](workload-selection.md) for alternatives and [support handoff](troubleshoot-support-handoff.md) for unresolved service boundaries.

## Separate external catalogs from hosting

For a supported Snowflake external catalog, configure access to the existing source and verify permitted schemas from the actual AIDP compute. This does not provision Snowflake natively in OCI. Use the [AIDP feature-status guidance](service-ai-data-platform.md) before choosing credential, lineage or Git workflows; preview features are not required steps in this GA recipe.

## Sources

- [Data platform architecture](https://docs.oracle.com/en/solutions/data-platform-lakehouse/index.html)
- [External catalogs](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/external-catalogs.html)
- [Workspaces](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/workspaces.html)
- [AIDP and Data Science workflow architecture](https://docs.oracle.com/en/solutions/ai-data-platform-data-science-workloads/)
- [AIDP dated feature history and preview labels](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidwn/index.html)
- [AIDP deployed agents and runtime identity](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/agent-flow-deployment.html)
- [AI compute autoscaling](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/ai-compute.html)
- [Agent memory and retention](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/agent-memory.html)
