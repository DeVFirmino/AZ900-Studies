# Public and private endpoints

Many Azure PaaS services are reachable over the internet by default. **Private endpoints** and **service endpoints** change how traffic reaches those services and how exposure is controlled.

## Public endpoint

A public endpoint uses a public IP address or public DNS name so the service can be reached from the internet, subject to firewalls, access rules, and authentication.

Public access is appropriate when:

- users on the internet must reach the service directly;
- the scenario does not require private-only connectivity.

## Private endpoint

A private endpoint assigns a **private IP address inside your VNet** to an Azure service instance. Traffic stays on the Microsoft network and reaches the service through a private link connection.

Use a private endpoint when the scenario mentions:

- access a PaaS service without a public internet route;
- connect from a VNet using private IP addresses;
- reduce public exposure of storage, SQL, Key Vault, or similar services.

**Exam clue:** PaaS service should be reachable privately from a VNet → **private endpoint**.

## Service endpoint

A service endpoint extends your VNet identity to an Azure service and routes traffic to the service over the Azure backbone. It does **not** place the service inside your VNet with its own private IP the way a private endpoint does.

At AZ-900 level:

- **Private endpoint:** private IP in your VNet for the service.
- **Service endpoint:** secure routing from subnet to service over Azure's network.

When the exam emphasizes a **private IP in the VNet**, choose **private endpoint**.

## Compare at a glance

| Feature | Public endpoint | Service endpoint | Private endpoint |
|---|---|---|---|
| Reachable from internet by default | Often yes | Service remains a PaaS endpoint | No public route required for private access |
| Uses private IP in your VNet | No | No | Yes |
| Typical goal | Public access | Secure subnet-to-service path | Private-only access from VNet |

## Scenario

A storage account must be accessed only from VMs inside a virtual network, with no public internet exposure.

**Best fit:** **private endpoint** on the storage account, combined with network rules that deny public access.

## Scenario

Developers need to reach Azure SQL from a subnet while keeping traffic off the public internet, using a private address in the VNet.

**Best fit:** **private endpoint**.

## Exam clues

- "Private IP in the VNet" → **private endpoint**.
- "No public internet path" to PaaS → **private endpoint** or private networking design.
- "Public website for customers" → public endpoint or front-door/load-balanced public access, not private endpoint alone.

## Official references

- [Private endpoints overview](https://learn.microsoft.com/azure/private-link/private-endpoint-overview)
- [Virtual network service endpoints](https://learn.microsoft.com/azure/virtual-network/virtual-network-service-endpoints-overview)
