# Cloud Concepts practice quiz

Choose the best answer before opening the [answer key](10-answer-key.md).

## Questions

1. A company wants to migrate an old application without changing it and must retain control of the operating system. Which service model fits best?

   - A. IaaS
   - B. PaaS
   - C. SaaS
   - D. Serverless

2. A development team wants to publish a web application without patching an operating system. Which service model fits best?

   - A. IaaS
   - B. PaaS
   - C. SaaS
   - D. Private cloud

3. An organization wants a ready-to-use email and collaboration application. Which model fits best?

   - A. IaaS
   - B. PaaS
   - C. SaaS
   - D. Hybrid cloud

4. A VM changes from 4 vCPUs to 16 vCPUs. What type of scaling is this?

   - A. Scale out
   - B. Scale in
   - C. Scale up
   - D. Elasticity only

5. An application changes from two VM instances to eight VM instances. What type of scaling is this?

   - A. Scale out
   - B. Scale down
   - C. Scale up
   - D. CapEx

6. A company keeps a sensitive database on-premises and hosts its web tier in Azure. Which deployment model is this?

   - A. Public only
   - B. Private only
   - C. Hybrid
   - D. SaaS

7. Who is responsible for deciding which employees can access organizational data in a SaaS application?

   - A. Microsoft only
   - B. The customer
   - C. The internet provider
   - D. The datacenter operator

8. Where are separate Azure availability zones located?

   - A. Within the same region
   - B. Only in different geographies
   - C. Inside one server rack
   - D. In the customer's office

9. Does deploying a VM in a paired region automatically replicate it to the other region?

   - A. Yes, for every VM
   - B. Only during business hours
   - C. No; replication or a multi-region design must be configured
   - D. Yes, if the VM is IaaS

10. The same Azure Policy must apply to many subscriptions. Which scope is the best fit?

    - A. One resource
    - B. One resource group
    - C. Management group
    - D. Availability zone

11. Can one Azure resource belong to two resource groups at the same time?

    - A. Yes
    - B. No
    - C. Only if they are in one region
    - D. Only for virtual machines

12. Which statement best distinguishes a tenant from a subscription?

    - A. A tenant contains identities; a subscription contains and bills for Azure resources
    - B. A tenant is a region; a subscription is a zone
    - C. A tenant is a VM; a subscription is a virtual network
    - D. They are identical terms

13. A retailer automatically adds instances for a two-hour demand spike, then removes them. Which benefit is emphasized?

    - A. CapEx
    - B. Elasticity
    - C. Sovereignty
    - D. Private cloud

14. Which statement about resource groups is correct?

    - A. Every contained resource must use the resource group's region
    - B. Resource groups can be nested
    - C. Deleting a resource group deletes its contained resources
    - D. One resource must belong to at least two resource groups

15. A file upload should trigger a short piece of code without the team managing a server. What is the best fit?

    - A. Azure Functions/serverless
    - B. SaaS email
    - C. Private cloud
    - D. Scale up

16. Which cloud characteristic means the provider records usage through meters such as compute time, stored capacity, or executions?

    - A. Measured service
    - B. Availability zone
    - C. Private endpoint
    - D. Resource lock

17. An environment is dedicated to one organization and provides automated self-service provisioning. Which cloud model is it?

    - A. Private cloud
    - B. Public cloud only
    - C. SaaS only
    - D. Availability set

18. Buying physical servers and cooling equipment before they are used is primarily which type of expenditure?

    - A. CapEx
    - B. OpEx
    - C. Serverless execution
    - D. Elasticity

19. A workload must recover in another Azure region after a catastrophic regional outage. Which capability is emphasized?

    - A. Disaster recovery
    - B. Scale up
    - C. Tag inheritance
    - D. CapEx

20. Who normally patches the operating system underneath Azure App Service?

    - A. Microsoft, because App Service is PaaS
    - B. The customer, because every cloud OS is customer-managed
    - C. The application end user
    - D. The customer's internet provider

21. In a SaaS solution, who remains responsible for deciding which employees may access organizational data?

    - A. The customer
    - B. Microsoft alone
    - C. The physical datacenter operator alone
    - D. Nobody

22. A single VM is pinned to Availability Zone 1. Which statement is correct?

    - A. The VM is zonal but is not automatically resilient to failure of Zone 1
    - B. Azure automatically copies the VM to every other zone
    - C. The VM is automatically replicated to a paired region
    - D. Availability zones are different subscriptions

23. Which should be considered when selecting an Azure region?

    - A. Compliance, service availability, latency, resilience, and cost
    - B. Only the alphabetical order of region names
    - C. Only the portal language
    - D. The user's password length

24. An organization wants one Policy assignment to govern production subscriptions across several departments. Which scope fits best?

    - A. Management group
    - B. One individual VM
    - C. Availability zone
    - D. Datacenter rack

25. Which statement about a resource group's location is correct?

    - A. It stores resource-group metadata; contained resources can use other regions
    - B. It forces every contained resource into that location
    - C. It automatically creates a paired resource group
    - D. It controls user authentication
