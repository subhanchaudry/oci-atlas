# Tenancy foundations and IAM

Reviewed: 2026-10-29 · Basis: documentation review; examples are not live-tested.

## Mental model

An OCI tenancy is the account's root resource boundary and root compartment. Compartments organize resources and form policy/cost boundaries; they do not create a network boundary. A compartment can hold resources from multiple regions. An OCID identifies a resource; display names can repeat and are unsuitable as the sole target of a write.

A region is a geographic deployment scope. Availability domains are isolated locations within a region; fault domains separate placements within an availability domain. Discover what the target region actually offers instead of assuming three availability domains everywhere. The home region matters for IAM administration; a workload's deployment region can be different.

## Identity and authorization

| Object | Role | Common confusion |
| --- | --- | --- |
| Identity domain | Identity administration, users/groups, federation and sign-in | Not an application compartment |
| User and group | Human identity and collections granted access | Signing in does not grant all resource permissions |
| Dynamic group | Rule-based membership for supported OCI resources | Membership alone grants no permissions |
| Policy | Grants actions on resource types in a scope | A policy's attachment location and its target scope both matter |
| Resource/instance principal | A workload authenticates using its resource identity | Not the human's Console session |

OCI policy verbs include `inspect`, `read`, `use`, and `manage`; their exact permissions depend on the service/resource type. Use the service policy reference rather than treating `read` as a universal least-privilege recipe. Workload identity in OKE has its own supported principal/policy pattern; don't automatically replace it with node-wide dynamic-group access.

Policy statement **shape**, not a copy-paste policy:

```text
Allow group <identity-domain>/<group> to <verb> <resource-type> in compartment <compartment>
```

Resolve actual domain/group names and supported syntax from the current policy reference. Start from the caller, operation, resource type, and scope. Avoid proposing tenancy-wide administrator access to fix a local failure. Allow for policy propagation when a recent correct grant has not taken effect.

## Discover and navigate

Use Console search for **Compartments**, **Domains**, **Policies**, and **Limits, Quotas and Usage**. Verify region and compartment filters before interpreting a service page. In CLI workflows start with `oci iam`, `oci search`, `oci limits`, and `oci quota`; see [access conventions](access-and-tools.md).

Read-only example: recursively list compartments visible to the selected user under the tenancy:

```bash
oci iam compartment list --compartment-id "$ATLAS_TENANCY_ID" \
  --compartment-id-in-subtree true --access-level ACCESSIBLE --all \
  --profile "$ATLAS_PROFILE" --auth "$ATLAS_AUTH" --region "$ATLAS_REGION"
```

This is not proof that all tenancy compartments or resources were discovered. For a complete inventory, state regions, services, pagination and visibility limitations. Resource Search covers supported indexed types and can lag recent changes; verify critical existence/state with the owning service's get/list operation.

## Resource lifecycle and limits

Before creating a compartment, determine its parent and intended policy ownership. Changes to IAM policy can affect descendants; preview scope as well as statement text. Removing a compartment requires resolving its resources and service-specific deletion prerequisites first. Empty lists under one identity or region do not establish emptiness.

Separate four different blockers: IAM authorization, Oracle-set service limits, administrator-set compartment quotas, and current service capacity. A limit increase does not guarantee available capacity. Budgets are spending alerts, not hard enforcement. Use quotas for supported resource consumption controls, not as a universal monetary ceiling.

## Sources

- [IAM overview](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm)
- [Policy syntax](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policysyntax.htm)
- [Regions and availability domains](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm)
- [Compartment list command](https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/list.html)
- [Search coverage and visibility](https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/queryoverview.htm)
- [Search consistency and missing results](https://docs.oracle.com/en-us/iaas/Content/Search/Troubleshooting/noresults.htm)
- [Compartment quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas.htm)
