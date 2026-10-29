# Validation record

## 1.0.0 — 2026-10-29

### Source, package, and publication preparation

- Preserved the 73-reference catalog, its schema, all IDs/paths, 48 service guides, 12 recipes, and UPL 1.0 licensing. The plugin remains 80 files with a 124-line entry skill. Onboarding and illustrated walkthroughs remain repository documentation outside the plugin ZIP.
- Existing catalog, metadata, local-link, selected sensitive-data-pattern, and archive checks passed. Workflow/issue-form YAML parsed. The new release helper selected only the matching changelog section and rejected mismatched versions, prerelease tags, leading-zero tags, and invalid paths. These are contract checks, not a complete workflow emulator.
- Oracle documentation was consulted for the three suggested architecture walkthroughs. Review dates on existing service guides were not advanced. The walkthroughs label illustrative responses and designs explicitly rather than claiming deployments.
- GitHub's Markdown API rendered the README, getting-started guide, and walkthroughs. A local browser preview with Mermaid 12 rendered the two existing README diagrams and all three walkthrough diagrams. The README/banner were visually inspected against light/dark backgrounds; walkthrough flow labels, arrows, and surrounding text were inspected. This preview is distinct from GitHub's own Mermaid implementation.
- Before publication, a targeted review covered five reachable commits/161 historical blobs, the working files, 166 members from three prior release archives, and 30 log files from seven prior Actions runs. Selected private-key, API-token, OCI identifier, and internal-Oracle-URL patterns produced no matches. File paths/source content and release metadata were also reviewed for customer-specific material. This is a publication-focused review, not a comprehensive security audit. Prior release IDs, publication dates, asset IDs, and digests were captured for preservation checks.

### Fresh installed-skill observations

Codex CLI `0.165.0-alpha.1.2` on macOS installed the local v1.0.0 candidate. A fresh ephemeral session outside the repository used only the installed skill directory in read-only mode for three documentation-only tasks:

| Scenario | Actual observation |
| --- | --- |
| Choose a container API runtime | Read service selection and Container Instances/OKE/Functions guides; recommended conditionally, identified availability/scaling inputs, and separated customer operating responsibilities |
| Design a private database application | Read private application/database recipes and relevant network, IAM, load balancing, Compute, and Object Storage guides; separated HTTPS ingress, private SQL, service-gateway object access, OCI identity, and SQL grants |
| Diagnose a hypothetical managed-job timeout | Read connectivity guidance; treated the timeout as the only evidence, began with resolution from the actual runtime, and conditioned corrections on the next observation |

The trace contained 13 completed local read commands: `SKILL.md` and 12 distinct references. No model-issued OCI calls, access prechecks, profile/credential reads, external-service calls, or file/resource writes occurred. No demo or production setting was invented. The host attempted normal plugin/MCP initialization and emitted unrelated startup warnings; this was not an offline-host exercise. Final responses were inspected against the actual reads. The optional 30-second live precheck instruction was inspected but not exercised against a tenancy.

### User-reported desktop results and limits

The owner supplied two v0.3.0 desktop conversation outputs: broad onboarding that attempted a slow live read, and a knowledge-only container runtime comparison naming the three focused service guides. These are user-provided observations, not independently captured desktop traces. They informed the v1 conceptual-onboarding and workload-framing refinements; they do not establish a separate ChatGPT account installation or browser/OCI execution compatibility.

Publication evidence—public access, source/tag agreement, workflow outcomes, downloaded asset integrity, private-reporting enablement, installed release pin, and preservation of earlier releases—is recorded in the GitHub release notes. No live OCI provisioning, connection troubleshooting, exhaustive model/service evaluation, hosted execution backend, or public-directory submission was performed.

## 0.3.0 — 2026-10-29

### Source, routing, and package

- Oracle's current service catalog and owning product documentation were consulted while authoring 33 service guides and four recipes. Every addition records the actual review date, source links, aliases, and a focused routing summary in the existing catalog schema. The new bodies are approximately 451–496 words before sources. They are original synthesis; no upstream skill or executable code was vendored.
- Existing catalog, metadata, local-link, license, selected sensitive-data-pattern, and archive checks passed. The ZIP contains 80 files: 73 references and seven package files. All 37 additions are directly routed and packaged. The collection has 48 service guides, 12 recipes, eight domains, three troubleshooting guides, one access guide, and one decision guide. All 36 prior IDs, kinds, and reference paths remain intact.
- The entry skill is 122 lines. Generated navigation, review/source metadata, and the content index agree with the catalog. Skill frontmatter, workflow, and both issue forms parsed with Ruby's YAML library. Both README Mermaid diagrams and the repository-only banner were retained; README language remains focused on the product. The earlier rendering record is below; no new visual-rendering claim is made for this content expansion.
- The archive passed path/member, CRC, and byte comparison checks and has a SHA-256 companion. The installed candidate's 80 files were compared byte-for-byte with plugin source. Checks do not establish every external URL, command, host, or service behavior.

