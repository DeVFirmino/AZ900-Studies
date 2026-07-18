# IaaS, PaaS, SaaS, and serverless

Service models describe **how much the provider manages for you**.

| Model | Customer focus | Azure/provider focus | Example |
|---|---|---|---|
| IaaS | OS, applications, configuration, data | Physical infrastructure and virtualization | Azure Virtual Machines |
| PaaS | Application code, data, access | Infrastructure, OS, runtime, managed platform | Azure App Service, Azure SQL Database |
| SaaS | Users, data, access settings | Application, platform, infrastructure | Microsoft 365 |

## The managed stack

```text
Layer                  IaaS          PaaS          SaaS
───────────────────────────────────────────────────────
Data                   Customer      Customer      Customer
Application            Customer      Customer      Provider
Runtime/middleware     Customer      Provider      Provider
Operating system       Customer      Provider      Provider
Virtualization         Provider      Provider      Provider
Physical infrastructure Provider     Provider      Provider
```

Identity, access, data classification, and endpoint security remain customer concerns across all three models.

## IaaS: configure the server

Choose Infrastructure as a Service when the scenario requires:

- control of the operating system;
- installation of custom or legacy software;
- a lift-and-shift server migration;
- custom server configuration.

IaaS offers the most control of the three models and the most customer administration.

### IaaS operational checklist

The customer normally handles:

- guest OS hardening and patching;
- installed software and runtime updates;
- backup and recovery design;
- malware protection and host configuration;
- VM availability and scaling architecture;
- network rules and exposed ports;
- data, identities, and permissions.

Microsoft operates the datacenter, physical hosts, physical network, and hypervisor.

### IaaS scenario

A vendor application requires a specific Windows Server version, a custom driver, and administrator access to the OS.

**Best fit:** Azure Virtual Machines as **IaaS**.

## PaaS: publish the application

Choose Platform as a Service when the team wants to:

- focus on code and data;
- host a web app or API without patching an OS;
- use a managed database;
- reduce platform maintenance.

### PaaS trade-offs

Benefits:

- less patching and platform administration;
- built-in scaling and availability options;
- faster application delivery;
- integrated deployment, identity, and monitoring features.

Trade-offs:

- less control over the operating system and runtime;
- supported languages, versions, networking, or extensions can be constrained;
- migration might require application changes.

### PaaS scenario

A team wants to deploy a REST API, configure autoscale, and use deployment slots without maintaining Windows or Linux servers.

**Best fit:** Azure App Service as **PaaS**.

## SaaS: use the software

Choose Software as a Service when users need a ready-made application and the organization does not want to build or operate the application platform.

### SaaS customer responsibilities

The provider runs the application, but the customer still manages:

- user lifecycle and access;
- data classification and sharing;
- tenant-level settings;
- retention and compliance choices;
- endpoint security and user behavior;
- integration configuration.

### SaaS scenario

Employees need email, calendars, document collaboration, and meetings without the company building those applications.

**Best fit:** Microsoft 365 as **SaaS**.

## Serverless

Serverless means the customer does not provision or manage the underlying servers. It does **not** mean no servers exist.

Typical characteristics include:

- event-driven execution;
- automatic scaling;
- highly abstracted infrastructure;
- consumption-based billing on eligible plans.

```text
Blob uploaded → event → Azure Function runs → execution completes
```

Azure Functions is the common AZ-900 example. Billing and always-on behavior depend on the selected hosting plan, so avoid absolute statements such as “serverless always charges only per execution.”

## Serverless execution model

Serverless platforms commonly combine:

- **triggers:** the event that starts execution;
- **bindings/integrations:** connections to queues, storage, databases, or HTTP;
- **automatic allocation:** platform adds or removes execution capacity;
- **stateless design preference:** durable state is stored in external services;
- **managed runtime:** platform operates the underlying hosts and runtime infrastructure.

Long-running workflows, warm instances, networking requirements, and predictable performance can require different hosting plans or related services. "Serverless" describes the infrastructure abstraction, not a guarantee that every workload has zero idle cost or unlimited execution time.

## PaaS versus serverless

Serverless is often treated as a highly managed form of PaaS.

| PaaS application hosting | Serverless function model |
|---|---|
| Usually hosts an application continuously | Commonly invokes code in response to events |
| Scaling follows the hosting plan | Scaling often follows trigger demand |
| App is the deployment unit | Functions or workflows are smaller execution units |
| May reserve always-on instances | Consumption or always-ready plans can be selected |

## Database example

The same database engine can appear in different service models:

- SQL Server installed on an Azure VM → **IaaS**; customer patches OS and SQL Server.
- Azure SQL Database → **PaaS**; Microsoft operates OS and database platform.
- A finished online business application that stores data internally → **SaaS** to its user.

The model depends on what the customer consumes and manages, not only on the product category.

## Decision rule

- Need OS control → **IaaS**.
- Need to deploy code without managing the OS → **PaaS**.
- Need finished software → **SaaS**.
- Need event-triggered code with no server administration → **serverless**.

## Exam elimination method

1. Does the customer need guest OS control? → IaaS.
2. Does the customer supply code but not manage OS/runtime? → PaaS.
3. Does the customer consume a complete application? → SaaS.
4. Is small event-driven code emphasized? → serverless/Functions.
5. Does an answer claim SaaS removes responsibility for data and identities? → reject it.

## Official reference

[Describe cloud service types — Microsoft Learn](https://learn.microsoft.com/training/modules/describe-cloud-service-types/)
