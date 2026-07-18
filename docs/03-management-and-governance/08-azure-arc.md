# Azure Arc

Azure Arc extends Azure management, governance, and selected Azure services to resources that run **outside Azure**.

## The problem Azure Arc addresses

Organizations often operate resources across:

```text
Azure
├── On-premises datacenters
├── Branch and edge locations
└── Other public clouds
```

Without a common control plane, each environment can develop different inventory, policy, monitoring, and security processes.

Azure Arc projects supported external resources into Azure so they can participate in Azure management experiences.

## What Azure Arc can connect

Azure Arc capabilities include support for categories such as:

- servers running outside Azure;
- Kubernetes clusters in other environments;
- selected data services and infrastructure platforms;
- VMware vSphere and System Center Virtual Machine Manager environments through applicable Arc features.

Exact Arc capabilities depend on resource type, region, licensing, and connected-service configuration. AZ-900 focuses on the purpose, not installation steps.

## Azure Arc-enabled servers

An Arc-enabled server is a Windows or Linux machine outside Azure that is connected through the Azure Connected Machine agent.

After connection, it appears in Azure as a resource with an Azure Resource Manager ID. Depending on configuration, teams can use Azure capabilities such as:

- inventory and organization with subscriptions, resource groups, and tags;
- Azure Policy guest configuration or machine configuration;
- monitoring and update-management integrations;
- Defender for Cloud integrations;
- RBAC-based management access.

The server continues running in its original location. Arc does not turn it into an Azure VM.

## Arc-enabled Kubernetes

Connecting a Kubernetes cluster can provide centralized inventory, governance, GitOps, monitoring, and security integrations for supported clusters outside Azure.

**Exam clue:** apply Azure governance to Kubernetes running on-premises or in another cloud → **Azure Arc**.

## What Azure Arc does not mean

Azure Arc does **not** automatically:

- migrate a server into Azure;
- copy its data into an Azure region;
- make an external server an Azure VM;
- provide network connectivity like VPN Gateway or ExpressRoute;
- replace backup, disaster recovery, or patching design;
- make every Azure service work on every connected resource.

## Azure Arc compared with related services

| Requirement | Best fit |
|---|---|
| Manage external servers with Azure governance | Azure Arc |
| Assess and migrate servers into Azure | Azure Migrate |
| Connect an on-premises network privately to Azure | ExpressRoute |
| Replicate VMs for disaster recovery | Azure Site Recovery |
| Monitor supported hybrid resources | Azure Monitor, often integrated through Arc |

## Control-plane flow

```text
External server or cluster
↓ agent / connector
Azure Arc resource representation
↓
Azure Resource Manager
├── RBAC
├── Policy
├── Tags
├── Monitor integrations
└── Defender integrations
```

The resource representation and metadata live in Azure, while the workload remains in its original environment unless separately migrated.

## Scenario

A company has Linux servers in its datacenter and AWS. It wants a unified Azure inventory and consistent governance without migrating them.

**Best fit:** connect the servers with **Azure Arc-enabled servers**.

## Scenario

A company wants to calculate readiness and move 200 VMware machines into Azure.

**Best fit:** **Azure Migrate**, not Arc. Arc is for extending management; Migrate is for assessment and migration.

## Exam clues

- Azure management for on-premises and multicloud resources → **Azure Arc**.
- External resource receives an Azure Resource Manager identity → **Azure Arc**.
- Move workload into Azure → **Azure Migrate**.
- Arc automatically relocates the workload → **false**.

## Check yourself

**Statement:** Connecting a physical server to Azure Arc converts it into an Azure Virtual Machine.

**Answer:** False. The machine remains outside Azure and gains an Azure resource representation plus supported management integrations.

## Official references

- [Azure Arc overview](https://learn.microsoft.com/azure/azure-arc/overview)
- [Azure Arc-enabled servers overview](https://learn.microsoft.com/azure/azure-arc/servers/overview)
- [Azure Arc-enabled Kubernetes overview](https://learn.microsoft.com/azure/azure-arc/kubernetes/overview)
