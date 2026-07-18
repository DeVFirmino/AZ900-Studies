# Azure Policy and policy initiatives

Azure Policy evaluates Azure resources against organizational rules. It can audit, deny, modify, deploy supporting configuration, and report compliance at scale.

## The exam question Azure Policy answers

> What resource configuration is allowed, required, or considered compliant?

Examples:

- allow resources only in approved regions;
- require an Environment tag;
- audit storage accounts that allow insecure settings;
- deploy a monitoring agent when it is missing;
- restrict expensive or unapproved resource SKUs.

## Policy building blocks

| Component | Purpose |
|---|---|
| Policy definition | The rule, condition, and effect |
| Policy assignment | Applies a definition or initiative at a scope |
| Parameters | Reusable values such as allowed regions or required tag names |
| Initiative | Group of policy definitions supporting one objective |
| Compliance state | Whether evaluated resources satisfy assigned policies |
| Remediation task | Applies supported corrective effects to existing resources |
| Exemption | Records that a resource or scope is intentionally excluded from compliance evaluation |

## Scope and inheritance

Policy can be assigned at:

```text
Management group
└── Subscription
    └── Resource group
        └── Resource
```

Assignments at a higher scope generally apply to resources below it. A policy assignment can exclude a lower scope when there is a valid exception.

**Exam clue:** enforce one rule across many subscriptions → assign Policy at a **management group**.

## Common policy effects

### Audit

The resource is allowed, but noncompliance is recorded.

Use when:

- discovering current configuration;
- measuring impact before enforcement;
- reporting without blocking deployment.

### Deny

Blocks a noncompliant create or update request.

Use when the organization must prevent an invalid configuration, such as deploying outside approved regions.

### Modify

Adds, changes, or removes supported resource properties or tags during creation/update and can remediate existing resources with a task.

### DeployIfNotExists

Deploys a related configuration when it is missing, typically using a managed identity and remediation task. Examples include diagnostic settings or monitoring extensions.

### Append and Disabled

- **Append:** adds supported fields during a request.
- **Disabled:** turns off evaluation for the definition in that assignment.

Effects have prerequisites and service-specific limitations. Do not assume every effect can change every property.

## Policy initiatives

An initiative is a collection of related policy definitions.

```text
Initiative: Production baseline
├── Require approved regions
├── Audit missing diagnostic settings
├── Require CostCenter tag
└── Deny public access on selected services
```

Benefits:

- one assignment for multiple rules;
- combined compliance reporting;
- shared parameters;
- easier management of standards and regulatory baselines.

**Exam clue:** group many policies into one compliance objective → **initiative**.

## Evaluation and remediation

Policy evaluates new or updated resources during requests and periodically reevaluates existing resources.

Important distinctions:

- Audit detects but does not change the resource.
- Deny blocks a create/update but does not repair old resources.
- Modify and DeployIfNotExists can require a remediation task for existing resources.
- A noncompliant result is a governance signal, not proof that the resource is compromised.

## Policy compared with RBAC and locks

| Question | Tool |
|---|---|
| Who may create a VM? | Azure RBAC |
| In which regions may VMs be created? | Azure Policy |
| Prevent deletion of an existing critical VM | Resource lock |
| Apply a repeatable VM definition | ARM template or Bicep |

RBAC permission does not override a Deny policy. A user can be authorized to create VMs but still be blocked because the requested configuration violates Policy.

## Scenario

A user has Contributor access but attempts to create a VM in a region not approved by company policy.

**Result:** Azure Policy with **Deny** can block the deployment even though RBAC authorized the action.

## Scenario

Security wants to discover how many storage accounts violate a new rule before enforcement begins.

**Best fit:** assign an **Audit** policy, review compliance, then plan remediation or stronger enforcement.

## Exam clues

- What configuration is allowed → **Azure Policy**.
- Report noncompliance without blocking → **Audit**.
- Block invalid deployment → **Deny**.
- Add or correct supported properties → **Modify**.
- Deploy a missing related resource/configuration → **DeployIfNotExists**.
- Collection of policies → **initiative**.

## Check yourself

**Statement:** Azure Policy determines which individual user is allowed to create resources.

**Answer:** False. Azure RBAC controls authorization. Policy evaluates the requested resource configuration.

## Official references

- [Azure Policy overview](https://learn.microsoft.com/azure/governance/policy/overview)
- [Azure Policy effects](https://learn.microsoft.com/azure/governance/policy/concepts/effect-basics)
- [Policy initiative definitions](https://learn.microsoft.com/azure/governance/policy/concepts/initiative-definition-structure)
- [Remediate noncompliant resources](https://learn.microsoft.com/azure/governance/policy/how-to/remediate-resources)
