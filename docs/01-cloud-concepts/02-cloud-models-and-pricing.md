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

## Compare deployment models deeply

| Decision factor | Public cloud | Private cloud | Hybrid cloud |
|---|---|---|---|
| Physical ownership | Cloud provider | One organization or dedicated provider environment | Combination |
| Initial hardware purchase | Usually avoided by customer | Often required or contractually dedicated | Depends on each side |
| Elastic scale | Usually highest | Limited by owned/dedicated capacity | Can use public cloud for additional capacity |
| Infrastructure control | Lowest physical control | Highest physical/custom control | Workload-specific balance |
| Operational responsibility | Shared with provider | Organization manages more | Split across environments |
| Common scenario | New digital service or variable demand | Strict dedicated-infrastructure requirement | Gradual migration, data locality, or cloud bursting |

### Public cloud isolation

Public cloud is multitenant at provider scale, but tenants are logically isolated. A customer does not gain access to another customer's resources simply because physical infrastructure is pooled.

### Private cloud is still cloud

A virtualized datacenter is not automatically a private cloud. A private-cloud design normally includes cloud characteristics such as self-service, automation, resource pooling, and measured or allocated capacity.

### Hybrid requires integration

Simply owning on-premises servers and separately using Azure does not create a useful hybrid architecture. Hybrid scenarios normally integrate identity, networking, data, management, or application workflows across the environments.

Examples:

- Microsoft Entra identities used with on-premises directories;
- VPN Gateway or ExpressRoute connecting networks;
- Azure Arc governing servers outside Azure;
- applications split between local and Azure tiers.

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

## Cloud pricing patterns

### Consumption pricing

Pay for measured usage with minimal long-term commitment. This maximizes flexibility but may have a higher unit price than commitment models.

### Fixed or provisioned capacity

Some services charge for provisioned capacity whether it is fully used or not. The service can still be cloud computing even if its meter is not per request.

### Commitment discounts

Reservations and savings plans exchange flexibility for a lower effective price on eligible usage. They are billing benefits, not separate cloud deployment models.

### Serverless consumption

Eligible serverless plans can charge based on executions, duration, or consumed capacity. Other serverless hosting plans may use reserved or always-ready capacity. Avoid saying serverless always has one exact billing model.

## Total cost considerations

Compare more than the service price:

- migration and data-transfer cost;
- staff skills and operational effort;
- licensing and support;
- backup and disaster recovery;
- compliance and security controls;
- cost of unused capacity;
- cost of downtime and slow delivery.

Cloud can reduce large upfront purchases and improve flexibility, but financial benefit depends on architecture and ongoing governance.

## Scenario decisions

- A company must keep regulated data locally but wants cloud capacity for demand spikes → **hybrid cloud**.
- A company wants infrastructure dedicated to only itself → **private cloud**.
- A startup wants resources immediately without buying servers → **public cloud**.

## Exam elimination method

Ask these questions in order:

1. Is infrastructure dedicated to one organization? → private cloud may fit.
2. Are on-premises/private and public environments integrated? → hybrid cloud.
3. Are multiple public providers involved? → multicloud.
4. Does the question emphasize upfront assets or ongoing consumption? → CapEx versus OpEx.
5. Does it claim cloud is always cheaper? → reject the absolute claim.

## Official reference

[Describe cloud models — Microsoft Learn](https://learn.microsoft.com/training/modules/describe-cloud-compute/5-define-cloud-models)
