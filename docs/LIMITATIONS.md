# Host requirements and scope

OCI Atlas supplies sourced OCI knowledge, service selection and reusable workflows. Version 1.2 includes 100 references, 63 service guides and 19 recipes. Application examples are maintained alongside the plugin in the repository; this release adds no runnable examples or integrations.

## Choose the appropriate host capability

| Task | Required capability |
| --- | --- |
| Explain services or design an architecture | A host that can load the packaged skill and references |
| Look up changing service details | Documentation or web access |
| Inspect or change OCI resources | Available OCI CLI or supported Console/browser tools, authentication and the appropriate OCI permissions |
| Run application examples | The example's documented runtime, existing services, network paths and scoped credentials |

Installation and browser/shell availability depend on the product, version and managed workspace. A web conversation does not automatically have access to a laptop's CLI profile. Installing Atlas creates no OCI login, hosted execution service or additional IAM rights.

Atlas is a knowledge plugin, not an MCP server. OCI's database-native tools, Database Tools MCP endpoints, Enterprise AI hosted applications, and Agent Sandbox are separate services with their own authentication, permissions, and lifecycle. Describing them does not connect them to the host.

## Availability and evidence

The v1.2 research cutoff is November 17, 2026. Only documented, generally available functionality enters recommended architectures and operational guidance. Oracle GA announcements can establish a high-level offering; exact shapes, access, endpoints, configuration, and regional capacity require owning documentation and environment checks. Preview, limited availability, future announcements, and unresolved source conflicts are deferred.

The [evidence register](RELEASE-EVIDENCE-1.2.md) records accepted changes and exclusions, including future TPUs/Cerebras, AI Media Models preview, Cost Advisor limited availability, native Snowflake-on-OCI, AI Security Mesh, and unverified AIDP ontology/reasoning capabilities. Snowflake external catalogs are a distinct documented integration. AIDP service-account setup currently links to a Preview credential feature and is not prescribed here.

Review dates identify the content and sources reviewed, not proof of universal regional availability or a successful deployment. See the [validation record](VALIDATION-1.2.md) for documentation checks separately from live testing.

## Workload prerequisites

Confirm region/realm support, service availability, capacity, quotas, current prices and API/model compatibility for the selected environment. Database guides explain service relationships and operating workflows; they do not replace product-specific database administration documentation.

Examples use Bash syntax and explicit customer inputs. Adapt shell syntax for PowerShell. The application examples consume existing foundations and describe their resource ownership; adding public ingress, multi-user authorization or additional availability requires a corresponding application design.

OCI and the customer's environment enforce IAM, network isolation, quotas and approvals. Budgets provide alerts rather than a general spending stop. See [installation](INSTALL.md), [workload selection](../plugins/oci-atlas/skills/oci-atlas/references/workload-selection.md) and [access guidance](../plugins/oci-atlas/skills/oci-atlas/references/access-and-tools.md).

## Data handling

Atlas adds no telemetry or remote storage. Host/model services may process the task context and tool results. Keep passwords, MFA codes, wallets, tokens and private keys in appropriate authentication and secret mechanisms, outside conversations and source control.

The v1 compatibility commitment preserves package/skill identity, catalog schema and existing reference paths. OCI features and host capabilities evolve independently.
