# Azure portal, Cloud Shell, Azure CLI, and Azure PowerShell

Azure provides graphical, command-line, and programmatic management experiences. The exam tests whether you can distinguish the **interface**, the **execution environment**, and the **command tool**.

## The key distinction

```text
Azure portal     = graphical web interface
Azure Cloud Shell = browser-hosted command environment
Azure CLI         = commands that usually start with az
Azure PowerShell  = PowerShell Az module and Verb-AzNoun cmdlets
```

Cloud Shell is not a third command language. It is a place where Azure CLI or Azure PowerShell can run.

## Azure portal

The Azure portal is a web-based graphical interface for creating, configuring, monitoring, and deleting Azure resources.

Use it when:

- learning or exploring a service;
- completing a one-time visual task;
- viewing dashboards, charts, and configuration blades;
- using a guided workflow.

Strengths:

- visual and discoverable;
- no command syntax required;
- integrated access to IAM, monitoring, cost, and support experiences.

Limitations:

- repeated manual work is slow and error-prone;
- click-by-click actions are difficult to version and reproduce;
- automation is usually better through CLI, PowerShell, templates, SDKs, or APIs.

## Azure Cloud Shell

Azure Cloud Shell is a browser-accessible shell managed by Microsoft. It provides authenticated access to Azure management tools without requiring you to install them on the current computer.

Cloud Shell offers:

- **Bash**, commonly used with Azure CLI;
- **PowerShell**, used with Azure PowerShell and also capable of running Azure CLI;
- preinstalled Azure tools;
- an authenticated session connected to the selected Azure account and subscription context.

Depending on the Cloud Shell configuration, files can use persistent storage or an ephemeral session. Do not treat the shell environment as permanent application hosting.

**Exam clue:** run Azure commands from a browser on a temporary computer without installing tools → **Azure Cloud Shell**.

## Azure CLI

Azure CLI is a cross-platform command-line tool. Commands normally follow this pattern:

```bash
az <service> <action> --parameter value
```

Examples:

```bash
az login
az group list
az vm list --output table
az storage account show --name examplestorage --resource-group rg-demo
```

Recognition clues:

- command begins with `az`;
- long parameters commonly use `--name`;
- often used in Bash and shell scripts;
- JSON is a common output format, with table and other formats available.

Azure CLI runs on Windows, macOS, Linux, and Cloud Shell. It is not restricted to Bash.

## Azure PowerShell

Azure PowerShell is the **Az PowerShell module** for managing Azure resources.

Cmdlets use PowerShell's Verb-Noun pattern:

```powershell
Connect-AzAccount
Get-AzResourceGroup
Get-AzVM
New-AzResourceGroup -Name rg-demo -Location westeurope
```

Recognition clues:

- cmdlet contains `Az`;
- verbs include Get, New, Set, Remove, Start, and Stop;
- parameters commonly use one dash, such as `-Name`;
- results are PowerShell objects that work naturally with pipelines and properties.

PowerShell is the shell and automation language. Azure PowerShell is the Az module installed inside PowerShell.

## Compare the tools

| Scenario | Best fit |
|---|---|
| Visual one-time configuration | Azure portal |
| Browser terminal with no local installation | Azure Cloud Shell |
| Bash-oriented automation and `az` syntax | Azure CLI |
| PowerShell cmdlets and object pipelines | Azure PowerShell |
| Repeatable declarative infrastructure | Bicep or ARM template, deployed through portal/CLI/PowerShell |

## Authentication and authorization

Signing in proves identity, but management actions still require authorization.

```text
Sign in with CLI or PowerShell
↓
Microsoft Entra ID authenticates identity
↓
Azure RBAC checks permission at the target scope
↓
Azure Policy evaluates the requested configuration
↓
Azure Resource Manager processes the request
```

Using Cloud Shell does not bypass RBAC, Policy, locks, or other governance controls.

## Local installation versus Cloud Shell

| Local CLI/PowerShell | Cloud Shell |
|---|---|
| Install and update tools yourself | Microsoft maintains the hosted tool environment |
| Works from local scripts and automation runners | Opens quickly in a browser |
| Can integrate with local files and development tools | Useful on unmanaged or temporary computers |
| Authentication must be established locally | Browser session is integrated with Azure sign-in |

## Scenario

An administrator receives a borrowed laptop and must immediately run `Get-AzVM` without installing software.

**Best fit:** open **Azure Cloud Shell**, select PowerShell, and run Azure PowerShell.

## Exam clues

- Menus, dashboards, and browser GUI → **Azure portal**.
- Terminal in the browser → **Cloud Shell**.
- Command starts with `az` → **Azure CLI**.
- Command resembles `Get-AzVM` → **Azure PowerShell**.
- Cloud Shell replaces CLI and PowerShell → **false; it hosts them**.

## Check yourself

**Statement:** Azure CLI can only run in Bash on Linux.

**Answer:** False. Azure CLI is cross-platform and can run from Bash, PowerShell, command prompts, automation agents, and Cloud Shell.

## Official references

- [Azure portal documentation](https://learn.microsoft.com/azure/azure-portal/)
- [Azure Cloud Shell overview](https://learn.microsoft.com/azure/cloud-shell/overview)
- [Azure CLI overview](https://learn.microsoft.com/cli/azure/what-is-azure-cli)
- [Azure PowerShell overview](https://learn.microsoft.com/powershell/azure/what-is-azure-powershell)
