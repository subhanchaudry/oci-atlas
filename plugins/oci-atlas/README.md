# OCI Atlas

**Oracle Cloud expertise for ChatGPT and Codex.**

Understand OCI services, choose architectures, work with resources, and troubleshoot issues with focused guidance grounded in Oracle documentation.

**Version 1.2.0 · 100 references · 63 service guides · 19 recipes**

Research cutoff: **November 17, 2026**. This package is prepared for v1.2.0; publication is separate. Versioned repository links and the GitHub command below resolve after the tag is published. For prepublication review, register the repository checkout with `codex plugin marketplace add .` instead.

## Get started

After publication, for Codex CLI with plugin support:

```sh
codex plugin marketplace add subhanchaudry/oci-atlas --ref v1.2.0
codex plugin add oci-atlas@oci-atlas-marketplace
```

Start a new session and ask:

> Use OCI Atlas to explain how compartments, VCNs, and IAM fit together. Use packaged guidance only; do not connect to OCI.

For ChatGPT installation and release ZIP workflows, use the [installation guide](https://github.com/subhanchaudry/oci-atlas/blob/v1.2.0/docs/INSTALL.md). Keep `plugin.json` and the complete `skills` directory together when importing this package through a supported plugin-creation flow.

Choose a path in the packaged [getting-started guide](skills/oci-atlas/references/getting-started.md), or explore the packaged [three illustrated walkthroughs](skills/oci-atlas/references/walkthroughs.md).

## Explore OCI

The [OCI Atlas skill](skills/oci-atlas/SKILL.md) routes to tenancy foundations, networking, Compute and storage, databases and data, AI and ML, application platforms, operations and security, and infrastructure architecture. It reads relevant guides on demand.

Focused guides cover core networking/security, storage and GPU/HPC, database engines and migration, messaging, application platforms, and AI retrieval. Recipes connect them into private applications, hybrid access, observability, backup/recovery, database cutover, and data/AI workflows. See the [full presentation and diagrams](https://github.com/subhanchaudry/oci-atlas) or [content catalog](https://github.com/subhanchaudry/oci-atlas/blob/v1.2.0/docs/CONTENT.md).

## Work with your environment

Knowledge questions require no OCI login. Resource operations use the host's available OCI CLI, Console, or Cloud Shell access and your OCI permissions. OCI Atlas requires no hosted backend or separate OpenAI API key. Keep authentication material in your normal OCI and host authentication flows.

Atlas supplies guidance, not execution tools or an MCP server. Describing Autonomous AI Database or Database Tools MCP does not install or authorize those services. GA-only recommendations remain subject to regional support, edition, configuration, and actual tenancy capacity.

## What changed in v1.2

Six new guides cover [VM migration](skills/oci-atlas/references/service-cloud-migrations.md), [Database Tools](skills/oci-atlas/references/service-database-tools.md), [Database Management](skills/oci-atlas/references/service-database-management.md), [Ops Insights](skills/oci-atlas/references/service-ops-insights.md), [IoT](skills/oci-atlas/references/service-internet-of-things.md), and [Speech](skills/oci-atlas/references/service-speech.md). Existing guides and recipes clarify identity, overlapping networks, Acceleron shape compatibility, database tools, Enterprise AI, AIDP, OKE, registry caches, diagnostics, and recovery.

See the dated [change summary](https://github.com/subhanchaudry/oci-atlas/blob/v1.2.0/docs/WHATS-NEW-1.2.md) and [evidence register](https://github.com/subhanchaudry/oci-atlas/blob/v1.2.0/docs/RELEASE-EVIDENCE-1.2.md). Future TPU/Cerebras availability, AI Media Models preview, Cost Advisor limited availability, and unresolved announcement-only capabilities are excluded from supported guidance. Documentation review does not establish live tenancy validation.

Find more [example prompts](https://github.com/subhanchaudry/oci-atlas/blob/v1.2.0/docs/EXAMPLES.md), [support](https://github.com/subhanchaudry/oci-atlas/blob/v1.2.0/SUPPORT.md), and [contribution guidance](https://github.com/subhanchaudry/oci-atlas/blob/v1.2.0/CONTRIBUTING.md) in the source repository.

---

Released under [UPL 1.0](LICENSE.txt). OCI Atlas is a community project; Oracle and OpenAI endorsement is not implied. See [attribution and notices](NOTICE.md).
