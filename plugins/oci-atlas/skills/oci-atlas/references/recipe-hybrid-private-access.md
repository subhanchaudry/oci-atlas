# Recipe: on-premises access to private OCI applications

Reviewed: 2026-10-29 · Basis: documentation-based suggested pattern; no live network changes.

## Define the application flow

Connect a selected on-premises caller to a private OCI application or database while preserving existing network ownership. Resolve source location/CIDR, target service/FQDN, protocol/port, expected traffic, availability needs and the teams operating customer routers, providers, OCI networking and DNS.

Start from existing suitable VPN/FastConnect connectivity. A new application does not automatically need another circuit, DRG or VCN. Distinguish permanent application access from a bounded administrative [Bastion](service-bastion.md) session. A browser sign-in or a successful laptop query is not evidence of access from an on-premises job runtime.

## Suggested sequence

1. **Map addresses and ownership.** Read the customer's actual VCN, subnets, DRG attachments, connection objects and routing configuration. Check overlapping ranges and current IaC/provider ownership before proposing changes.
2. **Select the connection.** Use [hybrid connectivity](service-hybrid-connectivity.md) to choose supported VPN or FastConnect private-peering behavior. Resolve provider handoffs, routing method and required encryption separately.
3. **Establish forward and return routes.** Identify customer advertisements, DRG import/export and route tables, target-subnet routes and any inspection path. An up tunnel or circuit proves neither prefix reachability nor a working return path.
4. **Resolve private naming.** Identify the source resolver and the OCI DNS zone/view and forwarding/listening path. Configure the intended resolution through the owning teams; don't replace a hostname with a transient IP to hide an unresolved DNS design.
5. **Permit the intended flow.** Inspect NSGs/security lists, ZPR where used, host controls and any routed Network Firewall. Preserve shared rules and narrow changes to the requested endpoints/protocol.
6. **Verify the transport and application.** From the actual caller context, resolve the expected address and establish a bounded connection. Then verify TLS and application/SQL authentication with the intended identity. Treat each result as evidence of its own layer.

## Availability and diagnosis

Map redundancy to the real failure domains: customer equipment, provider, physical location, tunnel/circuit and OCI attachments. Don't assume two logical connections are independent. When transition/failover behavior needs verification, coordinate an authorized bounded exercise and observe actual route selection; a design document alone does not establish availability.

For failure, capture timestamp, caller, hostname/resolved address and sanitized error. Work from connection state to routing, security, DNS/TLS and the application as the evidence indicates. A small packet working does not prove large requests or sustained sessions behave correctly. Use [connectivity troubleshooting](troubleshoot-connectivity.md) to avoid changing the database engine or exposing a private service to bypass a network issue.

## Change record and cleanup

Report the exact connection/attachment/route/security objects inspected or changed and the actual client-side result. Identify external-team work separately from completed OCI operations. Removing a temporary route or session is different from canceling a shared provider circuit. Before cleanup, enumerate other users of the DRG, resolver endpoints and connection, and preserve the requested long-lived application access.

## Sources

- [FastConnect connectivity and peering models](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm)
- [Site-to-Site VPN setup paths](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm)
- [DRG routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm)
- [Private DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm)
