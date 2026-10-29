# VCN routing, network controls, and DNS

Reviewed: 2026-10-29 · Basis: documentation review; no live network changes.

## Describe one flow

Represent a connection as caller → DNS answer → source interface/subnet → route/next hop → destination → return path. Record protocol and destination port. This makes network diagnosis more precise than asking whether two resources are “in OCI.”

Use a regional subnet when it fits the workload. Check non-overlapping CIDRs against peered and on-premises networks, not just other subnets in the VCN. A private subnet, private service endpoint and private DNS name are separate objects/choices.

## Select the gateway

| Destination | Candidate path | What still needs configuration |
| --- | --- | --- |
| Inbound/outbound public internet | Internet gateway with suitable endpoint addressing | Routes, security rules, listener and return path |
| Outbound internet from private hosts | NAT gateway | Egress route and permitted destination |
| Supported regional Oracle services | Service gateway | Correct service destination and endpoint support |
| On-premises or transit VCN | DRG with appropriate attachments | VCN routes, DRG route tables/distributions, remote routes and DNS |

A DRG attachment selects its own DRG route table for traffic entering the DRG. VCN and DRG routing both matter; a transit design can fail even when each attachment exists. Don't equate an established VPN tunnel with application reachability.

## Effective security and name resolution

Review applicable security lists and NSGs together; they are not ordered deny rules. Check stateful/stateless handling, host firewall and any ZPR policy/attributes. Narrow application-specific NSGs are often easier to reason about than subnet-wide openings, but an NSG only helps if the relevant service/interface actually belongs to it.

Private DNS must answer from the caller's resolver context. Establish resolver endpoints/forwarding and resolution scope in hybrid designs. A route to an IP does not make the hostname resolve. Inspect the resolved address before changing a network rule.

## Operate without replacing unrelated configuration

Navigate through **Virtual cloud networks**, the subnet details, route table, NSGs and DNS. Inspect `oci network ... --help` or `oci dns ... --help` for the selected object. Read existing rule arrays before replacing them in an update. Route and security objects can be shared by other workloads.

For a change, capture the previous intended configuration, modify the smallest relevant object, and retest from the actual source. For cleanup, inspect VNICs, private endpoints and gateway references before deletion. See [connectivity diagnosis](troubleshoot-connectivity.md) for symptom-based checks.

## Sources

- [Networking components](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm)
- [DRG attachments and route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm)
- [Security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm)
- [DNS overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm)
