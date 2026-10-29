# Load Balancer, Network Load Balancer, and backend health

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Choose the traffic contract

Use Load Balancer for reverse-proxy behavior, HTTP routing and supported TLS termination. Consider Network Load Balancer (NLB) for connection-level distribution, source-address preservation and network-appliance or long-lived connection requirements. Choose by protocol and packet behavior before discussing bandwidth. API Gateway adds API policies and routing; it does not replace every load-balancing use case.

Decide public versus private reachability from the intended clients. A private load balancer still needs a client network path and DNS. Inspect current protocol, address-preservation and backend support for the selected service; don't transfer a Load Balancer feature to NLB because the object names look similar.

## Resource relationships

A listener accepts a protocol/port and directs traffic to a backend set. The backend set combines backend members, a distribution policy and health-check configuration. TLS certificates and hostname/routing configuration belong to the actual frontend/backend contract. The load-balancer resource, its subnets/security, and the application servers have separate lifecycle and permissions.

Distinguish client → listener from load balancer → backend. A healthy VM is not necessarily a healthy backend, and a passing TCP probe does not establish that the application can serve the intended HTTP route. With NLB, address-preservation choices affect return routing and which source must be permitted by backend controls.

## Prerequisites and working sequence

Navigate to **Load balancers** or **Network load balancers**. Inspect installed `oci lb --help` or `oci nlb --help` for the chosen interface. Resolve the compartment, region, existing IaC owner, client network, backend addresses/ports, capacity and certificate references.

1. Read existing listeners, backend sets, health status, and subnet/NSG configuration before creating a parallel frontend.
2. Select the backend protocol and a health check that represents useful readiness. Account for a host header, path or authentication expectation where supported.
3. Configure only the requested listener/routing/TLS behavior. Keep certificate material in supported certificate management; see [Certificates](service-certificates.md).
4. Observe the work request and resource lifecycle, then inspect individual backend health and logs.
5. Send a bounded application request from the actual client path. Verify the selected route and backend behavior separately from provisioning success.

## Diagnose and change

For unhealthy backends, check the listener process, health-check port/path, security rules, return routing and application dependencies. For certificate errors, inspect hostname, chain and frontend/backend TLS separately. For intermittent responses, correlate backend health transitions, session persistence, timeouts and deployment revision.

When updating members, preserve healthy capacity and use the service's supported draining/weight behavior rather than terminating all servers. Determine whether OKE or another controller owns the frontend before changing it manually. Before deletion, inspect DNS records, API consumers, Kubernetes ownership and certificate associations. Remove requested resources without deleting shared networking or application data.

## Sources

- [Load Balancer concepts and components](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/balanceoverview.htm)
- [NLB behavior and service comparison](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/overview.htm)
- [Backend health-check policies](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/load_balancer_health_management.htm)
