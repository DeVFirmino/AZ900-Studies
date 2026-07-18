# Architecture and Services practice quiz

Choose the best answer before opening the [answer key](15-answer-key.md).

## Questions

1. A company needs 20 web-server VM instances managed as one group that automatically increases and decreases with traffic. Which service fits best?

   - A. Availability set
   - B. Virtual Machine Scale Sets
   - C. Azure Virtual Desktop
   - D. Azure Functions

2. Which Azure service provides an isolated private network for resources such as VMs and subnets?

   - A. Azure DNS
   - B. ExpressRoute
   - C. Virtual Network
   - D. VPN Gateway

3. A datacenter must connect to Azure over a private dedicated connection that does not use the public internet. Which service fits best?

   - A. VPN Gateway
   - B. VNet peering
   - C. ExpressRoute
   - D. Private endpoint

4. A branch office needs an encrypted connection to Azure over the public internet for a pilot project. Which service fits best?

   - A. ExpressRoute
   - B. VPN Gateway
   - C. Azure DNS
   - D. Blob Storage

5. A team stores photos, videos, and backup files as unstructured objects. Which storage service fits best?

   - A. Azure Files
   - B. Queue Storage
   - C. Blob Storage
   - D. Table Storage

6. A legacy application requires a shared SMB file share in Azure. Which service fits best?

   - A. Blob Storage
   - B. Azure Files
   - C. Queue Storage
   - D. Archive tier only

7. Compliance archives are accessed once or twice a year and cost must be minimized. Which blob tier fits best?

   - A. Hot
   - B. Cool
   - C. Archive
   - D. Premium SSD

8. A storage account must remain readable from a secondary region if the primary region fails. Which redundancy option fits best?

   - A. LRS
   - B. ZRS only
   - C. RA-GRS
   - D. Locally redundant with no secondary copy

9. A company must ship 80 TB of data to Azure because the network link is too slow. Which option fits best?

   - A. AzCopy over a slow VPN
   - B. Azure Data Box
   - C. Azure File Sync
   - D. Queue Storage

10. Which tool is best for assessing and migrating on-premises servers into Azure?

    - A. Azure Migrate
    - B. Storage Explorer
    - C. Conditional Access
    - D. Defender for Cloud

11. Employees need Windows desktops hosted in Azure and delivered to remote devices. Which service fits best?

    - A. Azure Virtual Desktop
    - B. Virtual Machine Scale Sets
    - C. App Service
    - D. Azure DNS

12. A storage account should be reachable from a VNet using a private IP address rather than a public endpoint. What should you add?

    - A. Service endpoint only
    - B. Private endpoint
    - C. Hot tier
    - D. Availability set

13. Which service provides the organization's cloud identity directory for users and groups?

    - A. Microsoft Entra ID
    - B. Azure RBAC
    - C. Azure Policy
    - D. Resource group

14. Sign-ins from untrusted locations must require an authenticator app in addition to a password. Which capability enforces this?

    - A. Azure RBAC
    - B. Conditional Access
    - C. LRS
    - D. VNet peering

15. A contractor should view resources in one resource group but not modify them or grant access. Which RBAC role fits best?

    - A. Owner
    - B. Contributor
    - C. Reader
    - D. User Access Administrator

16. An app needs Kerberos and domain join in Azure, but the company does not want to manage domain controller VMs. Which service fits best?

    - A. Microsoft Entra Domain Services
    - B. Blob Storage
    - C. VPN Gateway
    - D. Archive tier

17. A Node.js web API should run on a managed platform with autoscale and no OS patching. Which service fits best?

    - A. Azure Virtual Machine
    - B. Azure App Service
    - C. Azure Data Box
    - D. ExpressRoute

18. Which security model uses multiple layers such as identity, network, application, and monitoring?

    - A. Defense in depth
    - B. CapEx
    - C. Archive tier
    - D. Region pair

19. Which service provides secure score recommendations and threat protection for Azure workloads?

    - A. Microsoft Defender for Cloud
    - B. Azure Files
    - C. Azure DNS
    - D. Table Storage

20. A blob upload should trigger a short function without the team managing servers. Which compute option fits best?

    - A. Azure Functions
    - B. Virtual Machine Scale Sets
    - C. Azure Virtual Desktop
    - D. ExpressRoute

21. An Azure VM needs private communication with other resources in a virtual network. Which supporting resource connects the VM to a subnet?

    - A. Network interface (NIC)
    - B. Azure Data Box
    - C. Availability set
    - D. Archive tier
