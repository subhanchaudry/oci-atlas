# DevOps builds, deployments, and rollback

Reviewed: 2026-11-03

## Separate build and deployment

A DevOps project groups connections, build pipelines, deployment pipelines, artifacts and target environments. Build stages produce artifacts; deployment stages change the selected target. Use OCI DevOps when its supported targets and stages fit, or retain the customer's existing delivery system. A green build is not a running application.

## Inputs and access

Record source revision, dependency versions, build specification, artifact repository, target environment and release owner. Distinguish publisher, deployment principal and application runtime identity. Resolve private source/target access, registry authentication and secret references independently. Do not embed credentials in a build specification.

## Release sequence

1. Build a pinned revision with an explicit environment and reproducible dependency inputs.
2. Publish the artifact and capture digest/version; pass that identity into deployment rather than a moving tag.
3. Inspect the deployment stages and target scope. Use supported approval or rollout stages where the customer's process requires them.
4. Deploy through the owning pipeline and observe stage/work-request results.
5. Check the intended client response, dependency access and application signal. Correlate the deployed artifact with logs/traces.
6. Record the prior release and supported rollback action. Database migrations and externally committed business effects need separate recovery procedures.

## Failures and cleanup

For a build failure, find the first source/dependency/credential error. For deployment failure, inspect target reachability, deployment permissions and actual partial state. A retry can repeat stages; check whether those stages create non-idempotent effects.

Budget build execution, artifact retention and target capacity separately. Preserve shared connections, repositories and target environments when retiring a pipeline. Deleting run history does not remove deployed infrastructure. Use [Resource Manager](service-resource-manager.md) for infrastructure ownership and [Container Registry](service-container-registry.md) for image access.

## Sources

- [DevOps overview](https://docs.oracle.com/en-us/iaas/Content/devops/using/devops_overview.htm)
- [DevOps lifecycle guide](https://docs.oracle.com/en-us/iaas/Content/GSG/Reference/getting-started-as-devops.htm)
