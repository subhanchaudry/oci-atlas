# Autonomous Database operations and access

Reviewed: 2026-10-29 · Basis: documentation review; no live database or SQL changes.

## Select the right deployment

Resolve the workload, deployment option, compute model, data protection requirements, client/driver and intended region. ATP/ADW terminology can persist in customer materials while current documentation uses Autonomous AI Transaction Processing/Lakehouse labels. Translate labels carefully; don't infer that an API field or workload enum changed with a product name.

Use Autonomous Database when its managed operating model fits the application. Compare Base Database or Exadata offerings for specific control/features rather than provisioning a familiar database type automatically. Verify current licensing, availability and scaling characteristics for the selected option.

## Three access layers

1. OCI management identity creates, scales or configures the database resource.
2. The caller's network resolves and reaches the selected endpoint.
3. The database identity authenticates and has SQL privileges on the intended schema objects.

Success at one layer does not establish the others. A wallet configures the client security/connection material; it does not create routing or grant table privileges. TLS versus mTLS support depends on database configuration and driver/version. Obtain the actual descriptor and port; avoid default-port guesses.

## Lifecycle pattern

Inspect `oci db autonomous-database --help` and the chosen operation's request schema. Before creation, resolve network access, credentials through a secure mechanism, scaling/storage, backup and retention settings. Avoid placing passwords in command history or committed JSON input. After creation, inspect database state and connection details, then verify bounded SQL using an application identity where that is in scope.

For updates, read existing configuration and identify downtime, autoscaling, endpoint and consumer implications. Stop/start does not remove persisted storage and backups; inspect the current billing behavior rather than promising zero cost while stopped.

For a clone or restore, identify source, point in time, destination and data handling before executing. Before deletion, resolve dependencies, retention and recovery expectations; identify which backups/resources remain.

## Diagnose from the actual runtime

Use the [database connectivity recipe](recipe-database-connectivity.md) for application setup. Unknown hostname suggests DNS investigation; a TCP timeout suggests endpoint/routing/security checks; a TLS failure suggests driver/trust/descriptor checks; successful login with a denied query suggests grants/schema resolution. Changing ATP/ADW workload type is not a network troubleshooting step.

## Related database and application choices

For engine/deployment alternatives, use [Base Database](service-base-database.md), [Exadata](service-exadata.md), and [service selection](service-selection.md). For supported database-native retrieval, use [Oracle AI Vector Search](service-ai-vector-search.md). [APEX workspaces and ORDS](service-apex-ords.md) have application/schema boundaries inside and around the database; OCI compartment access does not supply application or SQL authorization. [Data Safe](service-data-safe.md) and [Database Migration](service-database-migration.md) require their own target connections and privileges.

## Sources

- [Private endpoints and network configuration](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/private-endpoints-autonomous.html)
- [Python mTLS connection](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/connecting-python-mtls.html)
- [JDBC TLS/mTLS distinctions](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/connect-jdbc-thin-wallet.html)
- [Autonomous Database CLI discovery](https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/db/autonomous-database/list.html)
