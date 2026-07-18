# Microsoft Entra ID and Domain Services

Identity is the front door to Azure and Microsoft cloud services. AZ-900 expects you to distinguish the **directory**, **domain services**, and **what each one provides**.

## Microsoft Entra ID

Microsoft Entra ID (formerly Azure Active Directory) is Azure's cloud-based **identity and access management** service.

It provides:

- a directory of users, groups, and devices;
- authentication for users and applications;
- single-tenant and multi-tenant application support;
- integration with Microsoft 365, Azure, and thousands of SaaS apps.

**Exam rule:** identity directory in Microsoft cloud → **Microsoft Entra ID**.

Every Azure subscription is associated with a Microsoft Entra tenant. Users and groups in that tenant can be granted access to Azure resources, usually through role assignments.

## Entra ID versus on-premises Active Directory Domain Services

| Feature | Microsoft Entra ID | Traditional AD DS on a VM |
|---|---|---|
| Primary design | Cloud identity for users, apps, and devices | Windows domain with Kerberos, LDAP, and Group Policy |
| Common use | Sign-in to Azure, Microsoft 365, and SaaS | Legacy domain-joined servers and apps |
| Protocol emphasis | Modern auth such as OAuth, OpenID Connect, SAML | Classic domain protocols |

Entra ID is not a full lift-and-shift replacement for every legacy domain controller scenario.

## Microsoft Entra Domain Services

Entra Domain Services provides **managed domain services** in Azure without deploying and patching your own domain controllers.

It offers:

- domain join for Azure VMs;
- LDAP, Kerberos, and NTLM authentication;
- Group Policy support in a managed domain;
- compatibility for apps that need traditional domain services in the cloud.

Use Domain Services when the scenario mentions:

- lift-and-shift apps that require domain join;
- LDAP or Kerberos in Azure without managing DC VMs;
- Group Policy in a managed Azure domain.

**Exam clue:** need domain services in Azure without operating domain controller VMs → **Microsoft Entra Domain Services**.

## Scenario

A company moves line-of-business servers to Azure. The apps require domain join and Kerberos, but the team does not want to manage domain controller VMs.

**Best fit:** **Microsoft Entra Domain Services**.

## Scenario

Employees need one identity to sign in to Azure portal, Microsoft 365, and a custom SaaS app.

**Best fit:** **Microsoft Entra ID**.

## Exam clues

- Cloud identity directory → **Entra ID**.
- Managed domain join in Azure without DC VMs → **Entra Domain Services**.
- Who the user is → identity service; what they can do in Azure → RBAC (covered in the next lessons).

## Official references

- [Microsoft Entra ID documentation](https://learn.microsoft.com/entra/identity/)
- [Microsoft Entra Domain Services overview](https://learn.microsoft.com/entra/identity/domain-services/overview)
