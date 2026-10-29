# Maintain and release OCI Atlas

## Canonical source and organization

Edit the repository's plugin source, not installed caches. Keep the entry skill concise and directly link each packaged reference. Put stable service relationships, decision criteria and gotchas in the guides. Leave volatile prices, model IDs, availability matrices and large command schemas in their authoritative sources.

Every substantive guide records the date it was actually reviewed and a source list. A changed review date means a maintainer checked the relevant content, not that a link checker received HTTP 200. Do not bulk-update dates to make content appear fresh.

Original synthesized guidance needs citations. Any copied/adapted upstream skill or code also needs a file path, exact upstream revision, license and preserved notices in the package's NOTICE. Currently no upstream skill or executable code is vendored.

## Update when evidence changes

1. Identify the changed service behavior or recurring user confusion.
2. Read current owning product documentation and relevant release notes; consult command help when syntax matters.
3. Revise the affected canonical guide and dependent recipes. Distinguish documented facts from suggested design choices.
4. Check the entry routing and aliases when a service is renamed or a new topic is added.
5. Run the lightweight checks, inspect changed examples, and update the changelog.

Before a release, review changed topics and outstanding stale-content issues. A monthly freshness triage is recommended, with extra attention to AI APIs, model capabilities, regional behavior and product renames. This is a documented maintenance practice; the repository does not create a recurring cloud task or external automation.

## Lightweight review prompts

Try a few questions from [examples](EXAMPLES.md), without live writes. Check whether the agent selects the relevant guide, avoids loading the entire library, distinguishes service boundaries and asks only for information that changes the answer. Check at least one unrelated request for unnecessary activation. Record observed behavior accurately; a static route check is not an independent model evaluation.

## Build and inspect

```sh
python3 tools/check.py
python3 tools/package.py
python3 tools/check.py --archive dist/oci-atlas-0.1.0.zip
```

The checker validates local package structure and content conventions. It doesn't contact OCI, validate every command against a live CLI, fetch all source URLs, or prove host compatibility. The packager uses a fixed ZIP timestamp, refuses unexpected source files, checks archive paths/content, and emits a checksum. Build artifacts are ignored by Git.

## Version and release

The canonical version is in the plugin manifest. Use SemVer: patch for corrections, minor for additive knowledge/workflows, major for incompatible interface or invocation changes. During 0.x, clearly document changes that affect users. Keep existing skill identifiers and reference paths stable where practical.

1. Set the version, update the README/version references and add a changelog entry.
2. Run the commands above and review the archive listing and limitations.
3. Commit the reviewed source in your chosen GitHub repository and tag the matching version, for example `v0.1.0`.
4. Attach the ZIP and `.sha256` to that GitHub release. The included GitHub Actions workflow builds downloadable artifacts on pushes, pull requests and manual runs; it doesn't publish a release or submit a plugin automatically.
5. Test installation when a target host is available, then update compatibility evidence with the exact version, route and observed result. Don't change “not verified” to “verified” from a packaging pass alone.

Use a pinned tag/commit for customers who need reproducible installs. Workspace imports can follow a branch and sync changes, so document releases before advancing the recommended version. No public OpenAI directory submission is part of this workflow.

## Sources

- [Agent Skills authoring practices](https://agentskills.io/skill-creation/best-practices)
- [Oracle skill authoring standards](https://github.com/oracle/skills/blob/main/SKILL_AUTHORING_GUIDE.md)
- [OCI service release notes](https://docs.oracle.com/en-us/iaas/releasenotes/)
- [Plugin packaging](https://developers.openai.com/plugins/build/plugins)
