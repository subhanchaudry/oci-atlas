# Recipe: private application deployment

Reviewed: 2026-10-29 · Basis: documentation-based suggested pattern; not a live-tested deployment.

## Intent and defaults

Deploy an application with private backends and an explicitly chosen entry point. Start with Compute for a conventional single application; choose OKE when Kubernetes is a workload requirement. Use an existing VCN/landing zone when it fits the address plan and ownership model. Public client access, if requested, can terminate at a public load balancer while backends remain private; an internal application can use a private entry point.

Resolve only design-changing inputs: application artifact/runtime, client locations, target compartment/region, data dependencies and required availability. Do not turn an architecture explanation into provisioning.

## Suggested working sequence

1. Discover relevant existing resources and management ownership. Record application, ingress and data paths and who operates them.
2. Resolve subnets, routes, DNS and narrowly scoped NSGs. Add NAT for required internet egress or service-gateway access for supported Oracle services; don't assume private subnets can download dependencies automatically.
3. Establish the workload principal and specific service permissions. Keep secrets outside images and configuration committed to source control.
4. Launch/configure the chosen runtime or deploy through its existing Terraform/Resource Manager workflow. Configure storage retention and backups to match the request.
5. Establish administrative access from an approved network or supported Bastion session rather than adding public SSH by default. A Bastion session doesn't replace application ingress or general-purpose routing.
6. Configure the entry point, TLS, backend membership, health checks and DNS. Check backend health from the load balancer's perspective.
7. Verify from the intended client: hostname, reachable entry point, application response and any required data access. Report what was actually observed.

## Updates, diagnosis, and cleanup

Deploy an immutable application revision where practical; verify new backends before removing old ones. For failure, use the sequence DNS → route → security → listener → backend health → application/data dependency. A healthy Compute instance doesn't establish application readiness.

For cleanup, distinguish workload-owned resources from a shared VCN, gateway or data service. Establish data retention, remove consumers before dependencies, and report disks, backups, addresses or load balancers that remain. Use the owning IaC workflow where one exists.

## Load detail only when needed

- [Networking](networking.md): routes, NSGs, DNS, load-balancer behavior.
- [Compute and storage](compute-storage.md): images, shapes, volumes and retention.
- [Applications](applications.md): OKE or container workflow.
- [Infrastructure](infrastructure-architecture.md): IaC ownership and repeatability.

## Sources

- [Load-balancer frontend/backend concepts](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/balanceoverview.htm)
- [Bastion access model](https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/bastionoverview.htm)
- [Well-Architected design considerations](https://docs.oracle.com/en/solutions/oci-best-practices/)
