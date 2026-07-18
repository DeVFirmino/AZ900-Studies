# What is cloud computing?

Cloud computing is the delivery of computing services over the internet. Instead of buying and maintaining every physical server, an organization requests compute, storage, networking, databases, and other services when needed.

## On-premises versus cloud

| On-premises | Cloud |
|---|---|
| Buy hardware before using it | Rent capacity when needed |
| Large initial investment | Consumption-based spending |
| Provisioning may take weeks | Provisioning may take minutes |
| Maintain the physical datacenter | Provider maintains physical infrastructure |
| Estimate capacity in advance | Scale capacity with demand |

Cloud does **not** mean that resources are automatically free, secure, highly available, or correctly sized. Those outcomes depend on the selected services and configuration.

## Core characteristics of cloud computing

### On-demand self-service

Teams can provision supported resources when needed without waiting for a provider employee to install physical hardware.

Example: a developer creates a test database through the portal or a template, uses it for a week, and removes it.

### Broad network access

Cloud services are reachable through standard networks and interfaces from many client types. Access can be public, private, or hybrid depending on the design.

Broad access does not mean anonymous access. Authentication, authorization, firewalls, and private networking still apply.

### Resource pooling

The provider pools large amounts of compute, storage, and networking capacity. Customers share provider infrastructure while their subscriptions, identities, networks, and data are logically isolated.

Some Azure offerings also provide dedicated hosts or isolated capacity when a workload requires it. Public cloud therefore describes the provider model, not a promise that every physical component is shared.

### Rapid elasticity

Capacity can be added and removed far more quickly than purchasing and installing datacenter hardware. Elasticity is especially useful for temporary or unpredictable demand.

### Measured service

Azure measures service usage through billing meters such as compute time, stored capacity, transactions, executions, and network transfer. The meter depends on the service.

## Cloud is more than remote hosting

Traditional hosting can place a fixed server in someone else's datacenter. Cloud platforms add capabilities such as:

- API-driven provisioning;
- elastic capacity;
- managed platform services;
- global regions and availability features;
- consumption-based meters;
- centralized identity, governance, monitoring, and automation.

## Provisioning, configuration, and operation

These are separate responsibilities:

1. **Provisioning:** create the resource.
2. **Configuration:** set networking, identity, security, performance, and application options.
3. **Operation:** monitor, patch where responsible, back up, optimize, and respond to incidents.

Fast provisioning does not remove the need for correct configuration and ongoing operations.

## Scenario

A retailer expects a short traffic spike during a sale.

- On-premises: buy enough hardware for peak traffic, then leave much of it idle.
- Cloud: add capacity during the sale and remove it afterward.

## Exam clues

Think **cloud computing** when the requirement mentions:

- on-demand resources;
- rapid provisioning;
- avoiding a large hardware purchase;
- increasing or decreasing capacity;
- paying for consumed services.

## Common misconceptions

| Statement | Why it is wrong |
|---|---|
| Cloud means no physical servers | Servers still exist; the provider operates them |
| Every cloud resource is reachable from the internet | Resources can use private endpoints, VNets, firewalls, and private connectivity |
| Cloud automatically provides disaster recovery | Multi-zone or multi-region recovery must be selected and designed |
| Pay-as-you-go means idle resources are free | Billing follows service meters; retained or allocated resources can still cost money |
| The provider owns all security responsibility | Cloud uses a shared responsibility model |

## Decision example

A business needs a new development environment today, expects it to exist for only two weeks, and cannot justify purchasing servers.

Cloud is a strong fit because it provides on-demand provisioning, temporary capacity, automation, and consumption-based billing. The team must still secure, monitor, and remove the environment when finished.

## Check yourself

**Statement:** Moving to the cloud guarantees lower cost.

**Answer:** False. Cloud makes costs more flexible; unused or oversized resources can still be expensive.

## Official reference

[What is cloud computing? — Microsoft Learn](https://learn.microsoft.com/training/modules/describe-cloud-compute/2-what-cloud-compute)
