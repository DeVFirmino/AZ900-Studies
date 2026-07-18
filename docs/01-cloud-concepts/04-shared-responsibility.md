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

## Scenarios

### SQL Server on an Azure VM

This is IaaS. Microsoft manages the physical infrastructure. The customer manages the guest operating system, patches, installed SQL Server, accounts, configuration, and data.

### Azure SQL Database

This is PaaS. Microsoft manages the infrastructure, operating system, and database platform. The customer manages the data, identities, access, and application-level configuration.

### Microsoft 365

This is SaaS. Microsoft operates the application and platform. The customer still protects data, configures sharing, and gives access to the correct users.

## Exam trap

**“In SaaS, Microsoft is responsible for all security.”** False. Identities, access decisions, endpoints, and organizational data remain customer responsibilities.

## Official reference

[Shared responsibility in the cloud — Microsoft Learn](https://learn.microsoft.com/azure/security/fundamentals/shared-responsibility)
