# OCI Atlas

**OCI context, ready when your agent needs it.**

OCI Atlas packages Oracle Cloud Infrastructure service knowledge and practical workflows for ChatGPT and Codex. It helps a foundation model choose services, understand dependencies, navigate a tenancy, troubleshoot issues, and complete authorized resource tasks using tools the customer already has.

Version **0.1.0** · **UPL 1.0** · Community project; no Oracle endorsement is implied.

## What is included

One concise OCI skill, an access guide, eight knowledge areas, and four cross-service recipes. Detailed references load on demand rather than becoming one large always-present prompt.

| Area | Packaged context |
| --- | --- |
| Foundations | Tenancy, IAM, compartments, regions, identifiers, quotas |
| Networking | VCNs, routes, gateways, NSGs, DNS, private access, load balancing |
| Compute and storage | Instances, shapes, images, volumes, Object Storage, File Storage |
| Databases and data | Database selection, Autonomous Database, integration, Spark, streaming |
| AI and ML | Generative AI, agents, RAG, Data Science, AI services |
| Applications | OKE, Functions, API Gateway, Container Registry, DevOps |
| Operations and security | Metrics, logs, Audit, Cloud Guard, keys, secrets, cost |
| Infrastructure | Terraform, Resource Manager, landing zones, architecture |

Recipes connect these into private applications, Autonomous Database connectivity, serverless APIs, and AI applications. Browse the [skill and guide index](plugins/oci-atlas/skills/oci-atlas/SKILL.md).

## Install and use

See [installation instructions](docs/INSTALL.md) for Codex, ChatGPT desktop, ChatGPT account/workspace routes, and a portable skill fallback. Available routes depend on your host and workspace settings; GitHub distribution does not create a public OpenAI directory listing.

After installation, try:

> Use OCI Atlas to explain compartments, VCNs, and regions, and how they relate.

> Use OCI Atlas to design a private application connected to Autonomous Database. Explain the service choices.

> Use OCI Atlas to inspect resources in my selected compartment with my existing OCI CLI. Report which regions and services you checked.

More examples are in [example prompts](docs/EXAMPLES.md).

For knowledge questions, no OCI credentials are needed. For live work, the host needs shell/CLI access or supported browser control, and you need your own OCI permissions. OCI Atlas does not supply these capabilities or add permissions. It runs no background process and requires no separate OpenAI API key.

## Build the release ZIP

Python 3.10+ is needed only for repository maintenance and packaging, not to read the skill:

```sh
python3 tools/check.py
python3 tools/package.py
```

This writes `dist/oci-atlas-0.1.0.zip` and a SHA-256 checksum. The ZIP contains one self-contained plugin, not the repository marketplace or development files. Windows users can use `py -3` in place of `python3`.

## Maintain and contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md) and the [maintenance guide](docs/MAINTENANCE.md). The repository is the canonical source; edit it rather than installed plugin caches. Rebuild the ZIP after changes.

## Scope and evidence

This release emphasizes sourced OCI understanding, examples, and workflow guidance. Examples are documentation-based and have not been executed against a live tenancy. Actual ChatGPT/Codex installation and browser workflows have not been verified for this release. No exhaustive API coverage, performance improvement, or production-readiness claim is made. See the [validation record](docs/VALIDATION.md) and [known limitations](docs/LIMITATIONS.md).

The plugin adds no telemetry, credential store, or hosted data service. Relevant CLI output and browser content can still be processed by your chosen host; local execution does not imply offline model inference. Keep secrets in the normal OCI and host authentication mechanisms.

Sources and attribution are in each guide and [NOTICE.md](plugins/oci-atlas/NOTICE.md). See the [changelog](CHANGELOG.md) and [license](LICENSE.txt).
