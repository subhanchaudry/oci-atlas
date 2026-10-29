# Application platforms

Reviewed: 2026-10-29 · Basis: documentation review; examples are not live-tested.

## Choose the runtime

| Need | Start with | Operational consequence |
| --- | --- | --- |
| A VM-hosted application with OS control | Compute | Customer manages host/runtime and application lifecycle |
| Kubernetes APIs and orchestration | OKE | OCI cluster/network resources plus Kubernetes operations |
| Event/request-driven bounded code | Functions | Function/application configuration, runtime and invocation limits |
| API front door, routing and policies | API Gateway | Gateway + deployment + backend; it doesn't host application code |
| Container artifacts | Container Registry (OCIR) | Image/repository access and retention, separate from running containers |
| Build and release orchestration | OCI DevOps | Build/deploy identities, artifacts, environments and pipeline runs |

Choose the simplest runtime that meets the workload's needs. A container image alone doesn't require Kubernetes, and a gateway doesn't replace a backend service.

## OKE: two control planes

An OKE cluster includes an API/control-plane endpoint and a data-plane choice. Node pools, images, subnets, pod networking and worker capacity must fit the workload. Basic and enhanced clusters differ; workload identity and virtual-node features have specific cluster requirements. Inspect the actual cluster type and supported versions rather than assuming all OKE features are present.

OCI IAM access to the cluster and Kubernetes RBAC on its objects are separate checks. Establish the kubeconfig context, namespace, and API endpoint reachability before `kubectl` operations. A private API endpoint needs a network path from the executor. For pod failures, inspect events, image pulls, scheduling capacity, probes and networking before recreating a cluster.

Read-only discovery using [selected context variables](access-and-tools.md):

```bash
oci ce cluster list --compartment-id "$ATLAS_COMPARTMENT_ID" --all \
  --profile "$ATLAS_PROFILE" --auth "$ATLAS_AUTH" --region "$ATLAS_REGION"
```

Create/update from current command schemas or the existing IaC configuration. When deleting Kubernetes services or clusters, inspect persistent volumes, load balancers and retained disks; don't assume every dependent resource disappears.

## Functions, API Gateway and registry

A Functions application groups functions and supplies shared network/configuration context. A function has code/image, runtime limits, configuration and an invocation endpoint. Check whether the customer uses a code-based workflow or a container-image workflow and follow its current deployment tooling. Verify the application subnet's access to required services. Enable logs for diagnosis and distinguish an invocation timeout from backend failure.

API Gateway resources provide public/private entry; API deployments contain routes and policies. The gateway's ability to invoke a Function or reach an HTTP backend needs its own authorization and connectivity. Client authentication, gateway-to-backend authorization and a Function's resource principal are different identities.

OCIR repositories store image artifacts; use the actual regional registry endpoint, namespace and supported login method. A CLI session is not automatically a Docker registry login. Keep registry credentials in normal credential tooling. Prefer immutable digest references for repeatable deployment and match image architecture to the runtime. A successful push does not prove worker image-pull access.

## DevOps and navigation

A DevOps project contains build pipelines, deployment pipelines, artifacts, environments and connections. Builds produce artifacts; deployments apply them to referenced targets. Grant pipeline/runtime identities the required scoped access. Record the source revision and artifact digest, observe the run/stages, and verify the target workload independently. A completed build isn't a deployed application.

Console search terms are **Kubernetes clusters**, **Functions**, **API gateways**, **Container Registry**, and **DevOps**. CLI roots include `oci ce`, `oci fn`, `oci api-gateway`, `oci artifacts container`, and `oci devops`; use `kubectl`, image tooling or Fn tooling only when required by the chosen task and available locally. Check help for exact resource command names.

## Additional application and integration platforms

[Container Instances](service-container-instances.md) runs containers without a Kubernetes control plane. Compare it with [OKE](service-oke.md) when orchestration is required and [Functions](service-functions.md) for bounded invocations. Define restart, exposure, durable storage, image-pull access, and operating ownership explicitly.

[Queue](service-queue.md) distributes work to consumers with visibility/retry handling. [Streaming](service-streaming.md) and [Streaming with Apache Kafka](service-streaming-kafka.md) support partitioned event processing with different resource and compatibility models. Choose the delivery contract before choosing a client library.

[APEX and ORDS](service-apex-ords.md) serve database-centric low-code and REST workloads: workspace, parsing schema, application login, and OCI compartment are different boundaries. [Oracle Integration](service-oracle-integration.md) connects business applications through adapters/integrations, whereas Data Integration publishes data tasks. [Analytics Cloud](service-analytics-cloud.md) exposes governed analytics with its own roles, data connections, and source permissions.

## Sources

- [OKE clusters, node choices and feature differences](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengclustersnodes.htm)
- [Cluster list command](https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/list.html)
- [Functions overview](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsoverview.htm)
- [Functions workflows and tools](https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm)
- [API Gateway resource model](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Concepts/apigatewayoverview.htm)
- [Container Registry](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryoverview.htm)
- [DevOps projects and pipelines](https://docs.oracle.com/en-us/iaas/Content/devops/using/devops_overview.htm)
