# Scope, compatibility, and limitations

## What 0.2.1 provides

Sourced OCI context, service selection, examples, and reusable workflows across 36 references. It can guide an agent's use of existing tools. It does not introduce an OCI execution service, create a login, or grant permissions. The eight knowledge areas and 15 focused service guides are a curated starting point, not every OCI API operation.

## Compatibility evidence

| Capability | Evidence for this release |
| --- | --- |
| Portable plugin and local marketplace structure | Checked by repository tooling; current platform documentation consulted |
| Codex CLI GitHub installation | Installed v0.2.1 from GitHub candidate `dd61498` with Codex CLI `0.165.0-alpha.1.2` on macOS; reported installed and enabled |
| Codex CLI skill discovery and explicit activation | Fresh read-only session loaded the installed skill and relevant references for three documentation-only scenarios |
| ChatGPT desktop/web plugin discovery and activation | Not verified end to end |
| ChatGPT workspace GitHub import | Documented platform route; depends on workspace administrator/features |
| Private account ZIP creation | Conditional on account tooling; not verified end to end |
| Signed-in OCI Console through host browser | Documented host capability; OCI-specific interaction not verified |
| Cloud Shell through browser controls | Documented OCI access route; terminal interaction not verified |
| Example OCI commands | Selected command references reviewed; no live execution |
| Non-mutating prompt checks | One fresh Codex session covering tenancy/network concepts, data-service selection, and hypothetical private database connectivity; no broad model evaluation |

## Boundaries

- Browser/shell tools, local computer access, sign-in support and plugin installation differ across products, versions, plans and managed workspaces.
- Guides use current official documentation and may encounter later service changes. Look up exact volatile details when needed.
- Regional/realm endpoints, government or dedicated-cloud availability, shape capacity and customer-specific policy constraints must be discovered for that environment. Do not extrapolate a public commercial-region example.
- Bash command examples require the indicated inputs and valid authentication. They are not universal PowerShell scripts or complete unattended provisioning programs.
- The package does not enforce IAM, budget caps, network isolation or approvals. Those are controlled by OCI, the host, and the customer's environment.
- Source-reviewed instructions do not establish production readiness, compliance, measured latency improvements or deployment acceptance.
- No live provisioning, deletion, exhaustive integration testing, or formal model evaluation was performed for this release.

## Data handling

OCI Atlas adds no telemetry or remote storage. CLI results, page content and task context may still be processed by the host/model service. Keep passwords, MFA codes, wallets, tokens and private keys in the appropriate authentication/secret mechanisms. Do not place them in conversations, prompts, Git commits, or release archives.
