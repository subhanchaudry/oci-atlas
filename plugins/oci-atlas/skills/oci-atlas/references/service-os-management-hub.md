# OS Management Hub registration, sources, and updates

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Establish management scope

OS Management Hub coordinates supported operating-system updates across OCI and supported non-OCI environments. Identify the OS/version, deployment location and current management tool before choosing a workflow. OCI resource ownership and OS package-management ownership are different concerns; avoid introducing two competing patch processes.

Check current supported environments and subscription/entitlement requirements. Oracle Linux software-source workflows and Windows update workflows differ. Do not apply Linux repository or module-stream instructions to Windows merely because both appear in the same management service.

## Resource relationships

A registration profile defines initial managed-instance characteristics. Groups support shared management, and lifecycle environments support controlled content promotion where applicable. Software sources describe Oracle Linux package/repository content. An agent communicates management work to the actual instance; non-OCI environments have additional connectivity/station requirements.

An instance being visible in Compute does not mean it is registered, actively checking in, or eligible for the requested update. IAM access to a managed-instance record does not establish package availability, source entitlement, guest connectivity or permission to interrupt the application.

## Prerequisites and working sequence

Navigate to **OS Management Hub** and inspect the current management API/CLI help. Resolve instance OS/location, registration state, selected profile, source/group/lifecycle ownership and the application maintenance window. See [Compute](service-compute.md) for host availability and replacement ownership.

1. Inspect the instance's existing registration and agent/plugin health. Read the actual status and last communication before attempting a duplicate enrollment.
2. Select a compatible profile and supported source/update model. For Oracle Linux, inspect attached vendor/custom/versioned sources and relevant filters.
3. Establish the documented registration and service connectivity through normal authentication. Do not paste registration material or private credentials into chat.
4. Inspect available updates and the package/OS scope requested. Explain whether a kernel, reboot, service restart or application dependency is involved.
5. Submit the bounded update job through the owning process. Observe its result and any per-instance failures rather than interpreting group submission as fleet completion.
6. Verify installed package/update state, reboot requirements, agent connectivity and the actual application health after the permitted maintenance.

## Diagnose and maintain

For missing packages, inspect OS compatibility, source selection, entitlement and content filters before broadening sources. For an offline managed instance, check the agent, management-station/network path where relevant, and local logs. A successful service API request does not prove guest package installation finished.

Keep content promotion and deployment scheduling explicit. Changing a shared software source or group can affect many machines beyond the one in the current incident. Removing a lifecycle stage or source without inspecting membership can break update reproducibility.

For cleanup, distinguish unregistering an instance from terminating Compute or removing guest data. Preserve the application's maintenance ownership and record any remaining reboots or failed nodes. Do not claim vulnerability remediation is complete from update submission alone; relevant installed-state and application evidence must support that outcome.

## Sources

- [Managed instances, agents, groups, and lifecycle model](https://docs.oracle.com/en-us/iaas/osmh/doc/overview.htm)
- [Registration profiles](https://docs.oracle.com/en-us/iaas/osmh/doc/profiles.htm)
- [Oracle Linux software sources and Windows distinction](https://docs.oracle.com/en-us/iaas/osmh/doc/software-sources.htm)
- [Supported setup and environment prerequisites](https://docs.oracle.com/en-us/iaas/osmh/doc/getstarted.htm)
