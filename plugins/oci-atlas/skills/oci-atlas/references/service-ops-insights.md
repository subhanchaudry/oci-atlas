# Ops Insights capacity, SQL trends, and AWR collection

Reviewed: 2026-11-17

## Choose historical analysis

Ops Insights uses collected database and host data for capacity planning and performance trends. It complements [Database Management](service-database-management.md), which supplies operational diagnostics and management. A utilization forecast supports a sizing decision; it does not reserve cloud capacity or guarantee a future workload's performance.

## Resources and prerequisites

Identify the target type, collection method, enabled feature set and observation period. Supported configurations differ across OCI, external, Autonomous and Exadata resources. Use the supported onboarding path and inspect credentials, IAM and required collectors/private access. The unified onboarding flow can enable Database Management and Ops Insights together without making their feature coverage identical.

For AWR analysis, distinguish recent snapshot collection, an AWR Hub, and a customer-owned warehouse. The reviewed Snapshot Collection release supports eligible Oracle Database 19c and later targets, including CDBs, configured for Private Endpoint telemetry. Select the documented collection/warehouse mode and verify database licensing, connectivity, credentials and retention before collecting performance data. An existing database does not automatically become an AWR warehouse.

## Working pattern

1. Open **Ops Insights** and inventory enabled resources and collection issues. Verify timestamps and coverage before interpreting an empty or quiet chart.
2. Compare a representative workload window with peaks, growth and known application changes. Separate missing samples from low utilization.
3. Use SQL Insights to identify fleet SQL trends and compare relevant databases. Open available SQL Monitoring reports for the selected SQL execution context rather than assuming every historical statement has a report.
4. Use AWR Snapshot Collection and AWR Explorer when the recent diagnostic window is appropriate. Use the supported Bring Your Own Warehouse flow when customer ownership of the warehouse is required.
5. Record the evidence, observation period, proposed action and expected validation. Reassess after a workload or capacity change.

## Retention, cost, and lifecycle

Inspect service and warehouse retention separately; a stopped target can leave historical data while creating a gap in new observations. Track service charges, warehouse capacity and related metric retrieval using current terms. Before disabling a resource or deleting a warehouse, identify reports and diagnostic consumers and export only authorized evidence.

The November Snapshot Collection release retains snapshots for 30 days by default, configurable per database up to 92 days. Bring Your Own Warehouse supports selected snapshots for up to 25 months using Autonomous AI Lakehouse resources. Recheck these settings and the selected collection mode before relying on an older diagnostic window.

The current overview flags Ops Insights for MySQL HeatWave as deprecated, with existing enabled resources available until January 29, 2027. Do not recommend it for new HeatWave onboarding; check the service-change notice and the owning HeatWave monitoring options.

## Sources

- [Ops Insights scope, retention and service-change notice](https://docs.oracle.com/en-us/iaas/operations-insights/doc/operations-insights.html)
- [Unified onboarding](https://docs.oracle.com/en-us/iaas/releasenotes/operations-insights/unified-onboarding-dbm-opsi.htm)
- [AWR collection and customer-owned warehouse](https://docs.oracle.com/en-us/iaas/releasenotes/operations-insights/awr-snapshot-collection-bring-your-own-warehouse.htm)
- [SQL Monitoring reports](https://docs.oracle.com/en-us/iaas/releasenotes/operations-insights/sql-monitoring-reports.htm)
