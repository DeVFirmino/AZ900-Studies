# Architecture and Services exam cheat sheet

## Scenario → answer

| Scenario or clue | Best match |
|---|---|
| Group of VM instances managed and scaled together | Virtual Machine Scale Sets |
| Identical VM instances from one shared profile | VMSS with Uniform orchestration |
| Mixed or standard VM instances managed as a scale set | VMSS with Flexible orchestration |
| Spread VMs across fault and update domains in one region | Availability set |
| Windows desktops delivered from Azure | Azure Virtual Desktop |
| Connect a VM privately to an Azure network | NIC attached to a VNet subnet |
| Persistent operating system storage for a VM | Managed OS disk |
| Direct inbound internet connection to a VM | Optional public IP, controlled with network rules |
| Host a web app without managing the OS | Azure App Service |
| Full OS control for a legacy server | Azure Virtual Machine |
| Event-triggered code without server admin | Azure Functions |
| Simple container run without a cluster | Azure Container Instances |
| Container orchestration at scale | Azure Kubernetes Service |
| Isolated private network in Azure | Virtual Network |
| Connect two Azure VNets privately | VNet peering |
| Reach a third VNet through a peered VNet | Not possible; peering is not transitive |
| Rule-based traffic filtering on a subnet or NIC, at no cost | Network security group |
| Managed, centralized filtering with FQDN rules and threat intelligence | Azure Firewall |
| Encrypted hybrid link over the public internet | VPN Gateway |
| A single remote device connecting to a VNet | Point-to-site VPN |
| An entire office network connecting to a VNet | Site-to-site VPN |
| Private hybrid link avoiding the public internet | ExpressRoute |
| Encryption over ExpressRoute | Configure MACsec or IPsec; it is not encrypted by default |
| Distribute non-HTTP traffic across VMs in a region | Azure Load Balancer |
| Route web traffic by URL path | Application Gateway |
| Block SQL injection and cross-site scripting | Web application firewall on Application Gateway or Front Door |
| Global HTTP entry point across regions | Azure Front Door |
| RDP or SSH to a VM with no public IP | Azure Bastion |
| Absorb volumetric attacks against your public IPs | Azure DDoS Protection |
| PaaS service with private IP in your VNet | Private endpoint |
| Objects such as images, video, and backups | Blob Storage |
| Managed SMB/NFS file share | Azure Files |
| Messages between application tiers | Queue Storage |
| Cheapest storage redundancy | LRS |
| Zone-resilient storage in one region | ZRS |
| Secondary region copy for stored data | GRS, GZRS, RA-GRS, or RA-GZRS |
| Rarely accessed long-term blob data | Archive tier |
| Bulk scripted copy to storage | AzCopy |
| GUI storage management | Azure Storage Explorer |
| Hybrid file share with cloud tiering | Azure File Sync |
| Discover and migrate servers to Azure | Azure Migrate |
| Huge offline data shipment | Azure Data Box |
| Cloud identity directory | Microsoft Entra ID |
| Managed domain services without DC VMs | Entra Domain Services |
| One login for many apps | SSO |
| Password plus another verification factor | MFA |
| Policy based on location, device, or risk | Conditional Access |
| Who can perform an action at a scope | Azure RBAC |
| Multiple overlapping security layers | Defense in depth |
| Never trust, always verify | Zero Trust |
| Security posture and threat protection | Microsoft Defender for Cloud |
| Government-specific isolated Azure environment | Sovereign cloud |

## Four fast comparisons

### Compute

- **VM:** manage the OS.
- **App Service:** publish the web app.
- **Functions:** respond to events without server admin.

### Hybrid networking

- **VPN Gateway:** encrypted traffic over the public internet.
- **ExpressRoute:** private dedicated connection; not encrypted by default.

### Traffic distribution

- **Load Balancer:** Layer 4, regional, any TCP/UDP traffic.
- **Application Gateway:** Layer 7, regional, URL-based routing plus optional WAF.
- **Front Door:** Layer 7, global.
- **Traffic Manager:** DNS-based, global.

### Identity versus access

- **Authentication:** who you are.
- **Authorization / RBAC:** what you may do.

## Dangerous absolute words

Watch for **always**, **automatically**, **guarantees**, and **all**. Common false claims include:

- Private endpoints make a service completely invisible with no other configuration.
- Archive blobs are instantly readable.
- RBAC replaces MFA.
- ExpressRoute and VPN Gateway are interchangeable.
- A network security group and Azure Firewall provide the same protection.
- VNet peering automatically connects every VNet in the chain.
- A storage account redundancy option alone replaces application disaster recovery.
