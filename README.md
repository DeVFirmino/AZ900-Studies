# AZ-900 Microsoft Azure Fundamentals Study Guide

A practical, scenario-focused study guide for the **AZ-900: Microsoft Azure Fundamentals** exam.

> Status: work in progress. The Cloud Concepts section is ready; Architecture and Services and Management and Governance are scaffolded for the next study sessions.

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

[Open the section roadmap](docs/02-architecture-and-services/index.md)

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
