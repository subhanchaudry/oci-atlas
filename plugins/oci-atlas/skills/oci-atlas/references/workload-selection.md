# Choose an OCI workload path

Reviewed: 2026-11-17

## Start with the outcome

Identify what the customer wants to accomplish and whether the request is explanation, design, inspection or an operational change. Ask only for missing inputs that affect the path: existing resources, runtime/data compatibility, client location, availability/recovery, operating skills and budget constraints. Reuse suitable foundations.

| Customer request | Start here | Deciding inputs and alternatives |
| --- | --- | --- |
| Host my API | [Private application](recipe-private-application.md) | Container Instances for a conventional container; Compute for OS control; OKE for Kubernetes requirements |
| Connect my private database | [Database connectivity](recipe-database-connectivity.md) | Actual runtime, private DNS, TLS mode and SQL identity |
| Expose a bounded handler | [Serverless API](recipe-serverless-api.md) | Payload, client authentication, duration and downstream access |
| Process uploaded files | [Event processing](recipe-event-processing.md) | Object versions, processing duration, idempotency and replay |
| Run private Kubernetes workloads | [Private OKE](recipe-private-oke.md) | Cluster/network ownership, pod identity, ingress and persistent data |
| Search company documents | [RAG](recipe-rag-application.md) | Source permissions, freshness, citations; compare managed agents and custom retrieval |
| Add an AI feature | [AI application](recipe-ai-application.md) | Inference versus agents versus predictive ML; data/tool boundaries |
| Train and serve a predictive model | [Model lifecycle](recipe-model-lifecycle.md) | Dataset, evaluation, batch/online contract and release owner |
| Move and transform data | [Data ingestion](recipe-data-ingestion.md) | Connector ETL, Spark or existing workspace; incremental and replay semantics |
| Build analytics on governed data | [Lakehouse and analytics](recipe-lakehouse-analytics.md) | Source freshness, table grain, catalog and consumption roles |
| Query a private source in AIDP | [AIDP private source](recipe-aidp-private-source.md) | Workspace runtime network, external catalog support and source privileges |
| Extend a Fusion workflow | [SaaS extension](recipe-saas-extension.md) | Supported business API, identity, orchestration and reconciliation |
| Move an existing application | [Enterprise modernization](enterprise-modernization.md) | Product support, licensing, middleware, database and operating model |
| Connect another cloud or data center | [Multicloud application](recipe-multicloud-application.md), [hybrid access](recipe-hybrid-private-access.md) | Deployment product, region pair, route/DNS owners and latency |
| Migrate a database | [Database migration](recipe-database-migration.md) | Compatibility, change rate, writer cutover and rollback boundary |
| Recover an application | [Backup and DR](recipe-backup-disaster-recovery.md) | Failure scenario, RPO/RTO, data point and writer ownership |
| Run HPC or GPU jobs | [HPC workload](recipe-hpc-workload.md) | Software/fabric, capacity, data staging, scheduler and checkpoints |
| Operate the workload | [Observability delivery](recipe-observability-delivery.md) | Application signal, logs/traces, recipient and recovery owner |

## Produce a usable design

Return the recommended path, existing services to reuse, architecture/data flow, identities, assumptions and the next useful action. Add cost drivers and recovery choices where they influence the decision. Use [service selection](service-selection.md) for a focused comparison and [landing zones](service-landing-zones.md) for missing foundations.

Oracle Architecture Center reference architectures describe patterns; solution playbooks describe implementation paths; Built & Deployed stories describe particular customer systems. Do not transfer a story's performance or topology to another customer. Verify current product behavior against its owning documentation. Select the relevant pattern instead of loading the whole library.

Two versioned source examples are available: [private container API](https://github.com/subhanchaudry/oci-atlas/tree/v1.2.0/examples/container-api) and [RAG over documents](https://github.com/subhanchaudry/oci-atlas/tree/v1.2.0/examples/rag). They consume existing foundations and expose their required inputs.

## More workload entry points

- **Move VMware or AWS instances:** [Cloud Migrations](service-cloud-migrations.md), then application cutover and infrastructure ownership.
- **Connect an AI client to database tools:** [Database Tools](service-database-tools.md), then identity, SQL privileges and private connectivity.
- **Investigate a database fleet:** [Database Management](service-database-management.md) for operations; [Ops Insights](service-ops-insights.md) for trends.
- **Collect device telemetry:** [IoT](service-internet-of-things.md), then downstream event-processing and retention decisions.
- **Transcribe or speak:** [Speech](service-speech.md), then any authorized retrieval or application workflow.

## Sources

- [Architecture Center](https://docs.oracle.com/solutions/)
- [Well-Architected Framework](https://docs.oracle.com/en/solutions/oci-best-practices/)
- [Cloud Migrations resource model and workflow](https://docs.oracle.com/en-us/iaas/Content/cloud-migration/cloud-migration-overview.htm)
- [Supported AWS Arm migrations](https://docs.oracle.com/en-us/iaas/releasenotes/cloud-migration/ocm_aws_arm_migration.htm)
- [Database Tools overview](https://docs.oracle.com/en-us/iaas/database-tools/doc/overview.html)
- [Database Tools MCP server support and authentication](https://docs.oracle.com/en-us/iaas/database-tools/doc/overview-mcp-server.html)
- [CIMD client access](https://docs.oracle.com/en-us/iaas/releasenotes/database-tools/cimd.htm)
- [MCP service logs](https://docs.oracle.com/en-us/iaas/releasenotes/database-tools/logging.htm)
- [Diagnostics and Management target support](https://docs.oracle.com/en-us/iaas/database-management/doc/database-management-oracle-databases.html)
- [Unified onboarding](https://docs.oracle.com/en-us/iaas/releasenotes/operations-insights/unified-onboarding-dbm-opsi.htm)
- [Privilege analysis](https://docs.oracle.com/en-us/iaas/releasenotes/database-management/privilege-analysis.htm)
- [Database Management releases](https://docs.oracle.com/en-us/iaas/releasenotes/services/database-management/)
- [Ops Insights scope, retention and service-change notice](https://docs.oracle.com/en-us/iaas/operations-insights/doc/operations-insights.html)
- [AWR collection and customer-owned warehouse](https://docs.oracle.com/en-us/iaas/releasenotes/operations-insights/awr-snapshot-collection-bring-your-own-warehouse.htm)
- [SQL Monitoring reports](https://docs.oracle.com/en-us/iaas/releasenotes/operations-insights/sql-monitoring-reports.htm)
- [IoT resources, endpoints and limits](https://docs.oracle.com/en-us/iaas/Content/internet-of-things/overview.htm)
- [Flow Runtime integrations and privilege delegation](https://docs.oracle.com/en-us/iaas/releasenotes/internet-of-things/update-11102026.htm)
- [Development and Production domain groups](https://docs.oracle.com/en-us/iaas/releasenotes/internet-of-things/update-04142026.htm)
- [Speech capabilities, regional restrictions and jobs](https://docs.oracle.com/en-us/iaas/Content/speech/using/speech.htm)
- [Realtime TTS API availability](https://docs.oracle.com/en-us/iaas/releasenotes/speech/realtime-tts.htm)
