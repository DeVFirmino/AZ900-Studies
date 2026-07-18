# Architecture and Services answer key

1. **B — Virtual Machine Scale Sets.** VMSS provides centralized management and autoscaling for a group of VM instances. Uniform orchestration is the specific pattern for identical instances; Flexible orchestration can also manage mixed VM types.
2. **C — Virtual Network.** A VNet is the private isolated network in Azure.
3. **C — ExpressRoute.** A private dedicated hybrid connection avoids the public internet.
4. **B — VPN Gateway.** Site-to-site or point-to-site VPN is the common encrypted internet-based hybrid option.
5. **C — Blob Storage.** Unstructured object data such as images, video, and backups maps to blobs.
6. **B — Azure Files.** Managed SMB/NFS file shares are the Azure Files use case.
7. **C — Archive.** Rarely accessed long-term data with lowest storage cost fits Archive, accepting rehydration delay.
8. **C — RA-GRS.** Read access to the secondary region requires geo-redundant storage with read access enabled.
9. **B — Azure Data Box.** Very large offline transfers use a physical Data Box appliance.
10. **A — Azure Migrate.** Discovery, assessment, and migration planning for workloads is Azure Migrate's role.
11. **A — Azure Virtual Desktop.** Cloud-hosted Windows desktops delivered to users is AVD.
12. **B — Private endpoint.** A private IP in the VNet for a PaaS service is the private endpoint pattern.
13. **A — Microsoft Entra ID.** The identity directory is Entra ID, not RBAC.
14. **B — Conditional Access.** Location-based MFA requirements are enforced with Conditional Access policies.
15. **C — Reader.** View-only access without change or permission-granting rights matches Reader.
16. **A — Microsoft Entra Domain Services.** Managed domain services without operating DC VMs is the key clue.
17. **B — Azure App Service.** Managed web/API hosting without OS patching is App Service.
18. **A — Defense in depth.** Layered security controls define defense in depth.
19. **A — Microsoft Defender for Cloud.** Posture management and threat protection are Defender for Cloud capabilities.
20. **A — Azure Functions.** Event-triggered, serverless-style execution fits Azure Functions.
21. **A — Network interface (NIC).** A NIC connects the VM to a subnet in a VNet and normally receives a private IP address. A public IP is optional.

## Score guide

- **18–21:** Strong. Explain every wrong option before moving on.
- **14–17:** Review the comparisons behind the missed questions.
- **0–13:** Revisit the concept pages, then retry without memorizing answer positions.

A score from a repeated quiz can measure memory rather than understanding. Use different practice sets and explain the distractors aloud.
