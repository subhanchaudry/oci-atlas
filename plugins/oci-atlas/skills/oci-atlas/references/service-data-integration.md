# Data Integration design and runtime artifacts

Reviewed: 2026-10-29 · Basis: documentation review; no live tasks or schedules.

## Choose it for the integration workload

Use Data Integration for supported data movement/transformation workflows when its design and connector model fits. Compare Data Flow for custom Spark application execution, Streaming for event transport, and AI Data Platform for governed workspace/catalog workflows. The phrase “data flow” does not identify which product the customer is using.

## The object chain

Workspace → project/folder → data assets/connections → design-time data flow or pipeline → task → published application artifact → task run. A data asset describes a source/target connection and metadata. A design-time pipeline orchestrates tasks; publishing prepares runtime artifacts. Saving a design does not run it or update every published copy.

Inspect operator access and service/runtime permissions separately. The service must reach source and target systems through the right DNS, network and credentials. Previewing source metadata in one tool does not establish job-run access.

## Working pattern

1. Select the actual workspace and project. Inspect existing source/target assets and runtime application before creating duplicates.
2. Resolve connection type, metadata, schemas, transformation intent, and source/target privileges. Keep secrets inside supported credential handling.
3. Build or update the design. Validate parameter mappings and dependencies; inspect schema changes and null/type behavior.
4. Create/update the appropriate task and publish it to the intended application. Record artifact/version/patch and runtime parameters.
5. Run the published task, inspect status/logs, and verify bounded target counts/objects and any expected reject behavior.
6. Add or modify a schedule only when requested. A schedule points to a runtime task; a successful manual run is not proof that the schedule uses the same parameters/version.

Console search: **Data Integration**. Inspect installed `oci data-integration --help` and the specific workspace/task/application operation. Use the current owning API contract rather than converting UI labels to guessed CLI commands.

## Updates and common mistakes

When a design changes, check publication state rather than repeatedly editing the same design while the runtime executes an older artifact. A successful orchestration result doesn't prove target data correctness. Before rerunning a partially completed load, inspect write mode, committed output and replay semantics to avoid duplicates.

For cleanup, inspect schedules, published consumers, connection reuse and retained target data. Don't delete a shared data asset solely because one task failed. Use [data ingestion](recipe-data-ingestion.md) for the full source-to-target workflow.

## Choose the integration layer

[Oracle Integration](service-oracle-integration.md) addresses application/business integrations and adapters. Data Integration addresses data assets, transformations, publication, and task runs. For ongoing database change capture inspect [GoldenGate](service-goldengate.md); for an engine move and coordinated cutover use the [migration recipe](recipe-database-migration.md). These are separate lifecycle and authorization models.

## Sources

- [Data Integration concepts](https://docs.oracle.com/en-us/iaas/Content/data-integration/using/overview.htm)
- [Data flows and transformation design](https://docs.oracle.com/en-us/iaas/Content/data-integration/using/data-flows.htm)
- [Data Integration tutorials](https://docs.oracle.com/en-us/iaas/Content/data-integration/tutorials/index.htm)
