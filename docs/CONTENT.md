# OCI Atlas content catalog

Generated from the [catalog](../plugins/oci-atlas/skills/oci-atlas/catalog.json). Edit catalog metadata and guide bodies, then run `python3 tools/catalog.py --write`.

The entry skill routes directly to these references; the agent need not load this entire index.

## Access

| Guide | Search terms | Reviewed |
| --- | --- | --- |
| [Access, tools, and onboarding](../plugins/oci-atlas/skills/oci-atlas/references/access-and-tools.md) | CLI, Console, Cloud Shell, authentication | 2026-10-29 |

## Decision

| Guide | Search terms | Reviewed |
| --- | --- | --- |
| [OCI service-selection decisions](../plugins/oci-atlas/skills/oci-atlas/references/service-selection.md) | service selection, decision table, alternatives | 2026-10-29 |

## Domain

| Guide | Search terms | Reviewed |
| --- | --- | --- |
| [Tenancy foundations and IAM](../plugins/oci-atlas/skills/oci-atlas/references/foundations.md) | tenancy, compartments, OCIDs, regions, quotas | 2026-10-29 |
| [Networking and private access](../plugins/oci-atlas/skills/oci-atlas/references/networking.md) | networking, DNS, load balancer, FastConnect, VPN | 2026-10-29 |
| [Compute and storage](../plugins/oci-atlas/skills/oci-atlas/references/compute-storage.md) | compute, block volumes, backups, File Storage | 2026-10-29 |
| [Databases and data services](../plugins/oci-atlas/skills/oci-atlas/references/databases-data.md) | databases, Autonomous Database, data platforms | 2026-10-29 |
| [AI, agents, and machine learning](../plugins/oci-atlas/skills/oci-atlas/references/ai-ml.md) | AI, ML, agents, inference | 2026-10-29 |
| [Application platforms](../plugins/oci-atlas/skills/oci-atlas/references/applications.md) | applications, OCIR, DevOps, containers | 2026-10-29 |
| [Operations, security, and cost](../plugins/oci-atlas/skills/oci-atlas/references/operations-security.md) | Monitoring, Logging, Audit, Cloud Guard, budgets | 2026-10-29 |
| [Infrastructure as code and architecture](../plugins/oci-atlas/skills/oci-atlas/references/infrastructure-architecture.md) | Terraform, Resource Manager, landing zones | 2026-10-29 |

## Service

| Guide | Search terms | Reviewed |
| --- | --- | --- |
| [IAM policies and workload identities](../plugins/oci-atlas/skills/oci-atlas/references/service-iam-policies.md) | IAM, policies, dynamic groups, resource principals | 2026-10-29 |
| [VCN routing, network controls, and DNS](../plugins/oci-atlas/skills/oci-atlas/references/service-vcn-routing.md) | VCN, routing, NSG, DRG, private DNS | 2026-10-29 |
| [Compute instances and persistent disks](../plugins/oci-atlas/skills/oci-atlas/references/service-compute.md) | Compute, VM, shape, image, instance | 2026-10-29 |
| [Object Storage buckets, objects, and retention](../plugins/oci-atlas/skills/oci-atlas/references/service-object-storage.md) | Object Storage, bucket, versioning, retention | 2026-10-29 |
| [Autonomous Database operations and access](../plugins/oci-atlas/skills/oci-atlas/references/service-autonomous-database.md) | Autonomous Database, ADB, ATP, ADW, wallet, TLS | 2026-10-29 |
| [OKE clusters, workloads, and identities](../plugins/oci-atlas/skills/oci-atlas/references/service-oke.md) | OKE, Kubernetes, node pool, workload identity | 2026-10-29 |
| [Functions deployment and invocation](../plugins/oci-atlas/skills/oci-atlas/references/service-functions.md) | Functions, serverless, Fn Project | 2026-10-29 |
| [API Gateway deployments and backend access](../plugins/oci-atlas/skills/oci-atlas/references/service-api-gateway.md) | API Gateway, routes, JWT, API deployment | 2026-10-29 |
| [Generative AI model and agent selection](../plugins/oci-atlas/skills/oci-atlas/references/service-generative-ai.md) | Generative AI, LLM, agents, embeddings | 2026-10-29 |
| [Data Science notebooks, jobs, and model serving](../plugins/oci-atlas/skills/oci-atlas/references/service-data-science.md) | Data Science, notebook, training, model deployment | 2026-10-29 |
| [AI Data Platform workspaces and catalogs](../plugins/oci-atlas/skills/oci-atlas/references/service-ai-data-platform.md) | AI Data Platform, AIDP, Workbench, external catalogs | 2026-10-29 |
| [Data Integration design and runtime artifacts](../plugins/oci-atlas/skills/oci-atlas/references/service-data-integration.md) | Data Integration, ETL, ELT, published task | 2026-10-29 |
| [Data Flow Spark applications and runs](../plugins/oci-atlas/skills/oci-atlas/references/service-data-flow.md) | Data Flow, Spark, application, run | 2026-10-29 |
| [Streaming producers, consumers, and replay](../plugins/oci-atlas/skills/oci-atlas/references/service-streaming.md) | Streaming, Kafka, partitions, consumer groups | 2026-10-29 |
| [Secret Management and encryption keys](../plugins/oci-atlas/skills/oci-atlas/references/service-secrets-keys.md) | Vault, Secret Management, KMS, rotation | 2026-10-29 |

