# Azure Monitor, Log Analytics, alerts, and Application Insights

Azure Monitor is Azure's observability service for collecting, analyzing, visualizing, and responding to telemetry from cloud and hybrid environments.

## Observability questions

```text
What is happening?       → metrics, logs, traces, events
Why is it happening?     → queries, correlation, diagnostics
Should someone respond?  → alert rules and action groups
How is the app behaving? → Application Insights
```

## Azure Monitor data types

### Metrics

Metrics are numeric time-series values collected at regular intervals.

Examples:

- CPU percentage;
- request count;
- disk operations;
- queue length;
- available memory, where supported;
- success and failure rates.

Metrics are efficient for dashboards, near-real-time charts, and threshold alerts.

**Exam clue:** alert when CPU exceeds 90% → **metric alert**.

### Logs

Logs are timestamped records containing richer context and dimensions.

Examples:

- application exceptions;
- operating-system events;
- security and audit records;
- diagnostic logs;
- custom application events.

Logs are suited to investigation, correlation, flexible querying, and longer-form analysis.

### Traces

Distributed traces follow requests across components and dependencies. They are important for diagnosing latency and failures in distributed applications.

## Azure Activity Log

The Activity Log records subscription-level **control-plane events**.

Examples:

- who deleted a VM;
- when a resource group was created;
- whether a role assignment changed;
- a failed Azure Resource Manager operation;
- Service Health events delivered through the activity-log system.

The Activity Log does not contain every application message or every row-level data operation.

**Exam clue:** who changed or deleted an Azure resource → **Activity Log**.

## Log Analytics workspaces

A Log Analytics workspace stores and organizes supported Azure Monitor log data. Users query it with **Kusto Query Language (KQL)**.

Conceptual query:

```kusto
AzureActivity
| where ActivityStatusValue == "Failure"
| summarize FailedOperations = count() by ResourceGroup
```

Log Analytics is the query and workspace experience. Azure Monitor is the broader observability platform.

## Azure Monitor alerts

An alert rule combines:

```text
Target resource or scope
+ signal (metric, log, activity event, health event)
+ condition and threshold
+ evaluation settings
+ action group
= alert response
```

Alert types include:

- metric alerts;
- log-search alerts;
- activity-log alerts;
- smart-detection or service-specific alert experiences.

### Static and dynamic thresholds

- **Static threshold:** a fixed value, such as CPU > 90%.
- **Dynamic threshold:** Azure evaluates learned historical behavior and identifies significant deviation for supported metrics.

### Action groups

Action groups are reusable notification and automation targets. Depending on support and configuration, they can invoke:

- email, SMS, voice, or mobile notifications;
- webhooks;
- Azure Functions;
- Logic Apps;
- Automation runbooks;
- IT service-management connectors.

An alert rule detects the condition. The action group decides who or what is notified.

## Application Insights

Application Insights is Azure Monitor's application performance monitoring capability.

It can collect and analyze:

- request rates and response times;
- failed requests and exceptions;
- dependency calls;
- availability-test results;
- users, sessions, and application usage where instrumented;
- distributed traces and application maps;
- custom events and metrics.

Modern Application Insights commonly uses a Log Analytics workspace and OpenTelemetry-based instrumentation options.

**Exam clue:** diagnose slow requests and exceptions in a web app → **Application Insights**.

## Visualization and analysis

Azure Monitor data can appear through:

- metrics explorer;
- Log Analytics queries;
- workbooks;
- dashboards;
- Application Insights views;
- integrations with other analysis tools.

## Monitor compared with common distractors

| Requirement | Best fit |
|---|---|
| CPU, request count, logs, and alerts | Azure Monitor |
| Query centralized logs with KQL | Log Analytics |
| Web-app performance, dependencies, and exceptions | Application Insights |
| Azure platform incident affecting subscription | Service Health |
| Personalized optimization recommendation | Azure Advisor |
| Financial-spend threshold | Cost Management budget alert |

## Scenario

A VM quota or supported usage metric should notify operations when it reaches 80%.

**Best fit:** create an **Azure Monitor alert** on the available quota/usage signal and attach an action group. Requesting more quota is a separate process through Azure Quotas or support.

## Scenario

An auditor asks who deleted a network security group yesterday.

**Best fit:** search the **Azure Activity Log**.

## Scenario

Users report that checkout is slow, and developers need request traces and SQL dependency duration.

**Best fit:** use **Application Insights**.

## Exam clues

- Numeric time-series value → **metric**.
- Rich event records and queries → **logs / Log Analytics**.
- Resource-management operation history → **Activity Log**.
- Threshold notification → **Azure Monitor alert**.
- Notification target shared by alert rules → **action group**.
- Application performance and exceptions → **Application Insights**.

## Check yourself

**Statement:** Log Analytics and Azure Monitor are identical names for the same complete service.

**Answer:** False. Log Analytics is the workspace and query experience for logs within the broader Azure Monitor platform.

## Official references

- [Azure Monitor overview](https://learn.microsoft.com/azure/azure-monitor/fundamentals/overview)
- [Azure Monitor data platform](https://learn.microsoft.com/azure/azure-monitor/fundamentals/data-platform-metrics)
- [Log Analytics overview](https://learn.microsoft.com/azure/azure-monitor/logs/log-analytics-overview)
- [Azure Monitor alerts overview](https://learn.microsoft.com/azure/azure-monitor/alerts/alerts-overview)
- [Application Insights overview](https://learn.microsoft.com/azure/azure-monitor/app/app-insights-overview)
