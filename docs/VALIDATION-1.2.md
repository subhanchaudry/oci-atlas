# OCI Atlas v1.2 validation

Validation date: **2026-11-17**. Scope: documentation, catalog, package, public references, and static prompt-to-guide review. Publication is pending.

## Repository and package

| Check | Result |
| --- | --- |
| `python3 tools/catalog.py --check` | Passed: generated routing, source metadata, and content catalog match the canonical catalog. |
| `python3 tools/check.py` | Passed: 100 references, 63 service guides, 19 recipes, eight domains, four troubleshooting guides, and 107 packaged files. |
| `python3 tools/package.py` | Passed: versioned ZIP and SHA-256 companion created and inspected. |
| `python3 tools/check.py --archive dist/oci-atlas-1.2.0.zip` | Passed: expected files and archive bytes match source. Independent ZIP integrity and SHA-256 checks also passed. |
| `python3 tools/release.py --tag v1.2.0 --notes-file dist/release-notes-v1.2.0.md` | Passed: manifest/tag consistency and exactly one dated changelog entry; draft release notes generated with versioned links. |
| Compatibility comparison with the prior revision | Passed: all 94 previous IDs, paths, and aliases retained; exactly six added entries; schema remains 1. Manifest differs only by version. |
| Scope and whitespace | Passed: no changes to runtime examples, tools, workflows, or marketplace identity; `git diff --check` is clean. |
| Diagrams and version references | Five Mermaid blocks are unchanged; two SVG assets parse as XML. Current installation and package references use v1.2.0. The existing example image tag `atlas-v1.1.0` identifies the unchanged example, not the plugin release. |

Prepared archive: `dist/oci-atlas-1.2.0.zip` (**265,150 bytes**). SHA-256: `0760320f4d47df4192662bd388f2f7fc55071dc9a07b1bf509dce0466a76a57b`. Its companion is `dist/oci-atlas-1.2.0.zip.sha256`; draft notes are `dist/release-notes-v1.2.0.md`. Build artifacts remain local and are not evidence of publication.

## Representative prompt review

These are **static routing and content reviews**, not conversations executed against a host/model. Each route is present in the generated skill/catalog, the linked guide exists in the package, and its content states the distinctions below. The review checks what the documentation enables; it does not measure model adherence or installation behavior.

| Area | Representative prompt | Expected route and reviewed distinction |
| --- | --- | --- |
| Foundations and identity | “Does an identity-domain OAuth token let this client manage OCI resources?” | `service-iam-policies` → identity-domain authentication/audience, OCI resource authorization, and Identity Assurance prerequisites remain separate. |
| Networking | “Plan maintenance on hybrid connectivity with overlapping private addresses.” | `recipe-hybrid-private-access` → `service-vcn-routing` and `service-hybrid-connectivity`; translation, DNS, alternate path, and return routes remain explicit. |
| Compute and storage | “Choose an Ax instance and investigate a failing GPU job.” | `service-compute` and `service-gpu-hpc`; architecture/image/attachment compatibility and supported health checks precede capacity or repair claims. |
| Databases and data | “Compare database-native MCP, Database Tools, and migration options.” | `service-autonomous-database`, `service-database-tools`, and `recipe-database-migration`; endpoint ownership, SQL grants, VM relocation, and database cutover differ. |
| AI and ML | “Choose hosted applications, Agent Sandbox, or an AIDP agent workflow.” | `service-generative-ai`, `service-ai-data-platform`, and `service-data-science`; persistence, caller/runtime identity, preview dependencies, and artifact verification have distinct scopes. |
| Application platforms | “Use an OKE workload with a regional image cache.” | `service-oke`, `service-container-registry`, and `recipe-private-oke`; lifecycle, GPU repair, virtual-node storage, and pull-only cache restrictions are explicit. |
| Operations and security | “Investigate slow SQL and database capacity growth.” | `service-database-management`, `service-ops-insights`, and `operations-security`; current diagnostics, historical collection, warehouse ownership, and evidence-led recovery differ. |
| Infrastructure and architecture | “Move AWS Arm VMs and plan application recovery.” | `service-cloud-migrations`, `enterprise-modernization`, and `recipe-backup-disaster-recovery`; compatible architecture, replication, cutover, and DR are separate responsibilities. |
| New IoT guide | “Ingest devices into twins and integrate a Flow Runtime.” | `service-internet-of-things`; domain groups, limits, downstream identities, and retained resources are explicit. |
| New Speech guide | “Generate speech as text arrives.” | `service-speech`; realtime TTS is API-only with feature-specific regional support, distinct from transcription jobs. |

