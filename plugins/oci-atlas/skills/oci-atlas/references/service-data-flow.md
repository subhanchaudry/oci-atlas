# Data Flow Spark applications and runs

Reviewed: 2026-10-29 · Basis: documentation review; no live Spark runs.

## Choose the execution model

OCI Data Flow runs Spark workloads without requiring the customer to operate a conventional persistent Spark cluster. It differs from a Data Integration design-time data flow and from an AI Data Platform workspace. Identify the service before looking up permissions, runtime settings or job status.

An application holds a reusable execution definition; a run is a particular execution with inputs, runtime/resource settings, logs and results. Pools and other supported execution choices have their own resource/cost behavior. Do not assume all resources stop simply because one application run finished.

## Resolve prerequisites

Capture code artifact and dependencies, supported Spark/language version, entry point, arguments, executor/driver sizing, data/output locations, principal behavior and logging. Access to an application definition is not automatically access to its code or data. Follow the documented execution identity for the selected mode; don't infer it from the human's current local profile.

For private sources, inspect the Data Flow private endpoint and network/DNS configuration. A driver connecting successfully doesn't prove every executor can use an external dependency. Keep external database credentials separate from OCI authentication.

## Execute and verify

Use Console **Data Flow** and `oci data-flow ... --help` for the actual application/run operation. Inspect existing application revisions before creating duplicates. Create a bounded run with explicit parameters and track its run identifier. Check lifecycle state, driver/executor logs and output location.

Verify output partitioning/schema and a bounded record count or business invariant appropriate to the task. Empty output may reflect filters or input selection; it is not necessarily a Spark infrastructure failure. For a failed run, identify the first meaningful error rather than reporting the last cascading executor message.

## Diagnose and change

Artifact read failure → inspect URI and execution identity. Connection error → inspect private endpoint/DNS/routes and source auth. Class/package mismatch → inspect runtime and bundled dependencies. Memory/skew issue → inspect plan, partitions and workload characteristics before increasing all compute. Current limits and available runtime settings must be checked at execution time.

For reruns, establish overwrite/append and partial-output behavior. Canceling or deleting run metadata doesn't establish that output objects were removed. Retain the application/run/code identifiers needed to reproduce a result and clean up only the requested data/capacity.

## Sources

- [Data Flow overview](https://docs.oracle.com/en-us/iaas/Content/data-flow/using/dfs_service_overview.htm)
- [Applications, runs, pools and private access](https://docs.oracle.com/en-us/iaas/Content/data-flow/using/concepts.htm)
- [Data Flow developer and troubleshooting entry points](https://docs.oracle.com/en-us/iaas/Content/data-flow/using/home.htm)
