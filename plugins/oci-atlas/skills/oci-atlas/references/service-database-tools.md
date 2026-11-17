# Database Tools connections and MCP access

Reviewed: 2026-11-17

## Choose the access service

Database Tools supplies managed connection resources and HTTPS database access. A connection captures access details; a private endpoint supplies the supported network path. Neither provisions the underlying database. Use [Database Management](service-database-management.md) for database monitoring and operational management.

Database Tools MCP Server is a managed gateway for external MCP clients. Its documented Oracle database support includes 19c and 26ai cloud database services, with Streamable HTTP transport, built-in reporting/script tools and custom SQL/PLSQL tools. Check the current support matrix before extending that to other engines. An engine supported by a general Database Tools connection is not automatically supported by every MCP tool.

## Authentication and authorization

Separate OCI permission to manage the connection/server, client OAuth authentication through IAM identity domains, and database privileges exercised by a tool. Private endpoint routing, DNS and secret access remain independent prerequisites. Limit the database account to the intended operations; a natural-language request does not restrict an overprivileged SQL account.

Client ID Metadata Documents (CIMDs) allow supported OAuth clients to identify themselves through an HTTPS metadata-document URL. With that configuration, the user supplies the MCP server URL without a separately entered client ID. This does not remove sign-in, token validation or database authorization.

## Working pattern

1. In **Database Tools**, identify the target engine/version, connection, credential reference and private endpoint. Reuse a suitable existing connection.
2. Verify a bounded query using the intended database identity and network path before adding an AI client.
3. Configure the MCP server, identity-domain client access and selected tools through the documented flow. Record the actual server URL and supported transport.
4. Test an allowed read and a deliberately out-of-scope request. Add write-capable tools only when the application requires and authorizes their effects.
5. Enable service logs where required; correlate client failures with server operations while protecting SQL and result data.

## Lifecycle and distinctions

Rotate connection credentials with their consumers. Before deleting a server, connection or endpoint, inventory dependent clients and shared resources. Budget the database, networking, logs and any model inference separately from the access layer.

[Autonomous AI Database built-in A2A/MCP tools](service-autonomous-database.md) use a separate configuration path. OCI Atlas documents these services; installing Atlas creates no MCP server, connection or database grant.

## Sources

- [Database Tools overview](https://docs.oracle.com/en-us/iaas/database-tools/doc/overview.html)
- [Database Tools MCP server support and authentication](https://docs.oracle.com/en-us/iaas/database-tools/doc/overview-mcp-server.html)
- [CIMD client access](https://docs.oracle.com/en-us/iaas/releasenotes/database-tools/cimd.htm)
- [MCP service logs](https://docs.oracle.com/en-us/iaas/releasenotes/database-tools/logging.htm)
