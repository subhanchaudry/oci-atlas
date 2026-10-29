# APEX workspaces, application access, and ORDS

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Resolve the deployment and application goal

APEX provides database-centered application development. ORDS supplies supported HTTPS/database gateway and REST capabilities, including APEX access. Identify APEX Service, APEX on a selected database service, or a self-managed installation before choosing administration and deployment steps.

Do not install a separate ORDS server merely because an application needs a REST endpoint; inspect the managed service's existing gateway capabilities first. Conversely, a self-managed ORDS deployment has its own runtime, configuration, TLS and maintenance responsibilities. Check actual APEX/ORDS/database version compatibility rather than applying a generic database provisioning example.

## Four distinct boundaries

An OCI compartment organizes cloud resources. An APEX workspace organizes developer/application context and maps to database schemas. A parsing schema supplies the application's database object/privilege context. End-user application authentication/authorization governs use of the app. Creating an OCI user or signing into APEX development does not automatically configure all four.

ORDS database pools, schema enablement, REST modules/handlers and their privileges/roles are another resource/access layer. A published REST module is not necessarily appropriately authenticated. A URL returning HTTP success does not prove row-level authorization or protection of other database objects.

## Working sequence

Use the selected database/APEX service Console and the actual APEX workspace/admin interface. For self-managed ORDS, inspect the installed `ords --help` and configuration/version documentation. Do not treat an APEX workspace as an OCI compartment create operation.

1. Read the existing service, APEX version, workspace/schema mapping, application identifier and ORDS management ownership.
2. Resolve the intended developer/admin, parsing schema and end-user identities. Grant only the required schema/application access through the appropriate layer.
3. Create/update the application or REST definition through its owning development/export process. Separate database DDL/data changes from importing application metadata.
4. For a REST endpoint, inspect schema enablement, module publication, route/handler, privileges and supported authentication. Keep secrets in the product's supported credential flow.
5. Verify a bounded app page or API request using the intended caller and network path. Check both successful authorized behavior and the relevant denied access when requested.
6. Record application/REST revision, schema dependencies and required database migrations for repeatable deployment.

## Diagnose and maintain

For a missing route, inspect the selected pool/schema alias, module status and reverse-proxy path. For authorization errors, distinguish OCI sign-in, workspace permissions, app authorization, ORDS privileges and SQL grants. For SQL failures, inspect the parsing schema and actual objects rather than granting a cloud administrator role.

In a self-managed deployment, pool credentials, JDBC connectivity and Java/runtime configuration can fail independently of APEX code. Preserve private configuration/wallets outside source and use the supported upgrade process.

Before deleting a workspace, app, REST module or schema, identify mapped schemas, shared applications and authoritative data. An application export is not automatically a complete database backup. Use [Autonomous Database](service-autonomous-database.md) or [Base Database](service-base-database.md) for the underlying service lifecycle.

## Sources

- [APEX cloud deployment entry points](https://docs.oracle.com/en/cloud/paas/apex/index.html)
- [Workspace-to-schema relationships](https://docs.oracle.com/en/database/oracle/apex/26.1/aeadm/managing-workspace-to-schema-assignments.html)
- [ORDS deployment and monitoring responsibilities](https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/26.3/ordig/deploying-and-monitoring-oracle-rest-data-services.html)
- [ORDS database pool installation and configuration](https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/26.3/ordig/installing-and-configuring-oracle-rest-data-services.html)
