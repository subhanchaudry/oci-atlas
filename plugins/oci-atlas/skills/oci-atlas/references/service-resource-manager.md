# Resource Manager stacks, plans, and ownership

Reviewed: 2026-11-03

## Choose a single owner

Use Resource Manager for OCI-hosted Terraform configuration, jobs and state. Reuse an existing stack when it owns the target; do not import the same resource into a second active state. The stack owns infrastructure definitions, not application source or SQL migrations.

## Inputs and permissions

Resolve configuration revision, Terraform/provider versions, variables, compartment, region, state owner and private dependencies. Keep secrets outside source and remember that state and saved plans can contain sensitive data. A stack operator needs Resource Manager permissions; jobs also need the target services' required authorization. A private Git source needs both repository authentication and network reachability.

## Plan, apply, and hand off

1. Read the stack and prior job outputs; identify shared resources and existing ownership.
2. Pin the source revision and generate a plan. Summarize creates, updates, replacements and deletes.
3. Apply the intended plan using the supported plan-job association. Confirm the source revision did not change between jobs.
4. Observe job state and the first failed operation. A timeout requires reconciliation before another apply.
5. Read resulting resources, then check the application from its client network. Return identifiers, endpoint metadata and remaining prerequisites without credentials.

Read-only discovery using the [access inputs](access-and-tools.md):

```bash
oci resource-manager stack list --compartment-id "$ATLAS_COMPARTMENT_ID" --all \
  --profile "$ATLAS_PROFILE" --auth "$ATLAS_AUTH" --region "$ATLAS_REGION"
```

## Import, drift, and recovery

Distinguish importing existing state, importing resource addresses and generating configuration through resource discovery. Preserve a state backup and retire the old writer before ownership transfer. Discovery coverage is service-specific; inspect missing dependencies.

Drift detection compares eligible resources with the recorded baseline. Decide whether to adopt an intentional change into configuration or restore the intended configuration, then inspect a new plan. Do not overwrite state to make a warning disappear. For partial apply, inspect committed resources and state before retrying.

Destroy only workload-owned resources through their owning stack. Existing networks, databases, secrets and retained backups must remain outside the destroy plan unless explicitly owned and requested. Use [infrastructure architecture](infrastructure-architecture.md) for design tradeoffs.

## Sources

- [Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm)
- [Apply a plan](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm)
- [Drift detection](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/detect-drift.htm)
