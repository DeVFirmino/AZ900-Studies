# Resource locks

Resource locks protect Azure resources from accidental deletion or modification through the Azure management plane.

## Lock types

| Portal name | Command/API name | Read | Modify | Delete |
|---|---|---:|---:|---:|
| Delete | CanNotDelete | Yes | Yes | No |
| Read-only | ReadOnly | Yes | No | No |

### Delete / CanNotDelete

Authorized users can read and modify the resource, but they cannot delete it until the lock is removed.

Common use:

- production databases;
- critical storage accounts;
- shared virtual networks and gateways;
- resource groups containing a production system.

### ReadOnly

Authorized users can read the resource but cannot update or delete it.

ReadOnly is more restrictive and can interfere with normal operations that require management-plane writes. Test its effect before applying it broadly.

## Scope and inheritance

Locks can be applied at:

- subscription;
- resource group;
- individual resource.

A lock at a higher scope is inherited by lower resources.

```text
Resource group: Production
└── Delete lock
    ├── VM inherits lock
    ├── Storage account inherits lock
    └── VNet inherits lock
```

The most restrictive lock in the inheritance chain takes effect. A child resource cannot override an inherited lock with a less restrictive setting.

## Locks override management permissions

Even an Owner or Contributor cannot perform an operation prohibited by a lock. The lock must first be removed by a principal with permission to manage locks.

This is why locks and RBAC solve different problems:

- **RBAC:** grants management permissions to identities.
- **Lock:** restricts certain management operations for everyone at the scope.

## Management plane versus data plane

This is the most important lock limitation.

Locks apply to Azure Resource Manager **management-plane** operations, such as deleting a storage account or changing its configuration.

They do not universally protect **data-plane** operations inside a resource.

Example:

```text
Delete lock on storage account
├── Delete storage account → blocked
└── Delete a blob inside the account → may still be allowed by data permissions
```

Protect data with service-specific features such as:

- soft delete;
- versioning;
- backup;
- immutability policies;
- data-plane RBAC and access controls.

## Deleting a resource group with locks

If a resource group or a resource inside it has a lock that blocks deletion, deleting the resource group fails until the relevant lock is removed.

Do not assume deleting a parent scope bypasses a child lock.

## Lock design guidance

1. Identify resources where accidental deletion would have high impact.
2. Prefer CanNotDelete when normal configuration changes must continue.
3. Use ReadOnly only when write operations truly should stop.
4. Document who can remove locks and under which change process.
5. Combine locks with backups and data-protection features.

## Tool comparison

| Requirement | Tool |
|---|---|
| Prevent deleting a critical resource | CanNotDelete lock |
| Prevent modification and deletion | ReadOnly lock |
| Decide which user may update the resource | Azure RBAC |
| Require an approved configuration | Azure Policy |
| Recover data deleted inside a service | Backup, soft delete, versioning, or service-specific protection |

## Scenario

A production storage account must remain configurable, but no administrator should accidentally delete the account.

**Best fit:** apply a **CanNotDelete** lock.

## Scenario

A legal archive must not be altered for seven years.

**Best fit:** use a service-specific **immutability/WORM policy**. A resource lock alone does not provide legal data immutability.

## Exam clues

- Prevent accidental deletion → **CanNotDelete**.
- Prevent modification and deletion → **ReadOnly**.
- Lock on resource group affects contained resources → **true**.
- Owner can ignore a lock → **false**.
- Lock protects every blob or database row → **false**.

## Check yourself

**Statement:** A CanNotDelete lock on a storage account guarantees that no blob can be deleted.

**Answer:** False. It blocks deletion of the storage-account resource through the management plane. Blob deletion is a data-plane operation requiring separate protection.

## Official references

- [Lock Azure resources](https://learn.microsoft.com/azure/azure-resource-manager/management/lock-resources)
- [Azure control plane and data plane](https://learn.microsoft.com/azure/azure-resource-manager/management/control-plane-and-data-plane)
