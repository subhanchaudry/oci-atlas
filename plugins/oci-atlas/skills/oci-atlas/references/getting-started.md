# Start with OCI Atlas

Reviewed: 2026-11-03

OCI Atlas adds focused Oracle Cloud knowledge to ChatGPT and Codex. Start with the [installation guide](https://github.com/subhanchaudry/oci-atlas/blob/v1.1.0/docs/INSTALL.md), enable the plugin, and open a fresh conversation. Choose the path closest to your goal below.

Knowledge questions and architecture discussions require no OCI login. Inspecting or changing resources uses your available tools, authenticated identity, and OCI permissions. A plugin installation does not connect a tenancy.

## Understand OCI

Use this path to learn how services and resource boundaries fit together.

**First prompt**

> Use OCI Atlas to explain tenancies, compartments, regions, VCNs, and IAM policies. Show how they relate using a small example. Use packaged guidance only; do not inspect profiles or connect to OCI.

**Helpful context:** your familiarity with cloud platforms and the concepts you want explained. You do not need to supply tenancy identifiers.

**What to expect:** a concise explanation, an example, and relevant next topics. Compartments organize resources and access; they do not create network isolation.

Continue with [tenancy foundations](foundations.md) or the [workload selection](workload-selection.md).

## Choose an architecture

Use this path when you know what the application needs to do but want help choosing OCI services.

**First prompt**

> Use OCI Atlas to design a small containerized API that stores application data in an Oracle database. Compare the suitable runtimes, explain your recommended starting point and its dependencies, and identify the requirements that could change the choice. Produce a design only.

**Helpful context:** application/runtime requirements, existing services, users and traffic, data location, availability needs, operating skills, and budget constraints. Share the inputs you know; the assistant should ask only for missing details that affect the design.

**What to expect:** a recommended path with reasons, a small architecture map, ownership and access boundaries, and a practical next step. Any unconfirmed requirements should be explicit assumptions.

Continue with [service selection](service-selection.md) and the [illustrated walkthroughs](walkthroughs.md).

## Inspect existing resources

Use this path when you want an explanation grounded in your actual tenancy.

**First prompt**

> Use OCI Atlas and my selected OCI CLI profile to list the compartments visible to me. Explain their hierarchy and the scope you inspected. Make no resource changes, and distinguish configured context from access you actually confirmed.

**Helpful context:** the intended CLI profile or signed-in Console session, region, and relevant compartment or resource. Provide only the metadata needed to identify the target. Keep passwords, tokens, private keys, wallets, and complete configuration files out of chat.

**What to expect:** a bounded read, observed identifiers and relationships, and clear visibility limitations. A configured profile is not proof of successful access; a list from one identity is not necessarily a complete tenancy inventory. A slow optional access check should end promptly, leaving the unverified scope clear.

Continue with [access and tools](access-and-tools.md). Use a later, explicit resource task when you want changes made.

## Troubleshoot an OCI issue

Use this path to narrow down a failure before changing infrastructure.

**First prompt**

> Use OCI Atlas to reason through a hypothetical application timeout connecting to private Autonomous Database. Separate DNS, forward/return routing, network controls, TLS, and SQL authentication. Explain which observation would distinguish the next likely causes. Do not connect to OCI.

**Helpful context for a real issue:** sanitized error, failing operation, time and time zone, actual caller/runtime, affected resource, and recent changes. An application pod, laptop, and managed job can have different network paths and identities.

**What to expect:** observed evidence separated from hypotheses, the next useful check, and a correction tied to evidence. A timeout alone should not lead to public exposure or broad policy grants.

Continue with [connectivity diagnosis](troubleshoot-connectivity.md), [access diagnosis](troubleshoot-access.md), or [workload diagnosis](troubleshoot-workloads.md).

## Keep the conversation useful

State whether you want an explanation, a design, inspection, or an operational change. You can change that goal as the conversation develops. For resource work, identify the intended scope; the assistant should carry forward clear authorization and clarify ambiguous targets or expanded consequences.

Use the [workload selection](workload-selection.md) for more tasks. If installation or guidance needs correction, see [support handoff](troubleshoot-support-handoff.md).

## Carry out a scoped task

State the target and intended result, for example: “Deploy the container API example into this existing private subnet using this database and secret.” The assistant should inspect dependencies and configuration ownership, prepare the relevant changes, execute within your authorization and check the application outcome. A planning request remains a design. If your host lacks an execution route, use the guide to prepare a concrete handoff.

## Sources

- [OCI CLI](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm)
- [Architecture Center](https://docs.oracle.com/solutions/)
