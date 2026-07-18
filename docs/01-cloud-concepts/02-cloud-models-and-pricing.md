# Cloud models and pricing

Deployment models describe **where the environment runs and who uses it**.

## Public, private, and hybrid cloud

| Model | Meaning | Typical clue |
|---|---|---|
| Public cloud | A third-party provider operates shared physical infrastructure with logical isolation between customers | Avoid buying hardware; provision quickly |
| Private cloud | Cloud environment dedicated to one organization | Dedicated environment; maximum infrastructure control |
| Hybrid cloud | Private/on-premises infrastructure is connected to a public cloud | Keep some workloads locally and place others in Azure |

### Common trap: hybrid versus multicloud

- Azure + an on-premises datacenter = **hybrid cloud**.
- Azure + another public cloud provider = **multicloud**.
- An environment can be both hybrid and multicloud.

## Consumption-based pricing

In a consumption-based model, charges follow measured usage. The billing unit depends on the service: time, storage capacity, operations, executions, data transfer, or another meter.

**Pay-as-you-go does not mean every resource stops billing when it is idle.** A running VM can incur compute charges even when no user is connected.

## CapEx versus OpEx

| CapEx | OpEx |
|---|---|
| Capital expenditure | Operational expenditure |
| Upfront purchase of long-lived assets | Ongoing payment for used services |
| Servers, racks, buildings, cooling | Cloud consumption and subscriptions |
| Capacity is purchased in advance | Spending can follow demand |

Cloud commonly shifts spending from CapEx toward OpEx, but Azure also offers commitment-based discounts such as reservations.

## Scenario decisions

- A company must keep regulated data locally but wants cloud capacity for demand spikes → **hybrid cloud**.
- A company wants infrastructure dedicated to only itself → **private cloud**.
- A startup wants resources immediately without buying servers → **public cloud**.

## Official reference

[Describe cloud models — Microsoft Learn](https://learn.microsoft.com/training/modules/describe-cloud-compute/5-define-cloud-models)
