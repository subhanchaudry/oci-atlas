# Recipe: connect an application to Autonomous Database

Reviewed: 2026-11-03

## Workload contract

**Outcome:** Application SQL connection through the intended private path.

**Inputs:** Runtime location; database private hostname/service/port; driver/version; TLS or mTLS; application SQL grants; secure credential/wallet source.

**Flow:** Application resolver → private endpoint → TLS listener → SQL session → permitted object.

**Starting configuration:** Start with the existing database and network. Keep connection-pool sizing and retry limits explicit. A credential rotation should refresh the pool through the application lifecycle; it should not recreate the database.

## Completion and handoff

Resolve the expected private address, connect with hostname verification, run SELECT 1 FROM dual and a permitted application read. Record which layer failed; do not print connection secrets.

Return the selected scope, artifact/configuration revision, observed application result, remaining dependencies and operating owner. Include recurring capacity and retained data in [cost planning](service-cost-management.md); keep cleanup scoped to workload-owned resources.

## Resolve the connection contract

Identify the database/deployment, application runtime and location, driver/version, intended DB account and SQL permissions, endpoint mode, and TLS/mTLS requirements. Keep OCI management access, network access and SQL authorization separate. Preserve an existing private endpoint unless the customer explicitly chooses a different architecture.

## Suggested working sequence

1. Read the database's actual connection details and network configuration. Use the advertised hostname, service name and port; don't synthesize a connect string from its display name.
2. From the actual application network, resolve that hostname and check TCP reachability. For on-premises/private callers, inspect private DNS forwarding and both directions of the network path. A successful test on a developer laptop says little about a Function or job runtime.
3. Select the supported driver connection mode. Where mTLS is required, obtain the appropriate wallet through the customer's secure workflow and mount/configure it at runtime. Where supported TLS is selected, follow that driver's walletless requirements. Don't log or upload wallet contents.
4. Provision or select a scoped application DB user. Store credentials using the customer's secret-management mechanism; don't use ADMIN as the long-term application identity.
5. Configure the driver's connection descriptor and pool. Perform a bounded SQL check such as `SELECT 1 FROM dual` using the application identity, then verify access to only the intended objects.
6. Verify the application connection path and a representative read. Record outcome without secrets. Configuration complete, TCP reachable, SQL authenticated and application functional are separate milestones.

## Diagnosis and lifecycle

Unknown hostname → inspect DNS. Timeout → inspect routing, endpoint policy and firewalls. TLS/certificate error → inspect descriptor, trust, wallet and driver mode/version. Authentication/SQL privilege error → inspect database identity and grants. Don't broaden NSGs or change the database workload type when the evidence points to SQL grants or DNS.

For password/wallet rotation, identify consumers and supported overlap/rollout behavior. Before deleting a database or secret, identify the application dependency and requested retention. Use [databases/data](databases-data.md) and [networking](networking.md) only when their details are needed.

## Private callers and other engines

For an on-premises runtime, use the [hybrid access recipe](recipe-hybrid-private-access.md) and [DRG/DNS guide](service-hybrid-connectivity.md). For temporary administration, use [Bastion](service-bastion.md); a session is not a permanent production application connection. For another engine, follow its actual endpoint/client rules in [Base Database](service-base-database.md), [MySQL HeatWave](service-mysql-heatwave.md), or [PostgreSQL](service-postgresql.md). OCI control-plane access, TCP/TLS success, SQL authentication, and table privileges remain separate checks.

## Sources

- [Autonomous Database private endpoint configuration and troubleshooting](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/private-endpoints-autonomous.html)
- [Python driver mTLS connection workflow](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/connecting-python-mtls.html)
- [JDBC TLS and mTLS distinctions](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/connect-jdbc-thin-wallet.html)
