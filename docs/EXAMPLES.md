# Example prompts

Use these after installing/enabling OCI Atlas. Replace context descriptions with your own. Prompts requesting resource changes can incur OCI charges; conceptual prompts don't need OCI access.

## Understand and choose

> Use OCI Atlas to explain the difference between compartments, VCNs, subnets, and regions. Show which are resource-management boundaries and which affect network access.

> I have a small containerized API. Compare Compute, Functions, and OKE on OCI. Recommend a starting point based on simplicity, runtime constraints, and operating responsibility.

> Explain OCI Data Integration versus Data Flow versus Streaming. Map a daily batch transformation and a real-time event ingestion workload to the appropriate service.

> Explain on-demand model inference, dedicated Generative AI hosting, Generative AI Agents, and Data Science model deployments. Don't assume a particular model or region is available.

## Design without provisioning

> Use OCI Atlas to design a private application connected to Autonomous Database. Identify the caller identities, DNS, network paths, connection mode, and secret handling. Produce a design only.

> Plan a Function behind API Gateway. Explain client authentication separately from the gateway's permission to invoke the Function and the Function's access to Object Storage.

> Help me choose a managed OCI approach for RAG over documents already governed by our existing data platform. Explain what can be reused before suggesting new services.

## Inspect using existing access

> Use OCI Atlas and my selected OCI CLI profile to list visible compartments. State which scope you checked and any visibility limitations. Make no resource changes.

> In my signed-in OCI Console, help me find the application's VCN and explain its subnets, routes, and security groups. Use the tenancy and region shown in that session.

## Execute a bounded task

> Using the profile, region, and compartment we selected, create a private Object Storage bucket with the name I provide. Preserve existing resources, verify its access setting, and report its identifiers.

> Help me deploy this application using its existing Resource Manager stack. Inspect the configuration and plan, identify unexpected replacements or deletions, and complete the requested deployment within that scope.

## Diagnose

> My application job times out connecting to Autonomous Database. Use OCI Atlas to identify the first checks from the job's network context. Distinguish DNS, routing, TLS and SQL authentication before recommending changes.

> My OKE workload is in ImagePullBackOff. Investigate the image reference, architecture, registry access and runtime network path before proposing cluster changes.

> An OCI alarm exists but nobody received a notification. Explain which evidence distinguishes alarm evaluation, destination configuration, subscription status and actual delivery.
