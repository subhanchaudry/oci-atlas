# Streaming producers, consumers, and replay

Reviewed: 2026-10-29 · Basis: documentation review; no live message publication.

## Model the delivery contract

Use Streaming for continuously produced events and decoupled consumers, rather than as a permanent relational store. Resolve message key/format, partitioning, ordering requirement, retention, expected rate and replay behavior. “Delivered to the stream” and “processed by the application” are different outcomes.

Streams are partitioned append-only logs. A stream pool supplies shared configuration and endpoint context. Producers publish messages; consumers or consumer groups track reading progress through supported mechanisms. Don't infer global ordering or exactly-once business effects from service durability.

## Network and identity

Distinguish management operations from the message endpoint used by producers/consumers. Use the actual stream/pool endpoint and selected interface. Compatibility with a Kafka API is not evidence that every Kafka feature, setting or authentication method behaves identically.

For private access, inspect pool/endpoint networking, DNS and permitted caller routes. Resolve the producer and consumer principals separately. A user able to list a stream may not have rights to publish or consume its data.

## Working sequence

1. In Console **Streaming**, identify the pool and stream in the correct region/compartment. Inspect `oci streaming --help` for the supported administrative/message operations.
2. Resolve partition/retention choices and supported changes from current service documentation before provisioning.
3. Publish a small non-sensitive event through the chosen authenticated message interface. Inspect per-message results instead of assuming a request-level success means every message was accepted.
4. Consume using the intended application identity/group and verify content and processing outcome.
5. Record consumer state and replay/idempotency behavior before applying retries or resetting progress.

## Operate and clean up

For lag, inspect production rate, partition distribution, consumer errors and processing capacity. A hot partition can persist even when other consumers are idle. For missing events, inspect the actual stream, time range, retention and cursor/group behavior before claiming data loss.

Consumers writing downstream systems should handle duplicates/replay according to the business contract. Changing a consumer group or cursor can reread data. Before deletion, identify producers/consumers and any requirement to archive/replay retained events; stream deletion is not a routine way to resolve lag.

## Sources

- [Streaming features and use cases](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streamingoverview.htm)
- [Stream lifecycle and private-endpoint prerequisites](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/managingstreams.htm)
- [OCI API retry and response behavior](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/usingapi.htm)
