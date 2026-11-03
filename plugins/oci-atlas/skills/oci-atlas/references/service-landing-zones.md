# Landing-zone adoption and existing tenancy foundations

Reviewed: 2026-11-03

## Choose an adoption path

A landing zone establishes reusable identity, compartment, networking, security and operating foundations. Oracle's Core Landing Zone is a starting blueprint; workload extensions add specialized needs. Use the existing suitable landing zone before creating a parallel hierarchy. A bounded application can consume established foundations without deploying an entire new tenancy layout.

## Discover before planning

Record the tenancy/home region, identity domains, compartment owners, IP address plan, hybrid connections, tagging, quotas, security requirements and Terraform state. Identify where existing resources differ intentionally from the selected blueprint. A new template is not authority to rename compartments, replace shared routes or broaden policies.

## Working sequence

1. Map required capabilities to existing foundations and list only missing components.
2. Select the official implementation and pin its revision and compatible module/provider versions. Read inputs, prerequisites and license.
3. Separate administrative bootstrap rights from application deployment and runtime rights. Resolve identity-domain names and policy locations.
4. Review the Terraform plan for shared-resource changes, security defaults and recurring resources. Integrate through the existing state owner.
5. Hand off workload compartments, subnet/NSG IDs, DNS paths, logging destinations, tags and operating contacts.
6. Check the intended application flow and a scoped caller operation. A completed foundation stack does not establish application availability or compliance.

## Operate and evolve

Treat module upgrades as configuration changes with a fresh plan. Preserve intentional customization; do not periodically reapply a moving upstream branch. Budget shared network/security services, retained logs and connectivity with an allocation owner. Foundation teardown is not routine application cleanup: enumerate dependent workloads first.

Use [Resource Manager](service-resource-manager.md), [IAM](service-iam-policies.md), and [cost management](service-cost-management.md) for the detailed boundaries.

## Sources

- [Landing Zones overview](https://docs.oracle.com/en-us/iaas/Content/cloud-adoption-framework/oci-landing-zones-overview.htm)
- [Core Landing Zone](https://docs.oracle.com/en-us/iaas/Content/cloud-adoption-framework/oci-core-landing-zone.htm)
- [Well-Architected landing zones](https://docs.oracle.com/en/solutions/oci-best-practices/simplify-provisioning-oci-landing-zones1.html)
