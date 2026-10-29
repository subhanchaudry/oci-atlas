# Recipe: governed source-to-target data ingestion

Reviewed: 2026-10-29 · Basis: documentation-based suggested pattern; no live data movement.

## Choose the control plane

For connector-led batch workflows, start with Data Integration. For custom Spark, inspect Data Flow. For governed workspace/catalog workflows, inspect AI Data Platform. For continuous transport, use Streaming with a separately chosen processing/sink layer. Reuse the existing suitable system before proposing a parallel platform.

Resolve source/target, schema, volume/cadence, incremental keys/watermarks, data privileges, network location and output/replay semantics. A medallion label describes a data-design choice, not an automatically provisioned service topology.

## Suggested sequence

1. Inspect existing assets, connections and source/target privileges. Identify the actual runtime principal and network, not only the operator.
2. Verify bounded source metadata/read access and target write mode. For a private external catalog, establish the workspace network, source credentials and supported catalog operations.
3. Define transformations, schema mappings, invalid-record handling and incremental/replay behavior. Keep raw data retention and sensitive fields aligned with the request.
4. Create/update the correct artifact chain: Data Integration design → task → published application; Data Flow application → run; or the platform's workspace/workflow path. Don't mix their terminology/API contracts.
5. Run a bounded slice and verify target counts/schema plus a relevant data invariant. Observe rejected/partial records and output locations as well as orchestration status.
6. Only add a schedule/event trigger when requested. Record the deployed revision, runtime parameters and watermark/state so the next run can be explained.

## Reruns and cleanup

Before retrying, inspect committed output and the intended append/merge/overwrite behavior. Prevent duplicates through the pipeline's documented business-key/idempotency strategy rather than assuming service retries are exactly once. Preserve lineage from source/window to execution to output.

Deleting a failed execution, connection or catalog doesn't necessarily delete target data, and deleting a shared asset can break other jobs. Enumerate downstream consumers and retention requirements before cleanup. See the relevant [selection guide](service-selection.md) or focused data-service reference for details.

## Select transport and replication deliberately

Use [Queue](service-queue.md) for distributed tasks, [Streaming](service-streaming.md) for retained event consumption, or [Streaming with Apache Kafka](service-streaming-kafka.md) when Kafka platform requirements determine the choice. Inspect [GoldenGate](service-goldengate.md) for supported database change replication and the [migration recipe](recipe-database-migration.md) when an application cutover is the goal. [Oracle Integration](service-oracle-integration.md) fits business application integrations; it does not share Data Integration's publication/run objects.

## Sources

- [Data Integration artifact lifecycle](https://docs.oracle.com/en-us/iaas/Content/data-integration/using/overview.htm)
- [Spark applications and runs](https://docs.oracle.com/en-us/iaas/Content/data-flow/using/concepts.htm)
- [Data Platform external catalogs](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/external-catalogs.html)
- [Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streamingoverview.htm)
