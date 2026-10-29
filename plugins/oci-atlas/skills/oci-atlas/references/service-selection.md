# OCI service-selection decisions

Reviewed: 2026-10-29 · Basis: documentation-based decision guidance; no workload benchmarking.

## Use the workload's constraint

Ask for missing inputs only when they change the choice: runtime/control needs, source data and compatibility, latency/throughput, network location, availability/recovery goals and operational ownership. Prefer the customer's existing suitable services before introducing new infrastructure. A product appearing in a reference architecture doesn't make it required for every workload.

## Application runtime

| Requirement that drives the choice | Starting point | Reason to choose another path |
| --- | --- | --- |
| OS control or a conventional persistent process | Compute | Customer wants less host administration and a managed runtime fits |
| Kubernetes API/ecosystem and orchestration | OKE | Small application needs no Kubernetes-specific capability |
| Run containers without Kubernetes administration | [Container Instances](service-container-instances.md) | Need orchestration, cluster APIs, or a function invocation model |
| Bounded event/request code in supported runtime | Functions | Long-lived process or unsupported runtime/resource behavior |
| API policies and routing | API Gateway in front of a backend | Only traffic balancing is needed; inspect Load Balancer/NLB |

API Gateway and Container Registry are not substitutes for an application runtime. Keep their roles separate when composing a deployment.

[APEX](service-apex-ords.md) fits database-centric low-code applications; its workspace/schema model differs from OCI compartments. [Oracle Integration](service-oracle-integration.md) connects applications and business processes through integrations/adapters. [Data Integration](service-data-integration.md) focuses on data movement/transformation tasks. Select by the application's transaction and data semantics rather than the shared word “integration.”

## Data and database choice

| Constraint | Starting point | Distinction to preserve |
| --- | --- | --- |
| Managed Oracle SQL workload | Autonomous Database | Compare Base DB/Exadata when specific control/features require them |
| Oracle database with more host/database operational control | [Base Database](service-base-database.md) | Understand customer patching, database operations, and HA responsibilities |
| Exadata capabilities or deployment constraints | [Exadata](service-exadata.md) | Compare dedicated infrastructure, Exascale, and Cloud@Customer responsibilities |
| Existing MySQL application or HeatWave analytics | [MySQL HeatWave](service-mysql-heatwave.md) | Check engine compatibility, HA, and optional HeatWave requirements |
| PostgreSQL application | [OCI Database with PostgreSQL](service-postgresql.md) | Check extensions, versions, privileges, and private connectivity |
| Key-oriented application with predictable table access | [NoSQL Database](service-nosql.md) | Relational joins/transactions or an existing SQL application may decide otherwise |
| Low-latency shared cached state | [OCI Cache](service-oci-cache.md) | Establish a durable source of truth and engine/client behavior |
| Connector-led batch movement and transformation | Data Integration | Saved design → task → published runtime → run |
| Custom Spark code | Data Flow | Application definition and execution run are separate |
| Continuous event transport | Streaming | Delivery and business processing are separate |
| Shared governed catalog/workspace and data workflows | AI Data Platform | OCI access, object permissions and source credentials remain separate |
| Governed dashboards and semantic models | [Analytics Cloud](service-analytics-cloud.md) | Application roles and source-data permissions need their own design |

Don't change the database engine or workload type to fix a DNS or IAM problem. Select storage by semantics: objects/artifacts → Object Storage; attached disk → Block Volume; shared file access → File Storage.

OCI resource administration and SQL/data privileges are separate for every database choice. [Data Safe](service-data-safe.md) adds supported security assessment, audit, and masking capabilities; it does not replace database administration. For an engine move, use [Database Migration](service-database-migration.md) and the [migration recipe](recipe-database-migration.md); for supported ongoing change replication, inspect [GoldenGate](service-goldengate.md). A replicated error can reach the target: replication and HA are not substitutes for independently retained recovery points.

## Messaging and event transport

| Need | Starting point | Operational distinction |
| --- | --- | --- |
| Competing workers claiming tasks | [Queue](service-queue.md) | Visibility, retries, acknowledgement, and dead-letter handling |
| Partitioned event log with independent consumers | [Streaming](service-streaming.md) | Offsets, retention, partitioning, and service-specific API constraints |
| Managed Apache Kafka platform | [Streaming with Apache Kafka](service-streaming-kafka.md) | Kafka clusters, brokers, topics, client security, and compatibility requirements |

Streaming's Kafka-compatible interface does not make it the managed Apache Kafka service. Check the exact API/feature requirements and client network/authentication path. Do not promise arbitrary Kafka ecosystem compatibility or exactly-once business effects from a protocol label.

## AI choice

Generation/embedding → supported managed model inference. Governed retrieval/tool orchestration → suitable agent service or application. Predictive/custom ML development and repeatable batch → Data Science. Custom serving → inspect managed model deployment before operating a general GPU server. Choose dedicated Generative AI hosting for a concrete capability/capacity requirement, with current cost and regional constraints understood.

For retrieval, compare [Oracle AI Vector Search](service-ai-vector-search.md) when relational data, SQL filters, and database governance already fit; [Search with OpenSearch](service-opensearch.md) when a search/index lifecycle is the desired platform; and existing [AI Data Platform](service-ai-data-platform.md) or managed agent knowledge sources. Verify supported integrations and permission filtering. Embedding generation and retrieval storage are separate choices. For specialized training/inference infrastructure, use [GPU/HPC](service-gpu-hpc.md) and compare [File Storage](service-file-storage.md) with [Lustre](service-lustre.md) by client semantics and access pattern.

## Output a usable recommendation

State the recommended path, the deciding constraints, dependent services, and one or two material alternatives. Identify assumptions and current details to verify. Include a small resource/caller/data-flow map when it clarifies the design; avoid a long catalog of equally weighted options. Use the relevant focused guide for execution detail.

An adaptable architecture response:

1. **Recommendation:** the starting design and the workload it serves.
2. **Deciding constraints:** requirements that support it and missing inputs that could change the choice. Treat demo/production intent as unknown unless established.
3. **Dependencies and boundaries:** runtime, network/data flow, identities, data permissions, and existing services to reuse.
4. **Responsibilities:** what OCI manages and what the customer operates, including application lifecycle and recovery where relevant.
5. **Next step:** one practical decision or requested action. Identify volatile details to confirm before deployment.

For example: “Start with Container Instances for a conventional API container if Kubernetes is unnecessary. Confirm the availability target before deciding capacity and placement. You still own the image, application configuration, release/replacement process, and frontend design.” This is a conditional recommendation, not a universal default for every API. Keep smaller comparisons brief.

## Sources

- [OCI Well-Architected Framework](https://docs.oracle.com/en/solutions/oci-best-practices/)
- [Data Integration](https://docs.oracle.com/en-us/iaas/Content/data-integration/using/overview.htm)
- [Data Flow](https://docs.oracle.com/en-us/iaas/Content/data-flow/using/dfs_service_overview.htm)
- [Generative AI product layers](https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm)
- [Data Science](https://docs.oracle.com/en-us/iaas/Content/data-science/using/overview.htm)
- [OCI service catalog](https://docs.oracle.com/en-us/iaas/Content/home.htm)
- [Container Instances](https://docs.oracle.com/en-us/iaas/Content/container-instances/overview-of-container-instances.htm)
- [Streaming with Apache Kafka](https://docs.oracle.com/en-us/iaas/Content/kafka/concepts.htm)
- [Queue](https://docs.oracle.com/en-us/iaas/Content/queue/overview.htm)
