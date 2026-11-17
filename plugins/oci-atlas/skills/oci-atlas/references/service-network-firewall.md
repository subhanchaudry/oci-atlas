# Network Firewall inspection paths and policies

Reviewed: 2026-11-17

## Choose the control by traffic

Network Firewall provides managed network inspection and intrusion-detection/prevention capabilities for supported OCI network paths. WAF handles web application enforcement, NSGs/security lists permit flows at their resource boundaries, and ZPR adds attribute-based packet authorization. Choose the layer that addresses the actual requirement; these controls do not have interchangeable policy languages.

An instantiated firewall inspects only traffic routed through its path. It does not automatically protect every subnet or DRG attachment because it exists in the VCN. Treat traffic steering and inspection policy as separate configuration tasks.

## Resource model and prerequisites

Resolve the firewall resource, subnet/address context, policy and reusable policy components. Rules may reference supported address, service, application or inspection constructs; use the selected service version's schema. If decryption is required, inspect certificate/secret integration, client trust and workload compatibility before proposing it.

Map source → gateway/DRG/subnet route → firewall → destination and the return path. Stateful inspection depends on a coherent path. Routes, NSGs/security lists, ZPR and host controls must also allow the intended flow. Inspect placement/availability and supported features in the customer's region instead of relying on a static capacity table.

## Working sequence

Use Console **Network firewalls** and **Network firewall policies**, or current `oci network-firewall --help`. Identify the owning IaC workflow and shared consumers before editing a policy or route table.

1. Record the precise source/destination, protocol/port, direction and inspection objective. Determine whether traffic currently bypasses the proposed firewall.
2. Read current policy components and rule order. Preserve unrelated rules and understand the relevant default behavior.
3. Configure the requested policy and firewall, observing work-request and lifecycle state. Keep policy creation separate from routing activation.
4. Steer the intended flow through the supported route design, including return traffic and any transit gateways.
5. Enable relevant traffic/threat logs through the normal service interface. Send a bounded allowed request and inspect the resulting path and rule outcome.
6. Verify the application outcome, not only a connection to the firewall or a successful policy update.

## Diagnose and change

For a timeout, inspect route selection and return routing before changing a deny rule. For missing logs, inspect logging enablement and whether the actual flow traverses this firewall. For an inspected TLS failure, distinguish certificate trust, protocol support and application behavior from ordinary reachability.

Explain whether a proposed decryption, NAT or route change alters addresses or trust seen by downstream systems. Don't paste a sample default route into shared tables without resolving its scope. When rolling back or removing a firewall, update traffic steering through an explicit supported path first; deleting a routed next hop can interrupt unrelated workloads. Preserve shared policies and [Certificates](service-certificates.md)/secret dependencies unless their removal is requested. Use [hybrid connectivity](service-hybrid-connectivity.md) for provider/VPN and DRG coordination.

## Inspection handoff

Record forward and return routing, firewall policy revision, required application destinations and TLS inspection boundaries. Confirm certificate trust and data handling before decrypting traffic. Include firewall capacity, logs and any redundant path in the estimate. Rollback must restore a coherent route and policy pair, not only remove the firewall.

## Capture traffic at the firewall

Network Firewall can be a VTAP source for packets on its attached VNICs. Use a scoped capture filter and authorized destination to investigate the selected flow. Captured encrypted traffic remains encrypted: packet capture is not TLS decryption. Correlate timestamps, translated addresses and both directions with firewall logs and [routing](service-vcn-routing.md) before changing policy. Captures can contain sensitive traffic; limit retention and access to the diagnostic purpose.

## Sources

- [Inspection capabilities and routed architectures](https://docs.oracle.com/en-us/iaas/Content/network-firewall/overview.htm)
- [Policy components, logging, decryption, and lifecycle](https://docs.oracle.com/en-us/iaas/Content/network-firewall/home.htm)
- [DRG routing model](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm)
- [Security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm)
- [Network Firewall VTAP source](https://docs.oracle.com/en-us/iaas/releasenotes/network-firewall/network-firewall-as-vtap-source.htm)
