# Secret Management and encryption keys

Reviewed: 2026-10-29 · Basis: documentation review; no secret reads or key changes.

## Select the object by purpose

Use a secret for versioned sensitive application material such as a password or token. Use KMS keys for supported cryptographic/encryption operations and service integrations. Current documentation distinguishes Secret Management from key management, though legacy API/CLI/Console names can retain “Vault.” Identify the actual interface before assuming a rename changed commands or permissions.

A vault/key's management endpoint, cryptographic endpoint and a secret retrieval interface are different operations. Permission to view metadata or manage a container does not automatically authorize retrieving a secret's value or using a key.

## Application access pattern

1. Resolve the runtime principal that needs the material or operation. Prefer supported workload identity over copying a human API key into the application.
2. Select scoped permissions for the secret/key and required operation, including dependencies of the service being encrypted.
3. Configure a reference through the runtime's supported mechanism. Keep secret values out of source, command history, generated artifacts, logs and chat.
4. Verify metadata and a bounded application action. Do not retrieve/display the value merely to demonstrate that access exists.

Use Console **Secret Management**, **Vault**, or **Key Management**, as appropriate to the available interface. Discover current operations through the service's developer documentation and installed CLI help instead of guessing new command names from marketing labels.

## Rotation and lifecycle

Distinguish creating a new secret version, updating application references/caches, and retiring an old credential at its source. Updating a stored secret doesn't necessarily rotate the external system password or cause all consumers to refresh. Resolve the supported rotation strategy and rollout/rollback behavior first.

For keys, rotation, disabling and scheduled deletion have different impacts. Enumerate encrypted data/service consumers before changing availability. A key deletion can make dependent data inaccessible; this is not comparable to deleting an unused configuration label.

## Diagnose

If an application fails after rotation, inspect which version it retrieves, runtime identity, propagation/cache, network access and external credential validity. If a service can't use a key, inspect the service's required principal/policy and key lifecycle state. Don't grant all secret access to a human group to fix a workload-specific failure.

## Sources

- [Secret Management](https://docs.oracle.com/en-us/iaas/Content/secret-management/home.htm)
- [Vaults and key-management concepts](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/keyoverview.htm)
- [IAM principal and policy model](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm)
