# Access, tools, and onboarding

Reviewed: 2026-10-29 · Basis: documentation review; no live sign-in or command execution.

## Choose an execution route

| Available capability | Use it for | Establish first |
| --- | --- | --- |
| Local shell and OCI CLI | Structured discovery, provisioning, and operations | Installed CLI, selected profile/auth type, tenancy and region |
| Supported signed-in browser control | Console navigation, visual inspection, form-based tasks | User completes OCI sign-in and MFA; verify tenancy/region in the UI |
| OCI Cloud Shell through the browser | CLI work without a local OCI installation | Cloud Shell access, its selected region, and ability to read terminal output |
| Documentation tools only | Explain, design, prepare commands | No OCI authentication is needed |

OCI Atlas supplies knowledge and workflow instructions. A plugin install does not create a terminal, browser controller, OCI login, or additional IAM rights. Don't invent host tool names: discover and use the tools actually available.

## Onboard without collecting secrets

1. Identify whether the customer wants knowledge, a design, or live work. For knowledge, start answering immediately.
2. For live work, detect available tools. If the CLI exists, inspect its version/help and ask for a profile only if the intended one is not already clear. Read only the profile metadata needed to determine context; don't print entire credential files.
3. Use an existing authenticated profile. For interactive session setup, OCI supports `oci session authenticate`; the user signs in through the browser. This writes local session configuration, so do it only as part of requested setup. For session-token profiles, pass `--auth security_token`; don't silently switch to an API key when the token expires.
4. Confirm the tenancy and target context with a harmless scoped read, such as region subscriptions or the requested resource list. Listing public region names alone does not prove access to a customer's resources or identify the active caller.
5. For browser access, let the user sign in in the host's supported sign-in surface. Check the tenancy, current region, compartment filter, and relevant resource detail page. Never copy browser cookies or tokens into a CLI profile.

Cloud Shell already has a CLI configured for the signed-in OCI user. Preserve its supplied authentication environment rather than applying a local API-key profile over it. The Console region when Cloud Shell starts affects its configuration; inspect the actual context after switching regions. A local laptop normally has no direct route to private OCI endpoints merely because it is signed in.

## CLI example conventions

Examples in this collection use Bash syntax. Set these **illustrative shell variables** from the customer's selected context; they are not special OCI settings:

```bash
ATLAS_PROFILE='chosen-profile'
ATLAS_AUTH='security_token'  # Use api_key only for an actual API-key profile.
ATLAS_REGION='chosen-region'
ATLAS_TENANCY_ID='chosen-tenancy-ocid'
ATLAS_COMPARTMENT_ID='chosen-compartment-ocid'
```

These are inputs to replace, not runnable tenancy configuration. Pass profile, auth type, and region explicitly for local profile examples. In Cloud Shell, retain its environment and omit local-profile overrides. In PowerShell use its variable and multiline syntax; do not paste Bash assignments unchanged. Check the installed command's help before adapting an example.

Use JSON results for structured reasoning. Keep list results bounded to the request; use supported pagination or `--all` when completeness is needed. Don't remove permission or pagination caveats from an inventory. Generate complex request input using the command's `--generate-full-command-json-input` where supported; fill the necessary fields and use `--from-json file://...` rather than guessing nested shell quoting. Generated templates are not dry runs or verified deployment plans.

## Operational completion

Read before changing state, identify dependencies and IaC ownership, then execute within the customer's request. Use supported waiters/work requests, re-read the resource, and report its actual state. A transport timeout can leave a successful creation behind: inspect before retrying. A CLI exit code of zero is not application readiness. Keep CLI request IDs and sanitized error details when diagnosing failures.

## Sources

- [OCI CLI concepts](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm)
- [Session-token authentication](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clitoken.htm)
- [Using Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/devcloudshellgettingstarted.htm)
- [OCI CLI command reference and global options](https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/)
- [OCI REST API behavior, request IDs, retry tokens, and ETags](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/usingapi.htm)
- [ChatGPT browser availability and sign-in](https://learn.chatgpt.com/docs/browser)
