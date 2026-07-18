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

## Availability zone

An availability zone is a separated group of one or more datacenters within a region, with independent power, cooling, and networking.

- A **zonal resource** is pinned to one zone and is not automatically resilient to that zone failing.
- A **zone-redundant resource** is distributed or replicated across zones by the service.

Zones protect against zone-level failures. They do not, by themselves, protect against losing an entire region.

## Region pairs

Microsoft pairs some regions, while many newer regions are nonpaired. Some services use pairs for geo-replication or disaster-recovery behavior.

Important: placing a VM in a region does **not** automatically copy it to the paired region. Cross-region resilience must be designed and configured.

## Sovereign regions

Sovereign cloud environments address specific government, legal, compliance, or data-sovereignty requirements. They are separated from the global Azure environment and may offer a different service catalog.

## Exam clues

- Physically separated locations inside one region → **availability zones**.
- Reduce latency for users → choose a **nearby region**.
- Protect from a full regional outage → design a **multi-region** solution.
- Government-specific isolated cloud → **sovereign cloud**.

## Official references

- [What are Azure regions?](https://learn.microsoft.com/azure/reliability/regions-overview)
- [What are Azure availability zones?](https://learn.microsoft.com/azure/reliability/availability-zones-overview)