## Troubleshooting

| Guide | Search terms | Reviewed |
| --- | --- | --- |
| [Diagnose authentication, authorization, and limits](../plugins/oci-atlas/skills/oci-atlas/references/troubleshoot-access.md) | NotAuthenticated, NotAuthorizedOrNotFound, limits, quota | 2026-10-29 |
| [Diagnose private and application connectivity](../plugins/oci-atlas/skills/oci-atlas/references/troubleshoot-connectivity.md) | DNS, timeout, connectivity, TLS, private endpoint | 2026-10-29 |
| [Diagnose workloads, runs, and serving failures](../plugins/oci-atlas/skills/oci-atlas/references/troubleshoot-workloads.md) | ImagePullBackOff, CrashLoopBackOff, failed run, work request | 2026-10-29 |

## Recipe

| Guide | Search terms | Reviewed |
| --- | --- | --- |
| [Recipe: private application deployment](../plugins/oci-atlas/skills/oci-atlas/references/recipe-private-application.md) | private application, load balancer, deployment | 2026-10-29 |
| [Recipe: connect an application to Autonomous Database](../plugins/oci-atlas/skills/oci-atlas/references/recipe-database-connectivity.md) | database connectivity, private ADB, SQL | 2026-10-29 |
| [Recipe: Function behind API Gateway](../plugins/oci-atlas/skills/oci-atlas/references/recipe-serverless-api.md) | serverless API, Functions, API Gateway | 2026-10-29 |
| [Recipe: choose and deploy an AI application](../plugins/oci-atlas/skills/oci-atlas/references/recipe-ai-application.md) | AI application, deployment choice, inference | 2026-10-29 |
| [Recipe: private OKE application with workload access](../plugins/oci-atlas/skills/oci-atlas/references/recipe-private-oke.md) | private OKE, private cluster, workload identity | 2026-10-29 |
| [Recipe: governed source-to-target data ingestion](../plugins/oci-atlas/skills/oci-atlas/references/recipe-data-ingestion.md) | ingestion, pipeline, checkpoint, replay | 2026-10-29 |
| [Recipe: retrieval over governed enterprise data](../plugins/oci-atlas/skills/oci-atlas/references/recipe-rag-application.md) | RAG, retrieval, citations, document permissions | 2026-10-29 |
| [Recipe: train, register, and serve a predictive model](../plugins/oci-atlas/skills/oci-atlas/references/recipe-model-lifecycle.md) | model lifecycle, MLOps, batch scoring, serving | 2026-10-29 |