### Fresh installation and documentation-only walkthrough

Codex CLI `0.165.0-alpha.1.2` on macOS replaced the OCI Atlas marketplace registration with the local candidate checkout, then installed `oci-atlas@oci-atlas-marketplace` version `0.3.0`. No other marketplace was changed. A fresh ephemeral session outside the repository used the installed skill in read-only mode for all six requested scenarios:

| Scenario | Actual observation |
| --- | --- |
| Container Instances versus OKE and Functions | Read the three focused service guides; distinguished managed container lifecycle, Kubernetes orchestration, and bounded invocation, including remaining operating ownership |
| Streaming versus managed Apache Kafka | Read both focused guides; distinguished streams/pools from clusters/brokers and management IAM from client authorization; left exact Streaming Kafka-client settings for current documentation |
| Private database access from on-premises | Read hybrid and database connectivity recipes plus the hybrid service guide; separated forward/return routing, DRG, DNS, TLS, and SQL access from the real application runtime |
| FIRING alarm without notification receipt | Read observability and Monitoring/Notifications guidance; separated evaluation, destination, subscription, endpoint acceptance, and recipient evidence; made no delivery or root-cause claim |
| GPU/HPC networking and storage | Read GPU/HPC, Lustre, and File Storage guides; separated RDMA from VCN paths and compared object, attached, NFS, and parallel-file storage without inventing capacity/performance figures |
| Migration versus replication and DR | Read migration/recovery recipes and Database Migration, GoldenGate, Base Database, and Full Stack DR guides; separated movement, checkpoints, standby roles, retained recovery points, orchestration, and writer cutover |

The trace contained 21 completed local read commands for the cached `SKILL.md` and 19 distinct references (one recipe was read twice). No model-issued OCI commands, credential-file reads, external-service calls, or resource writes occurred. The host performed normal plugin/MCP startup attempts and emitted unrelated connection warnings; this was not an offline-host exercise. The session's final answer was reviewed against the actual reads. This checks explicit skill activation and these six scenarios, not general model accuracy or implicit activation reliability.

### Release scope

Repository visibility was confirmed **private** before publication. Publication evidence (GitHub checks, downloaded asset integrity, and the final release pin) is recorded in the GitHub release notes separately from these content/host observations. The historical installation and presentation evidence below is retained separately.

No live OCI discovery, provisioning, browser sign-in, database movement, recovery action, extensive evaluation, new execution backend, or public-directory submission was performed. ChatGPT account/workspace installation remains unexercised; see [compatibility](LIMITATIONS.md).

## 0.2.1 — 2026-10-29

### Installation and guide discovery

Codex CLI `0.165.0-alpha.1.2` on macOS registered the GitHub marketplace at candidate commit `dd61498` and installed `oci-atlas@oci-atlas-marketplace`. The install response identified version `0.2.1`; the subsequent plugin list reported it installed and enabled. Existing marketplace settings were inspected before registration. Repository visibility was preserved as private at the owner's request.

A fresh ephemeral Codex session used the installed skill in read-only mode, outside this repository, for three documentation-only scenarios:

| Scenario | Observed result |
| --- | --- |
| Explain compartments versus VCNs | Separated resource/IAM organization from regional networking; requested no OCI authentication |
| Compare Data Integration, Data Flow, and AI Data Platform | Distinguished published tasks, Spark application/runs, and workspace/catalog objects |
| Diagnose a hypothetical private Autonomous Database timeout | Started from the job runtime and separated DNS, routing/security, TLS, and SQL authorization without claiming a root cause |

The execution trace showed reads of the installed `SKILL.md` and seven relevant references: foundations, networking, Data Integration, Data Flow, AI Data Platform, database connectivity, and connectivity troubleshooting. No model-issued OCI commands, credential-file reads, or resource writes occurred. The host attempted its normal plugin/MCP startup operations; this was not an offline-host exercise. The installed package's content was compared with release source. These observations establish this CLI route and explicit activation, not universal host compatibility or benchmarked accuracy.

### Presentation and packaging

- Both READMEs were reviewed for removal of testing, validation, build instructions, CI badges, and development-status commentary. Supporting evidence remains in this record and the compatibility document.
- GitHub's Markdown API rendered the root README. A local preview of that HTML rendered both Mermaid diagrams with Mermaid 12 and was visually inspected in light and dark themes. The SVG banner was also rasterized and inspected against light and dark page backgrounds. Direct logged-out GitHub viewing returned 404 for the private repository; no claim of an authenticated GitHub UI walkthrough is made.
- Catalog, local references, metadata, license consistency, sensitive-data patterns, and the complete 43-file ZIP passed existing package checks. The banner, support guide, issue forms, and development files remain outside the plugin ZIP. Issue form YAML was parsed.
- No live OCI operations, browser sign-in, ChatGPT account/workspace installation, public-directory submission, or exhaustive model/service evaluation was performed. Earlier release evidence is retained below.

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
