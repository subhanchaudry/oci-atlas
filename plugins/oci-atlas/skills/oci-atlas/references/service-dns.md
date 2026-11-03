# DNS zones, views, and private resolution

Reviewed: 2026-11-03

## Model resolution separately from routing

A zone holds records, a private view groups zones, and a VCN resolver uses associated views and forwarding rules. Listening and forwarding endpoints enable supported cross-network DNS paths. Network peering alone does not make another network's private names resolve.

Resolve the application's FQDN, intended public/private answer, querying runtime, resolver and zone owner. A public certificate or reachable IP does not establish correct private name resolution.

## Configure the intended path

1. Query from the actual caller's resolver context and record the returned address and TTL.
2. Inspect the zone/view association and any protected service-managed zones. Do not replace service-managed records to hide a routing failure.
3. For hybrid forwarding, identify the authoritative side, forwarding suffix, endpoint subnet and security rules. Avoid forwarding loops and overlapping zones with unintended precedence.
4. Permit the documented DNS traffic and resolve from each relevant source network.
5. Check the subsequent application connection and TLS hostname. Correct DNS can still lead to a blocked route or wrong listener.

## Change and recovery

Plan TTL and caches before an endpoint cutover; a record update is not immediate convergence for every client. Preserve previous records and forwarding configuration for rollback. Resolve split-horizon behavior deliberately when the same name has public and private answers. Private DNS does not inherit public DNS Traffic Management features.

Before removing a zone, view or endpoint, enumerate dependent applications and forwarding rules. Endpoint network resources and public DNS/traffic services have their own cost/retention behavior; inspect current terms. Use [hybrid access](recipe-hybrid-private-access.md) and [connectivity diagnosis](troubleshoot-connectivity.md) for routes and application checks.

## Sources

- [Private DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm)
- [DNS overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm)
