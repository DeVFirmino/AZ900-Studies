# Tags and cost organization

Tags are metadata expressed as **name-value pairs**. They add business context to Azure resources so teams can organize, search, report, automate, and allocate costs.

```text
Environment = Production
CostCenter  = CC-2040
Owner       = payments-team
Application = Checkout
```

## What tags are for

Tags can help with:

- cost reporting by department, product, owner, or environment;
- resource inventory and search;
- automation that selects resources by metadata;
- operational ownership;
- governance rules that require or add metadata.

## What tags do not do

Tags do **not**:

- grant or deny access;
- encrypt resources;
- move resources into a different subscription;
- create a security boundary;
- prevent deletion;
- automatically make a resource compliant.

| Requirement | Correct tool |
|---|---|
| Label a resource as Production | Tag |
| Decide who can modify it | Azure RBAC |
| Require every resource to have an Owner label | Azure Policy |
| Prevent accidental deletion | Resource lock |

## Tag scope and inheritance

Tags can be applied to subscriptions, resource groups, and resources where supported. Tags are **not automatically inherited** through the Azure Resource Manager hierarchy.

Example:

```text
Resource group tag: Environment = Production
└── VM has no Environment tag unless it is added separately
```

Azure Policy can require, append, or modify tags on resources. Microsoft Cost Management also has a separate **tag inheritance** feature that copies subscription or resource-group tags into cost records. That cost-reporting feature does not write those tags onto the actual resources.

## Tags and cost allocation

Cost Analysis can group and filter supported cost records by tag. This lets a shared subscription produce reports such as:

```text
CostCenter CC-1000 → €12,400
CostCenter CC-2000 → €7,800
CostCenter missing → €1,300
```

Important limitations:

- tag reporting depends on consistent spelling and capitalization;
- not every Azure resource type or historical cost record handles tags identically;
- adding a tag today does not necessarily rewrite all historical cost data;
- tags help allocate and report cost but do not change the legal invoice boundary.

## Design a tagging strategy

A useful strategy defines:

1. **Required names:** for example Owner, CostCenter, Environment, Application.
2. **Allowed values:** Production, Test, Development—not many spelling variations.
3. **Ownership:** who corrects missing or invalid tags.
4. **Enforcement:** Azure Policy with Audit, Deny, Modify, or another suitable effect.
5. **Reporting:** Cost Analysis views and exports grouped by the chosen tags.

Avoid storing secrets, passwords, personal data, or confidential values in tags. Tags are metadata and can be visible to users with resource-management access.

## Scenario

A company uses one subscription for several departments and wants monthly cost reports for each department.

**Best fit:** apply a consistent **CostCenter tag** and group Cost Analysis by that tag.

## Scenario

Every new resource must contain an Owner tag, and deployments without it should be rejected.

**Best fit:** define the tag convention, then use **Azure Policy with a Deny effect**. A tag by itself cannot enforce its presence.

## Exam clues

- Key-value business metadata → **tags**.
- Group cost by department → **tags + Cost Analysis**.
- Enforce required tags → **Azure Policy**.
- Tags on a resource group automatically appear on resources → **false without Policy or other automation**.
- Tag changes the invoice owner → **false**.

## Check yourself

**Statement:** Applying `Environment=Production` to a resource group automatically copies the tag to every contained resource.

**Answer:** False. Azure Resource Manager tags are not inherited automatically. Use Policy, automation, or Cost Management tag inheritance for its specific reporting purpose.

## Official references

- [Use tags to organize Azure resources](https://learn.microsoft.com/azure/azure-resource-manager/management/tag-resources)
- [Use tags in cost and usage data](https://learn.microsoft.com/azure/cost-management-billing/costs/enable-tag-inheritance)
- [Cost allocation in Microsoft Cost Management](https://learn.microsoft.com/azure/cost-management-billing/costs/allocate-costs)
