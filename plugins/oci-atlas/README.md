# OCI Atlas

**Oracle Cloud expertise for ChatGPT and Codex.**

Understand OCI services, choose architectures, work with resources, and troubleshoot issues with focused guidance grounded in Oracle documentation.

**Version 0.2.1 · 36 references · 15 service guides · 8 recipes**

## Get started

For Codex CLI with plugin support:

```sh
codex plugin marketplace add subhanchaudry/oci-atlas --ref v0.2.1
codex plugin add oci-atlas@oci-atlas-marketplace
```

Start a new session and ask:

> Use OCI Atlas to explain how compartments, VCNs, and IAM fit together.

For ChatGPT installation and release ZIP workflows, use the [installation guide](https://github.com/subhanchaudry/oci-atlas/blob/v0.2.1/docs/INSTALL.md). Keep `plugin.json` and the complete `skills` directory together when importing this package through a supported plugin-creation flow.

## Explore OCI

The [OCI Atlas skill](skills/oci-atlas/SKILL.md) routes to tenancy foundations, networking, Compute and storage, databases and data, AI and ML, application platforms, operations and security, and infrastructure architecture. It reads relevant guides on demand.

Recipes connect services into private applications, database access, serverless APIs, private OKE, data ingestion, RAG, and the predictive model lifecycle. See the [full presentation and diagrams](https://github.com/subhanchaudry/oci-atlas) or [content catalog](https://github.com/subhanchaudry/oci-atlas/blob/v0.2.1/docs/CONTENT.md).

## Work with your environment

Knowledge questions require no OCI login. Resource operations use the host's available OCI CLI, Console, or Cloud Shell access and your OCI permissions. OCI Atlas requires no hosted backend or separate OpenAI API key. Keep authentication material in your normal OCI and host authentication flows.

Find more [example prompts](https://github.com/subhanchaudry/oci-atlas/blob/v0.2.1/docs/EXAMPLES.md), [support](https://github.com/subhanchaudry/oci-atlas/blob/v0.2.1/SUPPORT.md), and [contribution guidance](https://github.com/subhanchaudry/oci-atlas/blob/v0.2.1/CONTRIBUTING.md) in the source repository.

---

Released under [UPL 1.0](LICENSE.txt). OCI Atlas is a community project; Oracle and OpenAI endorsement is not implied. See [attribution and notices](NOTICE.md).
