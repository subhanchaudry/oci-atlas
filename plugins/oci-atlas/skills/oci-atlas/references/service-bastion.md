# Bastion sessions and private administration

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Choose a session for the actual target

Bastion provides restricted, time-limited access to resources without public endpoints. Use it for an administrative session when supported target/network requirements fit. It is not a general replacement for persistent application connectivity through VPN or FastConnect.

Choose the documented session type. Managed SSH has target OS, SSH server, Oracle Cloud Agent and Bastion plugin prerequisites. Port forwarding tunnels a supported TCP service and has different target requirements. Check current dynamic-port-forwarding support when that mode is needed. A Bastion session does not itself grant an operating-system login or database SQL privileges.

## Resource and access model

A bastion has a selected VCN/subnet context and client CIDR allowlist. Sessions identify their target, type, public key and lifetime. Keep the private key on the authorized client. Session access depends on both OCI authorization and the actual client/network/target configuration.

Distinguish the human's permission to create/use the session, the SSH key that opens the tunnel, and the final operating-system or database authentication. A successful tunnel only establishes one part of the route. Inspect supported target placement rather than assuming any resource in a peered network can be reached through any bastion.

## Prerequisites and working sequence

Navigate to **Bastions** and inspect `oci bastion --help`. Identify the selected compartment, bastion, target address/port, session type, actual client egress address and requested duration. Read existing service-gateway/network and target prerequisites before altering a subnet.

1. Inspect the existing bastion and target configuration. Confirm target state and, for Managed SSH, the required agent/plugin condition.
2. Check the client CIDR allowlist against the address the service will see, including a corporate VPN or proxy path.
3. Establish the appropriate session using the user's public key and scoped target. Keep private keys and account passwords out of parameters recorded in chat.
4. Obtain the service-generated connection command after the session is ready. Use it rather than reconstructing regional session hostnames from memory.
5. Open the tunnel/session from the intended client. For a database, use the actual database connection details and TLS mode through the forwarded path.
6. Verify the requested administrative action independently and close the client connection when finished.

## Diagnosis and lifecycle

For session creation errors, inspect IAM, target placement and required service prerequisites. For a tunnel failure, check session state/expiry, client allowlist, key pairing, target port and network rules. For a login failure after connection, inspect target user/key or SQL authentication. Do not broaden database grants or publicize the target merely because an SSH tunnel failed.

Record the session identifier and expiry without logging secret material. Reconnecting to an expired session requires a supported new session, not a permanent bypass. Deleting a session or bastion does not delete its target, and closing a local terminal is not proof a session resource was removed. Preserve a shared bastion and its unrelated sessions during requested cleanup. See [connectivity troubleshooting](troubleshoot-connectivity.md) for the remaining path.

## Sources

- [Bastion concepts and session types](https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/bastionoverview.htm)
- [Bastion prerequisites and target workflows](https://docs.oracle.com/en-us/iaas/Content/Bastion/home.htm)
- [OCI identity and policy model](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm)
