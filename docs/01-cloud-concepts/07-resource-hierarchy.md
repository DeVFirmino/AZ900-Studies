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

## Scope versus identity boundary

The Microsoft Entra tenant is the identity boundary. Azure Resource Manager scopes organize management and governance.

```text
Tenant asks: Who are the identities?
Scope asks:  Where does an assignment or resource belong?
```

A subscription trusts one Microsoft Entra tenant for authentication. One tenant can be associated with multiple subscriptions. Moving a subscription between tenants is an identity and access change, not merely a billing-folder change.

## Microsoft Entra tenant

A tenant is the organization's identity directory. It contains users, groups, applications, service principals, and authentication settings.

**Exam rule:** tenant = identities.

## Management group

Management groups organize multiple subscriptions so governance can be applied at scale. Azure Policy and Azure role-based access control (RBAC) assignments at a management group can apply to subscriptions below it.

**Scenario:** apply the same policy to 20 subscriptions → use a **management group**.

### Root management group

Each tenant has a root management group at the top of its management-group hierarchy. New subscriptions are placed under that hierarchy and can be reorganized into child management groups.

Assignments at the root have very broad impact. Use least privilege and controlled change processes at high scopes.

Example organization:

```text
Tenant root management group
├── Platform
│   ├── Identity subscription
│   └── Connectivity subscription
├── Production
│   ├── Customer Apps subscription
│   └── Data subscription
└── Sandbox
    └── Developer subscription
```

Management groups are governance containers; they do not directly hold VMs or storage accounts.

## Subscription

A subscription is an Azure resource and management boundary associated with:

- billing;
- quotas and limits;
- access and administration;
- organization of resource groups and resources.

Organizations often use multiple subscriptions to separate environments, departments, billing, quotas, or administrative control.

**Exam rule:** subscription = billing, access, quotas, and limits.

### Why subscriptions are separated

- billing ownership or chargeback;
- production versus nonproduction isolation;
- administrative boundaries;
- quota separation;
- regulatory or business-unit structure;
- limit the impact of mistakes and broad assignments.

A subscription is not itself an availability or network boundary. Resources in different subscriptions can be connected when the architecture and permissions allow it.

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

### Resource-group lifecycle design

Place resources together when they share deployment, ownership, permissions, policy scope, and deletion lifecycle.

Do not group resources only because they are in the same region. A shared network might outlive several applications and therefore belong in a separate resource group.

Example:

```text
rg-shared-network       → long-lived VNet and gateway
rg-checkout-production  → app and database deployed together
rg-checkout-test        → temporary test environment
```

### Moving resources

Many resources can move between resource groups or subscriptions, but support and prerequisites vary. A move changes the resource ID because the subscription or resource-group segment changes. Applications, scripts, RBAC assignments, and dependencies can need review.

Never assume every resource can move without downtime or dependency changes.

## Resource

A resource is a manageable Azure item such as a virtual machine, storage account, virtual network, database, or web app.

Every ARM resource has a unique resource ID resembling:

```text
/subscriptions/<subscription-id>
/resourceGroups/<resource-group>
/providers/<resource-provider>/<type>/<name>
```

The resource provider namespace identifies the Azure service, such as `Microsoft.Compute` or `Microsoft.Storage`. A subscription may need a provider registered before using some resource types.

## Scope and inheritance

A policy or RBAC assignment at a higher scope can affect lower scopes.

```text
Management group: allowed locations policy
└── Subscription
    └── Resource group
        └── VM must comply
```

Do not assume every property is inherited. For example, tags on a resource group are not automatically copied to its resources unless automation or policy applies them.

## Governance at scope

| Control | Can apply at multiple ARM scopes? | Main purpose |
|---|---:|---|
| Azure RBAC | Yes | Who may perform actions |
| Azure Policy | Yes | Which configurations are compliant or allowed |
| Resource locks | Subscription, resource group, resource | Restrict management-plane change/deletion |
| Tags | Subscription, resource group, supported resources | Metadata and organization |

Higher-scope RBAC and Policy assignments normally flow to lower scopes. Exclusions, deny assignments, role combinations, and Policy exemptions can affect the final result.

## Deletion impact

- Delete a resource → that resource is removed, subject to locks and service behavior.
- Delete a resource group → all resources in the group are deleted, subject to locks and dependencies.
- Cancel/delete a subscription → broad service and retention consequences; it is not a normal way to delete one application.
- Delete a management group → subscriptions must be moved or handled according to platform rules; it does not act like deleting a resource group full of resources.

## Exam elimination method

1. Identities and authentication directory → tenant.
2. Apply governance to several subscriptions → management group.
3. Billing, quotas, and major administration boundary → subscription.
4. Shared lifecycle for resources → resource group.
5. Actual service instance → resource.
6. Same tag automatically appears below → false unless Policy/automation or a reporting feature does it.

## Official references

- [Azure management groups](https://learn.microsoft.com/azure/governance/management-groups/overview)
- [Azure Resource Manager resource groups](https://learn.microsoft.com/azure/azure-resource-manager/management/manage-resource-groups-portal)
- [Azure subscriptions and management groups](https://learn.microsoft.com/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure)
