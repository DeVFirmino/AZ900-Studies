# Azure Architecture and Services

This domain currently represents **35–40%** of the AZ-900 exam. It is the largest section.

## Lessons

1. [Core architectural components](01-core-architectural-components.md)
2. [Compute choices: VMs, containers, and functions](02-compute-choices.md)
3. [VM options and required resources](03-vm-options.md)
4. [Application hosting: Web Apps, containers, and virtual machines](04-application-hosting.md)
5. [Virtual networking: VNets, subnets, peering, DNS, VPN, and ExpressRoute](05-virtual-networking.md)
6. [Public and private endpoints](06-public-and-private-endpoints.md)
7. [Azure Storage services and account types](07-azure-storage-services.md)
8. [Storage tiers and redundancy](08-storage-tiers-and-redundancy.md)
9. [File movement and migration tools](09-file-movement-and-migration.md)
10. [Microsoft Entra ID and Domain Services](10-microsoft-entra-id.md)
11. [Authentication: SSO, MFA, passwordless, and Conditional Access](11-authentication.md)
12. [Authorization and security: RBAC, Zero Trust, defense in depth, and Defender for Cloud](12-authorization-and-security.md)
13. [Exam cheat sheet](13-cheat-sheet.md)
14. [Practice quiz](14-practice-quiz.md)
15. [Answer key](15-answer-key.md)

## High-value comparisons

| Requirement | Likely answer |
|---|---|
| VM instances managed and scaled together | Virtual Machine Scale Sets |
| Connect a VM privately to a subnet | Network interface with a private IP |
| Persistent operating system storage for a VM | Managed OS disk |
| Isolated private network in Azure | Virtual Network |
| Encrypted hybrid connection over the public internet | VPN Gateway |
| Private hybrid connection that avoids the public internet | ExpressRoute |
| Objects such as images, video, and backups | Blob Storage |
| Managed SMB/NFS file share | Azure Files |
| Identity directory | Microsoft Entra ID |
| Who can perform an action at a scope | Azure RBAC |

The lesson list follows the [current official AZ-900 skills measured](https://learn.microsoft.com/credentials/certifications/resources/study-guides/az-900).

## Related Cloud Concepts lessons

Some foundational topics were introduced earlier in the study sequence and are also covered directly by this section:

- [Regions, zones, and datacenters](../01-cloud-concepts/06-global-infrastructure.md)
- [Tenant, management groups, subscriptions, and resource groups](../01-cloud-concepts/07-resource-hierarchy.md)

Review those pages if you need a refresher before starting this section.
