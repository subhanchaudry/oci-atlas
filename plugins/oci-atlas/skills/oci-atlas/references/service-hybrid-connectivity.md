# Hybrid connectivity with FastConnect, VPN, DRG, and DNS

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Choose the connection and ownership

Site-to-Site VPN connects an on-premises network to OCI using IPSec over an internet path. FastConnect supplies a dedicated connectivity path through the applicable provider or colocation model. Select by traffic, availability, lead time and operating responsibility. A private circuit is not automatically an encrypted application connection; inspect the required encryption design separately.

FastConnect private peering reaches private VCN resources, while public peering serves a different address/service scope. Don't describe public peering as a private-subnet attachment. Resolve who operates the customer router, provider connection, OCI resources, DNS and application endpoints; an OCI API operation cannot configure an external provider's physical circuit.

## Build the route model

The DRG connects supported network attachments and uses its own route tables and route distributions. VCN subnet routing and DRG routing are distinct decisions. VPN adds customer-premises equipment (CPE), an IPSec connection and tunnels; FastConnect introduces the selected virtual-circuit and provider/cross-connect objects. Existing connectivity may be shared by many workloads.

Record both sides' CIDRs, advertised prefixes, next hops, BGP/session configuration where used, and expected return path. Check overlaps before provisioning. A connected circuit or tunnel does not prove that the intended application prefix is advertised, imported, selected and reachable.

## Prerequisites and working sequence

Use Console **FastConnect**, **Site-to-Site VPN**, **Dynamic routing gateways**, and **DNS**. Inspect the selected `oci network` or `oci dns` operation's help. Reuse [VCN routing](service-vcn-routing.md) for shared route/security concepts.

1. Draw source → customer router/provider → VPN or virtual circuit → DRG → target subnet, including return traffic and resolver location.
2. Inspect current attachments and route tables. Identify existing redundancy and which change affects other consumers.
3. Establish the supported provider/VPN configuration and approved prefix advertisements. Check both tunnel/circuit and routing state.
4. Configure required subnet/DRG routes and security controls. For inspected traffic, include the [Network Firewall](service-network-firewall.md) path in both directions.
5. Resolve private names through the correct DNS views, forwarding/listening endpoints and customer resolvers. Peering or BGP does not configure DNS forwarding automatically.
6. Verify a bounded connection from the intended on-premises client, then the actual application authentication and response.

## Availability and diagnosis

Plan independent failure paths according to the provider/location topology; two logical connections can share a physical dependency. Inspect current Oracle redundancy guidance rather than assuming a backup VPN will receive the right routes automatically.

For failure, separate carrier/circuit state, IPSec negotiation, BGP, route selection, security, DNS, MTU and application behavior. A small probe working does not establish large-payload behavior. Before changing advertisements, document affected prefixes and rollback intent. Before cleanup, identify shared DRG attachments and provider commitments; deleting an OCI object does not necessarily cancel a carrier service. Use the [hybrid application recipe](recipe-hybrid-private-access.md) for a cross-team sequence.

## Sources

- [FastConnect peering and connectivity models](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm)
- [Site-to-Site VPN and supported setup paths](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm)
- [DRG attachments, routing, and distributions](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm)
- [Private DNS management](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm)
