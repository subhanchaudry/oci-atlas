# Contributing to OCI Atlas

Contribute OCI-specific knowledge that changes an agent's decisions or saves repeated research. Prefer a precise correction or useful example over an exhaustive manual.

## Add or update a guide

1. Find the existing topic in the [skill index](plugins/oci-atlas/skills/oci-atlas/SKILL.md). Extend it before adding another explanation of the same concept.
2. Research official product documentation first, followed by Oracle-owned repositories, product-team posts, and LiveLabs. Check command names and parameters against a command reference or installed help.
3. Use [the guide template](docs/GUIDE-TEMPLATE.md). Include service relationships, prerequisites, useful decision criteria, practical examples, gotchas, authoritative links, and the date actually reviewed.
4. Keep files focused. Link shared concepts instead of repeating long IAM, network, or authentication sections. Add new references directly to the skill's routing table and update the README if coverage changes.
5. Clearly mark conditional behavior, version differences, and assumptions. Don't turn a source-checked example into a claim of live testing. Do not guess OCI defaults or copy customer-specific configuration.
6. Run `python3 tools/check.py`, build with `python3 tools/package.py`, and inspect changed guides and the archive. A live tenancy is not required.

## Style and examples

- Use official OCI terminology and explain why a choice matters.
- Prefer a working pattern and one clear default over a menu of every option.
- Use `ATLAS_*` variables for examples; define required inputs in the access guide or locally. They are illustrative shell variables, not OCI configuration settings.
- Mark commands that change resources. Never include private keys, tokens, wallets, real customer identifiers, production endpoints, or customer data.
- Keep Bash examples in Bash code fences. Do not label them as PowerShell-compatible.
- Keep the skill's frontmatter values as single-line JSON-quoted strings (valid YAML), as in the current file. The dependency-free checker intentionally supports this small subset.
- Attribute reused text/code and retain its license notices. For upstream adaptations, record the repository file and exact commit. Do not add an unpinned submodule or runtime dependency for reference content.
- Keep user intent and existing authorization above plugin guidance. Don't add universal confirmation requirements to ordinary workflows.

## Changes and releases

Open a focused change describing the knowledge gap, sources consulted, guides affected, and checks performed. Update the changelog. Follow [maintenance and releases](docs/MAINTENANCE.md) for versioning and packaging. Report credentials or sensitive disclosures through the repository host's private reporting mechanism if one is enabled; do not include secrets in a public issue.
