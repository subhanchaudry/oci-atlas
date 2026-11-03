# Recipe: Extend SaaS with application and integration services

Reviewed: 2026-11-03

## Outcome and inputs

Extend Fusion workflows without confusing SaaS and OCI authorization.

**Inputs:** SaaS product/version, documented API/event, user identity, extension UI, business object/key, integration ownership and transaction/retry rules.

**Flow:** User or SaaS event → extension UI/API → integration or application logic → supported SaaS API → reconciled business result.

## Starting architecture

Use Oracle Integration for supported adapter/orchestration needs, Visual Builder for a suitable extension UI, or an OCI application API when custom logic is required. OCI IAM does not grant access to Fusion business objects.

## Implementation sequence

Confirm API contract, pagination, privileges and rate limits with the SaaS owner. Configure credentials through the product mechanism. Map user/service identity and row/object access. Start with a bounded read, then an explicitly scoped business transaction with a correlation/idempotency strategy.

Before changing resources, establish the selected identity, region, compartment and existing configuration owner. Provision dependencies before consumers, then observe resource state and the application result separately.

## Configure the first business transaction

1. Select one supported SaaS business API/event and a nonproduction business object. Record API version, required SaaS role, business validation rules and the expected completion state.
2. Configure the SaaS connection and narrowly scoped credentials before enabling orchestration. Use [Oracle Integration](service-oracle-integration.md) when supported adapters and process orchestration fit; a custom API can own simpler logic.
3. Add the extension UI only after the business transaction works through its supported API. Use the SaaS/product identity flow and keep user authorization separate from the integration's service identity.
4. Carry one correlation key through the UI, integration and SaaS response. Persist accepted/in-progress/completed/failed states when completion is asynchronous. Retry only where idempotency or reconciliation prevents duplicate business objects.
5. Change one compatible API/integration/UI revision at a time and verify the resulting business object, not just HTTP success. Route incomplete transactions to their operating owner before replay.

Optional production choices include approval workflows, throttling, audit retention and user-specific business-object filtering. No extension should bypass SaaS authorization by directly modifying the underlying application database.

## Application checks

Observe the business object in the authoritative SaaS system and the extension response; a successful HTTP call alone may not mean an asynchronous business process completed.

## Updates, recovery, and cleanup

A multi-system transaction may partially complete. Persist correlation and reconciliation state; retry only the failed boundary where supported. Version integration/UI/API changes together and preserve shared connections. Do not describe an illustrative extension as a verified customer integration.

Use [cost management](service-cost-management.md) to record runtime, retained storage, traffic and shared-service costs. Use [workload selection](workload-selection.md) for alternatives and [support handoff](troubleshoot-support-handoff.md) for unresolved service boundaries.

## Sources

- [SaaS extension architecture](https://docs.oracle.com/en/solutions/extend-saas-cloud-native/index.html)
- [Oracle Integration](https://docs.oracle.com/en/cloud/paas/application-integration/)
