# Microsoft Cost Management, budgets, and Cost Analysis

Microsoft Cost Management is a suite of FinOps tools for understanding, allocating, monitoring, and optimizing Microsoft Cloud spending.

## The mental model

```text
Estimate before deployment → Pricing Calculator
Analyze actual usage       → Cost Analysis
Set a spending target      → Budget
Notify on a threshold      → Budget alert
Export cost data           → Scheduled export / APIs
Find savings opportunities → Cost recommendations and Advisor
```

## Cost Management scopes

Cost data and permissions can be viewed at supported scopes such as:

- billing account or billing profile;
- management group, when supported by the agreement type;
- subscription;
- resource group.

The selected scope answers a different question. A resource-group owner might analyze one application's cost, while a billing administrator might analyze the entire organization.

## Cost Analysis

Cost Analysis is the interactive reporting experience for actual and forecasted Azure costs.

You can:

- view cost over time;
- group by service, resource, resource group, subscription, location, or tag;
- filter to a team, application, or environment;
- compare actual and forecasted cost;
- inspect amortized reservation or savings-plan usage;
- save and share customized views.

Cost data is not a live transaction stream. New usage can take time to appear, and final invoice values can differ because of taxes, credits, support charges, and billing processing.

## Budgets

A budget defines a spending target for a period such as monthly, quarterly, or annually.

Budget alerts can use:

- **actual cost**, after spending reaches a percentage of the budget;
- **forecasted cost**, when Azure predicts the budget will be exceeded.

Example:

```text
Monthly budget: €10,000
├── 50% actual → notify team lead
├── 80% forecast → notify finance
└── 100% actual → trigger an action group workflow
```

### Critical exam trap

A budget does **not** automatically stop, delete, or throttle resources. It tracks spending and sends notifications or triggers configured automation.

If a company needs enforcement, it must design an approved automation workflow or apply other governance controls. Cost budgets themselves are not spending caps.

## Cost alerts and action groups

Cost Management can generate notifications for budgets, anomalies, scheduled reports, and other supported cost conditions. An action group can connect an alert to email, SMS, webhook, Logic Apps, Functions, or automation, depending on the alert type and configuration.

Do not confuse:

- **budget alert:** financial threshold;
- **Azure Monitor metric alert:** resource telemetry threshold;
- **Service Health alert:** Azure platform event affecting selected subscriptions/services/regions.

## Exports and APIs

For recurring reporting or integration with external systems, Cost Management can publish cost details through:

- scheduled exports to a storage account;
- Cost Details and Query APIs;
- Power BI integrations for advanced reporting.

**Exam clue:** automatically deliver detailed cost records to storage → **Cost Management export**.

## Cost optimization

Cost optimization is an ongoing process:

1. Establish ownership and tagging.
2. Analyze cost and usage trends.
3. Create budgets and alerts.
4. Right-size or remove unused resources.
5. Apply reservations, savings plans, Hybrid Benefit, or autoscale when appropriate.
6. Review Azure Advisor cost recommendations.

## Scenario

Finance wants an email when a subscription is forecasted to exceed €5,000 this month.

**Best fit:** create a **monthly budget** at the subscription scope with a **forecasted-cost alert**.

## Scenario

An engineer needs to find which service produced the largest charge last month.

**Best fit:** use **Cost Analysis**, group by service, and set the relevant date range.

## Exam clues

- Explore actual costs and trends → **Cost Analysis**.
- Notify at a financial threshold → **budget alert**.
- Predict overspend → **forecasted budget alert**.
- Export detailed cost data regularly → **scheduled export**.
- Automatically stop resources at the budget amount → **not a native budget behavior**.

## Check yourself

**Statement:** A subscription budget of €1,000 prevents Azure from charging more than €1,000.

**Answer:** False. The budget measures and alerts; resources continue operating unless a separately designed action changes them.

## Official references

- [What is Microsoft Cost Management?](https://learn.microsoft.com/azure/cost-management-billing/costs/overview-cost-management)
- [Get started with Cost Analysis](https://learn.microsoft.com/azure/cost-management-billing/costs/quick-acm-cost-analysis)
- [Create and manage budgets](https://learn.microsoft.com/azure/cost-management-billing/costs/tutorial-acm-create-budgets)
