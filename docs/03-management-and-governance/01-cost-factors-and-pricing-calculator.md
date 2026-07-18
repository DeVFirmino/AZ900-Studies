# Cost factors and the Azure Pricing Calculator

Azure does not have one universal price. A solution's cost is the result of multiple meters, configuration choices, discounts, and usage patterns. AZ-900 questions usually ask **which factor changes cost** or **which tool estimates cost before deployment**.

## The cost model

```text
Estimated Azure cost
├── Service and SKU selected
├── Quantity and duration of use
├── Region
├── Data transfer
├── Software and support charges
└── Discounts and commitments
```

## Factors that affect Azure cost

### Resource type and service

Different services use different billing meters.

| Service | Example meters |
|---|---|
| Virtual Machines | VM size, operating system, runtime, disks, and network transfer |
| Blob Storage | Capacity, redundancy, access tier, operations, retrieval, and transfer |
| Azure Functions | Executions, execution duration, memory, and hosting plan |
| Azure SQL | Compute tier, provisioned/serverless model, storage, and backup retention |

**Exam trap:** creating a VM can also create separately billed supporting resources such as managed disks and a public IP address.

### Service tier, SKU, and size

A larger VM, premium disk, or higher database tier normally costs more because it provides additional capacity, performance, or features.

- **Scale up:** increases the capacity and usually the price of one resource.
- **Scale out:** adds instances, increasing aggregate consumption.
- **Scale in/down:** can reduce cost when capacity is no longer needed.

### Consumption and time

Pay-as-you-go charges follow the service's meter. Turning off an application does not necessarily stop every charge.

- A stopped but allocated VM can continue to incur compute charges.
- A **deallocated** VM stops compute billing, but disks and other retained resources can still cost money.
- Stored data continues to incur capacity charges even when it is not read.

### Region

Prices can differ by Azure region because infrastructure, energy, taxes, demand, and service availability differ. Choose a region for compliance, latency, resilience, and cost—not cost alone.

### Data transfer

The direction and destination of network traffic matter.

- Inbound data transfer to Azure is often free, with service-specific exceptions.
- Outbound transfer from Azure can be charged.
- Transfer between regions or availability zones can incur charges depending on the services and traffic path.

**Exam rule:** never assume all network transfer is free. Check the relevant service pricing page.

### Software, marketplace, and support

Costs can include:

- Windows Server or SQL Server licensing;
- third-party Azure Marketplace software;
- support plans;
- managed-service or partner charges.

## Ways to reduce cost

| Option | Best fit | Main trade-off |
|---|---|---|
| Pay-as-you-go | Uncertain or short-term usage | Highest flexibility, usually no commitment discount |
| Azure reservations | Predictable eligible resources for one or three years | Commitment reduces flexibility |
| Azure savings plan for compute | Predictable compute spend across eligible services | Hourly spend commitment |
| Azure Spot Virtual Machines | Interruptible, fault-tolerant workloads | Azure can evict the VM |
| Azure Hybrid Benefit | Existing eligible Windows Server or SQL Server licenses | Requires qualifying licenses |
| Right-sizing and autoscale | Match capacity to real demand | Requires monitoring and correct rules |

Reservations and savings plans are billing discounts; they do not automatically redesign, secure, or scale the workload.

## Azure Pricing Calculator

The Azure Pricing Calculator estimates the expected cost of a proposed Azure solution **before deployment**.

Typical workflow:

1. Add the Azure services the architecture needs.
2. Select regions, tiers, sizes, quantities, and usage hours.
3. Configure storage, transactions, data transfer, licensing, and support assumptions.
4. Compare pay-as-you-go with eligible commitment discounts.
5. Save, export, or share the estimate.

The result is an estimate, not a bill or guarantee. Actual cost can differ because usage, prices, exchange rates, taxes, discounts, and architecture change.

## Tool comparison

| Question | Tool |
|---|---|
| What might this Azure design cost before deployment? | Azure Pricing Calculator |
| Which Azure resources are generating actual charges? | Cost Analysis in Microsoft Cost Management |
| How does current on-premises cost compare with a cloud migration? | Total Cost of Ownership (TCO) Calculator or migration assessment |
| Which changes could reduce cost in deployed resources? | Azure Advisor and Cost Management recommendations |

## Scenario

A team is deciding between two VM sizes in West Europe and North Europe before creating anything.

**Best fit:** configure both options in the **Azure Pricing Calculator** and compare the assumptions.

## Exam clues

- Estimate before deployment → **Pricing Calculator**.
- Actual historical or current cloud spend → **Cost Management / Cost Analysis**.
- Long-term predictable eligible workload → **reservation or savings plan**.
- Existing eligible Microsoft licenses → **Azure Hybrid Benefit**.
- Batch workload can tolerate eviction → **Spot VM**.

## Check yourself

**Statement:** Deallocating a VM removes every cost associated with it.

**Answer:** False. Compute billing stops, but retained disks, snapshots, public IP configurations, or other supporting resources can continue to incur charges.

## Official references

- [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)
- [Plan and manage Azure costs](https://learn.microsoft.com/azure/cost-management-billing/costs/cost-mgt-best-practices)
- [Azure savings options](https://learn.microsoft.com/azure/cost-management-billing/savings-plan/)
