# Compute choices: VMs, containers, and functions

Azure offers several ways to run code and workloads. The exam tests **which compute option fits a scenario**, not deep implementation details.

## Compare the main options

| Option | You manage | Azure manages | Best when |
|---|---|---|---|
| Virtual Machines (IaaS) | OS, apps, patching, scaling design | Physical hosts and hypervisor | Lift-and-shift, full OS control, legacy apps |
| Azure Container Instances | Container image and app | Underlying host for the container | Simple, quick container runs without orchestrating a cluster |
| Azure Kubernetes Service (AKS) | Containers, manifests, app design | Managed Kubernetes control plane | Container orchestration at scale |
| Azure Functions (serverless) | Function code and triggers | Runtime scaling and underlying infrastructure | Event-driven, short-lived tasks without server admin |

## Virtual Machines

Choose a VM when the scenario mentions:

- control of the operating system;
- installing custom or legacy software;
- migrating an on-premises server with minimal change;
- running software that is not containerized or supported on PaaS.

VMs offer the most control and the most operational responsibility among common compute choices.

## Containers

Containers package an application with its dependencies so it runs consistently across environments.

- **Azure Container Instances (ACI):** run one or more containers without managing cluster infrastructure.
- **Azure Kubernetes Service (AKS):** run and orchestrate many containers with scaling, networking, and deployment automation.

**Exam clue:** need containers without managing servers → **Container Instances** or a managed Kubernetes service such as **AKS**, depending on scale and orchestration needs.

## Azure Functions

Functions run code in response to triggers such as HTTP requests, timers, queue messages, or blob uploads.

Typical serverless clues:

- run code only when an event happens;
- no server administration;
- automatic scaling on eligible plans;
- short-lived processing.

Serverless does **not** mean no servers exist. It means the customer does not provision or manage them.

## Decision flow

```text
Need full OS control or legacy server?
  └── Yes → Virtual Machine
  └── No → Need a long-running web/API platform?
        └── Yes → see Application hosting lesson
        └── No → Event-driven short task?
              └── Yes → Azure Functions
              └── No → Container workload?
                    └── Simple run → Container Instances
                    └── Orchestrated fleet → AKS
```

## Scenario

An image-processing job should run for a few seconds whenever a file is uploaded to storage. The team does not want to patch servers.

**Best fit:** Azure Functions. The upload is the trigger; execution scales with demand.

## Exam clues

- Patch the operating system → **VM**, not Functions or Container Instances alone.
- Upload triggers small code → **Azure Functions**.
- Run a container quickly without a cluster → **Azure Container Instances**.
- Manage many microservices at scale → **AKS**.

## Official references

- [Compare compute options — Microsoft Learn](https://learn.microsoft.com/training/modules/describe-azure-compute-networking-services/2-describe-compute-services)
- [Azure Virtual Machines overview](https://learn.microsoft.com/azure/virtual-machines/overview)
- [Azure Functions overview](https://learn.microsoft.com/azure/azure-functions/functions-overview)
