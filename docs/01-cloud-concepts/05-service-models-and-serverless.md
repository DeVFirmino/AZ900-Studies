# IaaS, PaaS, SaaS, and serverless

Service models describe **how much the provider manages for you**.

| Model | Customer focus | Azure/provider focus | Example |
|---|---|---|---|
| IaaS | OS, applications, configuration, data | Physical infrastructure and virtualization | Azure Virtual Machines |
| PaaS | Application code, data, access | Infrastructure, OS, runtime, managed platform | Azure App Service, Azure SQL Database |
| SaaS | Users, data, access settings | Application, platform, infrastructure | Microsoft 365 |

## IaaS: configure the server

Choose Infrastructure as a Service when the scenario requires:

- control of the operating system;
- installation of custom or legacy software;
- a lift-and-shift server migration;
- custom server configuration.

IaaS offers the most control of the three models and the most customer administration.

## PaaS: publish the application

Choose Platform as a Service when the team wants to:

- focus on code and data;
- host a web app or API without patching an OS;
- use a managed database;
- reduce platform maintenance.

## SaaS: use the software

Choose Software as a Service when users need a ready-made application and the organization does not want to build or operate the application platform.

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

## Decision rule

- Need OS control → **IaaS**.
- Need to deploy code without managing the OS → **PaaS**.
- Need finished software → **SaaS**.
- Need event-triggered code with no server administration → **serverless**.

## Official reference

[Describe cloud service types — Microsoft Learn](https://learn.microsoft.com/training/modules/describe-cloud-service-types/)
