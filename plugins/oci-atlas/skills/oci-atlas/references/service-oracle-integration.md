# Oracle Integration instances, connections, and activation

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Distinguish application integration from data integration

Oracle Integration connects applications and automates supported business/integration workflows using its adapter/runtime model. OCI Data Integration focuses on its data movement/transformation artifacts. A Data Integration task published to an application and an Oracle Integration integration activated in a project are different objects and deployment processes.

Resolve the customer's actual product generation, integration style, source/target applications, latency and business contract. Verify adapter/feature support and the selected service entitlement rather than assuming every SaaS API operation is supplied by an installed adapter. A request to create an integration definition does not authorize scheduling live business transactions.

## Resource and access model

The OCI service instance is the control-plane resource. Product projects, adapter connections, integrations/versions and runtime executions belong to the integration platform. OCI permission to create an instance does not automatically give every user the product role needed to design, activate or monitor an integration.

Connection credentials authorize the actual source/target systems and are separate from human sign-in and OCI IAM. A connectivity agent or supported private endpoint can supply a particular outbound/private path, depending on the adapter and configuration. It does not universally make every endpoint reachable or authorize the source application.

## Working sequence

Navigate to **Oracle Integration** in OCI for instance management, then the selected instance's product interface for integration design/runtime work. Use the current control-plane versus product API references separately; do not translate a UI label into a guessed `oci data-integration` command.

1. Inspect the instance, project/integration/version, connection references, current activation and schedule state. Identify the deployment owner and existing consumers.
2. Resolve supported adapter operations, request/response mapping, source/target identities and network path from the actual runtime.
3. Configure connections through the secure product workflow. Validate the specific operation's permissions; a successful connection check need not prove a complete business transaction.
4. Build/update the scoped integration and inspect mappings, retries/fault handling and tracking identifiers using authorized synthetic inputs where appropriate.
5. Activate only the requested version through the supported process. Reconcile whether changed connections require affected integrations to refresh/reactivate.
6. Invoke or schedule only within the customer's task. Observe the runtime instance and verify the intended downstream outcome separately from activation success.

## Diagnose and operate

Distinguish instance availability, activation/configuration, adapter authentication, runtime network failures and target application errors. Retry/resubmit can repeat a purchase, notification or database write; inspect the business idempotency and partial effects before resending.

Use tracking/correlation metadata and bounded sanitized payloads for diagnosis. Broad tracing can expose sensitive business content. Before changing a shared connection, enumerate integrations that use it; a credential refresh can affect more than the failing flow.

Before deactivation/deletion, inspect schedules, inbound consumers, running executions and shared connections/agents. Deleting the OCI instance is much broader than removing an unused integration version. Preserve data-system ownership and record incomplete or retained runtime work. Use [Data Integration](service-data-integration.md) for ETL-specific workflows and [hybrid connectivity](service-hybrid-connectivity.md) for underlying private routes.

## Sources

- [OCI instance administration and inbound/outbound access](https://docs.oracle.com/en-us/iaas/application-integration/index.html)
- [Oracle Integration product documentation and adapters](https://docs.oracle.com/en/cloud/paas/application-integration/index.html)
- [Outbound network access](https://docs.oracle.com/en-us/iaas/application-integration/doc/manage-outbound-network-access.html)
- [Activation and connection-update behavior](https://docs.oracle.com/en/cloud/paas/application-integration/integrations-user/activate-deactivate-integrations.html)
