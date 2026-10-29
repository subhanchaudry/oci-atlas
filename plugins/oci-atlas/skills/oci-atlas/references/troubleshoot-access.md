# Diagnose authentication, authorization, and limits

Reviewed: 2026-10-29 · Basis: documentation review; no credential or policy changes.

## Capture a minimal incident record

Operation/interface, sanitized error/code, timestamp, request ID, actual caller identity, tenancy, region, resource OCID and compartment. Identify whether the failure came from local CLI, browser, managed workload, gateway or application SQL client. Keep tokens/keys and whole credential files out of the record.

| Signal | Starting hypothesis | Next check |
| --- | --- | --- |
| `NotAuthenticated` | Missing/invalid authentication material | Actual auth mode, selected profile, session validity, signing/client clock |
| `NotAuthorizedOrNotFound` | Missing resource or insufficient visibility | OCID, region, actual caller, service policy and dependent-resource scope |
| `RelatedResourceNotAuthorizedOrNotFound` | A referenced dependency is missing/inaccessible | Subnet/image/key and their compartments, not only the primary object |
| `NotAllowed` for a region-sensitive IAM operation | Operation directed at the wrong region | Home-region requirements for that operation |
| `LimitExceeded` | Oracle-defined limit | Correct service/resource scope and available limit |
| `QuotaExceeded` | Administrator-defined compartment quota | Applicable quota policy and compartment hierarchy |
| Capacity error | Placement/shape capacity | Available approved alternatives; raising IAM rights doesn't create capacity |
| Throttling/transient service failure | Rate or transient condition | Current service retry guidance, bounded backoff, request outcome |

An HTTP status alone is not a root cause. Some services wrap errors or have additional service-specific codes; inspect their owning error contract.

## Diagnose in order

1. Check that the intended identity is selected. Browser and CLI can be different; a managed job/function can use another principal.
2. Validate only the authentication mechanism actually in use. An expired session should lead to reauthentication, not silent fallback to another user's key.
3. Verify target/region and relevant visibility. Empty Resource Search results do not prove absence.
4. Inspect exact operation permissions, attachment/target scope and recent propagation. For workloads, inspect membership or workload-identity conditions.
5. Separately inspect the managed product's own object permissions and any data-system login/grants. OCI IAM cannot replace database SQL authorization or Data Platform object access.

## Apply a bounded correction

Explain the identified failing layer and proposed correction. Carry forward the customer's existing task authorization, but don't use a local error as permission for a tenancy-wide policy grant. After a correction, retry the narrow original operation and report its result. For a timed-out write, first reconcile resource/work-request state; avoid duplicate creation.

## Sources

- [OCI common API errors](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm)
- [Session-token authentication](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clitoken.htm)
- [IAM policy syntax](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policysyntax.htm)
- [Compartment quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas.htm)
- [Request IDs, retries and concurrency](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/usingapi.htm)
