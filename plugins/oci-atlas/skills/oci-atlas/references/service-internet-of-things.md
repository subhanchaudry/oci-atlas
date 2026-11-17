# Internet of Things domains, digital twins, and flows

Reviewed: 2026-11-17

## Choose the device workflow

OCI Internet of Things connects devices and external systems to normalized telemetry and digital twin resources. Use it when device models, adapters and relationships matter. [Streaming](service-streaming.md) transports events and [Queue](service-queue.md) distributes work; neither alone supplies an IoT digital twin model.

## Resource and identity boundaries

A domain group supplies the database-backed environment. An IoT domain contains digital twin models, adapters, instances and relationships, with its own schema/device endpoint. An IoT domain is not an IAM identity domain. Inspect the regional device and data endpoints rather than constructing URLs from display names.

Choose Development or Production when creating the domain group; the type cannot be changed in place. Use current limits for region, domain group and domain. Development is not the default basis for a production availability claim. Models and their versions also consume resource limits.

## Working pattern

1. In **Internet of Things**, inspect the domain group, domain, region, authentication and access controls. Reuse the intended environment.
2. Define the twin model and any adapter needed to normalize device data. Register a bounded test device/instance and send synthetic telemetry.
3. Check accepted, rejected and normalized data. Successful transport does not prove the payload mapped to the intended fields or twin.
4. Use a Flow Runtime for the supported managed Node-RED integration workflow. The November update adds nodes for Queue, Streaming, Functions, Monitoring and Logging; update an existing runtime through the supported software-update procedure before expecting new nodes.
5. Configure each node's service permissions and endpoint. Where needed, an authorized workspace administrator can delegate supported database privileges to a Flow Runtime in the same IoT domain. Verify the grant and retain a revocation path.
6. Test retries and duplicate effects at downstream services, then monitor flow execution and telemetry freshness separately.

## Ownership and cleanup

Record device authentication, schema/model revision, runtime version, downstream owners and retention. Estimate domain-group capacity, runtime consumption, retained telemetry and downstream service use. Before deletion, enumerate twin resources and running flows; do not treat removal of a flow as removal of telemetry or devices. Reconcile active dependents and export only data the user intends to retain.

## Sources

- [IoT resources, endpoints and limits](https://docs.oracle.com/en-us/iaas/Content/internet-of-things/overview.htm)
- [Flow Runtime integrations and privilege delegation](https://docs.oracle.com/en-us/iaas/releasenotes/internet-of-things/update-11102026.htm)
- [Development and Production domain groups](https://docs.oracle.com/en-us/iaas/releasenotes/internet-of-things/update-04142026.htm)
