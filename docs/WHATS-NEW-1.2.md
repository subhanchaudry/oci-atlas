# What changed in OCI Atlas v1.2

**Prepared version: 1.2.0 · Research cutoff: November 17, 2026 · Publication pending**

v1.2 makes current OCI service choices easier to explain and operate from documented prerequisites. It contains **100 references, 63 service guides, and 19 recipes**, preserves existing guide paths and aliases, and keeps catalog schema version 1. The plugin remains knowledge-first: operations require the host's tools, authentication, and OCI permissions. No execution tools, MCP server, or runnable examples were added.

## Six new starting points

| Need | Guide |
| --- | --- |
| Relocate supported VMs with explicit compatibility and cutover ownership | [Cloud Migrations discovery, replication, and VM cutover](../plugins/oci-atlas/skills/oci-atlas/references/service-cloud-migrations.md) |
| Connect database clients and distinguish MCP authentication from SQL permissions | [Database Tools connections and MCP access](../plugins/oci-atlas/skills/oci-atlas/references/service-database-tools.md) |
| Diagnose databases, inspect privilege use, and manage jobs | [Database Management diagnostics, jobs, and privileges](../plugins/oci-atlas/skills/oci-atlas/references/service-database-management.md) |
| Analyze historical capacity and SQL trends with known collection/warehouse ownership | [Ops Insights capacity, SQL trends, and AWR collection](../plugins/oci-atlas/skills/oci-atlas/references/service-ops-insights.md) |
| Connect devices, digital twins, and scoped runtime integrations | [Internet of Things domains, digital twins, and flows](../plugins/oci-atlas/skills/oci-atlas/references/service-internet-of-things.md) |
| Choose transcription or speech generation with feature-specific regional/API support | [Speech transcription and realtime voice output](../plugins/oci-atlas/skills/oci-atlas/references/service-speech.md) |

## Improvements across all eight areas

| Area | Practical improvement and canonical guidance |
| --- | --- |
| Foundations and identity | [IAM policies and workload identities](../plugins/oci-atlas/skills/oci-atlas/references/service-iam-policies.md) separates authentication, delegated tokens, and OCI authorization; Identity Assurance requires Premium and supported provider access. [Access, tools, and onboarding](../plugins/oci-atlas/skills/oci-atlas/references/access-and-tools.md) clarifies Console and regional Cloud Shell context. |
| Networking | [VCN routing, network controls, and DNS](../plugins/oci-atlas/skills/oci-atlas/references/service-vcn-routing.md) and [Hybrid connectivity with FastConnect, VPN, DRG, and DNS](../plugins/oci-atlas/skills/oci-atlas/references/service-hybrid-connectivity.md) explain overlapping IPv4 networks and maintenance draining without losing DNS or return-path dependencies. [Network Firewall inspection paths and policies](../plugins/oci-atlas/skills/oci-atlas/references/service-network-firewall.md) adds capture boundaries. |
| Compute and storage | [Compute instances and persistent disks](../plugins/oci-atlas/skills/oci-atlas/references/service-compute.md) ties documented Ax shapes to architecture, images, and attachment behavior. [GPU and HPC capacity, cluster networking, and storage](../plugins/oci-atlas/skills/oci-atlas/references/service-gpu-hpc.md) connects health checks to workload recovery. |
| Databases and data | [Autonomous AI Database operations and access](../plugins/oci-atlas/skills/oci-atlas/references/service-autonomous-database.md) distinguishes built-in A2A/MCP tools and Iceberg access from Database Tools. [GoldenGate deployments, connections, and change replication](../plugins/oci-atlas/skills/oci-atlas/references/service-goldengate.md), [MySQL HeatWave systems, access, and availability](../plugins/oci-atlas/skills/oci-atlas/references/service-mysql-heatwave.md), and [OCI Database with PostgreSQL systems and private access](../plugins/oci-atlas/skills/oci-atlas/references/service-postgresql.md) clarify connectors and upgrade choices. |
| AI and ML | [Generative AI model and agent selection](../plugins/oci-atlas/skills/oci-atlas/references/service-generative-ai.md) covers sandbox lifecycle, hosted authentication/persistence, and compaction. [AI Data Platform catalogs, agents, and compute](../plugins/oci-atlas/skills/oci-atlas/references/service-ai-data-platform.md) separates deployed agents, workflow tasks, memory, and compute from preview dependencies. [Data Science notebooks, jobs, and model serving](../plugins/oci-atlas/skills/oci-atlas/references/service-data-science.md) adds artifact verification and compute-target considerations. |
| Application platforms | [OKE clusters, workloads, and identities](../plugins/oci-atlas/skills/oci-atlas/references/service-oke.md) updates version lifecycle, GPU repair, and storage. [Container Registry and artifact delivery](../plugins/oci-atlas/skills/oci-atlas/references/service-container-registry.md) distinguishes same-realm, pull-only caches from writable repositories. |
| Operations and security | [Data Safe targets, assessments, auditing, and masking](../plugins/oci-atlas/skills/oci-atlas/references/service-data-safe.md) adds cryptographic assessment. Database diagnostics and historical analysis have dedicated guides; [Operations, security, and cost](../plugins/oci-atlas/skills/oci-atlas/references/operations-security.md) connects those choices to evidence and recovery. |
| Infrastructure and architecture | [Choose an enterprise application modernization path](../plugins/oci-atlas/skills/oci-atlas/references/enterprise-modernization.md), [Recipe: database migration, replication, and application cutover](../plugins/oci-atlas/skills/oci-atlas/references/recipe-database-migration.md), and [Recipe: application backup, restore, and disaster recovery](../plugins/oci-atlas/skills/oci-atlas/references/recipe-backup-disaster-recovery.md) preserve the boundaries between VM relocation, database migration, replication, and recovery. |

## Clearer installation and availability

The [README](../README.md), [installation guide](INSTALL.md), packaged onboarding, and [example prompts](EXAMPLES.md) now describe audience, coverage, and actual host requirements consistently. Local checkout installation works for prepublication review; pinned v1.2 links apply only after publication. Documenting an OCI MCP service does not make Atlas an MCP server.

Only documented, generally available capabilities enter recommended guidance. The dated [evidence register](RELEASE-EVIDENCE-1.2.md) records restrictions and excluded announcements, including future TPUs/Cerebras, preview/limited AI features, and unresolved native Snowflake, AI Security Mesh, ontology/reasoning, and hardware deployment details. A GA service still requires region, entitlement, configuration, and capacity checks for a specific workload.

See the [validation record](VALIDATION-1.2.md) for documentation/package checks and explicit live-testing limits, or browse the [full catalog](CONTENT.md).