## Negative scenarios

| Prompt or misleading assumption | Required documentation response | Reviewed evidence |
| --- | --- | --- |
| “Deploy Google TPUs in OCI now.” | Do not provide an assumed current TPU deployment. The reviewed announcement targets 2027; defer to documented current options and capacity checks. | Entry skill availability rule; GPU/HPC availability section; evidence register exclusion. |
| “Use the newest AIDP ontology and Preview Credential Store as the standard GA architecture.” | Exclude preview prerequisites and unresolved ontology/reasoning claims. Explain Run As without prescribing Preview credential setup. | AIDP feature-status and runtime-identity sections; evidence E21 and exclusions. |
| “Peering alone connects these overlapping CIDRs.” | Explain supported 1:1 IPv4 DRG translation; inspect translated prefixes, DNS, security, and return routing. Do not imply a route alone fixes overlap. | VCN routing and hybrid recipe; E08–E09. |
| “Push our build into the pull-through cache.” | Use a writable source repository; caches are private and pull-only, with approved cross-region sources in the same realm. | Container Registry and OKE recipe; E14. |
| “Atlas's MCP access or my OCI admin role grants all database SQL permissions.” | Atlas supplies no MCP endpoint. Client authentication, OCI permissions, network reachability, and SQL grants are separate. | README, Database Tools and Autonomous guides, access troubleshooting; E02/E15. |
| “This GA GPU/model guarantees capacity in my chosen region.” | Require actual shape/model, region, access, quota, and capacity evidence; do not invent capacity or a deployment outcome. | Entry skill, Compute/GPU and Generative AI guides; E11/E12/E20. |
| “Snowflake external-catalog access means native Snowflake-on-OCI is ready.” | Keep source connectivity distinct from native hosting; defer unestablished hosting guidance. | AIDP guide and evidence exclusions. |
| “Persistent hosted storage supports multiple replicas.” | State the reviewed single-replica restriction; do not describe it as a multi-replica availability design. | Generative AI guide; E20. |

## Links, diagrams, and evidence

Public links are checked for retrieval separately from factual source review. Versioned v1.2 repository/release links intentionally await publication; their local target files and paths are checked instead. Blog retrieval restrictions are distinguished from broken links. Local document links and packaged navigation are checked by the repository tooling.

The final audit covered **316 distinct external URLs**: 302 returned HTTP 200, 11 are explicitly deferred v1.2 publication links, and three Oracle blog pages returned HTTP 403 to the automated client but were successfully read through web browsing. These are the November AI roundup, the Acceleron networking First Principles post, and the Vera CPU post linked in the evidence register. One outdated Data Flow link was corrected to the owning service overview; no unresolved 404 remained. Every versioned link in the package has a corresponding local source file. URL fragments are not independently browser-tested.

Existing architecture diagrams retain their topology: Atlas guidance versus host execution, public ingress versus private application/database access, and application/retrieval data paths. Mermaid blocks are compared with the prior revision and SVG assets are parsed as XML. No live architecture behavior is inferred from a diagram.

The [evidence register](RELEASE-EVIDENCE-1.2.md) traces 28 accepted change groups, all 63 service-guide dispositions, and excluded/deferred announcements. Review dates are advanced for substantively reviewed additions, not for every reachable URL. Recheck accepted evidence if publication is delayed beyond this review date.

## What was not tested

No OCI login, deployment, live capacity query, customer data access, host installation, workspace import, or model conversation was performed. Existing runnable examples were not rerun against OCI. Documentation and archive checks do not establish production readiness, successful tenancy operations, or public release availability. Publication and any environment-specific acceptance remain separate actions.
