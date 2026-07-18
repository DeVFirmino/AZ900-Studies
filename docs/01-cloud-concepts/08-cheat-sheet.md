# Cloud Concepts exam cheat sheet

## Scenario → answer

| Scenario or clue | Best match |
|---|---|
| Use cloud resources without buying physical servers | Public cloud |
| Environment dedicated to one organization | Private cloud |
| Azure connected to an on-premises datacenter | Hybrid cloud |
| Azure plus another public cloud provider | Multicloud |
| Buy servers upfront | CapEx |
| Pay for ongoing consumption | OpEx |
| Increase CPU or RAM on one VM | Scale up / vertical scaling |
| Add more VM instances | Scale out / horizontal scaling |
| Adjust capacity dynamically with demand | Elasticity |
| Maximize uptime | High availability |
| Recover and continue after failure | Reliability |
| Control and patch the operating system | IaaS |
| Deploy an app without managing the OS | PaaS |
| Use a ready-made application | SaaS |
| Run code in response to an event | Serverless / Azure Functions |
| Separated datacenters within one region | Availability zones |
| Associated Azure regions | Region pair |
| Directory of identities | Microsoft Entra tenant |
| Apply governance to several subscriptions | Management group |
| Billing, quota, and access boundary | Subscription |
| Group resources with one lifecycle | Resource group |

## Three fast comparisons

### Scale

- **Up/down** changes the size of one resource.
- **Out/in** changes the number of resources.

### Service model

- **IaaS:** configure the server.
- **PaaS:** publish the application.
- **SaaS:** use the software.

### Location

- **Datacenter:** physical building.
- **Availability zone:** isolated datacenter group inside a region.
- **Region:** geographic deployment area.
- **Region pair:** relationship used by some services; not automatic replication of everything.

## Dangerous absolute words

Question statements containing **always**, **all**, **automatically**, or **guarantees** deserve extra attention. Common false claims include:

- Cloud always costs less.
- SaaS transfers all security responsibility to Microsoft.
- A region pair automatically replicates every resource.
- One VM placed in a zone is automatically zone resilient.
- A resource group's region forces all its resources into that region.
