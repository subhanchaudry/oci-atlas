# Support handoff and incident evidence

Reviewed: 2026-11-03

## Capture the unresolved boundary

Start with business impact, affected service and the smallest reproducible failing operation. Distinguish an OCI service incident from a missing local credential, application bug or customer-managed network problem. Check existing incident ownership before opening another case.

## Useful handoff

- Impact and scope: affected users/workloads, start time and time zone, frequency, and whether a workaround exists.
- Target: service, region, compartment and relevant resource/request/work-request identifiers through the approved support channel.
- Reproduction: caller/runtime location, operation, sanitized error, expected result and actual result.
- Evidence: bounded log/metric window, recent configuration changes and observations from each checked layer.
- Remaining question: exact inaccessible policy, failed service step or unexplained behavior requiring the next owner.

Keep facts and hypotheses distinct. Include request IDs rather than full HTTP authorization headers. Remove passwords, tokens, wallets, private keys, customer records and unnecessary document bodies from attachments. A screenshot should show the relevant error and context without unrelated account data.

## Route and follow through

Use the customer's normal Oracle support account and current service-request workflow. Account eligibility, user-group privileges and support routing can affect case creation. Preparing a handoff is not submitting a case; submit only when requested. If an administrator owns the next step, name the specific view or operation needed rather than asking for broad privileges.

Record the case reference, owner, next action and requested evidence after submission. Keep investigating independent safe reads within the original task. Do not repeat failed writes to produce more logs or claim root cause from a case acknowledgement. Use [access](troubleshoot-access.md), [connectivity](troubleshoot-connectivity.md), and [workload diagnosis](troubleshoot-workloads.md) for the relevant investigation.

## Sources

- [Create a support request](https://docs.oracle.com/en-us/iaas/Content/GSG/support/create-incident.htm)
- [OCI API errors](https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm)
