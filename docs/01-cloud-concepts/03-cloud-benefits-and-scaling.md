# Cloud benefits and scaling

The exam often describes a business outcome and asks which cloud benefit it represents.

## Core benefits

| Benefit | What it means | Exam clue |
|---|---|---|
| High availability | Keep a service accessible and minimize downtime | Uptime, SLA, continue serving users |
| Scalability | Add or remove capacity | More CPU or more instances |
| Elasticity | Adjust capacity dynamically as demand changes | Automatic response to a temporary spike |
| Reliability | Recover from failures and continue operating | Resilience, redundancy, failover |
| Predictability | Forecast performance and cost | Stable performance, budgets, cost estimates |
| Agility | Provision and change resources quickly | Deploy in minutes |
| Governance | Enforce organizational standards | Compliance and approved configurations |
| Manageability | Manage resources through portals, commands, APIs, monitoring, and automation | Centralized or automated management |

## Vertical and horizontal scaling

### Vertical: scale up or down

Change the size of one resource.

```text
VM: 2 vCPU, 8 GB RAM
          ↓ scale up
VM: 8 vCPU, 32 GB RAM
```

Clue: **more CPU or memory for the existing VM**.

### Horizontal: scale out or in

Change the number of instances.

```text
2 VMs → scale out → 8 VMs
8 VMs → scale in  → 2 VMs
```

Clue: **add or remove instances**.

## Important distinctions

- Scalability is the ability to change capacity; elasticity emphasizes responding dynamically to demand.
- High availability focuses on uptime; disaster recovery focuses on restoring service after a major failure.
- Reliability can use availability, redundancy, backup, and recovery, but these terms are not interchangeable.

## High availability and SLA thinking

High availability is an architectural outcome, not simply a product name.

Common techniques include:

- multiple application instances;
- load balancing;
- availability zones;
- health probes and automatic failover;
- redundant data copies;
- removal of single points of failure.

An SLA is a provider commitment for a defined service configuration and measurement period. It does not guarantee that the entire application meets the same percentage.

If an application depends on several components, its end-to-end availability depends on the architecture and on how those dependencies behave together.

**Exam trap:** placing one VM in one availability zone does not make the application zone-resilient. The workload needs redundant instances or a zone-redundant service.

## Scalability versus performance

Scaling adds capacity, but it does not automatically repair inefficient code or a database bottleneck.

Before scaling, identify the limiting component:

```text
High CPU on one VM       → scale up or optimize
Too many web requests    → scale out behind load balancing
Database connection cap → scale database or redesign access
Temporary demand spike  → autoscale / elasticity
```

Every resource has service limits and quotas. A theoretically scalable architecture can still fail to scale if quota, regional capacity, dependencies, or application design impose a limit.

## Reliability, resilience, and disaster recovery

| Concept | Focus | Example |
|---|---|---|
| Reliability | System performs correctly over time | Redundant components and tested recovery |
| Resilience | Withstand and recover from failure | Fail over when one zone becomes unavailable |
| High availability | Minimize service interruption | Multiple healthy instances serve traffic |
| Disaster recovery | Restore after major disruption | Recover workload in another region |
| Backup | Recover data from a point in time | Restore a deleted or corrupted database |

Redundancy is not automatically backup. A deletion or corruption can replicate to redundant copies, while backup preserves recoverable historical state.

## Predictability in practice

### Performance predictability

Use service tiers, capacity planning, monitoring, load tests, and autoscale rules to understand expected behavior under load.

### Cost predictability

Use the Pricing Calculator before deployment, then budgets, Cost Analysis, tags, and forecasts during operation.

Predictability does not mean price or performance can never change. It means teams have tools and models to plan and observe them.

## Security and governance benefits

Cloud platforms provide built-in capabilities such as centralized identity, encryption options, Policy, Defender for Cloud, monitoring, and physical datacenter security.

These capabilities create a strong foundation, but the customer must select, configure, and operate them according to the shared responsibility model.

## Manageability: of the cloud and in the cloud

### Management of the cloud

Capabilities built into services:

- autoscaling;
- health monitoring;
- templates and automation;
- backup and recovery options;
- automatic platform maintenance for managed services.

### Management in the cloud

Ways administrators control Azure:

- portal;
- CLI and PowerShell;
- Cloud Shell;
- APIs and SDKs;
- ARM templates and Bicep.

## Exam traps

- Increasing a VM from 4 to 16 vCPUs is **scale up**, not scale out.
- Adding identical VMs is **scale out**, not scale up.
- Autoscaling can help performance and cost, but it does not guarantee that an application is highly available.
- Redundant storage is not the same as backup.
- An SLA for one component is not automatically the SLA for the whole application.
- Scale out requires the application to work correctly across multiple instances.

## Official reference

[Describe the benefits of cloud services — Microsoft Learn](https://learn.microsoft.com/training/modules/describe-benefits-use-cloud-services/)
