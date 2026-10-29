# Operations, security, and cost

Reviewed: 2026-10-29 · Basis: documentation review; examples are not live-tested.

## Pick the right evidence

| Question | Start with | Interpretation limit |
| --- | --- | --- |
| Is a resource healthy or overloaded? | Monitoring metrics, dimensions and time range | A missing series is not necessarily zero usage |
| Why did an application/request fail? | Relevant service/custom logs and request IDs | Logs may need enablement; coverage and retention differ |
| Who changed a cloud resource? | Audit event, caller, action, time and target | Audit coverage is not every application or object data access |
| What security issue was detected? | Cloud Guard target, detector, problem and evidence | A finding is not proof of exploitation or a complete assessment |
| What will/does this cost? | Current price inputs plus Cost Analysis/usage | Estimates and delayed spending data aren't hard spending controls |

Use explicit time zones and time windows. Correlate resource OCIDs, request IDs, deployment revisions and timestamps. State which evidence is missing rather than inventing a root cause.

## Monitoring and logging

Monitoring metrics are identified by namespaces and dimensions. Alarms evaluate a query and publish to a configured destination. Check dimensions and aggregation before comparing charts. An enabled alarm isn't proof of delivered notification; inspect its destination/subscription and delivery evidence when that is the question.

Logging separates service logs, custom logs and Audit-related views. Log groups organize log resources within compartments. Enable only the relevant categories for the task and examine the time of enablement. For Object Storage object access, use its supported service log categories; bucket-management Audit events don't cover every object read/write.

Read-only example, using [selected context variables](access-and-tools.md):

```bash
oci monitoring alarm list --compartment-id "$ATLAS_COMPARTMENT_ID" --all \
  --profile "$ATLAS_PROFILE" --auth "$ATLAS_AUTH" --region "$ATLAS_REGION"
```

Console search: **Metrics Explorer**, **Alarm Definitions**, **Logging**, and **Audit**. CLI roots: `oci monitoring`, `oci logging`, `oci logging-search`, and `oci audit`. Use the relevant query language and current command help rather than treating MQL, Logging Search and Resource Search as interchangeable.

## Security resources and identities

Cloud Guard targets define monitored scope; detector recipes produce problems and responders can change resources. Inspect the rule and resource evidence first. Enabling an automatic responder is an operational change; don't use it as a substitute for explaining a finding.

KMS manages encryption keys in vaults. The current documentation distinguishes Secret Management from key management, even where older Console/API names retain “Vault.” A secret stores versioned sensitive material; a key performs cryptographic functions. Use the supported service interfaces and runtime principal. Key rotation, disabling, and scheduled deletion have different effects on dependent data; identify consumers before changing them.

For access problems, inspect the authenticated identity, policy/resource scope, workload identity, service-specific permissions and recent changes. Don't fix every authorization failure by broadening a human policy; the failing caller may be a Function, job, node or pod.

## Cost and operational changes

Use defined tags for governed metadata and free-form tags for simple labels; inspect tag namespaces/defaults and preserve unrelated tags during updates. Never place secrets or personal data in names/tags.

Budgets are soft spending thresholds with periodically evaluated alerts. They do not stop consumption. For cost questions, state duration, utilization, region, currency, service options, storage/backup retention and network assumptions. Verify the applicable current price inputs rather than claiming an exact bill from a shape name. If cleanup is requested, identify ownership and dependencies; enumerate retained resources after the operation.

## Sources

- [Monitoring metrics and alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm)
- [Alarm list command](https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/alarm/list.html)
- [Logging categories and log groups](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/loggingoverview.htm)
- [Audit coverage](https://docs.oracle.com/en-us/iaas/Content/Audit/Concepts/auditoverview.htm)
- [Cloud Guard concepts](https://docs.oracle.com/en-us/iaas/Content/cloud-guard/using/cg-concepts.htm)
- [Vaults, keys and Secret Management distinction](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/keyoverview.htm)
- [Secret Management Service](https://docs.oracle.com/en-us/iaas/Content/secret-management/home.htm)
- [Budget behavior](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/budgetsoverview.htm)
- [Tagging](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/taggingoverview.htm)
