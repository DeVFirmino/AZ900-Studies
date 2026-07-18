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

## Exam traps

- Increasing a VM from 4 to 16 vCPUs is **scale up**, not scale out.
- Adding identical VMs is **scale out**, not scale up.
- Autoscaling can help performance and cost, but it does not guarantee that an application is highly available.

## Official reference

[Describe the benefits of cloud services — Microsoft Learn](https://learn.microsoft.com/training/modules/describe-benefits-use-cloud-services/)
