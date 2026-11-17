# AI Data Platform catalogs, agents, and compute

Reviewed: 2026-11-17

## Understand the boundaries

Oracle AI Data Platform/Workbench combines governed data access with notebook, workflow and compute resources. Identify the instance and current product/version terminology before applying examples. A workspace organizes files, notebooks, workflows and compute; the Master Catalog organizes registered data assets. A workspace folder is not a database schema or an OCI compartment.

An external catalog connects to an outside source using its configured credentials and exposes supported metadata/data access. It isn't evidence that source data has been copied into the platform or that every source operation is supported. Source-side privileges and platform-side permissions both matter.

## Permissions and private connectivity

OCI IAM access to the instance is separate from Data Platform object permissions. An instance administrator role doesn't remove the need for required OCI access. Inspect permissions on the workspace, folder, job, compute and catalog/schema/table actually involved.

For a private source, resolve the workspace's private-network configuration and the source network. Confirm connectivity from the selected workspace compute/job, not from a developer's browser. Check DNS, route and TLS settings alongside source credentials. Another workspace with different network configuration can behave differently against the same catalog.

## Working sequence

1. In the OCI Console, identify the AI Data Platform instance and open the intended workspace. Confirm which identity and compute context will execute the task.
2. For catalog discovery, identify source type, connection credentials managed through the product's secure flow, source privileges and supported catalog operations. Avoid treating a generic DB connection as an already configured catalog.
3. Register/query a bounded source and inspect metadata visibility. Missing schemas can be a source-credential visibility issue, not absent data.
4. For notebook or workflow execution, record code/revision, parameter values, compute/runtime, catalog bindings and output locations. Observe the run and verify bounded outputs.
5. Publish/reuse the intended artifacts through the current workspace/workflow interface. Confirm schedule behavior separately from a single manual run.

Use the current Console and installed `oci ai-data-platform --help` for supported management operations. Not every workspace feature is necessarily represented by the control-plane CLI. Consult the specific product docs before assuming an API for notebook/catalog operations.

## Gotchas and lifecycle

Do not transplant Data Integration “publish task to application” semantics into Data Platform workflows. Do not transfer a SQL tool's capabilities from an unrelated agent service. Inspect external-catalog operation limitations even when the underlying DB account has broader privileges. Before deleting a workspace/folder/catalog, enumerate contained artifacts, schedules and external consumers; a metadata deletion and source-data deletion are different operations.

## Source-to-workflow handoff

Use the [private-source recipe](recipe-aidp-private-source.md) for external catalog discovery from workspace compute. Record source credentials by secure reference, source-visible schemas, catalog permissions, runtime and output owner. Include scheduled compute, retained storage and source-system load in planning; a catalog registration does not by itself copy the source data.

## Agents, workflows, and AI compute

AIDP agents and knowledge bases are separate from [Generative AI Agents](service-generative-ai-agents.md). A deployment is a snapshot; editing the agent does not update the serving deployment until redeployment. Record the deployed revision and compute, then test invocation and downstream tools separately. A workflow Agent Task sends a prompt to an already deployed agent; it does not deploy that agent.

AI compute autoscaling uses configured replica bounds, request/CPU thresholds and cooldown. Set limits from workload demand and cost assumptions. Agent memory and session retention require explicit ownership: distinguish per-user long-term memory from conversation history, inspect database consumption, and plan deletion of retained data.

Run As describes the deployed agent's platform identity; caller authorization and downstream tool credentials remain separate. The deployment documentation links service-account credentials to Credential Store (Preview). This GA-only collection does not prescribe that preview credential setup or treat the Run As release note as proof that its entire dependency path is GA.

## External data and feature status

Snowflake is a supported external-catalog source. This means connecting to an existing Snowflake environment; it does not establish native Snowflake-on-OCI provisioning. AIDP also supports Iceberg tables, whose write/ownership model must be distinguished from querying an external catalog.

Use feature-specific status. Git integration, bundles/CI-CD, lineage, Credential Store and ML experiments/models have preview labels in the reviewed documentation; omit those preview workflows from GA recommendations. Newly announced ontologies and semantic reasoning are not substitutes for documented catalog, knowledge-base and agent operations.

## Sources

- [AI Data Platform entry point](https://docs.oracle.com/en/cloud/paas/ai-data-platform/)
- [Workspaces and private-network context](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/workspaces.html)
- [Permissions model](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/permissions-model.html)
- [External catalogs and source credentials](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/external-catalogs.html)
- [AI Data Platform control-plane CLI](https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ai-data-platform/ai-data-platform/create.html)
- [AIDP dated feature history and preview labels](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidwn/index.html)
- [AIDP deployed agents and runtime identity](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/agent-flow-deployment.html)
- [AI compute autoscaling](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/ai-compute.html)
- [Agent memory and retention](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/agent-memory.html)
