# OKE clusters, workloads, and identities

Reviewed: 2026-10-29 · Basis: documentation review; no live cluster operations.

## Select the cluster and data plane

Choose Kubernetes because the application needs its orchestration/API model. Resolve basic versus enhanced cluster features, supported Kubernetes version, managed/virtual/self-managed node choices, pod networking, worker sizing and API endpoint accessibility. Don't assume workload identity or virtual nodes are available on every cluster type. An OCI cluster OCID is not a Kubernetes context or namespace.

Separate three paths: the operator reaches the Kubernetes API; workers/pods reach registry and dependencies; clients reach the application. Private API access from a laptop needs actual network connectivity. A working Console view does not establish that path.

## Deploy a bounded workload

1. Inspect the chosen cluster/node pools and existing management ownership using `oci ce ... --help` or its IaC configuration.
2. Configure kubeconfig through the documented access workflow. Check current context and namespace before `kubectl` changes; avoid overwriting unrelated contexts.
3. Resolve image reference/digest and architecture, pod resources, service account, config/secrets, storage and probes.
4. Apply the intended workload through its owning release process. Observe pods, events and rollout, then check application reachability from the intended client.
5. Inspect any cloud load balancer or persistent volume created by Kubernetes controllers; those are separate OCI resources with their own dependencies/costs.

## Identity and image pulls

Kubernetes RBAC controls Kubernetes objects. OCI IAM controls OCI APIs. Workload identity can bind a supported enhanced-cluster workload's cluster/namespace/service-account identity to OCI permissions via a supported SDK. It is not a node-wide dynamic-group grant.

Registry image-pull authentication can be a separate mechanism from the application's runtime OCI API identity. A developer's successful image push is not proof that the node/runtime can pull it. Inspect the configured pull method, image reference and network path; don't broaden runtime IAM to fix a wrong image name.

## Update and diagnose

For ImagePullBackOff inspect events, image existence/digest, pull authentication and egress. For Pending inspect resources, node conditions, placement and storage. For CrashLoopBackOff inspect termination state and current/previous logs. For failed readiness inspect probe parameters and actual serving behavior. Check version compatibility and drain/disruption implications before node cycling or upgrades.

Delete workload-owned consumers before shared cluster/network/storage dependencies. A removed Deployment is not proof its PVC, external load balancer or image was removed.

## Sources

- [OKE cluster types and node choices](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengclustersnodes.htm)
- [Workload identity](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contenggrantingworkloadaccesstoresources.htm)
- [Container Registry](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryoverview.htm)
- [Kubernetes pod diagnosis](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/)
