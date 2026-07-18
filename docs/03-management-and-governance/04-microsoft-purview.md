# Microsoft Purview

Microsoft Purview is a family of solutions for **data governance, data security, data risk, and compliance** across an organization's data estate.

The key AZ-900 idea is:

> Purview helps an organization understand, govern, protect, and manage data wherever it lives.

## The problem Purview addresses

Organizations store data across:

- Azure data services;
- Microsoft 365;
- on-premises databases and file systems;
- other clouds and software-as-a-service platforms;
- analytics and AI environments.

Without a shared governance approach, teams may not know:

- what data exists;
- where sensitive data is stored;
- who owns it;
- how it moves between systems;
- which regulatory or retention requirements apply;
- whether data is being overshared.

## Main Purview solution areas

### Data governance

Purview data-governance capabilities help discover and describe data across supported sources.

Concepts include:

- **data map:** metadata describing discovered data assets and relationships;
- **data catalog:** searchable business and technical context for data consumers;
- **classification:** identification of data types such as personal, financial, or confidential information;
- **lineage:** visibility into how data moves and transforms;
- **business glossary:** shared definitions for business terms and data ownership.

**Exam clue:** find where sensitive data exists across many systems → **Microsoft Purview**.

### Data security

Purview can help identify and reduce data-security risks such as:

- sensitive information exposed too broadly;
- risky insider activity;
- data loss through email, endpoints, or collaboration tools;
- oversharing with AI applications or external users.

Capabilities in the Purview family include information protection, data loss prevention, insider risk management, and related controls.

### Risk and compliance

Purview compliance solutions help organizations address requirements involving:

- records and retention;
- auditing and investigations;
- eDiscovery;
- communication compliance;
- regulatory compliance assessment.

Purview supports governance and compliance work; it does not guarantee that an organization is legally compliant by simply enabling the product.

## Purview compared with common distractors

| Requirement | Best fit |
|---|---|
| Discover, classify, catalog, and trace organizational data | Microsoft Purview |
| Enforce which Azure resource configurations are allowed | Azure Policy |
| Grant a user access to an Azure resource | Azure RBAC |
| Detect threats and improve cloud security posture | Microsoft Defender for Cloud |
| Collect application logs and metrics | Azure Monitor |

## Data governance versus resource governance

These sound similar but operate on different subjects.

```text
Microsoft Purview
└── Governs and protects data
    ├── What data exists?
    ├── Is it sensitive?
    ├── Where did it come from?
    └── Who owns or uses it?

Azure Policy
└── Governs Azure resource configuration
    ├── Which regions are allowed?
    ├── Are required tags present?
    └── Is encryption configured?
```

## Scenario

A bank needs a searchable catalog showing databases that contain customer identifiers and the transformations that feed its reporting platform.

**Best fit:** **Microsoft Purview** for discovery, classification, cataloging, and lineage.

## Scenario

A company must prevent Azure storage accounts from being created without secure-transfer requirements.

**Best fit:** **Azure Policy**, not Purview. The requirement governs resource configuration.

## Exam clues

- Data catalog → **Purview**.
- Data classification and sensitivity → **Purview**.
- Data lineage → **Purview**.
- Data loss prevention and records management → **Purview family**.
- Allowed Azure region or required resource setting → **Azure Policy**.

## Check yourself

**Statement:** Microsoft Purview replaces Azure RBAC because it governs data.

**Answer:** False. Purview supplies data-governance, security, and compliance capabilities. RBAC authorizes management actions on Azure resources.

## Official references

- [Learn about Microsoft Purview](https://learn.microsoft.com/purview/purview)
- [Microsoft Purview data governance](https://learn.microsoft.com/purview/data-governance-overview)
- [Microsoft Purview compliance solutions](https://learn.microsoft.com/purview/)
