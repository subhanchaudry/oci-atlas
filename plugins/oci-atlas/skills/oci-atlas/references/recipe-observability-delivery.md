# Recipe: application evidence and notification delivery

Reviewed: 2026-11-17

## Workload contract

**Outcome:** An application signal reaches its intended operator.

**Inputs:** Application/resource; metric/log/trace; time window; signal condition; destination; recipient; retention and response owner.

**Flow:** Emitter → collection/query → alarm or connector → topic/subscriber → recipient.

**Starting configuration:** Start with one useful application signal. Add [APM](service-apm.md) for request traces; scope retention and redaction before expanding collection.

## Completion and handoff

Correlate one bounded signal through all configured stages and record actual receipt. A firing alarm and a delivered message remain separate observations.

Return the selected scope, artifact/configuration revision, observed application result, remaining dependencies and operating owner. Include recurring capacity and retained data in [cost planning](service-cost-management.md); keep cleanup scoped to workload-owned resources.

## Define the operational question

Choose the application/resource, success/failure signal, time window, intended recipient and required response. Map application/service → metric or log → query/connector/alarm → topic/subscription → recipient or action. Do not enable every available log or create a fleet-wide alarm for a narrowly scoped incident.

Decide whether the goal is immediate diagnosis, ongoing monitoring, evidence export or automatic response. Each has different retention, permissions and side effects. A notification sent to an automation endpoint can change resources or trigger business actions; a request to inspect an alarm does not authorize adding such a response.

## Suggested sequence

1. **Identify the emitter.** Find the resource's supported metric namespace/dimensions, service-log category or custom application log source. Resolve region/compartment and whether an agent/configuration is required.
2. **Confirm useful evidence.** Inspect a bounded metric/log window with explicit time zone and a request/run identifier. Distinguish missing emission, wrong query scope, retention and delayed arrival from a real zero/absence of activity.
3. **Configure only the requested path.** For alarms, select the relevant query/evaluation behavior. For export or log-to-metric processing, choose a supported Connector Hub source/task/target combination and scoped permissions.
4. **Resolve delivery.** Inspect the actual Notifications topic, subscription protocol/state and confirmation/endpoint requirements. Separate alarm/service publication rights from human permissions and downstream action identity.
5. **Exercise a harmless bounded signal when authorized.** Use a supported synthetic publication or appropriate known event. Check query/trigger state, publication and the destination's actual receipt separately. Do not create a production failure solely to trigger an alert.
6. **Record the operational result.** Report what is emitting, what matched, what was published, which recipient/action was observed and which part remains unobserved.

## Diagnostic branches

No expected metric/log → inspect the emitter/category/agent and actual resource dimensions. Data visible but alarm quiet → inspect aggregation, evaluation window, threshold, enabled/suppressed state and missing-data behavior. Alarm firing but no delivery → inspect destination, subscription confirmation, permissions and delivery diagnostics. Connector active but no exported data → inspect source filters, target access and observed records.

Correlate timestamps and request IDs without assuming adjacent events prove causality. Avoid sharing sensitive log bodies, authentication material or broad audit exports. Use [Monitoring/Notifications](service-monitoring-notifications.md) for queries and delivery, and [Logging/Audit/Connector Hub](service-logging-audit-connectors.md) for evidence collection and transport.

## Maintain and remove

Define an owner, useful signal scope, retention and expected recipient/action. Review whether application revisions changed labels, schemas or dimensions. An alarm that once worked can later monitor an obsolete resource ID.

Before changing a shared topic, connector or log group, enumerate dependent alarms, event rules and consumers. Deleting a connector does not necessarily delete exported destination data; deleting a log can remove evidence. Remove only requested temporary artifacts and report retained destinations/retention explicitly. A successful configuration operation should not be reported as verified alert receipt.

## Include database evidence where needed

For a database-backed application, link the alert/trace window to [Database Management](service-database-management.md) and [Ops Insights](service-ops-insights.md) when enabled for the target. Verify collection freshness before interpreting absent data. Retain relevant SQL/AWR evidence under the chosen access and retention policy; monitoring enablement is not proof that a notification reached its recipient.

## Sources

- [Monitoring streams and alarm evaluation](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm)
- [Notifications topics and subscriptions](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationoverview.htm)
- [Logging categories and ingestion](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/loggingoverview.htm)
- [Connector source-task-target relationships](https://docs.oracle.com/en-us/iaas/Content/connector-hub/overview.htm)
- [Microservices tracing architecture](https://docs.oracle.com/en/solutions/oci-apm-for-microservices/)
- [Diagnostics and Management target support](https://docs.oracle.com/en-us/iaas/database-management/doc/database-management-oracle-databases.html)
- [Unified onboarding](https://docs.oracle.com/en-us/iaas/releasenotes/operations-insights/unified-onboarding-dbm-opsi.htm)
- [Privilege analysis](https://docs.oracle.com/en-us/iaas/releasenotes/database-management/privilege-analysis.htm)
- [Database Management releases](https://docs.oracle.com/en-us/iaas/releasenotes/services/database-management/)
- [Ops Insights scope, retention and service-change notice](https://docs.oracle.com/en-us/iaas/operations-insights/doc/operations-insights.html)
- [AWR collection and customer-owned warehouse](https://docs.oracle.com/en-us/iaas/releasenotes/operations-insights/awr-snapshot-collection-bring-your-own-warehouse.htm)
- [SQL Monitoring reports](https://docs.oracle.com/en-us/iaas/releasenotes/operations-insights/sql-monitoring-reports.htm)
