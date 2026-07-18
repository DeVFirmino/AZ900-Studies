# AZ-900 Microsoft Azure Fundamentals Study Guide

A practical, scenario-focused study guide for the **AZ-900: Microsoft Azure Fundamentals** exam.

> Status: work in progress. Cloud Concepts and Architecture and Services are ready; Management and Governance is scaffolded for the next study session.

## Why this repository exists

The goal is not to memorize product names. The goal is to understand **which Azure concept or service best fits a scenario**, recognize exam keywords, and explain why the other options are wrong.

## Current exam domains

| Domain | Weight |
|---|---:|
| Describe cloud concepts | 25–30% |
| Describe Azure architecture and services | 35–40% |
| Describe Azure management and governance | 30–35% |

> Always verify the current skills measured on the [official Microsoft Learn AZ-900 study guide](https://learn.microsoft.com/credentials/certifications/resources/study-guides/az-900) before taking the exam.

## Study guide

### 01 — Cloud Concepts

1. [What is cloud computing?](docs/01-cloud-concepts/01-what-is-cloud-computing.md)
2. [Cloud models and pricing](docs/01-cloud-concepts/02-cloud-models-and-pricing.md)
3. [Cloud benefits and scaling](docs/01-cloud-concepts/03-cloud-benefits-and-scaling.md)
4. [Shared responsibility](docs/01-cloud-concepts/04-shared-responsibility.md)
5. [IaaS, PaaS, SaaS, and serverless](docs/01-cloud-concepts/05-service-models-and-serverless.md)
6. [Regions, zones, and datacenters](docs/01-cloud-concepts/06-global-infrastructure.md)
7. [Tenant, management groups, subscriptions, and resource groups](docs/01-cloud-concepts/07-resource-hierarchy.md)
8. [Exam cheat sheet](docs/01-cloud-concepts/08-cheat-sheet.md)
9. [Practice quiz](docs/01-cloud-concepts/09-practice-quiz.md)
10. [Answer key](docs/01-cloud-concepts/10-answer-key.md)

### 02 — Azure Architecture and Services

1. [Core architectural components](docs/02-architecture-and-services/01-core-architectural-components.md)
2. [Compute choices: VMs, containers, and functions](docs/02-architecture-and-services/02-compute-choices.md)
3. [VM options and required resources](docs/02-architecture-and-services/03-vm-options.md)
4. [Application hosting: Web Apps, containers, and virtual machines](docs/02-architecture-and-services/04-application-hosting.md)
5. [Virtual networking: VNets, subnets, peering, DNS, VPN, and ExpressRoute](docs/02-architecture-and-services/05-virtual-networking.md)
6. [Public and private endpoints](docs/02-architecture-and-services/06-public-and-private-endpoints.md)
7. [Azure Storage services and account types](docs/02-architecture-and-services/07-azure-storage-services.md)
8. [Storage tiers and redundancy](docs/02-architecture-and-services/08-storage-tiers-and-redundancy.md)
9. [File movement and migration tools](docs/02-architecture-and-services/09-file-movement-and-migration.md)
10. [Microsoft Entra ID and Domain Services](docs/02-architecture-and-services/10-microsoft-entra-id.md)
11. [Authentication: SSO, MFA, passwordless, and Conditional Access](docs/02-architecture-and-services/11-authentication.md)
12. [Authorization and security: RBAC, Zero Trust, defense in depth, and Defender for Cloud](docs/02-architecture-and-services/12-authorization-and-security.md)
13. [Exam cheat sheet](docs/02-architecture-and-services/13-cheat-sheet.md)
14. [Practice quiz](docs/02-architecture-and-services/14-practice-quiz.md)
15. [Answer key](docs/02-architecture-and-services/15-answer-key.md)

### 03 — Azure Management and Governance

[Open the section roadmap](docs/03-management-and-governance/index.md)

## Seven-day plan

| Day | Focus |
|---|---|
| 1–2 | Cloud concepts, service models, shared responsibility, regions, zones, subscriptions, and resource groups |
| 3–4 | Compute, networking, storage, and redundancy |
| 5 | Entra ID, authentication, RBAC, Zero Trust, and Defender for Cloud |
| 6 | Policy, locks, ARM, command-line tools, cost management, Advisor, Monitor, and Service Health |
| 7 | Two different practice exams, error review, and Exam Sandbox |

## Run it as a local website

This repository includes an optional MkDocs configuration.

```bash
python -m venv .venv
source .venv/bin/activate   # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
mkdocs serve
```

Then open the local address shown in the terminal.

## Contributing

Corrections, clearer examples, and additional practice questions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Disclaimer

This is an independent study resource and is not affiliated with or endorsed by Microsoft. Azure product names and exam objectives can change. Use official Microsoft Learn documentation as the source of truth.
