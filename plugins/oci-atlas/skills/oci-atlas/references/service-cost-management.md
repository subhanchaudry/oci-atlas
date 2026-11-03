# Cost planning, budgets, and resource ownership

Reviewed: 2026-11-03

## Separate an estimate from observed spending

For an estimate, collect region/currency, workload hours, capacity and utilization, storage growth, backup/replica retention, network paths and any licensing or commercial terms. Look up applicable prices at task time. Show quantities and assumptions alongside totals; distinguish list-price estimates from customer contract charges.

For observed spending, start with Cost Analysis or usage reports for an explicit time range, currency and grouping. Confirm billing access and reporting delay. Compare like periods and preserve subscription/compartment scope. An empty or delayed report is not evidence that resources are free.

## Work through a cost question

1. Identify the workload's runtime, data stores, protection, ingress/egress, observability and shared services.
2. Build a component table: quantity, unit, hours/volume, price source/date, owner and retention behavior.
3. Separate steady-state, burst, one-time migration and standby/recovery consumption.
4. For a cost change, group actual spending by service/SKU, region and compartment or applicable cost-tracking tag. Correlate with resource changes; don't infer causality from one chart.
5. Recommend a bounded change tied to demand and recovery needs. Rightsizing requires utilization evidence and compatibility checks, not only a price comparison.

## Budgets and tags

Budgets provide thresholds and alerts; they do not stop consumption. Establish budget scope, period, recipient and threshold, then inspect delivery. Quotas restrict selected resource quantities but are not general monetary spending caps.

Use defined tags and defaults for governed ownership/project metadata. Check permissions on the namespace and preserve unrelated tags. Cost-tracking tags have their own reporting behavior; applying a tag now does not guarantee historical costs are reattributed. Do not put personal data or secrets in tags.

## Cleanup and continuing charges

List workload-owned capacity separately from shared services. Check retained volumes, snapshots, backups, replicas, load balancers, IP resources, logs and model endpoints after runtime removal. Confirm billing behavior for stopped resources from the owning service. Return retained resources with an owner and reason; deleting data to reduce costs requires that deletion to be in scope.

## Sources

- [Billing and Cost Management](https://docs.oracle.com/en-us/iaas/Content/Billing/)
- [Budgets](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/budgetsoverview.htm)
- [Tagging](https://docs.oracle.com/en-us/iaas/Content/Tagging/Concepts/taggingoverview.htm)
