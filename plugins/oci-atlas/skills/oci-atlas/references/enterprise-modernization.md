# Choose an enterprise application modernization path

Reviewed: 2026-11-03

## Inventory the application before choosing infrastructure

Record application product/version, vendor support, licensing, database/middleware dependencies, filesystem and messaging state, identity integration, batch jobs and maintenance ownership. Separate rehosting, database migration, platform change and application refactoring; each changes a different compatibility boundary.

| Starting estate | Initial path | Decision that changes the path |
| --- | --- | --- |
| Custom WebLogic application | [WebLogic recipe](recipe-weblogic-application.md) | Supported VM deployment versus Kubernetes operator and an established OKE operating model |
| Packaged Oracle or third-party application | Product-specific Architecture Center playbook and vendor documentation | Certified versions/topology, license rights and support responsibilities |
| VMware estate | Oracle Cloud VMware Solution assessment | Host/storage sizing, network extension, VMware licensing and migration tooling compatibility |
| Database-centric application | [Database migration](recipe-database-migration.md) plus runtime assessment | SQL/features, outage budget, application integration and target operating model |
| SaaS customization | [SaaS extension](recipe-saas-extension.md) | Supported APIs/extension mechanisms rather than changes to managed SaaS infrastructure |

## Choose and sequence the change

1. Map the business transaction across components and identify authoritative data and state.
2. Select a currently supported reference topology. Consult the vendor's compatibility and licensing documentation for the exact product version.
3. Establish the landing-zone/network/data prerequisites and one owner for each deployment state.
4. Move a bounded application slice with a defined data synchronization point and consumer contract.
5. Coordinate writer cutover, jobs, DNS and user access. Preserve rollback conditions and retained source resources explicitly.
6. Hand off patching, capacity, application recovery, licensing and support contacts.

Do not assume a VM image alone captures databases, external files, identity providers or integration state. Do not recommend Kubernetes solely because a workload can be containerized. A VMware-compatible destination still needs a supported network/storage and migration design.

## Cost and recovery

Include overlapping environments during transition, software entitlements, persistent storage, protection and network transfer. Rehosting can preserve operating responsibility rather than remove it. Keep current certifications, service availability and commercial terms tied to authoritative sources; do not infer them from an old architecture diagram.

## Sources

- [Architecture Center](https://docs.oracle.com/solutions/)
- [WebLogic Server for OCI](https://docs.oracle.com/en/cloud/paas/weblogic-cloud/)
- [Oracle Cloud VMware Solution](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/ocvsoverview.htm)
