# Logging, Audit, and Connector Hub pipelines

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Select the evidence source

Logging manages supported service logs and custom application/agent logs. Audit records supported OCI API activity and answers a different question from an application's business audit trail. Connector Hub moves supported data between OCI services using a configured source, optional tasks and a target. It is not a universal arbitrary-endpoint integration engine.

Start with the incident question and actual emitting resource. Use application logs for handler/runtime failures, service logs for the relevant service category, and Audit for supported management activity. Bucket-management Audit events do not establish all Object Storage object reads/writes; inspect supported object-access service logs for that requirement.

## Resource relationships and prerequisites

A log group organizes log resources; a log identifies its source/category or custom ingestion setup. Logging Search scopes a query by location and time. Connector configuration specifies the selected source data, supported processing, destination and required access. Delivery to a destination is separate from source ingestion.

Resolve who can enable/read logs, which principal publishes custom data, and which permissions let the connector read and write its configured services. Inspect retained sensitive fields before creating a broad export. Logging Search syntax, Monitoring MQL and Resource Search expressions are different languages.

## Working sequence

Use Console **Logging**, **Audit**, and **Connector Hub**. Inspect `oci logging`, `oci logging-search`, `oci audit`, and the current connector CLI/API reference; legacy interfaces can retain service-connector naming.

1. Capture resource, region, compartment, explicit time zone/window and a request/run identifier. Read existing log enablement, category and retention.
2. Query a bounded window and inspect the source event structure. Expand time/scope only when the evidence warrants it. Do not dump entire logs into chat.
3. If required logs are absent, distinguish unsupported category, disabled emission, agent/ingestion failure, wrong scope and retention expiry. Enabling logs now does not recreate every past event.
4. For requested transport, choose a supported source/task/target combination and inspect the required service policy. Configure the destination with suitable retention and access.
5. Observe connector lifecycle, metrics and diagnostics, then verify a known bounded record at the destination. Source visibility alone does not establish delivery.
6. Report the query/window, source and destination, observed records and unobserved portions of the path.

## Operate and diagnose

For no data movement, inspect source filters/time, connector state, permissions, target availability and supported processing behavior. Replaying a pipeline can duplicate downstream application effects, so inspect the destination contract before rerunning data. Audit event time and log arrival time can differ; do not invent causality from adjacent timestamps alone.

Plan changes around shared consumers and sensitive outputs. Removing a connector does not necessarily delete destination objects; deleting a log group can remove evidence needed by other workflows. Keep deletion/retention intent explicit. Use [Monitoring and Notifications](service-monitoring-notifications.md) for alarms and delivery and [the observability recipe](recipe-observability-delivery.md) to connect the layers.

## Sources

- [Logging kinds, categories, and ingestion](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/loggingoverview.htm)
- [Audit coverage and event fields](https://docs.oracle.com/en-us/iaas/Content/Audit/Concepts/auditoverview.htm)
- [Connector sources, tasks, and targets](https://docs.oracle.com/en-us/iaas/Content/connector-hub/overview.htm)
- [Connector lifecycle and delivery troubleshooting](https://docs.oracle.com/en-us/iaas/Content/connector-hub/home.htm)
