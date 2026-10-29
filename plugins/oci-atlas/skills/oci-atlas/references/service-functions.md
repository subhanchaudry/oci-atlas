# Functions deployment and invocation

Reviewed: 2026-10-29 · Basis: documentation review; no live deployments.

## Select the deployment mode

Functions fits bounded event/request processing when its runtime and invocation constraints match the task. Resolve code-only versus image-based deployment; don't assume Docker/Fn tooling is required for every supported workflow. For an image-based function, align architecture, runtime and image access. For code-only functions, inspect supported managed runtimes and update behavior.

A Functions application groups function resources and shared configuration/network context. A function's invoke endpoint is distinct from its management API representation. Configuration values are not automatically a secure place for arbitrary plaintext secrets.

## Establish the three callers

- Deployer: creates/updates applications and functions and, where needed, pushes artifacts.
- Invoker: calls a function directly or through another service.
- Function principal: accesses downstream resources while code executes.

Granting the deployer access doesn't give API Gateway invocation permission or let function code read a bucket. Prefer scoped workload access for runtime dependencies. Inspect the actual runtime identity before modifying policy.

## Working sequence

Use Console **Functions** or inspect `oci fn application`, `oci fn function`, and the selected invocation tool's help. Read application subnets and egress requirements before deployment; a private subnet may still need a service/NAT path to dependencies.

1. Confirm target application, runtime/artifact and request/response contract.
2. Deploy with the supported code/image workflow and track its resource identifiers.
3. Enable relevant logs and invoke using a signed OCI interface or other documented caller. A function endpoint is not necessarily an anonymously callable web URL.
4. Check response, logs and downstream side effects using a bounded synthetic request where appropriate.
5. For HTTP publication, add a gateway deployment through the [serverless API recipe](recipe-serverless-api.md), keeping its authentication separate.

## Operational gotchas

Distinguish cold-start latency, timeout configuration, out-of-memory/runtime failure and an unreachable downstream service. Retrying a function can repeat application side effects; inspect the contract/idempotency behavior before resending a write request. A successful HTTP response is not evidence that all asynchronous processing completed.

For updates, preserve contract compatibility and record artifact/configuration revision. Before deletion, inspect gateway routes, event integrations and shared application settings; keep shared registry artifacts and networking unless their removal is requested.

## Sources

- [Functions runtime and deployment modes](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsoverview.htm)
- [Signed invocation methods](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm)
- [Functions deployment and troubleshooting entry points](https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm)
- [API Gateway integration tutorial](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm)
