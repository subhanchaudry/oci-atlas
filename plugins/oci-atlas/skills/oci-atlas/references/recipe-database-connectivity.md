# Recipe: connect an application to Autonomous Database

Reviewed: 2026-10-29 · Basis: documentation-based suggested pattern; not a live-tested connection.

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

## Sources

- [Autonomous Database private endpoint configuration and troubleshooting](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/private-endpoints-autonomous.html)
- [Python driver mTLS connection workflow](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/connecting-python-mtls.html)
- [JDBC TLS and mTLS distinctions](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/connect-jdbc-thin-wallet.html)
