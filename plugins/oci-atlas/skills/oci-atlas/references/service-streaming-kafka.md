# Streaming with Apache Kafka clusters and client access

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Distinguish the two streaming services

Streaming with Apache Kafka manages supported Kafka clusters in OCI. It is a different service from OCI Streaming's stream/stream-pool model and Kafka-compatible interface. Select by required Kafka behavior, supported version, client ecosystem, network/security requirements and operating model. The name “Kafka” in a client configuration does not identify which OCI control plane owns the resource.

Compare [Queue](service-queue.md) for independently acknowledged work messages and [Streaming](service-streaming.md) for that service's managed stream abstraction. Do not promise every upstream Kafka extension, configuration or version in a managed service; inspect the current support and configuration references.

## Resource and identity model

The OCI cluster resource supplies the managed Kafka environment and selected network/configuration. Topics, partitions, consumer groups and offsets govern the application data contract. OCI management operations and Kafka client administration/produce/consume are distinct interfaces.

Resolve supported SASL/SCRAM or mTLS configuration and Kafka ACLs for the actual cluster. OCI IAM administration is not automatically a client credential or topic-level permission. A bootstrap connection does not prove the client can reach every broker address advertised in metadata.

## Working sequence

Use Console **Streaming with Apache Kafka** and the service-specific management API/CLI. Do not use `oci streaming` stream-pool commands as an assumed Kafka-cluster management interface. Use compatible Kafka client tools/SDKs for data-plane tasks.

1. Inspect cluster identity/version, topology, network, endpoints and existing topic/consumer ownership. Verify current capacity and available configuration choices.
2. Define topic/partition, retention, message schema, key/ordering needs and consumer-group behavior. Treat application processing semantics separately from broker durability.
3. Establish the approved client authentication and scoped ACLs using secure credential/certificate handling.
4. Verify DNS and network reachability from producers/consumers to the actual advertised cluster endpoints.
5. Produce and consume a bounded synthetic message when that write is authorized. Inspect producer outcomes, consumer progress and the downstream processing result.
6. Observe lag, partition distribution, broker/storage health and application errors before changing cluster size or partitioning.

## Diagnose and operate

Bootstrap succeeds but metadata requests fail → inspect advertised broker addresses and their network path. Authentication succeeds but operations fail → inspect topic/group ACLs and actual client identity. Growing lag → separate producer rate, hot partitions, consumer capacity and failing downstream writes.

Changing partitions, retention, consumer offsets or serializers can alter ordering, replay and compatibility. Resetting offsets can repeat side effects; inspect the application idempotency/transaction contract first. A managed cluster does not automatically make an arbitrary sink exactly once.

Before upgrades or configuration changes, review supported version transitions, client compatibility and maintenance impact. Before deletion, enumerate topics, consumers, retained data and backup/export needs. Preserve external sources and shared clusters unless their removal is requested. Record resulting cluster/client behavior, not only a successful OCI work request.

## Sources

- [Managed Kafka concepts and resource model](https://docs.oracle.com/en-us/iaas/Content/kafka/concepts.htm)
- [SASL/SCRAM client security](https://docs.oracle.com/en-us/iaas/Content/kafka/security-sasl.htm)
- [Versions, ACLs, mTLS, and lifecycle tasks](https://docs.oracle.com/en-us/iaas/Content/kafka/home.htm)
- [Separate OCI Streaming service](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streamingoverview.htm)
