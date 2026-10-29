# Queue messages, visibility, and dead-letter handling

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Choose work delivery versus an event log

Queue decouples producers and consumers for independently processed messages. Choose it when work should be received, processed and acknowledged/deleted according to a queue contract. Compare Streaming/Kafka when retained log replay, partitions and consumer offsets are the deciding requirements. Notifications supplies a different topic/subscription delivery model.

Define message schema, business key, expiration, retry behavior and the processing side effect. A successfully published message is not a completed task. Service durability and temporary message invisibility do not establish exactly-once business processing after worker crashes or client timeouts.

## Resource relationships and access

A queue has configured retention and delivery behavior, and a message is handled through the applicable message endpoint/interface. Visibility timeout hides received work temporarily; successful processing must be followed by the supported deletion/acknowledgment operation to prevent redelivery. A failed/expired processing attempt can make the message available again.

Dead-letter handling isolates messages that exceed the configured processing attempts. Supported channels and other service features have their own lifecycle and limits. Resolve producer and consumer IAM permissions separately from queue-administration access, and use the actual advertised message endpoint rather than assuming the management endpoint is interchangeable.

## Working sequence

Navigate to **Queues** and inspect `oci queue --help` plus the selected supported messaging client. Resolve the actual queue, region, processing principal and network path. Keep sensitive payloads and tokens out of diagnostic output.

1. Read existing queue settings and producers/consumers. Choose retention, maximum attempts and visibility based on the workload instead of memorized defaults.
2. Publish a bounded synthetic or authorized message and inspect individual publication outcomes. A client timeout might leave accepted work in the queue.
3. Receive using the intended consumer. Correlate the message/business ID and current receipt/acknowledgment context.
4. Perform the requested bounded processing action with application-level duplicate protection where appropriate. Extend visibility through the supported interface if processing genuinely needs more time.
5. Delete/acknowledge after the intended durable side effect, not before work has completed. Record processing outcome separately from receive success.
6. Inspect visible/in-flight/dead-letter state and consumer errors to understand backlogs and repeated failures.

## Diagnose and replay

Repeated delivery can reflect expired visibility, a worker crash, failed deletion or intentional replay. Empty receive results can reflect in-flight work, polling/scope or no available messages; they are not proof the entire pipeline is complete. A dead-letter message needs diagnosis of the underlying data/handler problem before redrive.

For replay or backlog clearing, identify affected business effects and the exact requested message scope. Do not purge a production queue to investigate one bad message. Preserve the application schema/version contract when deploying new consumers. Before deleting a queue, enumerate producers, in-flight work, retained failures and recovery/export requirements. Use [Streaming](service-streaming.md) or [managed Kafka](service-streaming-kafka.md) when the actual requirement is log-oriented replay.

## Sources

- [Queue visibility, deletion, and processing concepts](https://docs.oracle.com/en-us/iaas/Content/queue/overview.htm)
- [Dead-letter queue handling](https://docs.oracle.com/en-us/iaas/Content/queue/deadletterqueues.htm)
- [Message publication, consumption, and lifecycle interfaces](https://docs.oracle.com/en-us/iaas/Content/queue/home.htm)
