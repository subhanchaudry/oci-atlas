# Container Registry and artifact delivery

Reviewed: 2026-11-03

## Choose the artifact store

Container Registry stores container images; Artifact Registry stores supported generic artifacts. Neither runs an application. Record repository, region/registry endpoint, namespace, image architecture and immutable digest. A mutable tag alone cannot identify the deployed application revision.

## Establish the two callers

The build publisher needs upload rights and supported registry authentication. The runtime needs its own pull method, repository access and network path. Its application identity for Secrets, Object Storage or other APIs is a separate boundary. Keep auth tokens and registry secrets out of Dockerfiles, image layers, logs and Terraform variables containing plaintext credentials.

## Working sequence

1. Select an existing repository or create a private workload-owned repository with an explicit retention owner.
2. Build for the runtime architecture. Use a small build context and exclude credential/configuration files.
3. Authenticate through the supported registry mechanism and push a versioned image; record the returned digest.
4. Configure the chosen runtime with that digest and its documented pull authentication. For Container Instances, distinguish registry secret access from application resource-principal access.
5. Observe image pull, container startup and application health separately. A successful developer push does not prove a private subnet can pull.
6. Retain the previous digest for rollback and reconcile database/schema changes independently.

## Failure and lifecycle

For pull failures, inspect exact endpoint/namespace/repository/digest, CPU architecture, credentials and runtime egress before granting broader application IAM. Use service-supported vulnerability scanning where required by the delivery process; a scan result is one input to image maintenance.

Budget retained layers/images and related transfer using current terms. Before deleting old images or applying retention policies, enumerate deployed digests and rollback dependencies. Do not remove a shared repository as part of one container's cleanup. Continue with [DevOps](service-devops.md).

## Sources

- [Container Registry](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryoverview.htm)
- [Artifact Registry](https://docs.oracle.com/en-us/iaas/Content/artifacts/overview.htm)
- [Container Instances registry secrets](https://docs.oracle.com/en-us/iaas/Content/container-instances/vault-secrets-image-authorization.htm)
