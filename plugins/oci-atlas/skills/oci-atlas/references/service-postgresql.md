# OCI Database with PostgreSQL systems and private access

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Establish managed-service compatibility

Choose OCI Database with PostgreSQL for a PostgreSQL-compatible application when the managed service's supported version, extensions and operational model fit. Capture required extensions, roles, replication/migration method and application driver behavior before promising compatibility with a self-managed source.

Do not assume unrestricted operating-system or PostgreSQL superuser access. A feature supported by upstream PostgreSQL is not automatically enabled or configurable in this managed service. Use current version/extension/configuration documentation for the selected system.

## Resource and connectivity model

A database system has managed nodes, configuration/management policies, storage and connection endpoints. Databases, schemas and PostgreSQL roles are data-plane objects, distinct from OCI IAM management resources. An OCI user who can resize a system does not automatically have SQL access to application tables.

The documented database endpoints require connectivity to the system's VCN/private subnet. Use the actual endpoint FQDN, CA certificate and supported client connection parameters. A developer signed in to Console still needs a network path. Bastion port forwarding can support bounded administration; VPN/FastConnect/private application networking support different ongoing access needs.

## Prerequisites and working sequence

Navigate to **PostgreSQL → DB systems** and inspect installed `oci psql --help`. Resolve region/compartment, subnet/NSGs, database version, nodes, backup policy, SQL identity and existing ownership. Keep credentials in the normal supported authentication mechanism.

1. Read the existing system and its actual connection details, configuration and protection state.
2. Confirm required extensions/configuration against the service-supported list. Inspect the documented enablement and any restart or privilege requirements before changing them.
3. Provision/update the intended resource through its owning workflow and observe lifecycle/work-request state.
4. Resolve DNS and verify the private network path from the real client. Configure hostname-verifying TLS with the advertised CA/endpoint rather than disabling verification to bypass a tunnel issue.
5. Use a bounded SQL connection/query with the intended application role. Inspect schema visibility and privileges separately from transport success.
6. For import/migration or restore, verify source/target compatibility, data completeness and application behavior before switching consumers.

## Diagnose and operate

Unknown hostname or timeout → inspect resolver, routes and network rules. TLS error → inspect the expected hostname, trust bundle and client settings. Login/query failure → inspect database role, secret validity and grants. Extension failure → inspect managed-service support and enablement rather than changing operating-system packages on an assumed host.

Use observed workload/node/storage signals for sizing; don't assume memory used by a database cache is a leak. Review node/configuration and maintenance effects before resizing or changing topology. Confirm current backup/restore semantics and retained recovery points instead of equating high availability with protection against logical deletion.

Before cleanup, identify schemas, applications, integrations, backups and management ownership. Deleting a database system is broader than dropping an unused schema or removing a temporary client. Preserve requested data and report retained resources. See [Bastion](service-bastion.md) and [connectivity diagnosis](troubleshoot-connectivity.md) for access paths, and the [migration recipe](recipe-database-migration.md) for coordinated cutover.

## Sources

- [Managed PostgreSQL concepts](https://docs.oracle.com/en-us/iaas/Content/postgresql/overview.htm)
- [Private endpoints, TLS, and Bastion client access](https://docs.oracle.com/en-us/iaas/Content/postgresql/connect-to-db.htm)
- [Supported extension enablement](https://docs.oracle.com/en-us/iaas/Content/postgresql/config-list-enable-extension.htm)
- [Backup, configuration, and node lifecycle entry points](https://docs.oracle.com/en-us/iaas/Content/postgresql/home.htm)
