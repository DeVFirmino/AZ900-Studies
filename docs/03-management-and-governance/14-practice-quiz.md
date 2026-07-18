# Management and Governance practice quiz

Choose the best answer before opening the [answer key](15-answer-key.md). Explain why each distractor is wrong before checking your answer.

## Questions

1. A team is comparing two Azure architectures before creating any resources. Which tool should it use to estimate their monthly cost?

   - A. Azure Pricing Calculator
   - B. Azure Service Health
   - C. Azure Policy
   - D. Resource Health

2. Which factor can change the price of otherwise similar Azure resources?

   - A. Region and selected SKU
   - B. The color of the portal theme
   - C. The user's display name
   - D. The order of dashboard tiles

3. A subscription has a monthly budget of €2,000 and reaches €2,001. What happens by default?

   - A. Every resource is deleted
   - B. Azure stops accepting all requests
   - C. Configured budget notifications are triggered; resources continue running
   - D. The subscription automatically changes owner

4. Finance needs to determine which Azure service generated the largest actual cost last month. Which tool fits best?

   - A. Cost Analysis
   - B. Azure Status
   - C. Azure Arc
   - D. ReadOnly lock

5. A company wants to group Azure costs by department inside one subscription. What should it apply consistently?

   - A. CostCenter tags
   - B. Availability zones
   - C. Public IP addresses
   - D. Update domains

6. An organization needs to discover sensitive customer data and trace its lineage across databases and analytics systems. Which service fits best?

   - A. Microsoft Purview
   - B. Azure Advisor
   - C. VPN Gateway
   - D. Azure DNS

7. New resources must be limited to West Europe and North Europe. Which tool and effect fit best?

   - A. Azure Policy with Deny
   - B. Azure RBAC with Reader
   - C. Resource lock with CanNotDelete
   - D. Service Health with an action group

8. Security wants to measure violations of a new rule without blocking deployments. Which Policy effect fits best?

   - A. Audit
   - B. Deny
   - C. ReadOnly
   - D. Owner

9. Fifty related policy definitions should be assigned and reported as one compliance baseline. What should be created?

   - A. Policy initiative
   - B. Resource lock
   - C. Availability set
   - D. Log Analytics workspace

10. Which service decides whether a user may create a VM in a resource group?

    - A. Azure RBAC
    - B. Azure Policy
    - C. Microsoft Purview
    - D. Azure Advisor

11. A production database must remain configurable, but administrators must not delete it accidentally. Which lock fits best?

    - A. CanNotDelete
    - B. ReadOnly
    - C. Reader role
    - D. Audit policy

12. A storage account has a CanNotDelete lock. Which statement is correct?

    - A. The storage-account resource cannot be deleted until the lock is removed
    - B. No blob can ever be deleted
    - C. The account becomes free of charge
    - D. Every user receives Owner access

13. An administrator needs a browser terminal on a temporary computer without installing Azure tools. Which service fits best?

    - A. Azure Cloud Shell
    - B. Azure Advisor
    - C. Microsoft Purview
    - D. Azure Data Box

14. Which tool uses commands such as `az vm list`?

    - A. Azure CLI
    - B. Azure PowerShell
    - C. ARM template JSON
    - D. Application Insights

15. Which tool uses cmdlets such as `Get-AzVM`?

    - A. Azure PowerShell
    - B. Azure CLI
    - C. Cost Analysis
    - D. Azure Status

16. A company wants Azure Policy and inventory for servers running on-premises and in another cloud without migrating them. Which service fits best?

    - A. Azure Arc
    - B. Azure Migrate
    - C. ExpressRoute
    - D. Blob Storage

17. Which Azure service is the consistent management control plane used by the portal, CLI, PowerShell, and templates?

    - A. Azure Resource Manager
    - B. Azure Files
    - C. Microsoft Purview
    - D. Azure Virtual Desktop

18. A team wants concise declarative Azure infrastructure files that are stored in Git and deployed through ARM. Which language fits best?

    - A. Bicep
    - B. KQL
    - C. SQL
    - D. HTML

19. Which service provides personalized recommendations for cost, reliability, security, performance, and operational excellence?

    - A. Azure Advisor
    - B. Azure Service Health
    - C. Azure DNS
    - D. Azure Files

20. Operations needs notification about planned Azure maintenance affecting VMs in its subscription and region. Which service fits best?

    - A. Azure Service Health
    - B. Cost Analysis
    - C. Microsoft Purview
    - D. Azure Pricing Calculator

21. An engineer needs the availability history of one specific VM. Which experience fits best?

    - A. Resource Health
    - B. Azure Status
    - C. Pricing Calculator
    - D. Policy initiative

22. CPU above 90% for ten minutes should send an email. Which solution fits best?

    - A. Azure Monitor metric alert with an action group
    - B. Azure Advisor cost recommendation
    - C. CanNotDelete lock
    - D. Microsoft Purview classification

23. An auditor asks who deleted a virtual network yesterday. Which data source should be checked first?

    - A. Azure Activity Log
    - B. Pricing Calculator
    - C. Azure Status
    - D. Purview data catalog

24. A team needs to query centralized Azure Monitor logs using KQL. Which experience fits best?

    - A. Log Analytics
    - B. Azure DNS
    - C. Azure reservations
    - D. Resource lock

25. Developers need request duration, exceptions, dependency calls, and distributed traces for a web application. Which capability fits best?

    - A. Application Insights
    - B. Azure Policy
    - C. Azure Arc
    - D. Cost Analysis

26. What does an Azure Monitor action group define?

    - A. Reusable notification and automation targets
    - B. The VM operating-system image
    - C. An Azure region pair
    - D. A storage redundancy mode

27. A resource group has `Environment=Production`. Which statement about its VM is correct by default?

    - A. The VM does not automatically inherit the ARM resource tag
    - B. The VM automatically receives the tag in every Azure service
    - C. The tag grants the VM Owner permissions
    - D. The tag prevents VM deletion

28. Finance wants an alert before overspending is likely, based on projected month-end cost. Which budget condition should it use?

    - A. Forecasted cost
    - B. VM CPU metric
    - C. Resource Health state
    - D. ReadOnly lock

29. A diagnostic setting should be deployed when it is missing from existing resources. Which Policy effect is designed for this pattern?

    - A. DeployIfNotExists
    - B. Audit only
    - C. CanNotDelete
    - D. Reader

30. A company needs to assess and move VMware servers into Azure, not merely govern them in place. Which service fits best?

    - A. Azure Migrate
    - B. Azure Arc
    - C. Azure Advisor
    - D. Cloud Shell
