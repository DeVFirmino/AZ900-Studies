# Azure Advisor

Azure Advisor analyzes Azure resource configuration and usage telemetry, then provides **personalized best-practice recommendations**.

## The question Advisor answers

> How could I improve this existing Azure deployment?

Advisor recommendations can help improve:

- **cost:** remove or right-size underused resources and evaluate savings opportunities;
- **reliability:** reduce single points of failure and improve resilience;
- **security:** surface relevant security recommendations, including integrations with Defender for Cloud;
- **performance:** improve speed, throughput, and responsiveness;
- **operational excellence:** improve deployment, process, and management practices.

## How Advisor works

```text
Azure resource configuration + usage telemetry
                        ↓
                  Azure Advisor
                        ↓
          Personalized recommendations
          ├── Impact
          ├── Affected resources
          ├── Suggested action
          └── Category
```

Recommendations are contextual to the subscriptions and resources Advisor supports. They are not generic architectural documentation alone.

## What Advisor does not do

Advisor does not normally:

- automatically apply every recommendation;
- guarantee that a recommendation fits every business requirement;
- replace monitoring and alerting;
- report all current Azure platform outages;
- enforce resource configuration like Azure Policy;
- grant access like Azure RBAC.

The resource owner should evaluate business risk, cost, maintenance windows, and dependencies before acting.

## Advisor recommendation lifecycle

Depending on the recommendation, authorized users can:

- review affected resources and potential benefit;
- follow the recommended action;
- dismiss or postpone a recommendation;
- filter by subscription, resource group, impact, or category;
- use Advisor score to track optimization posture.

Dismissing a recommendation does not change the underlying resource. It changes how the recommendation is presented.

## Common recommendation patterns

| Observation | Possible Advisor category |
|---|---|
| VM is consistently underused | Cost |
| Resource lacks a resilience configuration | Reliability |
| Service tier limits expected throughput | Performance |
| Security configuration needs improvement | Security |
| Operational configuration can follow a better practice | Operational excellence |

Recommendations evolve as Azure services and best practices change. Treat examples as patterns rather than a fixed list.

## Advisor versus related services

| Requirement | Best fit |
|---|---|
| Personalized optimization recommendations | Azure Advisor |
| Enforce an allowed resource configuration | Azure Policy |
| Detect threats and manage security posture | Microsoft Defender for Cloud |
| Collect metrics and trigger alerts | Azure Monitor |
| Show Azure service incidents affecting a subscription | Azure Service Health |
| Analyze actual cloud costs | Microsoft Cost Management |

## Advisor and Cost Management

Cost Management explains where spending occurred and supports budgets, analysis, and allocation. Advisor can recommend specific optimizations based on resource configuration and usage.

```text
Cost Analysis → "Where did the money go?"
Advisor      → "What change might reduce or optimize it?"
```

## Advisor and Defender for Cloud

Advisor can surface security recommendations, while Defender for Cloud provides the deeper cloud-security posture and workload-protection experience. Do not treat Advisor as a replacement for Defender for Cloud.

## Scenario

A company wants a list of underused VMs and recommendations that could lower cost without manually analyzing every utilization chart.

**Best fit:** review **Azure Advisor cost recommendations**.

## Scenario

An operations team needs an SMS immediately when CPU usage exceeds 90%.

**Best fit:** create an **Azure Monitor metric alert**, not an Advisor recommendation.

## Exam clues

- Personalized recommendations → **Advisor**.
- Cost, reliability, security, performance, operational excellence → **Advisor categories**.
- Real-time resource threshold notification → **Azure Monitor alert**.
- Azure regional outage affecting your subscription → **Service Health**.
- Advisor automatically fixes everything → **false**.

## Check yourself

**Statement:** Azure Advisor enforces its recommendations and blocks noncompliant resource creation.

**Answer:** False. Advisor recommends. Azure Policy evaluates and can enforce configuration.

## Official references

- [Azure Advisor overview](https://learn.microsoft.com/azure/advisor/advisor-overview)
- [Advisor score](https://learn.microsoft.com/azure/advisor/azure-advisor-score)
- [Advisor cost recommendations](https://learn.microsoft.com/azure/advisor/advisor-cost-recommendations)
