# Object Storage buckets, objects, and retention

Reviewed: 2026-10-29 · Basis: documentation review; no live object operations.

## Establish the exact target

Resolve tenancy namespace, region, bucket and object name/version. The namespace is not safely inferred from a tenancy display name. An object name containing slashes is still an object key; do not assume directory permissions or filesystem rename semantics. Bucket management, object access and encryption-key access can require different permissions.

Choose access, tier, versioning, retention and lifecycle behavior before populating a bucket. Use private access as the starting choice unless the task requires public delivery. A pre-authenticated request or publicly shared link changes who can use it; it is not simply a cosmetic URL.

## Lifecycle distinctions

| Mechanism | Purpose | Consequence to inspect |
| --- | --- | --- |
| Versioning | Preserve object revisions | Deleting the current name may leave old versions and costs |
| Retention rule | Prevent modification/deletion for a required period | Locking has irreversible implications; it is not a routine cleanup option |
| Lifecycle policy | Apply supported age/state-based transitions/deletions | Review what objects and versions the rule matches |
| Replication | Maintain a copy under a configured policy | Check destination ownership and behavior; don't infer a restore procedure |

Do not infer supported combinations of these features; read current documentation before enabling them together. A locked retention rule is materially different from an ordinary editable rule.

## Working sequence

In Console search **Buckets**, then verify compartment and region. Inspect `oci os ns`, `oci os bucket`, and `oci os object` help. First read bucket details and list a bounded prefix. For a requested create, use the private-bucket pattern in [compute/storage](compute-storage.md); for uploads, verify target key, size and overwrite intent before writing.

Validate a transfer with the relevant metadata/checksum and a bounded read when appropriate. A successful bucket creation says nothing about a workload's ability to read objects. For private clients, check service-gateway routing and the actual endpoint along with IAM.

For cleanup, inspect object versions, retained objects, multipart uploads and policies. Do not claim “empty” from one page of current objects. Preserve the difference between deleting a bucket's contents and deleting only a selected prefix/version. Report anything retained by policy rather than bypassing that policy.

## Sources

- [Object Storage model and private access](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm)
- [Object versioning](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning.htm)
- [Retention rules and locking](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules.htm)
- [Bucket creation options](https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/create.html)
