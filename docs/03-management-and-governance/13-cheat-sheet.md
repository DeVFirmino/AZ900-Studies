# Management and Governance exam cheat sheet

Use this page after studying the lessons. It is a recognition aid, not a replacement for understanding scope, limitations, and trade-offs.

## Scenario → answer

### Cost management

| Scenario or clue | Best match |
|---|---|
| Estimate a design before deployment | Azure Pricing Calculator |
| Explore actual cost and trends | Cost Analysis |
| Notify when spending reaches a threshold | Cost Management budget alert |
| Predict that a monthly target will be exceeded | Forecasted-cost budget alert |
| Export detailed cost records regularly | Cost Management scheduled export |
| Label resources by department or environment | Tags |
| Enforce the presence of tags | Azure Policy |
| Existing eligible Windows/SQL licenses | Azure Hybrid Benefit |
| Predictable eligible long-term usage | Reservation or savings plan |
| Interruptible compute workload | Spot Virtual Machines |

### Governance and compliance

| Scenario or clue | Best match |
|---|---|
| Discover and classify data across systems | Microsoft Purview |
| Trace where data came from and how it changed | Purview data lineage |
| What resource configuration is allowed | Azure Policy |
| Report noncompliance without blocking | Audit effect |
| Block a noncompliant deployment | Deny effect |
| Correct supported properties or tags | Modify effect |
| Deploy missing related configuration | DeployIfNotExists |
| Group many policy definitions | Initiative |
| Who can perform a management action | Azure RBAC |
| Prevent deletion but allow modification | CanNotDelete lock |
| Prevent modification and deletion | ReadOnly lock |
| Protect data inside a resource | Backup, soft delete, versioning, immutability, or data permissions |

### Management and deployment

| Scenario or clue | Best match |
|---|---|
| Graphical Azure management | Azure portal |
| Terminal hosted in a browser | Azure Cloud Shell |
| Command begins with `az` | Azure CLI |
| Cmdlet resembles `Get-AzVM` | Azure PowerShell |
| Govern on-premises or multicloud resources from Azure | Azure Arc |
| Assess and move workloads into Azure | Azure Migrate |
| Azure management control plane | Azure Resource Manager |
| Declarative JSON deployment | ARM template |
| Concise Azure-native declarative language | Bicep |
| Versioned repeatable infrastructure | Infrastructure as code |

### Monitoring

| Scenario or clue | Best match |
|---|---|
| Personalized optimization recommendations | Azure Advisor |
| Azure incident affecting your subscriptions | Azure Service Health |
| Health of one specific resource | Resource Health |
| Public overview of broad Azure incidents | Azure Status |
| Numeric time-series telemetry | Azure Monitor metrics |
| Search centralized log records with KQL | Log Analytics |
| Who changed or deleted an Azure resource | Activity Log |
| Notify when a resource signal crosses a threshold | Azure Monitor alert |
| Shared notification or automation target | Action group |
| Web-app requests, failures, dependencies, and traces | Application Insights |

## The four governance questions

```text
WHO may act?                  → Azure RBAC
WHAT configuration is valid? → Azure Policy
CAN it be changed/deleted?    → Resource lock
HOW is it deployed?           → ARM template or Bicep
```

## The four operations questions

```text
What should I improve?       → Advisor
Is Azure having a problem?   → Service Health
What is my resource doing?   → Azure Monitor
What did Azure management do?→ Activity Log
```

## Cost-tool decision flow

```text
No resources exist yet?
└── Estimate with Pricing Calculator

Resources are running?
├── Understand charges → Cost Analysis
├── Notify on target → Budget
├── Allocate by business context → Tags
└── Find optimizations → Advisor / Cost recommendations
```

## Commands at a glance

```text
Azure CLI
az group list
az vm show --name vm01 --resource-group rg01

Azure PowerShell
Get-AzResourceGroup
Get-AzVM -Name vm01 -ResourceGroupName rg01

Cloud Shell
Browser environment that can run either tool
```

## Important limitations

- A budget alerts; it does not automatically stop spending.
- Tags do not grant permissions and are not inherited automatically by ARM resources.
- Cost Management tag inheritance changes cost records, not actual resource tags.
- Policy controls configuration; RBAC controls authorization.
- A lock overrides management permissions until an authorized user removes it.
- Locks primarily protect management-plane operations, not every data-plane operation.
- Purview governs and protects data; Policy governs Azure resource configuration.
- Cloud Shell hosts CLI and PowerShell; it does not replace them.
- Arc extends Azure management; it does not migrate the workload.
- Bicep and ARM templates still pass through ARM and must satisfy RBAC, Policy, and locks.
- Advisor recommends; it does not enforce or automatically apply everything.
- Service Health reports Azure platform events; Monitor observes resource and application telemetry.

## Dangerous absolute statements

Treat these as likely false:

- "A budget guarantees Azure spending cannot exceed the target."
- "Tags are inherited automatically by all child resources."
- "Owners can ignore resource locks."
- "A storage-account lock prevents deletion of every blob."
- "Cloud Shell is a separate command language."
- "Azure Arc moves connected servers into Azure."
- "ARM templates bypass Policy."
- "Advisor automatically fixes every recommendation."
- "Service Health contains all application logs."
