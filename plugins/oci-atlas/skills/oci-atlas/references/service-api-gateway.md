# API Gateway deployments and backend access

Reviewed: 2026-10-29 · Basis: documentation review; no live gateway changes.

## Understand the objects

A gateway supplies a regional public/private endpoint. A deployment supplies API routes and policies on that gateway. A backend supplies application behavior, such as an HTTP service or Function. The gateway doesn't run the application's general-purpose code.

Resolve intended clients, API contract, endpoint exposure, authentication, backend identity/network access, TLS and operational limits. Use a gateway for an API policy/routing front door; compare a load balancer when the main requirement is distributing application traffic rather than API policy handling.

## Map authentication independently

Client → gateway authentication/authorization is separate from gateway → Function/HTTP backend access. A Function's downstream principal is a third context. CORS controls browser origins; it is not client authentication, and a permitted origin does not grant OCI resource access.

For a Function backend, inspect the documented gateway principal/policy pattern for the actual function scope. For an HTTP backend, inspect hostname resolution, routes, TLS trust and any required service authentication from the gateway's network context. A private backend may work from a VM while remaining unreachable from the gateway.

## Deployment sequence

1. Read existing gateway/deployments and their consumers using Console **API gateways** or `oci api-gateway ... --help`.
2. Confirm route path/method and backend contract. Inspect a minimal backend response independently where possible.
3. Create/update the intended deployment specification, preserving unrelated routes/policies. Use the current schema for optional authentication, transformation, rate and CORS settings.
4. Observe work/resource state and test the full request from the intended client, including authenticated and invalid requests when relevant.
5. Correlate request logs across gateway and backend instead of attributing every non-2xx response to the function.

## Diagnose and evolve

401/403 → determine which layer rejected identity. Missing path/method → compare the actual URL/deployment prefix and routes. Backend timeout/5xx → inspect backend network/invocation and logs. TLS failure → inspect endpoint hostname/certificate/trust. These are starting branches, not an assertion that every status has one cause.

For updates, preserve versioned API contracts and identify consumers before removing routes. When cleaning up, distinguish deployment deletion, gateway deletion and backend deletion; a shared gateway can host other APIs. Don't silently replace a private endpoint with public access to diagnose reachability.

## Sources

- [Gateway and deployment resource model](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Concepts/apigatewayoverview.htm)
- [Gateway-to-Function invocation setup](https://docs.oracle.com/en-us/iaas/Content/developer/functions/func-api-gtw/01-summary.htm)
- [OCI Logging and service logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/loggingoverview.htm)
