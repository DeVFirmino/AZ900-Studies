# Azure Service Health

Azure Service Health provides personalized information about Azure platform events that can affect the services and regions used by your subscriptions.

## Three related health experiences

| Experience | Scope | Question answered |
|---|---|---|
| Azure Status | Public/global | Is Azure reporting a broad service problem anywhere? |
| Service Health | Personalized to subscriptions and services | Is an Azure platform event relevant to my environment? |
| Resource Health | Individual resource | Is this particular resource available, unavailable, degraded, or unknown? |

These experiences complement each other. A public status page is not as targeted as Service Health, and Resource Health is more specific than a platform-service overview.

## Service Health event types

### Service issues

Active Azure service problems that may affect resources in selected subscriptions and regions.

### Planned maintenance

Upcoming Azure platform maintenance that could affect service availability or require preparation.

### Health advisories

Changes, retirements, configuration actions, or other notices that may require attention.

### Security advisories

Security-related platform notifications relevant to Azure customers and services.

## Personalized impact

Service Health filters information by context such as:

- subscription;
- Azure service;
- region;
- event type.

This makes it more useful than checking a worldwide public page for every incident.

## Service Health alerts

An administrator can create Service Health alert rules for selected subscriptions, services, regions, and event types.

Alerts can use action groups to notify or automate through supported channels such as:

- email;
- SMS;
- push notifications;
- webhooks;
- Logic Apps or Functions;
- IT service-management integrations.

Alerts must be configured. Simply having access to Service Health does not mean every stakeholder is automatically notified about every event.

## Resource Health

Resource Health reports the current and historical health of an individual resource. States can include:

- Available;
- Unavailable;
- Degraded;
- Unknown.

Resource Health can help distinguish a platform-caused issue from actions or conditions associated with the resource, but diagnostics still require broader context and telemetry.

## Service Health versus Azure Monitor

```text
Azure service incident or maintenance
→ Service Health

My VM CPU, application errors, or custom logs
→ Azure Monitor

One specific VM availability state
→ Resource Health
```

Service Health events are available through Azure's activity-log and alerting integrations, but Service Health and Azure Monitor still answer different exam scenarios.

## Scenario

An administrator wants email and SMS when Azure reports planned maintenance for virtual machines in West Europe used by the subscription.

**Best fit:** create a **Service Health alert** filtered to the subscription, service, region, and planned-maintenance event type.

## Scenario

A developer needs request duration and exception details for one web application.

**Best fit:** **Application Insights in Azure Monitor**, not Service Health.

## Scenario

Only one VM appears unavailable, and the team wants its platform health history.

**Best fit:** **Resource Health**.

## Exam clues

- Azure outage relevant to your subscription → **Service Health**.
- Planned Azure maintenance notification → **Service Health alert**.
- Worldwide public service overview → **Azure Status**.
- Health of one specific resource → **Resource Health**.
- Application exceptions and response time → **Application Insights**.

## Check yourself

**Statement:** Azure Service Health replaces Azure Monitor because both can create alerts.

**Answer:** False. Service Health focuses on Azure platform events affecting your environment. Monitor collects and analyzes resource and application telemetry.

## Official references

- [Azure Service Health overview](https://learn.microsoft.com/azure/service-health/overview)
- [Service Health alerts](https://learn.microsoft.com/azure/service-health/service-health-alert-overview)
- [Azure Resource Health overview](https://learn.microsoft.com/azure/service-health/resource-health-overview)
- [Azure Status](https://azure.status.microsoft/)
