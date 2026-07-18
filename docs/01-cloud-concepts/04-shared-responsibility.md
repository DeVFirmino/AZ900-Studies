# Shared responsibility

The shared responsibility model divides security and operational duties between the cloud provider and the customer. The division changes with the service model.

## What never moves

Microsoft is responsible for the physical cloud infrastructure:

- datacenters;
- physical hosts;
- physical networks;
- power, cooling, and physical security.

The customer always retains responsibility for:

- data and information;
- identities and accounts;
- endpoint devices;
- access management;
- configurations that remain under customer control.

## Responsibility by service model

| Layer | On-premises | IaaS | PaaS | SaaS |
|---|---:|---:|---:|---:|
| Physical datacenter and hosts | Customer | Microsoft | Microsoft | Microsoft |
| Operating system | Customer | Customer | Microsoft | Microsoft |
| Application/runtime | Customer | Customer | Shared/varies | Microsoft |
| Data, identities, and access | Customer | Customer | Customer | Customer |

The exact boundary varies by service and feature. The table expresses the exam-level model, not every implementation detail.

## Layer-by-layer view

| Responsibility layer | On-premises | IaaS | PaaS | SaaS |
|---|---|---|---|---|
| Physical datacenter | Customer | Microsoft | Microsoft | Microsoft |
| Physical network and hosts | Customer | Microsoft | Microsoft | Microsoft |
| Hypervisor | Customer | Microsoft | Microsoft | Microsoft |
| Guest operating system | Customer | Customer | Microsoft | Microsoft |
| Runtime and middleware | Customer | Customer | Microsoft | Microsoft |
| Application | Customer | Customer | Customer | Microsoft |
| Application configuration | Customer | Customer | Customer | Shared/customer settings |
| Identities and access | Customer | Customer | Customer | Customer |
| Data and classification | Customer | Customer | Customer | Customer |
| Endpoint devices | Customer | Customer | Customer | Customer |

"Microsoft" in the table means Microsoft operates that layer. The customer still chooses service configuration, regions, availability options, access, and data handling where the service exposes those choices.

## Security responsibilities that remain with the customer

### Data

The customer decides:

- what data is placed in the service;
- how it is classified;
- who may access it;
- retention and backup requirements;
- whether additional encryption or key management is needed.

### Identities and access

Microsoft operates the identity platform, but the customer manages users, groups, credentials, role assignments, Conditional Access, and removal of unnecessary access.

### Configuration

A managed service can still be configured insecurely. Examples include public exposure, excessive permissions, missing diagnostic settings, or weak data-retention choices.

### Endpoints

Compromised laptops, phones, administrator workstations, and credentials remain customer risks even when the application is SaaS.

## Responsibility shifts, not disappears

```text
On-premises → customer operates nearly every layer
IaaS        → provider takes physical infrastructure and virtualization
PaaS        → provider also operates OS, runtime, and managed platform
SaaS        → provider also operates the application
```

As provider responsibility increases:

- operational overhead usually decreases;
- direct control usually decreases;
- responsibility for data, identities, access, and configuration remains.

## Shared areas

Some responsibilities are genuinely shared or depend on configuration.

Examples:

- Microsoft secures the physical Azure network; the customer designs VNets, NSGs, routes, and public exposure.
- Microsoft patches a PaaS database engine; the customer controls database users and data access.
- Microsoft provides availability-zone capabilities; the customer selects and architects the appropriate deployment.
- Microsoft provides logging services; the customer enables, retains, queries, and responds to relevant telemetry.

## Scenarios

### SQL Server on an Azure VM

This is IaaS. Microsoft manages the physical infrastructure. The customer manages the guest operating system, patches, installed SQL Server, accounts, configuration, and data.

### Azure SQL Database

This is PaaS. Microsoft manages the infrastructure, operating system, and database platform. The customer manages the data, identities, access, and application-level configuration.

### Microsoft 365

This is SaaS. Microsoft operates the application and platform. The customer still protects data, configures sharing, and gives access to the correct users.

## Exam trap

**“In SaaS, Microsoft is responsible for all security.”** False. Identities, access decisions, endpoints, and organizational data remain customer responsibilities.

## Scenario method

When answering a shared-responsibility question:

1. Identify the service model.
2. Identify the layer in question.
3. Ask whether the provider operates that layer.
4. Separate platform operation from customer configuration and data responsibility.

Example: "Who patches Windows inside an Azure VM?" A VM is IaaS, and the guest OS remains the customer's responsibility.

Example: "Who replaces a failed physical host under the VM?" Microsoft operates the Azure physical infrastructure.

Example: "Who decides which employee can read a document in Microsoft 365?" The customer controls identities, sharing, and data access.

## Official reference

[Shared responsibility in the cloud — Microsoft Learn](https://learn.microsoft.com/azure/security/fundamentals/shared-responsibility)
