# Regions, zones, and datacenters

## The physical hierarchy

```text
Geography
└── Region
    ├── Availability Zone 1
    │   └── One or more datacenters
    ├── Availability Zone 2
    └── Availability Zone 3
```

Not every region supports availability zones, and not every Azure service supports every region or zone configuration.

## Geography and data residency

An Azure geography is a data-residency boundary containing one or more regions. Geographies help customers address requirements concerning where data is stored and processed.

Data residency, data sovereignty, compliance, backup location, and service-specific replication behavior are related but not identical. Always check the service documentation and legal requirements rather than assuming the region name answers every compliance question.

## Datacenter

A datacenter is a physical facility containing servers, storage, networking, power, cooling, and physical security. Customers normally select an Azure region or zone, not a specific building.

## Region

An Azure region is a set of physical facilities, including datacenters and networking infrastructure, within a geographic area. Regions are connected internally with high-capacity, low-latency networking.

Choose a region based on:

- proximity and latency;
- service availability;
- cost;
- data residency and compliance;
- availability-zone support;
- disaster-recovery design.

### Region selection process

1. Identify legal and data-residency requirements.
2. Confirm the required services and SKUs are available.
3. Check availability-zone and resilience support.
4. Evaluate latency to users and connected systems.
5. Compare cost and network-transfer implications.
6. Select a secondary-region or recovery approach when required.

The closest region is not automatically the best if it lacks a required service, zone support, compliance qualification, or capacity.

## Availability zone

An availability zone is a separated group of one or more datacenters within a region, with independent power, cooling, and networking.

- A **zonal resource** is pinned to one zone and is not automatically resilient to that zone failing.
- A **zone-redundant resource** is distributed or replicated across zones by the service.

### Deployment types

| Deployment type | Placement | Zone resilience |
|---|---|---|
| Zonal | Pinned to one selected zone | No; customer must add resilient instances/design |
| Zone-redundant | Service distributes across multiple zones | Yes, according to service behavior and configuration |
| Regional/nonzonal | Deployed to the region without customer-selected zone | Do not assume zone resilience |

Some services are automatically zone-redundant in supported regions; others require a specific tier or explicit configuration.

Zones protect against zone-level failures. They do not, by themselves, protect against losing an entire region.

## Region pairs

Microsoft pairs some regions, while many newer regions are nonpaired. Some services use pairs for geo-replication or disaster-recovery behavior.

Important: placing a VM in a region does **not** automatically copy it to the paired region. Cross-region resilience must be designed and configured.

### Paired and nonpaired regions

Some newer Azure regions are nonpaired and use availability zones as a primary local resilience mechanism. Many services support geo-redundancy between regions whether or not those regions form an official pair.

Region pairs can influence some platform-update and disaster-recovery behaviors, but service-specific documentation is the source of truth.

## Sovereign regions

Sovereign cloud environments address specific government, legal, compliance, or data-sovereignty requirements. They are separated from the global Azure environment and may offer a different service catalog.

Examples include:

- Azure Government for eligible US government scenarios;
- Microsoft Azure operated by 21Vianet in China.

Sovereign environments have separate endpoints, identities, compliance boundaries, and service availability. They are not simply ordinary public regions with a special tag.

## Availability versus disaster recovery

```text
Multiple instances in one datacenter
→ protects against instance failure

Instances across availability zones
→ protects against a zone-level failure

Architecture across regions
→ protects against a regional disaster

Backup in recoverable historical state
→ protects against deletion/corruption scenarios
```

Each layer addresses a different failure scope.

## Exam clues

- Physically separated locations inside one region → **availability zones**.
- Reduce latency for users → choose a **nearby region**.
- Protect from a full regional outage → design a **multi-region** solution.
- Government-specific isolated cloud → **sovereign cloud**.

## Common traps

- Every region has three customer-selectable zones → false.
- Every service is available in every region → false.
- A zonal VM is automatically zone-resilient → false.
- Region pairs replicate every resource → false.
- Availability zones are separate regions → false; they are inside one region.
- A resource group's metadata region determines every resource location → false.

## Official references

- [What are Azure regions?](https://learn.microsoft.com/azure/reliability/regions-overview)
- [What are Azure availability zones?](https://learn.microsoft.com/azure/reliability/availability-zones-overview)
