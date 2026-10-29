# IAM policies and workload identities

Reviewed: 2026-10-29 · Basis: documentation review; no live policy changes.

## Model the caller before the policy

Resolve the principal making the failing request, the operation, the target resource, and its compartment. A human deploying a Function and that Function reading an object are different callers. The same applies to a Data Science job, DevOps pipeline, or Kubernetes pod. Inspect the request context rather than assuming the signed-in user is responsible.

OCI permissions come from policy statements. A dynamic-group rule determines membership; it does not grant resource access. An identity-domain role and a resource policy solve different administration/access problems. A successful Console sign-in establishes neither service authorization nor database SQL privileges.

## Build a scoped grant

1. Find the operation in the owning service's policy reference and identify its required permissions/resource types.
2. Resolve whether the subject is a domain-qualified human group, dynamic group, service principal, or supported workload principal.
3. Choose resource and compartment scope. Inspect inherited grants before adding another policy. A compartment can contain resources across regions.
4. Inspect the policy attachment location and statement target. Use conditions only with variables supported for the operation; don't infer that a request variable exists on all APIs.
5. Read back the policy and check the intended caller's operation after propagation. Preserve unrelated statements during update.

Template, deliberately incomplete until the actual caller and service permissions are known:

```text
Allow <subject> to <verb> <resource-type> in compartment <target> where <supported-condition>
```

`inspect/read/use/manage` are service-defined permission bundles. A generic verb is not proof that the intended API is included. Prefer the narrow supported operation pattern over a tenancy-wide administrator policy.

## OKE distinction

For supported enhanced clusters, an OKE workload is identified by cluster, namespace and Kubernetes service account. Configure the supported SDK signer and IAM conditions for that identity. This is separate from Kubernetes RBAC and from node instance-principal policies. Do not assume an OKE workload can be placed in a dynamic group; follow the workload-identity documentation.

## Work and diagnose

Use Console **Policies**, **Domains**, or **Dynamic Groups**; inspect `oci iam policy --help` for resource policy operations. Identity-domain APIs can use a different interface from core IAM. For a denied request, compare the actual resource OCID, region, caller, policy scope and dependent resources. A 404 `NotAuthorizedOrNotFound` doesn't distinguish missing resources from denied visibility. Changing the wrong caller's policy will not fix it.

## Sources

- [Policy syntax](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policysyntax.htm)
- [IAM components and scope](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm)
- [OKE workload identity](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contenggrantingworkloadaccesstoresources.htm)
- [OCI API errors](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm)
