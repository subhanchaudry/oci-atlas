# Monitoring queries, alarms, and notification delivery

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Model the entire delivery chain

Monitoring stores/query metrics and evaluates alarms. Notifications publishes messages through topics and subscriptions. A resource metric existing, an alarm entering a firing state, publication to a topic, delivery to a subscriber and a human receiving it are separate outcomes. Diagnose the failing boundary rather than recreating every alarm.

Choose a signal and threshold that represent the customer's actual health or capacity question. Do not infer a useful threshold from a generic CPU percentage without the workload's aggregation interval and expected behavior. Use a log-derived metric or application metric when host utilization does not represent the outcome.

## Resource relationships and prerequisites

A metric stream has a namespace, metric name and dimensions. Queries select and aggregate streams over a time range. Alarms add an expression, evaluation behavior and destination. A Notifications topic has protocol-specific subscriptions whose state matters to delivery. Verify current confirmation and endpoint requirements for the chosen subscription protocol.

Operator permissions, metric publication permissions, alarm destination access and a downstream Function's runtime identity are distinct. Check the region and compartment at each point. A diagram showing Notifications connected to a Function is not proof the Function can access its own downstream data.

## Working pattern

Use Console **Metrics Explorer**, **Alarm Definitions**, and **Topics**. Inspect `oci monitoring --help` and `oci ons --help`. Reuse [access conventions](access-and-tools.md) for selected identity, auth mode and region.

1. Inspect actual metric names, dimensions, timestamps and units. Check whether the service or agent emits the expected data before creating an alarm.
2. Run the bounded query in the intended resource scope. Review aggregation, interval and missing-data handling. A missing stream is not a zero sample.
3. Read or configure the requested alarm using the real resource dimension and expected evaluation window. Inspect suppression, enabled state and destination.
4. Read the topic and intended subscription state. Resolve confirmation or endpoint configuration through the normal user/service flow.
5. Use an authorized harmless publication or known alarm transition when delivery verification is requested. Observe publication and destination behavior separately; do not manufacture a production incident to trigger the alarm.
6. Record the query, alarm/topic/subscription identifiers, time window and evidence at each completed stage.

## Diagnose and maintain

Alarm never fires → inspect query scope, metric availability, time window and suppression. Firing alarm but no message → inspect destination, service authorization and relevant publication evidence. Published but not received → inspect subscription confirmation, endpoint response, filtering and delivery diagnostics. An email appearing in one inbox does not prove every subscriber received it.

For updates, preserve useful dimensions and avoid merging unrelated resource streams into a misleading aggregate. Keep sensitive payloads out of broad topics. Before deletion, identify alarms, event rules and connectors using a shared topic. Use the [observability recipe](recipe-observability-delivery.md) for logs/metrics/notifications together and [Logging/Connector Hub](service-logging-audit-connectors.md) for evidence transport.

## Sources

- [Metric streams, queries, and alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm)
- [Topics, subscriptions, and delivery](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationoverview.htm)
- [Notifications confirmation and troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Notification/home.htm)
