# VM options and required resources

Virtual machines can be deployed individually or in patterns that improve scaling and resilience. These three options appear often on AZ-900 scenario questions.

## Resources required for a virtual machine

An Azure VM depends on supporting resources and configuration choices. At AZ-900 level, recognize these components:

| Component | Purpose |
|---|---|
| VM image and operating system | Defines the starting OS and software image |
| VM size | Determines vCPUs, memory, storage limits, and network capacity |
| Managed OS disk | Persistent disk containing the operating system |
| Optional data disks | Persistent storage for application or business data |
| Virtual network and subnet | Provide the VM's private network location |
| Network interface (NIC) | Connects the VM to the virtual network |
| Private IP address | Enables private communication inside connected networks |
| Optional public IP address | Enables direct internet communication when required |
| Network security group (NSG) | Allows or denies network traffic by rules such as source, port, and protocol |

The VM, disks, public IP, and other supporting resources can have separate charges. A public IP is optional; many production designs use private connectivity or a load balancer instead of exposing a VM directly.

**Exam rule:** a VM needs compute, an OS disk, and network connectivity. Data disks and public IP addresses depend on the scenario.

## Virtual Machine Scale Sets (VMSS)

A scale set creates and manages a **group of VM instances** with centralized scaling, availability, and lifecycle management.

| Orchestration mode | Exam-level distinction |
|---|---|
| Flexible | Recommended mode; can manage identical or mixed VM types and spread instances across zones or fault domains |
| Uniform | Uses a shared VM profile to create a large set of identical instances |

Use VMSS when the scenario mentions:

- many VM instances managed together;
- automatic scale out and scale in;
- load-balanced web or application tiers;
- updating many VMs with a consistent configuration.

**Exam rule:** a group of VMs that scales and is managed together → **Virtual Machine Scale Sets**. If the question specifically says identical instances, it is describing the Uniform pattern.

## Availability sets

An availability set is a logical grouping that spreads VMs across **fault domains** and **update domains** within one region.

| Domain | Purpose |
|---|---|
| Fault domain | Separate groups of hardware that have independent power and networking failure boundaries |
| Update domain | Group VMs so planned maintenance reboots only part of the set at a time |

Availability sets protect against **local hardware and planned maintenance** events inside a region. They do **not** protect against an entire region outage.

**Exam clue:** maximize VM uptime within one region using classic IaaS patterns → **availability set**.

## Availability sets versus availability zones

| Feature | Availability set | Availability zone |
|---|---|---|
| Scope | Within one region, across fault/update domains | Physically separated datacenter groups inside a region |
| Protects against | Correlated hardware, power, network, and planned-maintenance events | Zone-level datacenter failure |
| Common pairing | Individual VMs or smaller deployments | Zone-redundant or zonal VM deployments |

For new designs, Microsoft often recommends zones when the region and service support them. Availability sets remain a valid exam answer for spreading VMs within a region.

## Azure Virtual Desktop (AVD)

Azure Virtual Desktop delivers **Windows desktops and applications** from Azure to users on many devices.

Use AVD when the scenario mentions:

- virtual desktops for remote workers;
- centralized desktop management;
- multi-session Windows experiences in Azure;
- replacing or supplementing traditional VDI.

**Exam rule:** virtual desktops hosted in Azure → **Azure Virtual Desktop**, not a generic VM or App Service.

## Scenario

A web front end runs on identical VMs behind a load balancer. Traffic grows on weekdays and shrinks at night.

**Best fit:** **Virtual Machine Scale Sets** with autoscale rules.

## Scenario

Two legacy application servers must stay available if one server rack fails, but the app cannot yet use zones.

**Best fit:** place the VMs in an **availability set**.

## Exam clues

- VM instances managed together with autoscale and load balancing → **VMSS**.
- Spread VMs across fault and update domains in one region → **availability set**.
- Remote Windows desktops from the cloud → **Azure Virtual Desktop**.
- VM must communicate inside a VNet → **NIC attached to a subnet**, normally with a private IP.
- Persistent operating system storage → **managed OS disk**.

## Official references

- [Virtual Machine Scale Sets overview](https://learn.microsoft.com/azure/virtual-machine-scale-sets/overview)
- [Scale Set orchestration modes](https://learn.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-orchestration-modes)
- [Availability sets overview](https://learn.microsoft.com/azure/virtual-machines/availability-set-overview)
- [Virtual machines and their supporting resources](https://learn.microsoft.com/azure/virtual-machines/overview)
- [What is Azure Virtual Desktop?](https://learn.microsoft.com/azure/virtual-desktop/overview)
