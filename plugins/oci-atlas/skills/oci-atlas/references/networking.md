# Networking and private access

Reviewed: 2026-10-29 · Basis: documentation review; examples are not live-tested.

## Choose a path, not just a subnet

A VCN is regional; regional subnets are a useful default. Choose non-overlapping CIDRs against existing OCI, on-premises, and peered networks. VNICs attach resources to subnets; route tables decide next hops and security rules permit traffic. Neither routing nor a security rule alone establishes connectivity.

| Need | OCI building block | Check |
| --- | --- | --- |
| Public entry | Internet gateway and appropriately addressed/public-facing endpoint | Route, addresses, ingress rules and listener |
| Outbound internet from private resources | NAT gateway | Egress route, security rules, and destination reachability |
| Private access to supported Oracle services | Service gateway | Regional service destination, route, supported service/endpoint |
| On-premises or transit connectivity | DRG with VPN/FastConnect/attachments | Both directions' routes, imports/exports, DNS and firewall |
| Service-level isolation | NSGs where the service supports them | Resource membership and the full effective rule set |

An internet gateway does not make every VNIC public. A NAT gateway does not accept arbitrary inbound connections. A service gateway is not a substitute for a service-specific private endpoint or for routing to every OCI hostname.

## Security, DNS, and balancing

Security lists apply at subnet level; NSGs group supported resource interfaces. Effective allows from applicable rules are additive, not an ordered deny firewall. Prefer narrow application-facing NSG rules rather than opening a broad subnet rule. Inspect stateless rules and return-path requirements before assuming stateful behavior. If Zero Trust Packet Routing attributes/policies are in use, include that layer; NSGs alone may not permit traffic.

Private DNS handles names resolvable within the relevant private network context. Peering connectivity alone does not establish DNS forwarding. Diagnose resolution from the actual caller, especially for private database endpoints or hybrid networks.

Load Balancer adds listeners, backend sets, health checks, and optionally TLS termination. Distinguish listener reachability from backend health. Choose public/private placement explicitly; compare Network Load Balancer separately when transport-level behavior and source preservation are requirements. Verify current capabilities instead of treating the products as interchangeable.

## Work through a network task

Use Console search for **Virtual cloud networks**, **Network security groups**, **DNS**, or **Load balancers**. CLI families include `oci network`, `oci dns`, `oci lb`, and `oci nlb`. Establish [target/auth inputs](access-and-tools.md) first.

Creation example — **writes a VCN**, not a complete application network. Define `ATLAS_VCN_CIDR` to a CIDR checked against the customer's address plan:

```bash
oci network vcn create --compartment-id "$ATLAS_COMPARTMENT_ID" \
  --cidr-blocks "[\"$ATLAS_VCN_CIDR\"]" --display-name atlas-network \
  --profile "$ATLAS_PROFILE" --auth "$ATLAS_AUTH" --region "$ATLAS_REGION"
```

Inspect the created resource and defaults. Then configure the required subnets, gateways, routes, NSGs, and DNS; do not automatically create every gateway. For updates, inspect existing rule collections and preserve unrelated entries. Delete dependencies in reverse order after checking shared use; a route table or gateway may serve more than the named workload.

## Diagnose in layers

Record source, destination hostname/IP, protocol/port, and where the test ran. Check DNS → address/endpoint choice → route and return route → NSGs/security lists/ZPR → host firewall → listener/application. Use VCN Flow Logs where available to refine the hypothesis. Don't resolve a timeout by opening all ports or assigning a public IP without evidence and authorization for that design change.

## Sources

- [Networking components and gateway semantics](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm)
- [NSGs and ZPR interactions](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm)
- [Security rule behavior](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm)
- [DNS overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm)
- [Load Balancer overview](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/balanceoverview.htm)
- [VCN create command](https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/create.html)
