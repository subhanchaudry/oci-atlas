# Zero Trust Packet Routing and security attributes

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Understand the enforcement boundary

ZPR controls supported endpoint communication using security attributes and ZPR policy. It adds a packet-authorization layer to an existing network. It does not create routes, replace DNS, grant SQL privileges or remove the need for NSG/security-list permission. A flow needs the underlying network path and the applicable ZPR authorization.

Use ZPR when the requested policy should express resource roles independently of particular address/subnet layouts. Confirm supported resource types, region/tenancy scope and current policy semantics before applying attributes. Don't assume every OCI object supports ZPR because another resource from the same service does.

## Resource relationships

A security attribute namespace groups attribute definitions; supported resources receive attribute values referenced by policy. ZPR policies describe allowed communication for the relevant networks/endpoints. These security attributes are not ordinary cost tags, and ZPR rules are not OCI IAM statements.

Separate permission to administer attributes/policies from permission to operate a workload and from the packet rule that workload traffic must satisfy. Adding or removing an attribute can change live reachability. Treat attribute assignment as a network-affecting change, not a cosmetic relabeling operation.

## Prerequisites and working sequence

Use Console **Zero Trust Packet Routing**, security attributes and the protected-resources view. Inspect the ZPR and Security Attribute API/CLI references for their separate operations. Reuse [IAM guidance](service-iam-policies.md) for the operator's management grants.

1. Define a concrete flow: source role, destination role, applicable network, protocol and intended outcome. Read current resource attributes and policies before inventing new names.
2. Establish the existing route, DNS and NSG/security-list behavior. Resolve an underlying path failure before treating ZPR as its cause.
3. Check resource support and the exact policy-language reference. Use documented policy examples with the customer's actual namespaces/values; don't translate IAM syntax into a ZPR statement.
4. Plan policy and attribute changes together so necessary flows remain authorized during the transition. Identify shared resources carrying the same attribute values.
5. Apply the bounded requested change through the owning workflow. Inspect resulting assignments and policy state.
6. Verify the intended allowed flow from its real source and inspect an appropriate negative case when requested. A resource carrying an attribute is not evidence the application connection succeeded.

## Diagnose and maintain

For a sudden timeout after labeling, compare source/destination assignments and the applicable policies with the prior configuration. Check both sides of the flow and retain the base network checks. Do not fix a missing ZPR allow by broadly opening every subnet rule; the additional layer still applies.

Maintain an explicit owner and meaning for each namespace/value. Before deleting or changing a shared attribute or rule, enumerate protected consumers and intended remaining flows. A routing change can expose new paths even when attribute policy is stable, so inspect the combined design after topology changes. Use [network troubleshooting](troubleshoot-connectivity.md) to separate routing, security, TLS and application authorization.

## Sources

- [ZPR resource support and interaction with network controls](https://docs.oracle.com/en-us/iaas/Content/zero-trust-packet-routing/overview.htm)
- [ZPR policy language](https://docs.oracle.com/en-us/iaas/Content/zero-trust-packet-routing/zpr-policy-overview.htm)
- [Attribute namespaces and lifecycle](https://docs.oracle.com/en-us/iaas/Content/zero-trust-packet-routing/home.htm)
