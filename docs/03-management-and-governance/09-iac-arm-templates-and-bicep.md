# Infrastructure as code, Azure Resource Manager, ARM templates, and Bicep

Infrastructure as code (IaC) defines infrastructure in versioned files so environments can be deployed repeatedly and consistently.

## Azure Resource Manager

Azure Resource Manager (ARM) is Azure's management and deployment service—the control plane through which resource-management requests are processed.

```text
Portal / CLI / PowerShell / SDK / Template
                    ↓
          Azure Resource Manager
          ├── Authenticate identity
          ├── Check RBAC
          ├── Evaluate Policy
          ├── Enforce locks
          └── Send operation to resource provider
                    ↓
           VM / Storage / VNet / Database
```

ARM provides a consistent management layer for:

- creating, updating, and deleting resources;
- organizing resources into resource groups;
- applying tags, locks, RBAC, and Policy at scopes;
- tracking deployments;
- deploying declarative templates.

The Azure portal is not ARM. The portal is an interface that sends requests through ARM.

## Infrastructure as code

IaC replaces repeated manual configuration with code stored alongside normal software-development artifacts.

Benefits:

- **repeatability:** recreate development, test, and production environments;
- **consistency:** reduce configuration drift and manual differences;
- **version control:** review who changed infrastructure and why;
- **automation:** integrate deployments with CI/CD;
- **testing:** validate syntax, policy compliance, and expected changes;
- **recovery:** rebuild known infrastructure from source definitions.

## Declarative versus imperative

### Declarative

Describe the desired state:

> Create a storage account with this name, region, redundancy, and tags.

ARM templates and Bicep are declarative. Azure determines the operations and dependency order needed to reach the requested state.

### Imperative

Describe a sequence of commands:

```text
Create resource group
Then create VNet
Then create subnet
Then create VM
```

CLI and PowerShell scripts are commonly imperative, although they can deploy declarative templates too.

## ARM templates

An ARM template is a declarative JSON document.

Core sections can include:

- parameters for deployment-time input;
- variables for reusable values;
- resources to deploy;
- outputs returned after deployment.

Simplified example:

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "location": { "type": "string" }
  },
  "resources": []
}
```

ARM templates are powerful but JSON can become verbose when expressions and dependencies grow.

## Bicep

Bicep is Azure's domain-specific declarative language for deploying Azure resources. It offers concise syntax, type checking, modules, and tooling while using ARM as the deployment engine.

Simplified example:

```bicep
param location string = resourceGroup().location

resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: 'examplestorage1234'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}
```

Bicep is compiled into the ARM JSON representation for deployment. It does not bypass ARM, RBAC, Policy, or locks.

## Idempotency

Declarative deployments are designed to be repeatable. Reapplying the same desired state should not create duplicate resources simply because the deployment runs again.

However, idempotent does not mean risk-free:

- changing the desired definition can update or replace resources;
- deleting declarations can have different effects depending on deployment method and mode;
- resource names, locations, and immutable properties can constrain changes;
- Policy or locks can block the deployment.

Always preview and review changes before production deployments.

## Dependencies and parallel deployment

ARM analyzes resource dependencies. Independent resources can be deployed in parallel, while explicitly or implicitly dependent resources are sequenced.

```text
VNet
└── Subnet
    └── NIC
        └── VM
```

## Deployment scopes

Templates and Bicep can target scopes such as:

- resource group;
- subscription;
- management group;
- tenant.

The deployment identity needs appropriate RBAC permissions at the target scope, and the result must comply with Policy and locks.

## Tool comparison

| Requirement | Best fit |
|---|---|
| Graphical one-time deployment | Azure portal |
| Repeatable declarative Azure deployment | Bicep or ARM template |
| JSON Azure template | ARM template |
| Concise Azure-native IaC language | Bicep |
| Run a sequence of administrative commands | CLI or PowerShell script |
| Azure management and deployment control plane | Azure Resource Manager |

## Scenario

A team needs identical networking and storage environments for development, test, and production, reviewed through Git pull requests.

**Best fit:** define the resources with **Bicep or ARM templates** and use a controlled deployment pipeline.

## Exam clues

- Consistent management layer → **Azure Resource Manager**.
- Declarative JSON → **ARM template**.
- Declarative concise Azure language → **Bicep**.
- Repeatable environments stored in Git → **infrastructure as code**.
- Portal, CLI, and PowerShell bypass ARM → **false**.

## Check yourself

**Statement:** Bicep deployments do not need Azure RBAC permission because Bicep is infrastructure as code.

**Answer:** False. Bicep is deployed through ARM, which enforces identity, authorization, Policy, and locks.

## Official references

- [Azure Resource Manager overview](https://learn.microsoft.com/azure/azure-resource-manager/management/overview)
- [ARM template structure](https://learn.microsoft.com/azure/azure-resource-manager/templates/syntax)
- [What is Bicep?](https://learn.microsoft.com/azure/azure-resource-manager/bicep/overview)
- [Infrastructure as code](https://learn.microsoft.com/devops/deliver/what-is-infrastructure-as-code)
