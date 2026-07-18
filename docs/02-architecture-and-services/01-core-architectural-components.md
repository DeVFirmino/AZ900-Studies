# Core architectural components

This lesson covers the building blocks Azure uses to organize identity, billing, governance, and deployed resources. Some topics also appear in [Cloud Concepts](../01-cloud-concepts/06-global-infrastructure.md); here the focus is how they fit **architecture and deployment** decisions on the exam.

## Physical and logical layers

```text
Geography
└── Region
    ├── Availability Zone 1
    ├── Availability Zone 2
    └── Availability Zone 3

Microsoft Entra tenant
└── Management group
    └── Subscription
        └── Resource group
            └── Resource (VM, VNet, storage account, web app, …)
```

Physical placement (region and zone) and logical organization (subscription and resource group) answer different exam questions.

## Regions, zones, and datacenters

| Component | What it is | Exam clue |
|---|---|---|
| Datacenter | Physical facility with servers, power, cooling, and networking | Customers choose a region or zone, not a specific building |
| Region | Geographic area with one or more datacenters and low-latency internal networking | Latency, compliance, service availability, and cost |
| Availability zone | Separated datacenter group inside a region with independent power, cooling, and networking | Protect against a **zone** failure inside one region |

A zonal resource is pinned to one zone. A zone-redundant resource is spread or replicated across zones by the service. Zones do not protect against losing an entire region.

## Region pairs and sovereign regions

Microsoft pairs some Azure regions with another region in the same geography. Some services use region pairs for geo-replication, disaster recovery, and sequenced platform updates. Many newer regions are nonpaired, and region pairing does **not** automatically replicate every resource.

**Exam rule:** deploying a VM in a paired region does not copy it to the other region. You must configure replication or build a multi-region architecture.

Sovereign cloud environments are separated Azure environments designed for specific government, legal, compliance, or data-sovereignty requirements. Examples include Azure Government and Microsoft Azure operated by 21Vianet in China. Their service availability can differ from global Azure.

**Exam clue:** isolated environment for government or national data-sovereignty requirements → **sovereign cloud**.

## Resource hierarchy

| Scope | Primary purpose |
|---|---|
| Microsoft Entra tenant | Identity directory: users, groups, apps, and sign-in settings |
| Management group | Organize subscriptions and apply governance at scale |
| Subscription | Billing, quotas, access boundary, and container for resource groups |
| Resource group | Logical container for related resources that share a lifecycle |
| Resource | Individual Azure item such as a VM, storage account, or virtual network |

Important rules:

- A resource belongs to **one** resource group at a time.
- Resource groups cannot be nested.
- Resources in one resource group can be in **different** regions.
- Deleting a resource group deletes the resources it contains.

**Exam rule:** tenant = identities; subscription = billing and quotas; resource group = lifecycle grouping.

## Scenario

A company deploys a web app, its database, and a virtual network for one product release. All three resources are created and deleted together.

- Put them in one **resource group** so lifecycle operations apply to the whole solution.
- Choose a **region** close to users and compliant with data residency rules.
- Place resilient components across **availability zones** if the service supports zone redundancy.

## Exam clues

- Same policy for many subscriptions → **management group**.
- Separate production billing from development → separate **subscriptions**.
- Deploy and tear down a solution as one unit → one **resource group**.
- Reduce latency for European users → deploy in a **European region**.
- Survive one datacenter failure inside a region → **availability zones**.
- Use a government-specific isolated Azure environment → **sovereign cloud**.
- Associated regions used by some services for resiliency → **region pair**.

## Check yourself

**Statement:** Every resource in a resource group must use the resource group's region.

**Answer:** False. The resource group's region stores metadata; contained resources can be in different regions.

## Official references

- [Describe core architectural components of Azure — Microsoft Learn](https://learn.microsoft.com/training/modules/describe-core-architectural-components-of-azure/)
- [What are Azure regions?](https://learn.microsoft.com/azure/reliability/regions-overview)
- [Azure paired regions](https://learn.microsoft.com/azure/reliability/regions-paired)
- [Azure management groups](https://learn.microsoft.com/azure/governance/management-groups/overview)
