# Infrastructure as code and architecture

Reviewed: 2026-10-29 · Basis: documentation review; examples are not live-tested.

## Choose the management path

Use CLI/Console for an appropriately scoped operational task or exploration. Prefer an existing Terraform workflow for resources it owns. For a repeatable environment, use Terraform with explicit inputs and managed state. Resource Manager supplies OCI-hosted stacks/jobs and state management; it is not an application runtime.

Start with existing ownership: repository, provider configuration, state backend, stack, target compartment and deployment process. Do not create a second state owner or edit a managed resource out of band merely because the Console is convenient. If an urgent direct change is requested, explain and record how configuration/state will be reconciled.

## Resource Manager model and working pattern

A **stack** associates configuration, variables and state. A **job** runs a plan, apply, destroy or another supported operation. A plan describes proposed actions; it does not provision resources. Avoid interpreting Terraform execution success as application readiness.

Use Console search for **Stacks** or **Resource Manager**. Read-only discovery using [selected context variables](access-and-tools.md):

```bash
oci resource-manager stack list --compartment-id "$ATLAS_COMPARTMENT_ID" --all \
  --profile "$ATLAS_PROFILE" --auth "$ATLAS_AUTH" --region "$ATLAS_REGION"
```

For a requested deployment:

1. Resolve configuration source/revision, provider/runtime compatibility, variables, region and compartment. Keep credentials outside source files.
2. Inspect a plan. Summarize creates, updates, replacements and destroys, including shared dependencies. A request to deploy need not prompt for permission before every contained step; scope changes and unexpected destructive effects need clarification.
3. Apply the intended reviewed configuration/plan through the owning workflow. In Resource Manager, use the supported plan-job association; a moving Git branch can change between jobs, so track or pin the source and verify which revision each job used.
4. Observe the job, inspect sanitized logs and outputs, then verify resources and the requested outcome.
5. Preserve state. For cleanup, inspect destroy implications, external references and retained data before running it. State and plan files can contain sensitive values even when output is marked sensitive.

Check installed command help for exact job parameters. A generic CLI example cannot choose a compatible Terraform version or provider for the customer's stack.

## Architecture decision context

| Requirement | Useful OCI design question |
| --- | --- |
| Availability | What failure must survive: process, node, fault domain, availability domain or region? |
| Recovery | What are RPO/RTO, restore procedure and dependencies outside the primary region? |
| Private access | Where are callers, DNS resolvers and endpoints, and how does traffic return? |
| Security | Which humans/workloads call which APIs; where are data, keys and secrets? |
| Cost/performance | What is steady versus burst demand, and what remains billed when idle? |
| Operations | Who owns deployment, monitoring, patching, incident handling and cleanup? |

Use regional subnets, private application backends and workload-scoped identities as starting design choices where they fit the workload. Explain deviations. Fault domains within one availability domain do not provide cross-region recovery. A backup needs a restore procedure; HA and disaster recovery are different objectives.

A landing zone establishes reusable tenancy/network/security foundations. Evaluate Oracle's current landing-zone guidance before inventing a new tenancy layout, but don't deploy a full landing zone for a simple task or claim that a template makes an environment compliant. Use Well-Architected pillars to identify relevant tradeoffs rather than attaching a generic checklist to every answer.

## Sources

- [Resource Manager configuration, stacks, jobs and drift](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm)
- [Stack list command](https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/list.html)
- [Apply jobs and plan resolution](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm)
- [OCI Well-Architected Framework](https://docs.oracle.com/en/solutions/oci-best-practices/)
- [OCI Cloud Adoption Framework](https://docs.oracle.com/en-us/iaas/Content/cloud-adoption-framework/)
- [Current landing-zone implementations](https://docs.oracle.com/en-us/iaas/Content/cloud-adoption-framework/technology-implementation.htm)
