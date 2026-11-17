# Recipe: Build a governed lakehouse and analytics path

Reviewed: 2026-11-17

## Outcome and inputs

Connect ingestion, curated data, and governed analytics.

**Inputs:** Source ownership, freshness target, incremental keys, data classification, catalog, engine/runtime, target schema and analytics audience.

**Flow:** Source → raw/staging storage → selected transformation engine → curated tables → semantic model/dashboard.

## Starting architecture

Reuse suitable Object Storage and database resources. Choose Data Integration for supported connector workflows, Data Flow for Spark, or AIDP for its workspace/catalog model. A medallion label does not require three different services.

## Implementation sequence

Establish source and target grants from the execution runtime. Preserve raw lineage and schema versions, quarantine invalid rows, and apply a documented watermark/merge strategy. Publish a curated contract with keys, grain and freshness before connecting Analytics Cloud.

Before changing resources, establish the selected identity, region, compartment and existing configuration owner. Provision dependencies before consumers, then observe resource state and the application result separately.

## Configure the first data product

1. Start with one source table or file family, one raw prefix, one curated dataset and one dashboard. Record primary keys, event time, deletion semantics and a reproducible watermark.
2. Create or select governed destinations before scheduling ingestion. Select a connector workflow, Spark job or AIDP workspace based on supported source and transformation requirements; a reference architecture does not make them interchangeable.
3. Separate source-read, raw-write, transform-write and dashboard-read identities. Grant SQL/schema access separately from OCI service access. See [Data Integration](service-data-integration.md), [Data Flow](service-data-flow.md) and [Analytics Cloud](service-analytics-cloud.md).
4. Run one bounded load, reconcile row counts and totals, then repeat the same watermark range to check merge/deduplication behavior. Publish only reconciled curated output to dashboard readers.
5. Change schema with downstream compatibility in mind. Retain the prior transformation and raw input needed to reconstruct the affected partition; prevent two schedules from writing the same target concurrently.

Optional production choices include catalog governance, table-format selection, partition maintenance and separate development/production datasets. Confirm each selected engine's actual format and catalog compatibility.

## Application checks

Reconcile bounded source/target counts and one business measure, then verify the intended viewer can access permitted rows and sees the expected freshness.

## Updates, recovery, and cleanup

Keep source data, curated outputs and OAC content as separate recovery scopes. For backfill, select a partition/window and prevent duplicate effects. Version semantic changes and coordinate consumers; deleting a workflow does not remove copied datasets.

Use [cost management](service-cost-management.md) to record runtime, retained storage, traffic and shared-service costs. Use [workload selection](workload-selection.md) for alternatives and [support handoff](troubleshoot-support-handoff.md) for unresolved service boundaries.

## Choose table ownership before optimization

Distinguish AIDP-owned Iceberg tables from external-source registration and [Autonomous Iceberg external tables](service-autonomous-database.md). Record metadata ownership, storage permissions, freshness and write authority. Measure partition pruning on the actual query rather than promising a fixed performance gain. Keep preview lineage or bundle workflows outside the required delivery path.

## Sources

- [Lakehouse reference architecture](https://docs.oracle.com/en/solutions/data-platform-lakehouse/index.html)
- [Data Flow](https://docs.oracle.com/en-us/iaas/Content/data-flow/using/dfs_service_overview.htm)
- [AI Data Platform](https://docs.oracle.com/en/cloud/paas/ai-data-platform/)
- [AIDP dated feature history and preview labels](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidwn/index.html)
- [AIDP deployed agents and runtime identity](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/agent-flow-deployment.html)
- [AI compute autoscaling](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/ai-compute.html)
- [Agent memory and retention](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/agent-memory.html)
- [Autonomous built-in A2A and MCP tools](https://docs.oracle.com/en-us/iaas/releasenotes/autonomous-database-serverless/2026-11-support-mcp-server.htm)
- [Iceberg external-table partition pruning](https://docs.oracle.com/en-us/iaas/releasenotes/autonomous-database-serverless/2026-10-partition-pruning.htm)
