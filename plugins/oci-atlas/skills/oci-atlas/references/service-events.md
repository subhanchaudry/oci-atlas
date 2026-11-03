# Events rules and resource-triggered actions

Reviewed: 2026-11-03

## Start with the emitted event

Events routes supported OCI resource events using rules and action destinations. It is distinct from a durable task queue, an application event log and an alarm evaluating metrics. Supported action services include Functions, Streaming and Notifications; don't draw a direct Queue action without a documented integration or application bridge.

## Resource and identity map

An emitting service produces a typed event. A rule filters its fields and selects actions. The destination processes the event using its own permissions. Events delivery rights do not grant a Function permission to read the affected object or write the result. Some data events require service-specific enablement, such as Object Storage object events.

## Working sequence

1. Find the exact event type and example payload in the source service documentation. Capture resource/compartment filters and the required outcome.
2. Configure the destination and its runtime access before enabling a rule.
3. Scope the filter to the intended resources and event attributes; preserve other rules.
4. Match a bounded event and correlate event ID, rule/action and destination behavior.
5. Check the actual business result, including duplicate handling. Receiving an event does not prove the downstream transaction completed.

## Retry and lifecycle

Design consumers for repeated delivery and delayed processing. Use a business key or object version as appropriate; an event ID alone might not identify every semantic duplicate. Persist an idempotency record with the committed business result. For durable replay, select a supported retained transport and consumer design.

Rule disablement stops matching future events but does not undo downstream work already accepted. Before deletion, identify destinations shared with other producers. Budget destination execution, retained events and logs. Use the [event-processing recipe](recipe-event-processing.md) for retries, dead letters and reconciliation.

## Sources

- [Events overview](https://docs.oracle.com/en-us/iaas/Content/Events/Concepts/eventsoverview.htm)
- [Events documentation](https://docs.oracle.com/en-us/iaas/Content/Events/home.htm)
