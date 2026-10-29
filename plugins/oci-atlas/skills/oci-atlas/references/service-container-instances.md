# Container Instances runtime, image access, and lifecycle

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Choose a managed container runtime

Container Instances runs supported container workloads without requiring a customer-operated host or Kubernetes cluster. Consider it when an existing container image needs the service's supported runtime/network model and Kubernetes-specific orchestration is unnecessary. Compare OKE for the Kubernetes API/ecosystem, Functions for its invocation/runtime contract and Compute for OS control.

Do not promise Kubernetes controllers, automatic application replicas or every orchestration feature merely because containers run on managed compute. Establish availability, scaling, exposure and restart ownership for the actual application. A container image and an externally reachable service are different things.

## Resource relationships and prerequisites

A container instance groups configured containers with selected compute resources and networking. Individual images, commands/arguments, environment, health/restart behavior and supported storage/mount choices form the runtime contract. Distinguish temporary storage from separately managed persistent File Storage; a restart or instance deletion can have different data effects.

The runtime must reach and authenticate to its image registry. A developer's successful push or laptop Docker login does not prove service image-pull access. Resolve architecture compatibility, subnet egress, registry credentials/secrets and cross-compartment dependencies. Application runtime access to OCI resources is another identity boundary; use only the documented supported principal mechanism.

## Working sequence

Navigate to **Container instances** and inspect `oci container-instances --help`. Identify the existing release/IaC owner and read the selected service's current resource schema instead of applying an OKE pod manifest to it.

1. Pin the intended image revision/digest, compatible architecture, entry point, resource needs and exposed application port.
2. Resolve image-pull network/authentication, runtime dependencies and any persistent storage mount path. Keep secrets out of images and committed environment files.
3. Select supported restart/shutdown behavior and networking. An always-running web service and a one-shot job have different successful-exit expectations.
4. Create/update through the owning workflow and observe instance plus individual container states and exit information.
5. Inspect relevant logs and verify application reachability from the intended client, including any separately configured load balancer/API frontend.
6. Record the artifact/configuration revision, persistence boundaries and the process responsible for replacement or additional capacity.

## Diagnose and maintain

Image failure → inspect actual registry endpoint, credentials, subnet path and architecture. Repeated exits → inspect application exit code, entry point/configuration, resource pressure and restart policy. Healthy lifecycle but no response → inspect application listener, security rules, routing and frontend health separately.

Review current support before assuming an image or resource change is in place versus a replacement. Preserve useful capacity/rollback references when updating a consumer-facing application. For cleanup, inspect attached/shared filesystems, image repositories, secrets and external frontends. Deleting the runtime should not delete unrelated data or claim a registry image was removed. Use [load balancing](service-load-balancing.md) for ingress and [OKE](service-oke.md) when Kubernetes is the deciding requirement.

## Sources

- [Container Instances operating model](https://docs.oracle.com/en-us/iaas/Content/container-instances/overview-of-container-instances.htm)
- [Creation, registry access, restart policies, and storage](https://docs.oracle.com/en-us/iaas/Content/container-instances/creating-a-container-instance.htm)
- [Container logs and lifecycle tasks](https://docs.oracle.com/en-us/iaas/Content/container-instances/home.htm)
