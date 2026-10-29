# Diagnose private and application connectivity

Reviewed: 2026-10-29 · Basis: documentation review; no network probes or changes.

## Define the failing flow

Record caller/runtime location, destination hostname and resolved address, protocol/port, endpoint mode, time and error. A laptop, Cloud Shell, Function, OKE pod and Data Platform workspace have different paths. A successful test in one location doesn't establish access from another.

| Symptom | Check first | Avoid assuming |
| --- | --- | --- |
| Unknown hostname | Caller resolver, private zone/view and forwarding | A route or peering link supplies DNS automatically |
| Unexpected public/private address | Actual descriptor/endpoint and resolver context | Current Console region selects every application endpoint |
| TCP timeout | Forward/return routes, NSG/security-list/ZPR, endpoint and host firewall | Opening all ports is a justified fix |
| Connection refused | Listener/service state and advertised port | IAM is the primary cause |
| TLS/certificate failure | Hostname, trust, driver/version, TLS/mTLS and wallet | Downloading another wallet fixes routing |
| SQL login/query failure after connection | DB user, credential validity and grants/schema | OCI resource management access grants SQL rights |
| Gateway reaches no healthy backend | Gateway/LB network path, health check and backend state | The backend works because the VM is RUNNING |

These are diagnostic branches; use the actual error and evidence to narrow them.

## Work the path

1. Resolve the hostname from the actual runtime using available supported tools. Record which IP family/address it selects.
2. Read source subnet/endpoint routes and the return path, including DRG tables/distributions where relevant.
3. Review effective security rules, ZPR where used, and host-level controls.
4. Verify the listener and current service endpoint configuration, then TLS and application authentication.
5. Correlate service/application logs or VCN Flow Logs where available. Report unobserved layers as hypotheses, not established causes.

For Autonomous Database, use its actual connection details. For an external catalog, check the workspace network plus source credentials and catalog permissions. Do not convert a private database to public access or change database workload type just to bypass investigation.

## Correct and verify

Modify the smallest justified configuration while preserving shared rules. Retest the original flow, then verify the requested application behavior. If access can't be tested from the caller's location, state that limit and specify the remaining check. Keep a record of changed routing/security objects so a later cleanup doesn't remove shared connectivity.

## Service-specific branches

For on-premises callers, follow [hybrid routing and DNS](service-hybrid-connectivity.md): tunnel/virtual-circuit status, DRG imports/exports, forward/return advertisements, and resolver forwarding are distinct. Use the [hybrid recipe](recipe-hybrid-private-access.md) to keep the source runtime explicit.

For recent attribute changes, inspect [ZPR](service-zpr.md) and applicable network rules; for inspected flows, check [Network Firewall](service-network-firewall.md) routing symmetry and policy. For a web denial inspect [WAF](service-waf.md) logs; for unhealthy backends inspect [load-balancer health](service-load-balancing.md). Preserve TLS hostname/trust in [Bastion](service-bastion.md) tunnels and follow the chosen [database engine](databases-data.md) rather than assuming every private database uses an Autonomous wallet.

## Report the diagnosis

Separate **observed evidence**, **plausible causes**, **the next discriminating check**, and **a correction supported by the result**. Use a short paragraph or table according to the task. Do not present an unperformed check as evidence or make a change merely to complete the pattern.

For a hypothetical timeout: “The only observation supplied is a timeout from the job runtime; the cause remains unconfirmed. Check hostname resolution there first. If it selects the intended private address, inspect forward/return routing and effective security rules next. Propose a specific rule correction only after identifying the blocked flow.” Keep TLS and SQL authorization separate from transport reachability.

For other failure types, use [access diagnosis](troubleshoot-access.md) or [workload diagnosis](troubleshoot-workloads.md) and the same evidence-first reporting approach.

## Sources

- [OCI network components](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm)
- [Security rules and ZPR](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm)
- [DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm)
- [Autonomous Database private endpoint diagnosis](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/private-endpoints-autonomous.html)
- [Data Platform workspace private-network context](https://docs.oracle.com/en/cloud/paas/ai-data-platform/aidug/workspaces.html)
