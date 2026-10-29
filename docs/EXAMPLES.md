# Example prompts

Use these after installing/enabling OCI Atlas. Replace context descriptions with your own. Prompts requesting resource changes can incur OCI charges; conceptual prompts don't need OCI access.

New to the plugin? Use [Getting started](GETTING-STARTED.md) to choose a path, or explore the [illustrated walkthroughs](WALKTHROUGHS.md) for complete design conversations.

## Understand and choose

> Use OCI Atlas to explain the difference between compartments, VCNs, subnets, and regions. Show which are resource-management boundaries and which affect network access.

> I have a small containerized API. Compare Container Instances, Compute, Functions, and OKE on OCI. Recommend a starting point based on simplicity, runtime constraints, and operating responsibility.

> Explain OCI Data Integration versus Data Flow versus Streaming. Map a daily batch transformation and a real-time event ingestion workload to the appropriate service.

> Compare OCI AI Data Platform workspaces and external catalogs with Data Integration tasks and Data Flow applications. Explain where IAM, platform object permissions and database grants apply.

> Explain on-demand model inference, dedicated Generative AI hosting, Generative AI Agents, and Data Science model deployments. Don't assume a particular model or region is available.

> Compare OCI Streaming with Streaming with Apache Kafka. Explain the resource models, Kafka-compatible interface, broker connectivity, and client authentication. Include Queue when competing workers need to claim tasks.

> Compare Autonomous Database, Base Database, Exadata, MySQL HeatWave, OCI Database with PostgreSQL, and NoSQL for our existing application. Identify the compatibility and operating responsibilities that decide the choice.

> Explain Oracle Integration versus Data Integration, and APEX workspaces versus OCI compartments. Separate product roles, SQL privileges, and OCI management access.

## Design without provisioning

> Use OCI Atlas to design a private application connected to Autonomous Database. Identify the caller identities, DNS, network paths, connection mode, and secret handling. Produce a design only.

> Plan a Function behind API Gateway. Explain client authentication separately from the gateway's permission to invoke the Function and the Function's access to Object Storage.

> Help me choose a managed OCI approach for RAG over documents already governed by our existing data platform. Explain what can be reused before suggesting new services.

> Plan a private OKE deployment with access to Object Storage. Separate the operator's Kubernetes access, registry image pulls and the application's OCI workload identity.

> Plan a repeatable predictive-model workflow using Data Science. Compare batch scoring with a model deployment and identify the artifact, runtime, networking and rollback requirements.

> Design a daily ingestion pipeline with replay and checkpoints. Choose between Data Integration, Data Flow and an existing AI Data Platform workspace before adding new infrastructure.

> Plan connectivity from an on-premises application to a private OCI database. Cover FastConnect or VPN, DRG forward/return routes, DNS forwarding, security controls, TLS, and SQL identity. Produce a design only.

> Plan GPU/HPC infrastructure for distributed training. Explain cluster networks versus compute clusters, RDMA versus VCN paths, and when Object Storage, NFS, Block Volume, or Lustre fits.

> Plan application backup, restore, and disaster recovery with explicit RPO/RTO. Separate backups, storage replication, database HA, and Full Stack DR orchestration. Do not perform recovery operations.

> Sequence a database migration and application cutover. Separate initial copy, change replication, writer coordination, rollback conditions, and source retention. Compare Database Migration, GoldenGate, and Data Guard by role.

> Compare Oracle AI Vector Search, Search with OpenSearch, and our existing platform knowledge sources for RAG. Include permission filters, embedding compatibility, and deletion propagation.

## Inspect using existing access

> Use OCI Atlas and my selected OCI CLI profile to list visible compartments. State which scope you checked and any visibility limitations. Make no resource changes.

> In my signed-in OCI Console, help me find the application's VCN and explain its subnets, routes, and security groups. Use the tenancy and region shown in that session.

## Execute a bounded task

> Using the profile, region, and compartment we selected, create a private Object Storage bucket with the name I provide. Preserve existing resources, verify its access setting, and report its identifiers.

> Help me deploy this application using its existing Resource Manager stack. Inspect the configuration and plan, identify unexpected replacements or deletions, and complete the requested deployment within that scope.

## Diagnose

> My application job times out connecting to Autonomous Database. Use OCI Atlas to identify the first checks from the job's network context. Distinguish DNS, routing, TLS and SQL authentication before recommending changes.

> My OKE workload is in ImagePullBackOff. Investigate the image reference, architecture, registry access and runtime network path before proposing cluster changes.

> A request returns NotAuthorizedOrNotFound. Help me distinguish the wrong region/resource from a policy problem, using the identity that actually made the call.

> A Data Integration task works in the designer but the scheduled application run fails. Inspect publication, runtime parameters, identity, network and output evidence before replaying it.

> An OCI alarm is firing but nobody received a notification. Explain which evidence distinguishes alarm evaluation, destination configuration, subscription status and actual delivery.
