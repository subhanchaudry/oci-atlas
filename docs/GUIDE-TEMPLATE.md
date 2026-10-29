# Service or workflow title

Reviewed: YYYY-MM-DD · Basis: documentation review; state any actual execution separately.

Authoring note: add a matching entry to `plugins/oci-atlas/skills/oci-atlas/catalog.json`. The catalog owns the title, review date and Sources list. Remove this note from the finished guide and run `python3 tools/catalog.py --write` after editing the catalog.

## Choose this service

Explain the workload fit, relevant alternatives, and the distinction the model is likely to miss.

## Resource model

Explain the service's important objects, their scope, and dependencies. Link shared concepts.

## Prerequisites and access

Identify IAM, network, endpoint, authentication, or version requirements. Describe Console search terms and CLI command families without hard-coding customer context.

## Working pattern

Give a short discovery-to-operation sequence and a source-checked command example when useful. Define inputs; label writes; explain how to observe completion and update/cleanup dependencies.

## Gotchas

Capture specific failures, diagnosis order, changing details to verify, and misleading assumptions.

## Sources

Link the exact official pages actually consulted. For adapted upstream files, include the commit and attribution. Replace this template's instructions with substantive content before adding a guide to the plugin.
