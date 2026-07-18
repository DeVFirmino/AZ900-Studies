# Application hosting: Web Apps, containers, and virtual machines

Once you know **what** runs (web app, API, container, custom server), choose **where** to host it based on control, management effort, and scenario keywords.

## Compare hosting options

| Requirement | Likely answer |
|---|---|
| Host a web app or API without managing the OS | Azure App Service (Web Apps) |
| Run containers with orchestration | Azure Kubernetes Service |
| Run a simple container without cluster management | Azure Container Instances |
| Full control of OS and installed software | Azure Virtual Machines |
| Event-driven code with no server admin | Azure Functions |

## Azure App Service

App Service is a **PaaS** platform for hosting web apps, REST APIs, and mobile backends.

Choose App Service when the scenario mentions:

- deploy code or containers to a managed web platform;
- built-in scaling, deployment slots, and HTTPS;
- no OS patching by the development team;
- .NET, Java, Node.js, Python, PHP, or containerized web workloads on a managed platform.

App Service is the default AZ-900 answer for **managed web application hosting**.

## Containers as application hosting

Containers can run on:

- **App Service** for web-focused container hosting;
- **Container Instances** for simpler, shorter-lived runs;
- **AKS** for larger microservice architectures.

**Exam clue:** "web app without managing servers" usually points to **App Service**, not AKS, unless the scenario emphasizes orchestration across many services.

## Virtual Machines for applications

Use VMs when the application needs:

- a specific OS configuration;
- software that App Service does not support;
- maximum control comparable to an on-premises server.

The trade-off is more patching, scaling, and availability design work for the customer.

## Scenario

A team has a Node.js REST API and wants HTTPS, deployment slots, and autoscale without managing virtual machines.

**Best fit:** **Azure App Service**.

## Scenario

A company runs a custom ERP system that requires a specific Windows Server role and third-party drivers.

**Best fit:** **Azure Virtual Machines**.

## Exam clues

- Managed web platform, no OS patching → **App Service**.
- Many identical web servers behind a load balancer with VM control → **VMSS on VMs**, not App Service.
- Microservices fleet with Kubernetes → **AKS**.
- Legacy server with custom OS setup → **VM**.

## Official references

- [Azure App Service overview](https://learn.microsoft.com/azure/app-service/overview)
- [Choose an Azure compute service — Microsoft Learn](https://learn.microsoft.com/training/modules/describe-azure-compute-networking-services/2-describe-compute-services)
