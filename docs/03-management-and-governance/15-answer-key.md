# Management and Governance answer key

1. **A — Azure Pricing Calculator.** It estimates a proposed design before deployment. Cost Analysis examines incurred costs; Health and Policy solve unrelated problems.
2. **A — Region and selected SKU.** Azure pricing can vary with region, tier, size, usage, transfer, licensing, and discounts. Portal appearance does not affect billing.
3. **C — Notifications are triggered and resources continue.** A budget is a tracking and alerting construct, not an automatic hard spending cap.
4. **A — Cost Analysis.** It groups and filters actual cost by service, resource, subscription, resource group, location, and tags.
5. **A — CostCenter tags.** Tags add business context that Cost Analysis can use. They must be applied consistently and do not change the invoice boundary.
6. **A — Microsoft Purview.** Data discovery, classification, cataloging, and lineage are Purview scenarios. Policy governs Azure resource configuration.
7. **A — Azure Policy with Deny.** Policy evaluates requested configuration; Deny blocks deployments outside the approved locations. RBAC answers who may attempt the action.
8. **A — Audit.** Audit records noncompliance without blocking or changing the resource. Deny would enforce immediately.
9. **A — Policy initiative.** An initiative groups policy definitions for one assignment and combined compliance reporting.
10. **A — Azure RBAC.** RBAC authorizes who can perform actions at a scope. Policy can still reject an authorized request if its configuration is invalid.
11. **A — CanNotDelete.** It permits reads and modifications but blocks deletion. ReadOnly would also block normal configuration changes.
12. **A — The storage-account resource cannot be deleted.** The lock affects management-plane deletion. Blob deletion is a data-plane operation requiring separate protection.
13. **A — Azure Cloud Shell.** It is a browser-hosted environment with Azure CLI and Azure PowerShell available without local installation.
14. **A — Azure CLI.** CLI commands begin with `az` and commonly use double-dash parameters.
15. **A — Azure PowerShell.** The Az module provides cmdlets using PowerShell's Verb-AzNoun convention.
16. **A — Azure Arc.** Arc extends Azure inventory and governance to supported resources outside Azure without moving them.
17. **A — Azure Resource Manager.** ARM is the management and deployment control plane used by Azure management interfaces and IaC deployments.
18. **A — Bicep.** Bicep is Azure's concise declarative IaC language and deploys through ARM. KQL queries telemetry instead.
19. **A — Azure Advisor.** Advisor analyzes supported resource configuration and usage to produce personalized optimization recommendations.
20. **A — Azure Service Health.** It provides personalized service issues, planned maintenance, and advisories relevant to selected subscriptions, services, and regions.
21. **A — Resource Health.** It reports health states and history for an individual resource. Azure Status is the broad public view.
22. **A — Azure Monitor metric alert with an action group.** The metric rule detects the threshold; the action group sends the notification.
23. **A — Azure Activity Log.** It records subscription-level control-plane operations, including resource deletion and the calling identity.
24. **A — Log Analytics.** It is the Azure Monitor log workspace and KQL query experience.
25. **A — Application Insights.** It provides application performance monitoring for requests, failures, dependencies, traces, and usage telemetry.
26. **A — Reusable notification and automation targets.** Action groups can connect alerts to email, SMS, webhooks, Functions, Logic Apps, and other supported actions.
27. **A — No automatic ARM tag inheritance.** Policy or automation can copy tags. Cost Management tag inheritance affects cost records rather than the VM resource itself.
28. **A — Forecasted cost.** Forecast alerts notify when projected spending is likely to cross a budget threshold before actual cost gets there.
29. **A — DeployIfNotExists.** It is designed to deploy missing related configuration, often with a managed identity and remediation task for existing resources.
30. **A — Azure Migrate.** Migrate discovers, assesses, and moves workloads. Arc keeps workloads in place while extending Azure management.

## Score guide

- **26–30:** Strong. Re-explain every distractor before moving on.
- **21–25:** Good foundation. Review the comparison tables for missed questions.
- **15–20:** Revisit the relevant lessons, then retry with a fresh question order.
- **0–14:** Study the full lessons again before relying on the cheat sheet.

A repeated quiz can measure memory instead of understanding. Use new scenarios and practice stating both why the answer fits and why the closest alternative does not.
