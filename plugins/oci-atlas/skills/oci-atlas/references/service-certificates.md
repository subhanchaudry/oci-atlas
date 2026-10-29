# Certificates, trust chains, and renewal

Reviewed: 2026-10-29 · Basis: Oracle documentation review; suggested operational workflow.

## Choose the certificate lifecycle

Certificates manages TLS certificates, certificate authorities (CAs) and CA bundles. Identify whether the application imports an externally issued certificate, uses a supported internally issued certificate, or manages issuance outside OCI. A managed private CA is not automatically trusted by public browsers or by every application runtime.

Choose by hostname, trust requirements, issuance ownership and consumer integration. A certificate proves neither application authorization nor network reachability. For a load balancer, resolve frontend termination and backend TLS separately; the client and the proxy may trust different chains.

## Resource relationships

Distinguish a leaf certificate, an issuing/root CA, a CA bundle used for trust, and the current certificate version. Supported OCI resources can associate with certificate resources. Other consumers may need an explicit retrieval/deployment workflow rather than automatically refreshing when a version changes.

Creation/management access and retrieval of sensitive certificate material are separate permissions. Private CA configurations can depend on key-management resources and supported revocation publication settings. Inspect those dependencies before creating a new CA hierarchy. Reuse a suitable existing issuer rather than creating a root for each application.

## Prerequisites and working sequence

Use Console **Certificates**, **Certificate authorities**, and the consumer's TLS settings. Inspect current certificate management versus retrieval API/CLI interfaces; do not assume a similarly named endpoint returns only public metadata.

1. Identify the consumer, DNS names, expected issuer, trust store, validity requirements and existing certificate association.
2. Select the supported import or issuance mode. Supply secret material only through the host's normal secure flow, not through a committed file or chat transcript.
3. Inspect certificate state and the complete chain. Check hostname coverage and compatibility with the consuming service before attaching it.
4. Configure the intended association, listener or trust bundle using the owning deployment workflow.
5. Make a bounded TLS/application request from the actual client path. Confirm the certificate served by that endpoint, not just the resource shown in Console.
6. Record issuer, certificate/version, consumer references and renewal ownership. Track any manual work required at the consumer.

## Renewal, diagnosis, and removal

Treat issuance/renewal, selection of the current version, consumer refresh, and client trust as separate steps. Do not promise automatic rotation for an imported certificate or unsupported consumer. Preserve a known working association until the intended endpoint presents the replacement correctly.

For TLS errors, separate expired/not-yet-valid dates, hostname mismatch, incomplete chain, untrusted issuer, protocol/cipher compatibility and mTLS client authentication. A successful certificate import does not repair a missing intermediate on a separately configured backend. Revocation is different from deletion and depends on how clients validate trust.

Before disabling or deleting a certificate, CA or associated key, enumerate consumers and dependent issuance chains. A shared root or encryption key can affect many workloads. Use [load balancing](service-load-balancing.md) for listeners and backend health, and [secret/key guidance](service-secrets-keys.md) for distinct key lifecycle operations.

## Sources

- [Certificate objects, versions, and trust concepts](https://docs.oracle.com/en-us/iaas/Content/certificates/overview.htm)
- [Issuance, import, renewal, and retrieval entry points](https://docs.oracle.com/en-us/iaas/Content/certificates/home.htm)
- [Load Balancer certificate integration](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/balanceoverview.htm)
- [Key-management concepts](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/keyoverview.htm)
