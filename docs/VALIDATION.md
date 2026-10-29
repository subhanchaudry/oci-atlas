# Validation record

## 0.2.0 — 2026-10-29

- Catalog and offline package checks passed: 43 package files, an 85-line entry skill, 36 routed references, eight domain overviews, 15 focused service guides, three troubleshooting guides and eight recipes. All catalog entries have sources, aliases and review dates. Generated routing, title/date/source metadata and the content index agree with the catalog.
- The catalog controls packaging without a hard-coded guide list. Temporary negative checks rejected a duplicate ID, a path escaping the guide directory, an unlisted package file and an unexpected archive member. No test resources or temporary fixtures are packaged.
- Skill frontmatter and GitHub workflow parsed as YAML with Ruby's standard library. ZIP member paths, CRCs, source bytes, license consistency, local links and selected sensitive-data patterns passed the lightweight checks.
- The ZIP was built with a SHA-256 companion. Official documentation was consulted for the new service relationships and lifecycle guidance; representative command families were checked, including AI Data Platform control-plane management, API Gateway and Streaming. New operational sequences are documentation-based guidance, not evidence of executed deployments.

Manual non-mutating routing/content walkthroughs of the current skill:

| Request | Selected references | Guidance checked |
| --- | --- | --- |
| Compare Data Integration, Data Flow and AI Data Platform | Service selection; focused data guides | Published task, Spark run and workspace/catalog lifecycles stay separate |
| Plan private OKE with Object Storage access | Private OKE recipe; OKE and IAM guides | Operator access, registry pull and pod workload identity are distinct |
| Diagnose NotAuthorizedOrNotFound | Access troubleshooting | Actual identity, target, region and visibility precede policy changes |
| Diagnose a job's private database timeout | Connectivity troubleshooting; database recipe | Tests originate from the runtime's network context; TLS and SQL grants remain separate |
| Plan governed RAG | RAG recipe; relevant AI guide | Source access, retrieval, citations, revocation and generated answers are separate outcomes |
| Register and serve a predictive model | Model lifecycle recipe; Data Science | Training success, evaluation, artifact registration and serving behavior are separate |
| Rewrite an unrelated personal note | Entry description only | No OCI guide is relevant |

These are author walkthroughs, not independent model runs. No OCI discovery, provisioning, deletion, account installation, browser sign-in, public-directory submission or model evaluation was performed. GitHub publication/CI evidence is separate from host/OCI compatibility. The offline checker does not fetch every URL or validate the complete external manifest schema.

## Historical 0.1.0 record

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
