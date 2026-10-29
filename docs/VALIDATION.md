# 0.1.0 validation record

Date: 2026-10-29.

## Checks performed

- Offline package check: 19 packaged files, one 58-line entry skill, 13 directly linked references, eight knowledge areas, and four recipes. Manifest fields, local links, source sections, review-date syntax, license consistency, icon structure, and selected sensitive-data patterns were checked.
- Skill frontmatter and GitHub workflow were also parsed as YAML using the local Ruby standard library.
- Representative command syntax was reviewed against Oracle's CLI reference: recursive compartment listing, VCN creation with `--cidr-blocks`, private bucket creation with `NoPublicAccess`, Autonomous Database listing, Data Science project listing, OKE cluster listing, alarm listing, and Resource Manager stack listing.
- Codex marketplace registration and plugin-add syntax were inspected through the installed CLI's help. No account installation was performed.
- Release ZIP was built and inspected for its complete single-plugin layout, CRC integrity, contained paths, expected members and byte-for-byte agreement with package source. A SHA-256 file accompanies it.

These are packaging/content checks, not live OCI validation or a complete schema/conformance/security audit. The external sources were consulted during authoring; the offline checker does not fetch URLs.

## Non-mutating prompt walkthroughs

These were manual routing/content walkthroughs of the actual entry skill and references. They were not independent model runs or measurements of activation accuracy.

| Example request | Route checked | Content outcome |
| --- | --- | --- |
| Explain compartments versus VCNs without connecting to OCI | Foundations; networking for detail | Resource organization and network boundaries are separated; no authentication is required |
| Compare Data Integration, Data Flow and Streaming | Databases and data | Design artifacts/published tasks, Spark applications/runs and event streams are distinguished |
| Plan an application connection to private Autonomous Database | Database connectivity recipe | Caller location, DNS/routes, TLS mode and SQL identity are separate prerequisites |
| Explain permission for API Gateway to invoke a Function | Serverless API recipe | Client, gateway, deployer and function identities are distinguished |
| My OKE pod cannot pull its image | Applications | Diagnosis starts with the image, architecture, identity and network path rather than replacing the cluster |
| Rewrite an unrelated personal message | Entry skill description only | No OCI topic or workflow is relevant; no service guide should be loaded |

## Not performed

No live tenancy discovery, provisioning, deletion, browser sign-in, Cloud Shell control, ChatGPT/Codex installation, GitHub Actions execution, public-directory submission, or independent model evaluation. See [limitations](LIMITATIONS.md) for compatibility evidence and [maintenance](MAINTENANCE.md) for repeating the lightweight checks.
