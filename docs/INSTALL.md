# Install OCI Atlas

Reviewed: 2026-10-29. These instructions follow current host documentation and local CLI help; installation has not been exercised end to end for this release.

## Codex CLI and local plugin marketplaces

From a checkout of this repository, run:

```sh
codex plugin marketplace add .
codex plugin add oci-atlas@oci-atlas-marketplace
```

These commands change your Codex plugin configuration and install a cached copy. Start a fresh session after installation, then ask:

> Use OCI Atlas to explain how compartments, VCNs and IAM fit together. Do not connect to OCI.

For a published GitHub repository, register the actual `OWNER/REPOSITORY` instead of `.`. Use `codex plugin marketplace add OWNER/REPOSITORY --ref v0.1.0` to pin a published release tag when that tag exists, then install the same plugin selector. `OWNER/REPOSITORY` is a substitution, not an existing OCI Atlas repository address.

Check `codex plugin --help` and `codex plugin marketplace --help` if your client differs. In clients using the plugin browser, open `/plugins`, select the configured marketplace, and install OCI Atlas there.

## ChatGPT desktop

In a supported local Work/Codex environment, register the checkout as a local marketplace using the supported local tooling, then open Plugins and install OCI Atlas from **OCI Atlas**. Enable it for the conversation and start a new conversation if it has not appeared. The repository catalog lives in `.agents/plugins/marketplace.json`.

Desktop UI labels and local execution availability can vary. Verify skill discovery with the conceptual prompt above before attempting OCI operations. The plugin uses the host's existing browser/shell capabilities; it does not install a browser controller or OCI CLI.

## ChatGPT web: workspace import

For a workspace that supports GitHub plugin imports, an administrator can:

1. Open **Admin → Plugins → Add → Import marketplace**.
2. Enter the real GitHub repository URL. Leave the marketplace directory empty because the catalog is at the repository root.
3. Select a release tag/commit when a fixed version is desired.
4. Import and make OCI Atlas available to the intended workspace roles.
5. Install/enable it in a new conversation and try the conceptual prompt.

Import does not provide OCI credentials or browser access. Web-based signed-in browsing depends on the plan, workspace and rollout. A web conversation does not automatically have your laptop's terminal or CLI profile. Local computer access, if supported/enabled, is a separate host feature.

## Account plugin creation from the ZIP

If your account provides Plugin Creator and private package creation, attach the release ZIP and ask it to create a private skills-only plugin from that package, preserving its manifest and references. Complete the host's normal install flow, then verify OCI Atlas is available. Availability is account-dependent; do not assume a generic ZIP attachment installs a plugin or that every ChatGPT account has a direct ZIP import button.

This repository and ZIP do not create a listing in the universal public plugin directory. No public-directory submission is required to distribute the source on GitHub or use a supported private/local installation route.

## Portable skill fallback

For an agent that supports local Agent Skills but not plugin marketplaces, copy the complete `plugins/oci-atlas/skills/oci-atlas` directory into that host's documented skill directory. Keep the `references` directory with it. For Codex's user-level skill route, that directory is typically `~/.codex/skills/oci-atlas`; use the target host's current instructions and avoid replacing an existing copy unintentionally.

This installs the skill rather than the plugin listing/onboarding metadata. Choose either this route or the plugin in a given environment to avoid duplicate skill discovery. On a host that supports skill uploads, upload a correctly packaged skill folder, not the whole marketplace ZIP.

## Connect OCI only when needed

For live tasks, follow the packaged [access guide](../plugins/oci-atlas/skills/oci-atlas/references/access-and-tools.md). Use an existing OCI CLI profile or sign in through supported browser controls. Passwords, MFA codes, private keys and tokens belong in normal authentication flows, never in chat or the repository.

## Update or remove

Update the canonical checkout or marketplace source, then use the host's refresh/upgrade and reinstall flow. Inspect `codex plugin marketplace upgrade --help` for the installed version. Don't edit a cached plugin. To uninstall through the CLI, inspect `codex plugin remove --help` and remove the selected `oci-atlas@oci-atlas-marketplace` installation. A separately copied skill must be managed separately. Neither uninstall route deletes OCI resources.

## Sources

- [Plugin packaging and marketplaces](https://developers.openai.com/plugins/build/plugins)
- [Plugins in supported clients](https://learn.chatgpt.com/docs/plugins)
- [Workspace GitHub imports](https://learn.chatgpt.com/docs/enterprise/plugin-management)
- [Browser capabilities and availability](https://learn.chatgpt.com/docs/browser)
- [Local computer access](https://learn.chatgpt.com/docs/enterprise/cloud-local-access)
- Local `codex plugin add --help` and `codex plugin marketplace add --help`, inspected 2026-10-29.
