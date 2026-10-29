# Compute and storage

Reviewed: 2026-10-29 · Basis: documentation review; examples are not live-tested.

## Select the resource

| Requirement | Start with | Decision to resolve |
| --- | --- | --- |
| OS-level control or a conventional application host | Compute VM | Architecture, image, shape, availability and administration |
| Hardware-specific workloads | Bare metal or a suitable accelerated shape | Capacity, drivers, licensing and network/storage requirements |
| Persistent disk for an instance | Boot Volume / Block Volume | Retention, attachment type, capacity and performance |
| Objects, artifacts, backups or a data lake | Object Storage | Namespace, region, storage tier, access and lifecycle |
| Shared filesystem semantics | File Storage | Mount target, export, NFS access and client identity |

Don't choose an instance from a memorized free-tier allocation or advertised CPU count. Discover available shapes and compatible images in the customer's region. Check Arm versus x86 compatibility for the OS, native libraries, and container images. Explain whether a sizing figure is an OCPU, ECPU, or vCPU in that service's context.

## Resource relationships

A Compute instance combines a shape, image or boot-volume source, primary VNIC/subnet, boot storage, metadata and optional attached volumes. Availability-domain placement and shape/image compatibility must align. Resource creation permission does not automatically grant permission to use another compartment's subnet, image, key, or volume.

Boot volumes hold the OS; block volumes supply additional persistent disks. An attachment and usable guest filesystem are separate concerns. Expansion of a volume may need guest partition/filesystem work. A preserved boot volume can remain after instance termination; deleting an instance is not a universal storage cleanup operation.

Object Storage uses a tenancy namespace, regional buckets, and objects. Bucket location and compartment are independent of a filesystem path; object-name prefixes are not ordinary directories. Fetch the actual namespace instead of deriving it from the tenancy display name. Choose versioning, retention and lifecycle settings before bulk writes or cleanup; they change deletion semantics and storage retention.

File Storage connects a filesystem to clients through a mount target and export configuration. NFS reachability and export/Unix permissions are separate from OCI IAM authorization to manage the filesystem. Don't replace a private NFS design with public exposure to solve a failed mount.

## Working patterns

Use Console search for **Instances**, **Block volumes**, **Buckets**, and **File systems**. CLI families: `oci compute`, `oci bv`, `oci os`, and `oci fs`. Use [the access guide](access-and-tools.md) for context inputs.

Before launching a VM, inspect compatible image/shape choices, subnet reachability, SSH or other access method, boot-volume settings, and relevant limits. Generate and inspect complex CLI input from installed help. After creation, verify lifecycle state and the intended VNIC/volume attachments; application health needs a separate check. For resize or stop/start, inspect the operation's downtime and shape-specific behavior first.

Example — **creates a private bucket**, using a selected namespace and unique bucket name:

```bash
# Set ATLAS_NAMESPACE from the actual tenancy namespace; choose ATLAS_BUCKET_NAME.
oci os bucket create --namespace-name "$ATLAS_NAMESPACE" \
  --compartment-id "$ATLAS_COMPARTMENT_ID" --name "$ATLAS_BUCKET_NAME" \
  --public-access-type NoPublicAccess \
  --profile "$ATLAS_PROFILE" --auth "$ATLAS_AUTH" --region "$ATLAS_REGION"
```

Re-read bucket configuration before uploading. For deletion, establish whether objects, versions, multipart uploads, retention rules, backups, or shared mounts must be retained. Distinguish changing bucket metadata from reading or deleting its objects. Account for storage, retained backups, network traffic, and attached services when discussing cost.

## Sources

- [Instance operations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm)
- [Shape selection](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm)
- [Boot-volume lifecycle](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumes.htm)
- [Block Volume overview](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm)
- [Object Storage resource model](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm)
- [File Storage overview](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/filestorageoverview.htm)
- [Bucket create command](https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/create.html)
