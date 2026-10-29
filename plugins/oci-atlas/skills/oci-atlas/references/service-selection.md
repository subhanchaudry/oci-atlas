# OCI service-selection decisions

Reviewed: 2026-10-29 · Basis: documentation-based decision guidance; no workload benchmarking.

## Use the workload's constraint

Ask for missing inputs only when they change the choice: runtime/control needs, source data and compatibility, latency/throughput, network location, availability/recovery goals and operational ownership. Prefer the customer's existing suitable services before introducing new infrastructure. A product appearing in a reference architecture doesn't make it required for every workload.

## Application runtime

| Requirement that drives the choice | Starting point | Reason to choose another path |
| --- | --- | --- |
| OS control or a conventional persistent process | Compute | Customer wants less host administration and a managed runtime fits |
| Kubernetes API/ecosystem and orchestration | OKE | Small application needs no Kubernetes-specific capability |
| Bounded event/request code in supported runtime | Functions | Long-lived process or unsupported runtime/resource behavior |
| API policies and routing | API Gateway in front of a backend | Only traffic balancing is needed; inspect Load Balancer/NLB |

API Gateway and Container Registry are not substitutes for an application runtime. Keep their roles separate when composing a deployment.

## Data and database choice

| Constraint | Starting point | Distinction to preserve |
| --- | --- | --- |
| Managed Oracle SQL workload | Autonomous Database | Compare Base DB/Exadata when specific control/features require them |
| Existing MySQL/PostgreSQL application | Appropriate managed engine | Verify supported versions/features before promising compatibility |
| Connector-led batch movement and transformation | Data Integration | Saved design → task → published runtime → run |
| Custom Spark code | Data Flow | Application definition and execution run are separate |
| Continuous event transport | Streaming | Delivery and business processing are separate |
| Shared governed catalog/workspace and data workflows | AI Data Platform | OCI access, object permissions and source credentials remain separate |

Don't change the database engine or workload type to fix a DNS or IAM problem. Select storage by semantics: objects/artifacts → Object Storage; attached disk → Block Volume; shared file access → File Storage.

## AI choice

Generation/embedding → supported managed model inference. Governed retrieval/tool orchestration → suitable agent service or application. Predictive/custom ML development and repeatable batch → Data Science. Custom serving → inspect managed model deployment before operating a general GPU server. Choose dedicated Generative AI hosting for a concrete capability/capacity requirement, with current cost and regional constraints understood.

## Output a usable recommendation

State the recommended path, the deciding constraints, dependent services, and one or two material alternatives. Identify assumptions and current details to verify. Include a small resource/caller/data-flow map when it clarifies the design; avoid a long catalog of equally weighted options. Use the relevant focused guide for execution detail.

## Sources

- [OCI Well-Architected Framework](https://docs.oracle.com/en/solutions/oci-best-practices/)
- [Data Integration](https://docs.oracle.com/en-us/iaas/Content/data-integration/using/overview.htm)
- [Data Flow](https://docs.oracle.com/en-us/iaas/Content/data-flow/using/dfs_service_overview.htm)
- [Generative AI product layers](https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm)
- [Data Science](https://docs.oracle.com/en-us/iaas/Content/data-science/using/overview.htm)
