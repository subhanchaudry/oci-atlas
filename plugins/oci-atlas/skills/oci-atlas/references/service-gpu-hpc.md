# GPU and HPC capacity, cluster networking, and storage

Reviewed: 2026-11-17

## Select the execution requirement

Start with training/inference/simulation behavior, accelerator memory, parallelism, runtime compatibility, data movement and checkpoint needs. A hosted model API or managed Data Science deployment can meet a request without a customer-operated GPU server. Select custom infrastructure when the required model, runtime, control or scale justifies its operating responsibility.

Resolve shape and image compatibility from current documentation and discovered capacity. A service-limit increase is not a hardware reservation. GPU generation, RDMA support, placement and available image/drivers cannot be inferred from a generic “GPU” label. Do not package a permanent regional capacity or price table.

## Cluster and network models

A single Compute node, a cluster network backed by an instance pool, and a compute cluster are different resource models. Cluster networks manage compatible grouped instances through the pool; compute clusters provide a supported RDMA grouping with individual instance management. Inspect the exact supported shapes and placement model before mixing nodes.

The application/control/storage VCN paths and the supported RDMA fabric have different purposes. Ordinary VCN peering or opening a subnet port does not create a supported accelerator interconnect. Likewise, an existing RDMA group does not establish access to datasets, package repositories, secrets or application clients.

## Prerequisites and working sequence

Use Console **Instances**, **Cluster networks**, **Compute clusters**, and the relevant capacity views. Inspect `oci compute`/`oci compute-management` help for the actual resource. Keep scheduler/OKE/IaC ownership explicit before changing group members.

1. Resolve code/model revision, CPU architecture, GPU memory needs, driver/runtime/collective-library compatibility and the intended node count.
2. Verify current shape/placement support, service limits, capacity arrangement and image requirements before requesting a large deployment.
3. Choose storage by access pattern: Object Storage for durable datasets/artifacts, appropriate attached devices for supported local work, File Storage for shared NFS, or [Lustre](service-lustre.md) for its parallel-filesystem workload fit.
4. Provision through the chosen owning workflow and inspect node/cluster lifecycle plus guest accelerator/driver visibility.
5. Verify bounded runtime, inter-node communication where required, dataset access and checkpoint output before submitting the requested full workload.
6. Observe GPU/host utilization, application progress, communication and data-loading behavior separately. Provisioned GPU count is not evidence of useful workload throughput.

## Diagnose and retain the right state

For launch failure, distinguish IAM/quota, unsupported placement and actual capacity. For poor scaling, inspect collective/network behavior, data pipeline, CPU preprocessing, runtime and workload distribution before adding nodes. A GPU out-of-memory failure and host memory exhaustion require different investigation.

Before resizing or deleting a pool/cluster, identify scheduler jobs, checkpoints, attached/shared storage and node-local data. Preserve requested artifacts in a durable location and account for retained disks/capacity commitments. Do not claim stopping nodes eliminates every charge. Use [Compute](service-compute.md) for pool lifecycle and [Monitoring](service-monitoring-notifications.md) for resource signals alongside application evidence.

## Job and data handoff

Record image/driver versions, scheduler queue, placement, GPU/fabric requirements, dataset path and checkpoint destination. Budget reserved/idle capacity and storage separately from productive job time. Use the [HPC recipe](recipe-hpc-workload.md) for staged inputs, scheduler submission, recovery from checkpoints and worker cleanup.

## Check cluster health before workload scale-up

Cluster Health Checks distinguish passive Oracle Cloud Agent health signals from optional active Slurm/Kubernetes tests. Inspect supported images, agents and GPU configurations first. Active tests exercise GPUs, transfers and inter-node communication; schedule them around running jobs and preserve checkpoints before repair. A diagnostic pass is evidence about the tested cluster, not model quality or sustained application throughput.

For eligible OKE nodes, connect health signals to the configured [GPU repair workflow](service-oke.md). Correlate the node, fault, maintenance event and repair state rather than treating every warning as permission to terminate a node.

## Availability boundary for announced hardware

At the November 17, 2026 review, Google's TPU offering on OCI is announced for 2027 and is excluded from current deployment recommendations. Vera/Rubin has explicit Oracle GA announcement language, but that does not establish a provisionable shape, access path, or regional capacity. Use the current shape and configuration documentation before proposing a deployment; unresolved hardware details stay outside this guide's operating instructions.

## Sources

- [HPC and accelerator infrastructure models](https://docs.oracle.com/en-us/iaas/Content/Compute/References/high-performance-compute.htm)
- [Cluster networks with instance pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm)
- [Compute clusters and individual node management](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/compute-clusters.htm)
- [Current shape and architecture compatibility](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm)
- [GPU Cluster Health Checks](https://docs.oracle.com/en-us/iaas/releasenotes/compute/cluster-health-checks.htm)
- [Future TPU announcement](https://www.oracle.com/news/announcement/ai-world-oracle-brings-google-tpus-to-oracle-cloud-infrastructure-2026-10-27/)
- [Vera/Rubin GA announcement and expansion scope](https://www.oracle.com/news/announcement/ai-world-nvidia-and-oracle-expand-nvidia-vera-rubin-to-multi-gigawatt-scale-2026-10-27/)
