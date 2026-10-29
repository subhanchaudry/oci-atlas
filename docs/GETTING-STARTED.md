# Start with OCI Atlas

OCI Atlas adds focused Oracle Cloud knowledge to ChatGPT and Codex. Start with the [installation guide](INSTALL.md), enable the plugin, and open a fresh conversation. Choose the path closest to your goal below.

Knowledge questions and architecture discussions require no OCI login. Inspecting or changing resources uses your available tools, authenticated identity, and OCI permissions. A plugin installation does not connect a tenancy.

## Understand OCI

Use this path to learn how services and resource boundaries fit together.

**First prompt**

> Use OCI Atlas to explain tenancies, compartments, regions, VCNs, and IAM policies. Show how they relate using a small example. Use packaged guidance only; do not inspect profiles or connect to OCI.

**Helpful context:** your familiarity with cloud platforms and the concepts you want explained. You do not need to supply tenancy identifiers.

**What to expect:** a concise explanation, an example, and relevant next topics. Compartments organize resources and access; they do not create network isolation.

Continue with [tenancy foundations](../plugins/oci-atlas/skills/oci-atlas/references/foundations.md) or the [content catalog](CONTENT.md).

## Choose an architecture

Use this path when you know what the application needs to do but want help choosing OCI services.

**First prompt**

> Use OCI Atlas to design a small containerized API that stores application data in an Oracle database. Compare the suitable runtimes, explain your recommended starting point and its dependencies, and identify the requirements that could change the choice. Produce a design only.

**Helpful context:** application/runtime requirements, existing services, users and traffic, data location, availability needs, operating skills, and budget constraints. Share the inputs you know; the assistant should ask only for missing details that affect the design.

**What to expect:** a recommended path with reasons, a small architecture map, ownership and access boundaries, and a practical next step. Any unconfirmed requirements should be explicit assumptions.

Continue with [service selection](../plugins/oci-atlas/skills/oci-atlas/references/service-selection.md) and the [three illustrated walkthroughs](WALKTHROUGHS.md).

## Inspect existing resources

Use this path when you want an explanation grounded in your actual tenancy.

**First prompt**

> Use OCI Atlas and my selected OCI CLI profile to list the compartments visible to me. Explain their hierarchy and the scope you inspected. Make no resource changes, and distinguish configured context from access you actually confirmed.

**Helpful context:** the intended CLI profile or signed-in Console session, region, and relevant compartment or resource. Provide only the metadata needed to identify the target. Keep passwords, tokens, private keys, wallets, and complete configuration files out of chat.

**What to expect:** a bounded read, observed identifiers and relationships, and clear visibility limitations. A configured profile is not proof of successful access; a list from one identity is not necessarily a complete tenancy inventory. A slow optional access check should end promptly, leaving the unverified scope clear.

Continue with [access and tools](../plugins/oci-atlas/skills/oci-atlas/references/access-and-tools.md). Use a later, explicit resource task when you want changes made.

## Troubleshoot an OCI issue

Use this path to narrow down a failure before changing infrastructure.

**First prompt**

> Use OCI Atlas to reason through a hypothetical application timeout connecting to private Autonomous Database. Separate DNS, forward/return routing, network controls, TLS, and SQL authentication. Explain which observation would distinguish the next likely causes. Do not connect to OCI.

**Helpful context for a real issue:** sanitized error, failing operation, time and time zone, actual caller/runtime, affected resource, and recent changes. An application pod, laptop, and managed job can have different network paths and identities.

**What to expect:** observed evidence separated from hypotheses, the next useful check, and a correction tied to evidence. A timeout alone should not lead to public exposure or broad policy grants.

Continue with [connectivity diagnosis](../plugins/oci-atlas/skills/oci-atlas/references/troubleshoot-connectivity.md), [access diagnosis](../plugins/oci-atlas/skills/oci-atlas/references/troubleshoot-access.md), or [workload diagnosis](../plugins/oci-atlas/skills/oci-atlas/references/troubleshoot-workloads.md).

## Keep the conversation useful

State whether you want an explanation, a design, inspection, or an operational change. You can change that goal as the conversation develops. For resource work, identify the intended scope; the assistant should carry forward clear authorization and clarify ambiguous targets or expanded consequences.

Use the [example prompts](EXAMPLES.md) for more tasks. If installation or guidance needs correction, see [support](../SUPPORT.md).
