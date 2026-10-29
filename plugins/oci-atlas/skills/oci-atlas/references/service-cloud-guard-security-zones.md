# Cloud Guard findings and Security Zones

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Separate detection from enforcement

Cloud Guard examines supported resources and activity for security problems; configured responders can suggest or execute corrective actions. Security Zones validate supported resource operations against a selected security-zone recipe and can deny a nonconforming create/update. Neither service is a substitute for the application's authorization model or a universal compliance certification.

Use Cloud Guard to understand posture and findings. Use Security Zones when the requested compartment guardrails match the intended workloads. A denied operation may be an enforced zone constraint even when IAM grants the caller permission. Expanding IAM will not override that constraint.

## Resource relationships

A Cloud Guard target defines monitored scope and uses detector/responder recipes. Rules produce problems with resource evidence and lifecycle state. Distinguish Oracle-managed recipes from customer-managed clones and inspect current inheritance/target boundaries before changing scope.

A Security Zone associates compartment scope with a recipe. Cloud Guard integration identifies relevant existing-resource issues; creating a zone does not automatically remediate every existing violation. Inspect the effect on Cloud Guard targets when establishing or changing a zone. Reporting-region behavior is separate from the location of each monitored resource.

## Prerequisites and working sequence

Navigate to **Cloud Guard** or **Security Zones**. Resolve tenancy enablement, reporting region, selected target/compartment, actual detector rule and required service permissions. Consult the current service interface rather than interpreting the Console region selector as a filter for every finding.

1. Read the finding's resource, evidence, severity, observation time, state and applicable recipe/rule. A finding is a signal to investigate, not proof of exploitation.
2. Re-read the actual resource and management ownership. Determine whether the condition is current and whether other workloads depend on it.
3. Select a bounded correction consistent with the customer's request. Explain the proposed resource change independently from any dismiss/resolve action on the problem.
4. Apply through the owning workflow, then verify the resource condition. Observe the detector's subsequent evaluation separately from direct resource verification.
5. For a requested zone rollout, inspect workload/dependency compatibility and selected recipe scope before enablement. Identify which future operations would be denied.
6. Record actual changes, retained exceptions and remaining evidence. Do not report a compliance score as a complete assessment.

## Responders and lifecycle

An automatic responder changes operational behavior. Inspect its permissions, matching conditions and affected resources before enabling it; a diagnostic request alone does not authorize enabling broad automatic remediation. Prefer a narrowly scoped change over dismissing an unexplained finding.

For unexpected denials, compare IAM permissions, Security Zone policy and service prerequisites as separate layers. For missing findings, inspect target scope, monitored resource support and reporting context. Before removing a target, zone or recipe, identify inherited effects and consumers. Keep finding closure and actual mitigation distinct. Use [IAM](service-iam-policies.md) for caller grants and [network controls](service-zpr.md) for packet-level authorization.

## Sources

- [Cloud Guard targets, recipes, and reporting regions](https://docs.oracle.com/en-us/iaas/Content/cloud-guard/using/cg-concepts.htm)
- [Security Zone enforcement and Cloud Guard relationships](https://docs.oracle.com/en-us/iaas/Content/security-zone/using/security-zones.htm)
- [Cloud Guard responders and problem handling](https://docs.oracle.com/en-us/iaas/Content/cloud-guard/home.htm)
