# Recipe: Process uploaded objects with idempotent consumers

Reviewed: 2026-11-03

## Outcome and inputs

Process uploaded files, retry work, and reconcile dead letters.

**Inputs:** Bucket/prefix and event enablement, object version semantics, handler duration, target schema, deduplication key and recovery owner.

**Flow:** Object events → Events rule → Function → durable result; use Streaming for retained replay or an explicit Function-to-Queue bridge when worker claiming is required.

## Starting architecture

Events supports Functions, Streaming and Notifications actions. Do not assume a native Queue action. Use a bounded Function for short work; decouple longer work through the selected transport.

## Implementation sequence

Verify the event payload and selected rule; scope delivery and handler permissions separately. Read the object version represented by the event, validate its format, then commit output and the idempotency record together where the storage contract permits. A repeated event must not repeat a business side effect.

Before changing resources, establish the selected identity, region, compartment and existing configuration owner. Provision dependencies before consumers, then observe resource state and the application result separately.

## Configure the first workflow

1. Start with one dedicated object prefix, one event rule and one handler. Select object-create events and filter the intended bucket. Enable object events on that bucket before expecting deliveries.
2. Give the rule's delivery principal only the selected target access. Give the handler read access to the intended input objects and write access to its result destination; use the [IAM guide](service-iam-policies.md) to separate deployment from runtime access.
3. Persist a key such as bucket/object/version plus operation. A claim needs an expiry or recoverable state so a crashed handler cannot leave work permanently marked complete.
4. For Queue workers, configure visibility longer than a normal processing attempt, bounded retries and dead-letter handling using the [Queue guide](service-queue.md). Acknowledge only after durable output. A Function-to-Queue bridge must report enqueue failures rather than silently accepting the event.
5. Replay one failed item after correcting its cause, preserving its business key. Reconcile input and completed-output counts before replaying a batch. Events, Function invocation, Queue redelivery and business retries are distinct mechanisms; no universal dead-letter queue covers all four.

Optional production choices include partitioning, concurrency limits, poison-message quarantine and a dedicated replay operator. Select these from measured processing duration and downstream capacity.

## Application checks

Replay the same synthetic input twice and inspect one logical result; simulate a handler failure and confirm recoverable state. Do not infer exactly-once effects from message delivery.

## Updates, recovery, and cleanup

Track received, completed, retrying and failed work. Inspect dead-letter/error records before bounded replay; preserve original IDs and object versions. Keep raw objects until the result retention policy permits removal. Disabling a rule does not cancel accepted downstream work.

Use [cost management](service-cost-management.md) to record runtime, retained storage, traffic and shared-service costs. Use [workload selection](workload-selection.md) for alternatives and [support handoff](troubleshoot-support-handoff.md) for unresolved service boundaries.

## Sources

- [Events overview](https://docs.oracle.com/en-us/iaas/Content/Events/Concepts/eventsoverview.htm)
- [Queue](https://docs.oracle.com/en-us/iaas/Content/queue/overview.htm)
- [Serverless application architecture](https://docs.oracle.com/en-us/iaas/Content/cloud-adoption-framework/serverless.htm)
- [Event-triggered serverless reference architecture](https://docs.oracle.com/en/solutions/event-triggered-serverless-app/index.html)
