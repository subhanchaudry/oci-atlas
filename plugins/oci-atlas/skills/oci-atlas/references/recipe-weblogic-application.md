# Recipe: Modernize a WebLogic application on OCI

Reviewed: 2026-11-03

## Outcome and inputs

Plan WebLogic runtime, database, ingress, and release ownership.

**Inputs:** Application/archive and Java/WebLogic versions, supported deployment model, domain configuration, JDBC/JMS dependencies, sessions, licensing and maintenance ownership.

**Flow:** Client → load balancer → WebLogic managed servers → JDBC data source → database; administration and artifact delivery use separate paths.

## Starting architecture

Retain a supported VM deployment when OS/domain control is needed. Choose OKE only with a Kubernetes operating model and supported operator/images. Avoid converting a packaged application to containers solely because it uses WebLogic.

## Implementation sequence

Inventory domains, data sources, persistent stores, identity providers and application integrations. Select a supported Oracle architecture and image/operator combination. Provision through the existing ownership workflow, externalize credentials, deploy the pinned archive and establish private database access.

Before changing resources, establish the selected identity, region, compartment and existing configuration owner. Provision dependencies before consumers, then observe resource state and the application result separately.

## Configure the first deployment

1. Inventory the supported WebLogic/JDK combination, application archive, domain configuration, JDBC resources, JMS stores, session state and licensing. Choose VMs or a supported operator-managed OKE path based on the operating model.
2. Prepare private database and identity dependencies, durable stores and artifact access before creating the domain. Keep the administration interface on its intended private access path.
3. Begin with one representative application and explicit environment configuration. For Kubernetes, use the supported operator and domain/image workflow; do not assume a historical Marketplace stack is still available.
4. Verify sign-in, a database-backed transaction, messaging and session behavior as applicable. Use [APM](service-apm.md) for a trace across the application boundary and [database connectivity](recipe-database-connectivity.md) for JDBC network/TLS diagnosis.
5. Drain or preserve state before changing application/domain revisions. Retain the previous compatible archive and configuration; document whether a database migration prevents simple application rollback.

Optional production choices include managed-server clustering, load balancing, persistent-store replication and recovery topology. Size and license those components for the selected supported configuration.

## Application checks

Verify login, representative application transaction, JDBC connection and messaging/session behavior. A running managed server does not establish the business application.

## Updates, recovery, and cleanup

Coordinate domain configuration, application archives and schema migrations. Drain sessions and preserve persistent messaging state during updates. Restore the prior compatible release when possible; a rollback of the archive does not reverse schema writes. Retain licensed artifacts and data according to ownership.

Use [cost management](service-cost-management.md) to record runtime, retained storage, traffic and shared-service costs. Use [workload selection](workload-selection.md) for alternatives and [support handoff](troubleshoot-support-handoff.md) for unresolved service boundaries.

## Sources

- [WebLogic on Compute reference architecture](https://docs.oracle.com/en/solutions/deploy-wls-on-oci/index.html)
- [WebLogic on OCI](https://docs.oracle.com/en/cloud/paas/weblogic-cloud/)
- [WebLogic on OKE](https://docs.oracle.com/en/cloud/paas/weblogic-container/)
- [WebLogic Kubernetes Operator](https://oracle.github.io/weblogic-kubernetes-operator/)
