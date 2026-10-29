# File Storage with Lustre for parallel workloads

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Choose by I/O behavior

File Storage with Lustre is a managed parallel-filesystem service for supported AI/ML and HPC workloads. Evaluate it when shared parallel data access matches the application's I/O requirements. Ordinary File Storage offers a different NFS access model, Block Volume an attached device model, and Object Storage object semantics.

Capture file counts/sizes, metadata intensity, aggregate throughput, concurrency, capacity, checkpoint behavior and retention. Don't choose Lustre solely because a machine has a GPU, or claim that a new filesystem automatically fixes a slow data loader. Compare the actual workload and supported service configuration.

## Resource relationships and prerequisites

The managed service runs the Lustre server components; customer clients still need compatible Lustre client software and the documented mount/network configuration. A Linux NFS mount command is not a substitute for a supported Lustre client. Check client OS/kernel compatibility and installed packages before changing a production compute image.

Resolve filesystem, selected placement/network, capacity/performance configuration, encryption/key dependencies and client identities. OCI IAM controls management; client access and file permissions are different layers. Inspect root-squash and application UID/GID behavior rather than broadening every directory's permissions to fix a mount or ownership problem.

## Working sequence

Use Console **File Storage with Lustre** and its current API/CLI documentation. Inspect exact supported shapes/regions and service limits at task time. Read existing cluster/scheduler and IaC ownership before introducing another shared filesystem.

1. Define the dataset/checkpoint path and workload requirements. Identify the authoritative source and which data must survive compute replacement.
2. Verify compatible clients, kernel/software installation workflow and required service network rules.
3. Configure the requested filesystem with the intended capacity, placement and encryption. Observe lifecycle and actual connection details.
4. Mount through the supported client instructions from a selected worker. Verify the mounted source and a bounded file operation under the application identity.
5. Check representative concurrent access and application data-loading/checkpoint behavior. Record observed results only when actually exercised; do not present advertised throughput as measured performance.
6. Integrate mounts and permissions into the owning image/bootstrap/scheduler process so future workers use the same intended path.

## Change and diagnosis

For a failed mount, inspect client compatibility, advertised filesystem endpoint, routes and security before changing file permissions. For access denied after mounting, inspect root-squash and UID/GID/mode behavior. For poor throughput, separate metadata-heavy access, client concurrency, storage configuration and application preprocessing.

Inspect the service's current scaling and maintenance behavior before scheduling a capacity change. Shared clients can remain dependent on the filesystem after a training run ends. Do not assume node shutdown removes a managed filesystem or stops its storage charges.

Define the protection/export/recovery approach from the selected service's documented capabilities and the application's data contract. Do not transfer NFS snapshot/replication claims to Lustre without verification. Before cleanup, quiesce relevant writers, identify active mounts and preserve requested datasets/checkpoints. Use [GPU/HPC](service-gpu-hpc.md) for cluster execution and [File Storage](service-file-storage.md) when NFS fits the workload better.

## Sources

- [Managed Lustre architecture and service features](https://docs.oracle.com/en-us/iaas/Content/lustre/overview.htm)
- [Supported clients and filesystem mounting](https://docs.oracle.com/en-us/iaas/Content/lustre/file-system-connect.htm)
- [Capacity, encryption, maintenance, and root-squash tasks](https://docs.oracle.com/en-us/iaas/Content/lustre/home.htm)
