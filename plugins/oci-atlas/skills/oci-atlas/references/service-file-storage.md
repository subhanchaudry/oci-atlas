# File Storage exports, snapshots, and replication

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Select the shared-file model

File Storage supplies managed shared NFS storage for supported clients. Choose it for shared filesystem access; use Block Volume for an attached block device, Object Storage for object semantics, or evaluate [Lustre](service-lustre.md) for a workload with the corresponding parallel-filesystem requirements. A client seeing the same path string does not prove it mounted the same filesystem.

Plan client placement and the supported access protocol from current service documentation. Private NFS reachability over VCN/hybrid connectivity is separate from authorization to manage the filesystem resource. Don't expose a private filesystem publicly to solve a mount failure.

## Resource relationships and prerequisites

A filesystem stores data; a mount target supplies network access; an export associates a filesystem/path with a mount target's export configuration. Export options, network controls and Unix/user identity determine different parts of client access. OCI IAM management rights do not automatically grant file ownership or a particular UID's access.

Snapshots preserve point-in-time filesystem views. Replication uses a source filesystem, replication configuration, destination target resource and target filesystem. Inspect target eligibility, replication state and unreplicated resource configuration before planning failover. File replication does not automatically recreate every client mount, key association, network policy or application dependency.

## Working sequence

Use Console **File systems** and **Mount targets**, or inspect `oci fs --help`. Identify the filesystem OCID, target/export, region/placement, clients and any IaC owner before creating another mount target.

1. Inspect client routing/DNS and the required mount-target network rules, including host firewall and any ZPR policy.
2. Read the intended export path/options and application user identity. Resolve mount instructions from the actual target rather than guessing addresses.
3. Mount on the selected client through its owning operating-system/container configuration. Verify the mounted source and a bounded authorized file operation.
4. For a permissions failure, distinguish network timeout, NFS export restrictions, root-squash behavior and filesystem UID/GID/mode permissions.
5. Configure requested snapshot/replication protection with explicit retention and destination intent. Observe completed recovery points or replication cycles, not only object creation.
6. For recovery, use the supported clone/restore/failover path and re-establish target-side exports, clients and application checks as required.

## Change, diagnosis, and cleanup

A snapshot consuming little initial storage can retain changed/deleted data later. An active replication resource does not establish that initial transfer finished or that the last recovery point meets the application's RPO. Check the observed lag and target state. Consult current limitations before exporting or changing a target filesystem involved in replication.

For poor performance, inspect client behavior, placement, metadata/throughput characteristics and application concurrency before substituting a different storage service. For stale mounts, identify the active server/export and client state before recreating data resources.

Before deleting an export, mount target, snapshot or filesystem, enumerate clients, shared exports and recovery consumers. Unmount and quiesce through the application owner's workflow. Report retained snapshots, replicas and data explicitly. Use the [backup/recovery recipe](recipe-backup-disaster-recovery.md) for application consistency and recovery ordering.

## Sources

- [File Storage objects and access layers](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/filestorageoverview.htm)
- [Snapshot lifecycle](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingsnapshots.htm)
- [Replication concepts and target requirements](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/FSreplication.htm)
- [Creating replication and initial transfer](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/fsreplication-creating-a-replication.htm)
