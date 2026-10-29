# OCI Atlas 0.1.0

Packaged Oracle Cloud Infrastructure knowledge for ChatGPT and Codex.

This self-contained plugin includes one [OCI Atlas skill](skills/oci-atlas/SKILL.md), an access guide, eight knowledge areas, and four cross-service recipes. It uses existing host tools for any requested execution and requires no hosted backend or custom MCP server.

For a supported account package-creation workflow, import this ZIP as a skills-only plugin while preserving `plugin.json` and the complete `skills` directory. For GitHub/local marketplace installation, use the source repository's marketplace and installation guide. A generic chat attachment does not automatically install a plugin.

After installation, ask: “Use OCI Atlas to explain how compartments, VCNs, and IAM fit together. Do not connect to OCI.” For setup, invoke the plugin's onboarding action or ask OCI Atlas to help configure an available OCI access route.

The host must provide any terminal/browser access, and the customer supplies OCI authorization. OCI Atlas adds no credential store, background service or telemetry. The host can still process relevant task data.

Examples are based on documentation and have not been run against a live tenancy. Host installation and OCI browser interaction have not been verified end to end. Consult current sources for changing prices, model IDs, regional availability and exact parameters.

UPL 1.0. Community project; no Oracle endorsement is implied. See [LICENSE.txt](LICENSE.txt) and [NOTICE.md](NOTICE.md).
