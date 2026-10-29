# Compute instances and persistent disks

Reviewed: 2026-10-29 · Basis: documentation review; no live launches or resizes.

## Resolve the launch inputs

Choose CPU architecture, compatible image, available shape and capacity, placement, subnet, access method and boot storage. A shape advertised in a region can still lack capacity in the selected placement. An Arm image/container and an x86-only native dependency are not interchangeable. Look up current OCPU/vCPU interpretation instead of treating a CPU label as a universal unit.

Inspect who owns the instance's configuration before changing it. An instance in an existing Terraform stack should normally be updated through that stack. IAM access to launch an instance doesn't guarantee access to a cross-compartment image, subnet or customer-managed encryption key.

## Launch and observe

1. Inspect the image/shape pairing and intended networking and disk settings.
2. Generate request input from the installed `oci compute instance launch --help`/supported JSON-generation option, or use the owning IaC plan. Fill required fields from actual discovery.
3. Launch once within the request's scope and record the instance/request identifiers. After a timeout, reconcile the resource state before retrying.
4. Read lifecycle, VNIC and storage attachment state. Then check the guest access path and application readiness separately.

For metadata/cloud-init, keep secrets outside configuration captured in source, logs or an image. Confirm guest initialization actually finished instead of assuming that a RUNNING instance has the application installed.

## Configurations, pools, and autoscaling

An **instance configuration** is a launch template; it does not copy an existing instance's installed files or attached-volume contents. Capture the image and bootstrap process deliberately. An **instance pool** uses a configuration, placement rules, and a target size to manage a group. Pool placement can override configuration placement; verify the resulting compartment, subnet, and availability domains. A new configuration affects newly created instances; rotating existing members is a separate operation.

Use Console search for **Instance configurations**, **Instance pools**, and **Autoscaling configurations**. Inspect `oci compute-management --help` and `oci autoscaling --help` for the installed schemas. For a fleet change:

1. Identify the owning stack, image revision, startup process, and external data stores.
2. Check configuration/pool eligibility and capacity in each placement. Create or select the launch configuration, then set the intended pool size and backend association.
3. Observe instance creation, bootstrap, and [load-balancer health](service-load-balancing.md). A reached pool size does not establish application readiness.
4. Add a supported metric-based or schedule-based autoscaling policy only when requested. Resolve minimum/maximum capacity, cooldown behavior, metric emission, schedule time zone, and scale-in effects.
5. Rotate deliberately: drain requests, preserve necessary state, replace within the availability budget, and reconcile the owning configuration.

Scaling in terminates instances. Keep durable data outside disposable workers and understand shutdown/draining behavior before enabling automatic removal. A policy that requests more workers cannot manufacture capacity. Capacity reservations allocate capacity for specified placements/configurations; inspect actual allocated counts because a request may be partially fulfilled. Service limits and compartment quotas still apply, and unused reserved capacity can be billed. Reservations are distinct from a limit increase or a discounted-price commitment.

Assign ownership for image updates, [OS patching](service-os-management-hub.md), secrets, pool changes, capacity, and application health. For tightly coupled accelerated fleets, use the [GPU/HPC guide](service-gpu-hpc.md) rather than assuming a general-purpose instance pool supplies RDMA connectivity.

## Update, stop, and remove

Before resizing, check supported transitions, downtime, architecture and networking implications. A stop/start or reboot is operationally different from replacing the image or boot volume. For disk expansion, account for both cloud volume size and guest partition/filesystem size. A volume attachment is not necessarily a mounted, usable filesystem.

Before termination, identify boot-volume preservation, separate block volumes, backups, addresses and application data. “Delete the VM” should not silently erase retained data, or claim that retained disks stopped costing money. Return the remaining resources with their retention intent.

## Typical failure branches

Insufficient capacity → inspect alternative approved placements/shapes, not policy grants. Failed SSH → inspect user/key, route, security and guest state. Application fails after an image change → inspect architecture/runtime and cloud-init logs. Disk still full after expansion → inspect guest layout before adding another disk.

## Sources

- [Instance operations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm)
- [Shapes and compatibility](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm)
- [Boot-volume lifecycle](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumes.htm)
- [Block Volume and attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm)
- [Instance configuration inputs and limitations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm)
- [Instance pools and placement](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstancepool.htm)
- [Autoscaling policies and lifecycle](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm)
- [Capacity reservations and allocated capacity](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm)
