# Maintain and release OCI Atlas

## Canonical source and organization

Edit the repository's plugin source, not installed caches. Keep the entry skill concise and load focused references as needed. The catalog owns guide IDs, titles, paths, aliases, review dates and source links. Guide bodies own substantive explanations and operating workflows.

After editing the catalog and guide bodies, render navigation and source metadata with `python3 tools/catalog.py --write`. Preserve one canonical explanation per concept and link dependent recipes. Use the date sources and content were actually reviewed; do not advance dates merely because a URL responds.

## Source maintenance

Use current owning product documentation for behavior and Oracle Architecture Center for workload patterns. Consult installed command help where syntax matters. Keep prices, regional availability, model choices, capacity and service limits tied to current sources. Preserve upstream licenses and exact revisions when adapting source; do not vendor unpinned code.

Review changing AI APIs, product terminology and service retirement notices regularly. Revise dependent recipes when a service boundary changes. Keep application examples aligned with their documented dependencies and configuration interfaces.

## Version and release

The manifest is the canonical version. Use patches for corrections, minor releases for additive knowledge/workflows, and a major release for incompatible identity/schema/path changes. The v1 series preserves the plugin and marketplace names, skill identity, catalog schema version 1 and existing reference paths.

Prepare the package with `python3 tools/package.py`. The output is a versioned ZIP and SHA-256 companion. Examples remain in the repository and packaged recipes link to their matching release tag.

Update the changelog and installation version together. Prepare notes with `python3 tools/release.py --tag v1.1.0 --notes-file /tmp/oci-atlas-release-notes.md`. The tag-triggered release workflow publishes the matching ZIP and checksum. Preserve historical tags/assets and inspect partial publication state before retrying; do not automatically overwrite an existing release.

Pinned tags provide reproducible customer installs. Workspace imports following a branch can sync changes. Public-directory submission is separate from GitHub distribution.

## Sources

- [OCI service release notes](https://docs.oracle.com/en-us/iaas/releasenotes/)
- [Oracle Architecture Center](https://docs.oracle.com/solutions/)
- [Plugin packaging](https://developers.openai.com/plugins/build/plugins)
