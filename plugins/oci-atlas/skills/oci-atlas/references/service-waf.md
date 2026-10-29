# Web Application Firewall policies and enforcement

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Select the enforcement model

WAF evaluates supported web traffic using access controls, protection rules and other configured request/response behavior. Use it for application-layer threats and unwanted HTTP traffic. It does not replace application fixes, user authentication, subnet security or a routed network firewall.

Identify regional WAF versus an edge-policy deployment before selecting APIs or describing traffic changes. Regional policy association with a supported load balancer differs from an edge deployment using DNS/origin configuration. Do not copy an edge tutorial's DNS procedure into a regional policy rollout or promise automatic conversion between the models.

## Resource relationships and prerequisites

Resolve the WAF policy, actual enforcement resource, protected listener/domain, rule conditions/actions and backend/origin. The existence of a policy does not prove that requests traverse it. Determine where TLS terminates and how the protected application identifies the original client.

Use Console **Web application firewall** and the selected policy's current API/CLI help. Inspect the existing DNS/load-balancer owner, IAM permissions and logs. Select capabilities from the specific deployment model rather than assuming every protection or rule type exists everywhere. The customer's web application may rely on paths, methods and payload sizes that need explicit consideration.

## Working sequence

1. Identify a bounded set of application routes and intended clients. Capture the expected normal request behavior and current frontend association.
2. Read existing rules, conditions and actions, including priorities. Preserve unrelated allow/deny logic and address lists.
3. Select the requested protection or access change. Where supported, use an observation/detection action to inspect impact before a broad blocking rollout.
4. Associate/deploy through the correct regional or edge workflow. For edge changes, inspect DNS/origin dependencies and propagation independently.
5. Send a benign representative request through the actual public entry point. Inspect WAF logs and application response to confirm both enforcement path and intended access.
6. Record the policy/enforcement identifiers, revision and affected routes. A policy update being accepted is not proof all clients saw the intended behavior.

## Diagnose false positives and bypasses

For unexpected blocking, correlate timestamp, request ID, rule/action, path, method and sanitized request characteristics. Check whether another layer, such as API Gateway, a load-balancer listener or the application, rejected the request first. An HTTP error alone does not identify WAF as the cause.

Narrow an evidenced false-positive exception to the relevant condition instead of disabling protection for the entire application. Avoid collecting sensitive bodies or credentials merely to explain a rule match. For apparently unprotected traffic, confirm frontend association, DNS and whether direct origin access follows a separate path.

Before deletion or rollback, restore the intended association and account for DNS changes where applicable. Preserve a shared policy and other protected applications. See [load balancing](service-load-balancing.md) for backend health, [Certificates](service-certificates.md) for TLS, and [Network Firewall](service-network-firewall.md) for a different traffic-inspection layer.

## Sources

- [Regional WAF and edge enforcement distinctions](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/overview.htm)
- [WAF conditions, policies, protections, and actions](https://docs.oracle.com/en-us/iaas/Content/WAF/home.htm)
- [Load Balancer components and TLS](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/balanceoverview.htm)
