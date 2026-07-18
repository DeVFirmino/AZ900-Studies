# Tenant, management groups, subscriptions, and resource groups

## Management hierarchy

```text
Microsoft Entra tenant
└── Root management group
    └── Management group
        └── Subscription
            └── Resource group
                └── Resource
```

The Azure Resource Manager management scopes are management group, subscription, resource group, and resource. The tenant supplies identity; it is related to, but not simply another resource container in, that hierarchy.

## Microsoft Entra tenant

A tenant is the organization's identity directory. It contains users, groups, applications, service principals, and authentication settings.

**Exam rule:** tenant = identities.

## Management group

Management groups organize multiple subscriptions so governance can be applied at scale. Azure Policy and Azure role-based access control (RBAC) assignments at a management group can apply to subscriptions below it.

**Scenario:** apply the same policy to 20 subscriptions → use a **management group**.

## Subscription

A subscription is an Azure resource and management boundary associated with:

- billing;
- quotas and limits;
- access and administration;
- organization of resource groups and resources.

Organizations often use multiple subscriptions to separate environments, departments, billing, quotas, or administrative control.

**Exam rule:** subscription = billing, access, quotas, and limits.

## Resource group

A resource group is a logical container for related resources, commonly resources that share a lifecycle.

Important rules:

- A resource belongs to one resource group at a time.
- A resource group belongs to one subscription.
- Resource groups cannot be nested.
- Resources in one resource group can be in different Azure regions.
- Deleting a resource group deletes the resources it contains.
- Many, but not all, resource types can be moved between groups or subscriptions.

The resource group's location stores its metadata; it does not force every contained resource into that location.

## Resource

A resource is a manageable Azure item such as a virtual machine, storage account, virtual network, database, or web app.

## Scope and inheritance

A policy or RBAC assignment at a higher scope can affect lower scopes.

```text
Management group: allowed locations policy
└── Subscription
    └── Resource group
        └── VM must comply
```

Do not assume every property is inherited. For example, tags on a resource group are not automatically copied to its resources unless automation or policy applies them.

## Official references

- [Azure management groups](https://learn.microsoft.com/azure/governance/management-groups/overview)
- [Azure Resource Manager resource groups](https://learn.microsoft.com/azure/azure-resource-manager/management/manage-resource-groups-portal)
- [Azure subscriptions and management groups](https://learn.microsoft.com/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure)
