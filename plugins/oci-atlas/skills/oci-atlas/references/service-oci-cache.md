# OCI Cache clusters, users, and application behavior

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Establish the engine and data contract

OCI Cache manages memory-based cache clusters. Identify the selected supported engine/version, topology and client features; older customer terminology or examples may say Redis while current product documentation also covers Valkey. Do not assume every Redis-compatible command, module or persistence behavior is available in every configuration.

Define whether the application uses the cache for derived values, sessions, coordination or another supported pattern. Identify the authoritative data source, acceptable eviction/expiry and rebuild behavior. A cache is not automatically an approved durable database, and storing a value successfully does not establish a backup or recovery guarantee.

## Resource relationships and access

Resolve the cluster, nodes/shards, endpoint, configuration, users and ACL/authentication model. Cluster management IAM is separate from an application's authenticated data connection and allowed commands/keys. Supported IAM authentication and cache-user access need the correct client/session handling; don't substitute a broad OCI administrator policy for a missing data-plane credential or ACL.

Client network placement, TLS and engine authentication are separate prerequisites. Use actual connection details and supported client capabilities. Sharded/clustered modes can require client topology discovery; a standalone client that connects to one endpoint might still fail when following redirects or accessing other shards.

## Working sequence

Use Console **OCI Cache** and the current Cache developer/CLI reference. Legacy OCI API/CLI naming can differ from the display name, so discover the installed interface instead of guessing a root command.

1. Inspect the existing cluster, engine/version, configuration, endpoints and application consumers. Resolve management ownership and current limits.
2. Choose capacity/topology from measured data size, access patterns and expected growth. Define expiration, key naming and recovery assumptions before bulk loading.
3. Configure the supported user/authentication/ACL path and required network access with scoped application permissions.
4. Connect from the real runtime using the advertised TLS/endpoint settings. Perform a bounded synthetic set/get/expiry operation only when that write is requested.
5. Observe memory pressure, eviction, connections, latency and relevant node/shard health. Verify application cache misses and reconnect behavior as well as a successful direct request.
6. For supported replication or a configuration change, inspect current restrictions, synchronization state and consumers before changing endpoints or write ownership.

## Diagnose and maintain

Timeout → check DNS/routes/security from the application. Authentication/ACL error → inspect the actual cache user, credential/session and command/key permission. Redirect/topology errors → inspect client cluster support and reachability of advertised nodes. Repeated misses → inspect TTL, eviction, key construction and whether the application targets the expected cluster.

Plan resizing/maintenance around supported availability and client reconnect behavior; do not promise zero application impact. Never use a broad flush to diagnose a single key without explicit scope. Before deletion, enumerate session/coordination dependencies and the intended data rebuild path. Report retained replicas/resources. See [NoSQL](service-nosql.md) and [database selection](service-selection.md) when the data contract requires persistent managed records.

## Sources

- [OCI Cache engine and cluster overview](https://docs.oracle.com/en-us/iaas/Content/ocicache/overview.htm)
- [Cache users and access control](https://docs.oracle.com/en-us/iaas/Content/ocicache/cache-users.htm)
- [Authentication, sharding, configuration, and replication entry points](https://docs.oracle.com/en-us/iaas/Content/ocicache/home.htm)
