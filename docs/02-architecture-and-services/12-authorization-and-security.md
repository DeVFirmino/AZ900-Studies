# Authorization and security: RBAC, Zero Trust, defense in depth, and Defender for Cloud

After authentication verifies identity, authorization and security controls determine **permissions**, **risk posture**, and **threat protection**.

## Azure RBAC

Azure role-based access control (RBAC) authorizes **who can perform which actions on which resources at which scope**.

RBAC building blocks:

| Building block | Purpose |
|---|---|
| Security principal | User, group, service principal, or managed identity |
| Role definition | Collection of permissions, such as Reader or Contributor |
| Scope | Management group, subscription, resource group, or resource |
| Role assignment | Grants a role to a principal at a scope |

**Exam rule:** who can perform an action at a scope → **Azure RBAC**.

RBAC is about authorization, not authentication. A user may authenticate successfully but still be denied if no role assignment grants the action.

Common built-in roles at AZ-900 level:

- **Owner:** full access including permission to grant access to others;
- **Contributor:** manage resources but not grant access;
- **Reader:** view resources without making changes.

## Zero Trust

Zero Trust assumes **breach is possible** and verifies explicitly rather than trusting by network location alone.

Core principles:

- verify explicitly;
- use least privilege access;
- assume breach and limit blast radius.

**Exam clue:** never trust, always verify, least privilege, identity-centric security → **Zero Trust**.

## Defense in depth

Defense in depth uses **multiple layers of security** so one failure does not expose everything.

Example layers:

```text
Identity and access control
└── Perimeter and network controls
    └── Compute and application security
        └── Data protection and encryption
            └── Monitoring and response
```

If one layer fails, others still provide protection.

**Exam clue:** multiple overlapping security layers → **defense in depth**.

## Microsoft Defender for Cloud

Defender for Cloud is a **cloud security posture management** and **threat protection** service for Azure and hybrid workloads.

It helps with:

- secure score and recommendations;
- regulatory compliance dashboards;
- threat detection for servers, databases, storage, and other resources on supported plans.

**Exam clue:** security recommendations, posture management, and threat protection across Azure resources → **Microsoft Defender for Cloud**.

Defender for Cloud complements RBAC and network controls; it does not replace them.

## Scenario

A developer should view production resources but must not change them or assign access.

**Best fit:** **Reader** role assignment at the appropriate scope.

## Scenario

Security leadership wants continuous recommendations to improve configuration and detect suspicious activity in Azure subscriptions.

**Best fit:** **Microsoft Defender for Cloud**.

## Exam clues

- Permission to create VMs in one resource group → **RBAC role assignment**.
- Layered security controls → **defense in depth**.
- Verify every access attempt, least privilege → **Zero Trust**.
- Posture and threat protection service → **Defender for Cloud**.

## Check yourself

**Statement:** RBAC determines whether a password is valid.

**Answer:** False. Authentication verifies identity; RBAC authorizes actions after identity is established.

## Official references

- [Azure RBAC overview](https://learn.microsoft.com/azure/role-based-access-control/overview)
- [Zero Trust guidance](https://learn.microsoft.com/security/zero-trust/)
- [Microsoft Defender for Cloud overview](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-cloud-introduction)
