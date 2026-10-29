# Recipe: Function behind API Gateway

Reviewed: 2026-10-29 · Basis: documentation-based suggested pattern; not a live-tested API.

## Intent and identity map

Expose a bounded function through a controlled API route. Resolve payload/response contract, runtime, public versus private clients, authentication requirements and backend dependencies.

Keep these identities separate: the deployer creates resources; clients call the gateway; the gateway invokes the function; the function's workload principal accesses downstream OCI services. A policy for one does not grant the others access.

## Suggested working sequence

1. Establish target context, existing VCN/application resources and supported runtime/deployment tooling. Confirm image architecture and registry access when using a container-image workflow.
2. Create or select the Functions application in suitable subnets; deploy a minimal function implementing the agreed contract. Add only the required configuration and scoped downstream permissions.
3. Invoke the function directly with a bounded synthetic payload. Enable and inspect relevant logs. Establish the backend works before diagnosing gateway routing.
4. Create or select the gateway's public/private endpoint and regional subnet. Inspect security and routes without automatically exposing the backend.
5. Configure the documented gateway-to-Function invocation policy with the correct principal and resource scope. Use current policy guidance; don't copy a broad tutorial grant unchanged into a production compartment.
6. Add an API deployment containing the route, method, Function backend and required authentication/rate/CORS policies. CORS is a browser-origin control, not client authentication.
7. Test the intended client path: DNS/TLS, gateway route, client auth, invocation, response and correlated logs. State any layer not observed.

## Updates and cleanup

Preserve the API contract when changing function code or deployment routes. Track the function artifact revision and gateway deployment independently. A gateway 401/403, missing route, backend timeout and function exception need different investigation.

For requested deletion, check other routes/deployments sharing the function, application, gateway or registry image. Remove only owned dependencies and preserve any required logs. Consult [application platforms](applications.md) for resource relationships and [operations](operations-security.md) for evidence.

## Related execution and operational patterns

Compare [Container Instances](service-container-instances.md) when the backend needs a long-lived container rather than a bounded function invocation. Use [Queue](service-queue.md) for asynchronous work with explicit acknowledgement/retry handling. Add the [observability recipe](recipe-observability-delivery.md) for gateway/backend evidence and notification receipt; a successful deployment does not establish an observable application.

## Sources

- [API Gateway with Functions tutorial and invocation policies](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm)
- [API Gateway endpoints, deployments and backend routing](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Concepts/apigatewayoverview.htm)
- [Functions service overview](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsoverview.htm)
