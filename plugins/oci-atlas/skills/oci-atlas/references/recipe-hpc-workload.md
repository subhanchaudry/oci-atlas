# Recipe: Run an HPC or GPU job with recoverable data

Reviewed: 2026-11-17

## Outcome and inputs

Stage data, schedule accelerated jobs, preserve checkpoints, and release capacity.

**Inputs:** Application/MPI/CUDA requirements, image/driver versions, placement/fabric, scheduler, data sizes/I/O pattern, checkpoint interval and capacity budget.

**Flow:** Authoritative dataset → staged shared/local storage → scheduler → compatible workers → checkpoint/output store.

## Starting architecture

Choose supported shapes/fabric for the workload; ordinary multi-node Compute does not imply RDMA. Select Object Storage, Block Volume, NFS or Lustre by access semantics. Confirm current capacity before committing to a completion date.

## Implementation sequence

Pin the compatible software stack. Establish private administration, image access and dataset permissions. Stage a bounded dataset, submit a small job and inspect worker communication and output. Integrate storage mounts and identity into worker bootstrap so replacements reproduce the same environment.

Before changing resources, establish the selected identity, region, compartment and existing configuration owner. Provision dependencies before consumers, then observe resource state and the application result separately.

## Configure the first recoverable job

1. Select one representative job with known input, expected output and a restartable checkpoint. Confirm image, accelerator driver/runtime, scheduler and fabric compatibility before requesting capacity.
2. Stage inputs into the appropriate storage tier using [GPU/HPC](service-gpu-hpc.md), [File Storage](service-file-storage.md) or [Lustre](service-lustre.md). Define which storage is scratch and which survives worker removal.
3. Give scheduler and worker identities only their required dataset, image and secret access. Restrict administration and worker communication to the chosen private topology.
4. Run the smallest useful job, inspect resource utilization and output correctness, then stop and resume from a durable checkpoint. A written checkpoint is useful only if the intended replacement environment can read it.
5. Scale only after confirming regional capacity, quotas and the scheduler's failure behavior. Record worker/job ownership and cancel or drain jobs before removing worker resources.

Optional production choices include reservations, placement/RDMA topology, autoscaling and hierarchical storage staging. Do not promise shape availability or performance from an architecture diagram; check the current capacity path and representative job behavior.

## Application checks

Inspect application output correctness, checkpoint readability and scheduler completion independently. Report throughput only from the selected workload and configuration.

## Updates, recovery, and cleanup

Record job IDs, environment, inputs and checkpoints. Resume only from an application-compatible checkpoint. Release idle workers and reservations within scope while preserving authoritative data and completed checkpoints. Shared filesystems can remain billed after worker termination.

Use [cost management](service-cost-management.md) to record runtime, retained storage, traffic and shared-service costs. Use [workload selection](workload-selection.md) for alternatives and [support handoff](troubleshoot-support-handoff.md) for unresolved service boundaries.

## Validate health before job admission

Use [Cluster Health Checks](service-gpu-hpc.md) to separate passive node signals from active GPU/interconnect tests. Run active diagnostics in an appropriate job window and preserve checkpoints before repair. Record the tested nodes and workload conditions; diagnostic success alone does not validate training quality or sustained scaling.

## Sources

- [HPC reference architecture](https://docs.oracle.com/en/solutions/deploy-hpc-on-oci/)
- [GPU cluster architecture](https://docs.oracle.com/en/solutions/hpc-bare-metal-gpu-cluster/index.html)
- [Compute shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm)
- [GPU Cluster Health Checks](https://docs.oracle.com/en-us/iaas/releasenotes/compute/cluster-health-checks.htm)
