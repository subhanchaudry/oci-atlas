# Recipe: private OKE application with workload access

Reviewed: 2026-10-29 · Basis: documentation-based suggested pattern; not a live deployment.

## Intent

Run an application with private workers/backends, explicit client entry and scoped OCI access. Resolve whether Kubernetes is required, which clients connect, data dependencies, availability needs and the existing cluster/network ownership. “Private” needs an explicit meaning for API endpoint, nodes, ingress and data paths.

## Suggested sequence

1. Select the existing suitable cluster or plan the required cluster/node/network configuration. Confirm cluster features support the chosen node and identity model.
2. Establish operator access to the Kubernetes API from the intended executor. Keep kubeconfig context/namespace explicit.
3. Resolve image access from the worker/runtime network, including correct endpoint/digest, architecture and authentication. Don't rely on the developer's Docker login.
4. Select the application namespace/service account. For supported OKE workload identity, configure the matching OCI policy and SDK signer; keep Kubernetes RBAC separate.
5. Configure only necessary routes, DNS and security for model/database/object dependencies. Use the appropriate private endpoint or supported Oracle-service path.
6. Deploy with declared resources, configuration and readiness checks through the owning release/IaC workflow. Keep secrets out of manifests and images.
7. Add the requested public/private ingress and test from the actual client path. Verify a bounded downstream OCI operation using the workload identity.

## Evidence and updates

Report cluster/context, artifact revision, rollout state, client reachability and downstream result separately. For failure, inspect events and logs before replacing infrastructure. Roll out versioned artifacts and verify readiness before removing prior capacity. Check node/version compatibility and disruption behavior before upgrades.

## Cleanup

Identify workload-owned Services, load balancers, PVCs/volumes and image references. Remove only requested resources; preserve a shared cluster or VCN. Report retained disks and data explicitly. Load [OKE](service-oke.md), [routing](service-vcn-routing.md) or [IAM](service-iam-policies.md) only as needed.

## Supporting network and resilience guidance

Use [Load Balancer/NLB](service-load-balancing.md) for supported service exposure and health, [Certificates](service-certificates.md) for the chosen TLS boundary, and [hybrid networking](service-hybrid-connectivity.md) for on-premises operators/callers. For persistent data, follow the actual [Block Volume](service-block-volume.md) or [File Storage](service-file-storage.md) lifecycle. Coordinate application recovery with the [backup/DR recipe](recipe-backup-disaster-recovery.md); restoring a Kubernetes manifest does not restore its data.

## Sources

- [OKE cluster/data-plane choices](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengclustersnodes.htm)
- [Workload identity setup](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contenggrantingworkloadaccesstoresources.htm)
- [Registry access model](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryoverview.htm)
