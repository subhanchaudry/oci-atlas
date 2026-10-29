# Block Volume attachments, backups, and replication

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Choose storage and protection separately

Use Block Volume for persistent block devices attached through a supported Compute configuration. Boot volumes contain the system disk; block volumes provide separate application storage. Object Storage and File Storage have different access semantics. An OCI volume being attached does not mean the guest has connected, partitioned or mounted it.

Choose protection by recovery objective. A backup is a retained recovery point, a clone serves another copy/use case, and replication maintains a separate destination according to its own behavior. Replication can propagate unwanted changes; it does not replace a retention strategy. Volume durability does not establish application-consistent recovery.

## Resource relationships and prerequisites

Resolve volume, attachment type, availability-domain placement, instance, performance settings, encryption key and data owner. Multi-attach capabilities require a supported access mode and guest/application design; never mount an ordinary filesystem read-write on several hosts merely because attachment is allowed.

Volume groups organize related boot/block volumes for group-level backup, clone and supported replication operations. A point-in-time crash-consistent group is not automatically a database/application-consistent checkpoint. Coordinate the appropriate application quiescing or database-native protection when required.

## Working sequence

Navigate to **Block volumes**, **Boot volumes**, **Volume groups**, and **Backups**. Inspect `oci bv --help` and the exact Compute attachment operation. Read existing Terraform/Resource Manager ownership before modifying a managed disk.

1. Read the actual instance-volume attachment and guest usage before allocating or resizing storage. Resolve required capacity, throughput/IOPS behavior and current shape limits.
2. Create/attach through the supported workflow with the intended placement and key dependencies. Observe lifecycle and attachment state.
3. Connect/mount using the service-provided instructions and operating-system conventions. Validate the intended device and existing data before any formatting operation.
4. For expansion, inspect cloud volume size plus the guest partition, logical-volume and filesystem layers. Cloud resizing alone might not expose usable space.
5. For protection, inspect backup policy/retention, volume-group membership, destination region and replication state. Verify the intended recovery point is usable for the recovery scenario.
6. Restore or activate only within the requested scope, attach to the intended recovery host and verify a bounded application/data outcome.

## Change and cleanup

For poor performance, correlate workload, guest device metrics, volume performance level and instance limits before assuming capacity size is the cause. For an unavailable attachment, separate placement, IAM, key access and guest connection problems.

Record retained backups, replica/destination resources and their cost after instance termination. Before detaching an active disk, coordinate application writes and the guest unmount. Before deletion, identify mounted consumers and retention requirements; an attachment delete and a volume delete are different actions. Use [Compute](service-compute.md) for instance lifecycle and the [recovery recipe](recipe-backup-disaster-recovery.md) for application-wide sequencing.

## Sources

- [Volumes, attachment types, performance, and durability](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm)
- [Volume groups and consistency boundaries](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm)
- [Block and boot volume replication](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
- [Backup and restore task entry points](https://docs.oracle.com/en-us/iaas/Content/Block/home.htm)
