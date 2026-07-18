# Virtual networking: VNets, subnets, peering, DNS, VPN, and ExpressRoute

Azure networking lets resources communicate privately, reach the internet, and connect to on-premises environments. AZ-900 focuses on **what each service does**, not subnetting math.

## Azure Virtual Network (VNet)

A virtual network is your **isolated private network** in Azure.

Use a VNet when the scenario mentions:

- private IP communication between Azure resources;
- network segmentation;
- controlling inbound and outbound traffic;
- hybrid connectivity to on-premises networks.

**Exam rule:** isolated private network in Azure → **Virtual Network**.

## Subnets

Subnets divide a VNet into smaller address ranges. Resources such as VMs, private endpoints, and some PaaS integrations are placed into subnets.

Subnets help with:

- organization and segmentation;
- applying route tables and network security groups;
- controlling which services can be deployed in which segment.

## VNet peering

VNet peering connects two Azure virtual networks so resources in each can communicate over the **Microsoft backbone** using private addresses.

Peering can connect:

- VNets in the same region;
- VNets in different regions (global VNet peering).

Peering is not a substitute for hybrid connectivity to on-premises datacenters.

## Azure DNS

Azure DNS hosts DNS domains and records. It can:

- host public DNS zones for internet name resolution;
- provide name resolution for resources inside a VNet with a private DNS zone.

**Exam clue:** manage DNS records for your domain in Azure → **Azure DNS**.

## Hybrid connectivity

| Requirement | Service | Connection path |
|---|---|---|
| Encrypted connection over the **public internet** | VPN Gateway | Site-to-site VPN uses IPsec/IKE; point-to-site supports secure VPN protocols |
| Private dedicated connection that **avoids the public internet** | ExpressRoute | Dedicated private link through a connectivity provider |
| Quick temporary hybrid link for testing | VPN Gateway | Common exam answer for internet-based hybrid |

**Exam rules:**

- public internet, encrypted hybrid → **VPN Gateway**;
- private, dedicated, no public internet → **ExpressRoute**.

New ExpressRoute circuits can use two peering types:

- **Azure private peering** connects an on-premises network to Azure VNets through private IP addresses.
- **Microsoft peering** connects to Microsoft public services through public IP addresses advertised over the private ExpressRoute circuit.

Azure public peering is deprecated. Do not treat it as a current third peering option.

### Private does not automatically mean encrypted

ExpressRoute traffic avoids the public internet, but it is **not encrypted by default**. Encryption can be added with options such as MACsec on ExpressRoute Direct or an IPsec tunnel, depending on the design.

At AZ-900 level, remember:

- **VPN Gateway:** encrypted tunnel over the public internet.
- **ExpressRoute:** private connectivity that avoids the public internet; encryption is a separate design choice.

## Scenario

A company needs its Azure VMs to reach an on-premises datacenter securely without sending traffic over the public internet.

**Best fit:** **ExpressRoute**.

## Scenario

A branch office must connect to Azure for a pilot project with minimal setup cost, and using the public internet is acceptable if encrypted.

**Best fit:** **VPN Gateway**.

## Exam clues

- Private network in Azure → **VNet**.
- Two Azure VNets must talk privately → **VNet peering**.
- Hybrid over encrypted internet → **VPN Gateway**.
- Hybrid without public internet → **ExpressRoute**.
- Host your DNS zone → **Azure DNS**.

## Official references

- [Azure Virtual Network overview](https://learn.microsoft.com/azure/virtual-network/virtual-networks-overview)
- [Virtual network peering overview](https://learn.microsoft.com/azure/virtual-network/virtual-network-peering-overview)
- [ExpressRoute circuits and peering](https://learn.microsoft.com/azure/expressroute/expressroute-circuit-peerings)
- [Encryption for ExpressRoute](https://learn.microsoft.com/azure/expressroute/expressroute-about-encryption)
- [VPN Gateway vs ExpressRoute — Microsoft Learn](https://learn.microsoft.com/training/modules/describe-azure-compute-networking-services/4-describe-azure-virtual-networks)
