#!/usr/bin/env python3
"""Interactive AZ-900 practice quiz.

Run with no arguments for a mixed 20-question round:

    python3 tools/quiz.py

Pick a single topic, set the length, or list what is available:

    python3 tools/quiz.py --topic networking --count 15
    python3 tools/quiz.py --list

Answer with 1-4. Enter s to skip a question and q to stop early.
"""

from __future__ import annotations

import argparse
import random
import sys
from dataclasses import dataclass

# --------------------------------------------------------------------------
# Question bank
#
# Each entry lists one correct option and three plausible distractors. Options
# are shuffled at run time, so the position of the answer is never a clue.
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Question:
    topic: str
    prompt: str
    correct: str
    wrong: tuple[str, ...]
    why: str


BANK: list[Question] = [
    # ---------------------------------------------------------------- cloud
    Question(
        "cloud",
        "A company wants to stop buying servers up front and instead pay monthly for what it uses. Which shift does this describe?",
        "Capital expenditure to operational expenditure",
        (
            "Operational expenditure to capital expenditure",
            "Fixed cost to sunk cost",
            "Depreciation to amortisation",
        ),
        "Buying hardware up front is CapEx. Paying for consumption over time is OpEx, and moving to the cloud is the classic CapEx-to-OpEx shift.",
    ),
    Question(
        "cloud",
        "Which cloud model keeps some workloads in an on-premises datacenter and some in a public cloud, connected together?",
        "Hybrid cloud",
        ("Public cloud", "Private cloud", "Community cloud"),
        "Hybrid combines public and private, with connectivity between them. Private alone means dedicated infrastructure with no public component.",
    ),
    Question(
        "cloud",
        "An application automatically adds more instances when traffic spikes and removes them when it drops. Which characteristic is this?",
        "Elasticity",
        ("High availability", "Disaster recovery", "Fault tolerance"),
        "Elasticity is scaling capacity with demand. High availability is staying up despite failure, which is a different goal.",
    ),
    Question(
        "cloud",
        "Adding more CPU and memory to a single existing virtual machine is which kind of scaling?",
        "Scaling up (vertical)",
        (
            "Scaling out (horizontal)",
            "Scaling in (horizontal)",
            "Autoscaling",
        ),
        "Vertical scaling resizes one machine. Horizontal scaling changes the number of machines.",
    ),
    Question(
        "cloud",
        "In the shared responsibility model, which item is always the customer's responsibility, regardless of service model?",
        "Data and information",
        (
            "Physical datacenter security",
            "Physical hosts",
            "Physical network",
        ),
        "The physical layers are always Microsoft's. Data, and the accounts and identities that reach it, always stay with the customer.",
    ),
    Question(
        "cloud",
        "A team deploys a virtual machine and must patch the guest operating system themselves. Which service model is this?",
        "IaaS",
        ("PaaS", "SaaS", "FaaS"),
        "IaaS gives you the VM and leaves the OS to you. In PaaS the platform patches the OS; in SaaS you only use the application.",
    ),
    Question(
        "cloud",
        "Microsoft 365 is an example of which service model?",
        "SaaS",
        ("IaaS", "PaaS", "On-premises"),
        "SaaS delivers a finished application. The customer manages only data, accounts, and access.",
    ),
    Question(
        "cloud",
        "What is an Azure availability zone?",
        "A physically separate datacenter location inside a single region",
        (
            "A group of two or more Azure regions",
            "A logical container for resources",
            "A separate Azure subscription for redundancy",
        ),
        "Zones are isolated locations within one region, each with independent power, cooling, and networking, used to survive a datacenter failure.",
    ),
    Question(
        "cloud",
        "Which Azure scope sits directly above subscriptions and lets you apply governance to many of them at once?",
        "Management group",
        ("Resource group", "Tenant root resource", "Region"),
        "The hierarchy is management group, subscription, resource group, resource. Policy or RBAC set on a management group flows down to every subscription in it.",
    ),
    Question(
        "cloud",
        "A resource group in Azure can contain resources from:",
        "Multiple regions",
        (
            "Only the region the resource group is in",
            "Only one subscription and one region",
            "Only resources of the same type",
        ),
        "A resource group has a location for its own metadata, but the resources inside it can live in any region.",
    ),
    # -------------------------------------------------------------- compute
    Question(
        "compute",
        "A workload needs 30 identical VM instances that scale automatically with load. Which service fits best?",
        "Virtual Machine Scale Sets",
        ("Availability set", "Azure Virtual Desktop", "Azure Batch"),
        "Scale sets manage a group of identical instances as one resource and add autoscaling. Availability sets spread VMs for resilience but do not autoscale.",
    ),
    Question(
        "compute",
        "Which service runs a small piece of code in response to an event, with no server administration?",
        "Azure Functions",
        (
            "Azure Virtual Machines",
            "Azure Kubernetes Service",
            "Azure Container Instances",
        ),
        "Functions is the event-driven, serverless compute option. You supply code; Azure supplies everything under it.",
    ),
    Question(
        "compute",
        "A team must orchestrate hundreds of containers with automatic scaling, rolling updates, and self-healing. Which service?",
        "Azure Kubernetes Service",
        (
            "Azure Container Instances",
            "Azure App Service",
            "Azure Functions",
        ),
        "AKS is managed Kubernetes for orchestration at scale. Container Instances runs single containers with no orchestrator.",
    ),
    Question(
        "compute",
        "A company must host a web application without patching the operating system, but wants built-in deployment slots and scaling. Which service?",
        "Azure App Service",
        (
            "Azure Virtual Machines",
            "Azure Container Instances",
            "Azure Batch",
        ),
        "App Service is managed web hosting: Azure handles the OS, and you get slots, scaling, and custom domains.",
    ),
    Question(
        "compute",
        "Which service delivers full Windows desktops to users from Azure?",
        "Azure Virtual Desktop",
        ("Azure App Service", "Windows 365 Business only", "Azure Bastion"),
        "AVD provides cloud-hosted desktops and remote apps. Bastion is only for administrative RDP and SSH access to VMs.",
    ),
    Question(
        "compute",
        "What does an availability set protect against?",
        "Hardware failure and planned maintenance inside a single datacenter",
        (
            "The loss of an entire Azure region",
            "Accidental deletion of a VM",
            "Distributed denial-of-service attacks",
        ),
        "Availability sets spread VMs across fault and update domains within one region. Surviving a whole region requires zones or a second region.",
    ),
    # ----------------------------------------------------------- networking
    Question(
        "networking",
        "VNet-A is peered to VNet-B, and VNet-B is peered to VNet-C. What is needed for resources in VNet-A to reach VNet-C?",
        "A direct peering between A and C, or routing through an appliance in B",
        (
            "Nothing, peering is transitive",
            "A VPN Gateway in VNet-B",
            "Global peering, since transitivity only works globally",
        ),
        "Peering is never transitive. You either peer A to C directly, or send traffic through a hub appliance such as Azure Firewall using user-defined routes.",
    ),
    Question(
        "networking",
        "An application uses a custom protocol over TCP port 8443 across 6 VMs in one region. Traffic must be spread across all of them. Which service?",
        "Azure Load Balancer",
        ("Application Gateway", "Azure Front Door", "Traffic Manager"),
        "A non-HTTP protocol rules out the Layer 7 services. Load Balancer works at Layer 4 with any TCP or UDP traffic.",
    ),
    Question(
        "networking",
        "VMs must be allowed to reach only *.contoso.com on the internet, and everything else must be blocked. Which service?",
        "Azure Firewall",
        (
            "Network security group",
            "Application Gateway with WAF",
            "Azure DDoS Protection",
        ),
        "Filtering by fully qualified domain name needs application rules, which only Azure Firewall provides. NSGs match on IP, port, and protocol, not names.",
    ),
    Question(
        "networking",
        "Users in Europe and Asia must reach the nearest regional deployment of a web app, and HTTP requests must be inspected for SQL injection. Which service?",
        "Azure Front Door",
        ("Traffic Manager", "Application Gateway", "Azure Load Balancer"),
        "Global plus Layer 7 plus WAF is Front Door. Application Gateway has WAF but is regional; Traffic Manager is global but DNS-based and cannot inspect requests.",
    ),
    Question(
        "networking",
        "A storage account must be reachable from on-premises over an existing ExpressRoute circuit using a private IP address. What do you deploy?",
        "A private endpoint in a VNet connected to the circuit",
        (
            "A service endpoint on the storage account",
            "A public IP with an NSG restricting the source",
            "Azure Bastion",
        ),
        "A private endpoint gives the storage account a private IP inside the VNet, reachable over ExpressRoute private peering. Service endpoints keep the public endpoint and do not extend to on-premises.",
    ),
    Question(
        "networking",
        "Which statement about network security groups is true?",
        "An NSG can be attached to a subnet and to a NIC at the same time",
        (
            "An NSG can filter on the destination domain name",
            "An NSG applied to a subnet does not affect traffic inside that subnet",
            "NSGs are billed per rule evaluated",
        ),
        "Both attachments can apply, and traffic is evaluated against each. NSGs are free, cannot match domain names, and do apply to traffic between VMs in the same subnet.",
    ),
    Question(
        "networking",
        "Three remote employees need access to VNet resources from home laptops. There is no on-premises hardware and cost must be minimal. What do you deploy?",
        "Point-to-site VPN",
        ("Site-to-site VPN", "ExpressRoute", "Azure Bastion"),
        "Point-to-site connects individual client devices. Site-to-site connects a whole network and assumes on-premises VPN hardware.",
    ),
    Question(
        "networking",
        "An admin must open an SSH session to a Linux VM that has no public IP, from a laptop with no VPN to the VNet. Which service?",
        "Azure Bastion",
        (
            "Point-to-site VPN",
            "A public IP with an NSG allowing port 22",
            "Application Gateway",
        ),
        "Bastion provides browser-based SSH and RDP through the portal, so the VM keeps only a private IP and port 22 stays closed to the internet.",
    ),
    Question(
        "networking",
        "A datacenter must connect to Azure over a dedicated private connection that never uses the public internet. Which service?",
        "ExpressRoute",
        ("VPN Gateway", "VNet peering", "Azure Firewall"),
        "ExpressRoute is a private circuit through a connectivity provider. A VPN is encrypted but still travels the public internet.",
    ),
    Question(
        "networking",
        "Which statement about ExpressRoute is true?",
        "Traffic is private but not encrypted by default",
        (
            "Traffic is encrypted by default with IPsec",
            "It always costs less than a VPN Gateway",
            "It can only connect to a single Azure region",
        ),
        "Private and encrypted are different properties. Encryption over ExpressRoute is a separate design choice, such as MACsec or an IPsec tunnel.",
    ),
    Question(
        "networking",
        "Can a single Azure virtual network span the East US and West Europe regions?",
        "No, a VNet exists in exactly one region",
        (
            "Yes, if global peering is enabled",
            "Yes, if it uses a /16 address space",
            "Yes, for Premium subscriptions",
        ),
        "One VNet, one region. Multi-region designs use one VNet per region joined with global peering.",
    ),
    Question(
        "networking",
        "A web app must send /images requests to one backend pool and /api to another. Which service?",
        "Application Gateway",
        ("Azure Load Balancer", "Traffic Manager", "Azure DNS"),
        "Routing on the URL path requires Layer 7 awareness. Load Balancer only sees IP addresses and ports.",
    ),
    # -------------------------------------------------------------- storage
    Question(
        "storage",
        "A team stores photos, video, and backup files as unstructured objects. Which storage service?",
        "Blob Storage",
        ("Azure Files", "Queue Storage", "Table Storage"),
        "Unstructured object data is exactly the Blob Storage use case.",
    ),
    Question(
        "storage",
        "A legacy application needs a managed SMB file share it can mount as a drive. Which service?",
        "Azure Files",
        ("Blob Storage", "Queue Storage", "Azure Disks"),
        "Azure Files provides managed SMB and NFS shares that can be mounted like a traditional file server.",
    ),
    Question(
        "storage",
        "Compliance archives are read once or twice a year and cost must be as low as possible. Which blob access tier?",
        "Archive",
        ("Hot", "Cool", "Premium"),
        "Archive has the lowest storage cost, in exchange for rehydration latency measured in hours before the data can be read.",
    ),
    Question(
        "storage",
        "Data must remain readable from a secondary region if the primary region fails. Which redundancy option?",
        "RA-GRS",
        ("LRS", "ZRS", "GRS"),
        "Plain GRS replicates to a secondary region but does not allow reads from it. Read access requires the RA variants.",
    ),
    Question(
        "storage",
        "Which redundancy option protects against the loss of a single datacenter within one region, at the lowest cost?",
        "ZRS",
        ("LRS", "GRS", "RA-GZRS"),
        "ZRS spreads copies across availability zones in one region. LRS keeps all copies in a single datacenter, so it cannot survive losing it.",
    ),
    Question(
        "storage",
        "A company must ship 200 TB to Azure and its internet link is slow. Which tool?",
        "Azure Data Box",
        ("AzCopy", "Azure File Sync", "Storage Explorer"),
        "Data Box is a physical appliance shipped to you for very large offline transfers. AzCopy and Storage Explorer both move data over the network.",
    ),
    Question(
        "storage",
        "Which tool discovers on-premises servers, assesses them, and plans a migration to Azure?",
        "Azure Migrate",
        ("Azure Arc", "Azure Advisor", "Azure Data Box"),
        "Azure Migrate is the discovery, assessment, and migration hub. Arc manages resources outside Azure rather than migrating them.",
    ),
    # ------------------------------------------------------------- identity
    Question(
        "identity",
        "Which service is Azure's cloud identity directory?",
        "Microsoft Entra ID",
        ("Azure RBAC", "Azure Policy", "Microsoft Defender for Cloud"),
        "Entra ID, formerly Azure Active Directory, is the directory. RBAC decides what an identity may do once it exists.",
    ),
    Question(
        "identity",
        "A policy must require multi-factor authentication only when users sign in from outside the corporate network. Which feature?",
        "Conditional Access",
        ("Azure RBAC", "Azure Policy", "Resource locks"),
        "Conditional Access evaluates signals such as location, device, and risk, then applies controls like MFA.",
    ),
    Question(
        "identity",
        "Which built-in role allows viewing resources but not changing them or granting access?",
        "Reader",
        ("Contributor", "Owner", "User Access Administrator"),
        "Reader is view-only. Contributor can change resources but not grant access; Owner can do both.",
    ),
    Question(
        "identity",
        "Authentication and authorization differ how?",
        "Authentication proves who you are; authorization decides what you may do",
        (
            "Authentication decides what you may do; authorization proves who you are",
            "They are two names for the same process",
            "Authentication applies to users, authorization only to applications",
        ),
        "Identity first, permissions second. Entra ID authenticates; Azure RBAC authorizes.",
    ),
    Question(
        "identity",
        "Which security principle assumes no request is trusted by default, even from inside the network?",
        "Zero Trust",
        (
            "Defense in depth",
            "Least privilege",
            "The shared responsibility model",
        ),
        "Zero Trust means verify explicitly every time. Defense in depth is the separate idea of layering multiple controls.",
    ),
    Question(
        "identity",
        "Which service provides security posture management and threat protection across Azure resources?",
        "Microsoft Defender for Cloud",
        ("Azure Monitor", "Microsoft Purview", "Azure Advisor"),
        "Defender for Cloud scores your security posture and raises threat alerts. Advisor gives broader recommendations but is not a security monitoring tool.",
    ),
    # ----------------------------------------------------------- governance
    Question(
        "governance",
        "A company must ensure no one can create resources outside Europe. Which service enforces this?",
        "Azure Policy",
        ("Azure RBAC", "Resource locks", "Microsoft Purview"),
        "Policy enforces rules about resource configuration, such as allowed locations. RBAC controls who may act, not what the resource may look like.",
    ),
    Question(
        "governance",
        "Which feature prevents a resource from being deleted, even by an Owner?",
        "A resource lock",
        ("Azure Policy", "An RBAC deny assignment", "A tag"),
        "A CanNotDelete or ReadOnly lock blocks the operation regardless of role, until the lock itself is removed.",
    ),
    Question(
        "governance",
        "A finance team needs costs broken down by department across many resource groups. What should be applied?",
        "Tags",
        ("Resource locks", "Management groups", "Azure Policy initiatives"),
        "Tags are name and value pairs used to organise and report on resources, and they flow into cost analysis.",
    ),
    Question(
        "governance",
        "Which tool estimates the cost of a planned Azure deployment before you build it?",
        "Pricing Calculator",
        (
            "Total Cost of Ownership Calculator",
            "Cost Management",
            "Azure Advisor",
        ),
        "The Pricing Calculator prices a proposed deployment. The TCO Calculator compares on-premises against Azure; Cost Management analyses spend you already have.",
    ),
    Question(
        "governance",
        "Which service alerts you when actual spend crosses a threshold you set?",
        "Cost Management budgets",
        ("Azure Advisor", "Azure Monitor", "Azure Service Health"),
        "Budgets in Cost Management trigger alerts at spending thresholds.",
    ),
    Question(
        "governance",
        "A company runs servers in AWS and on-premises and wants to manage them with Azure tooling. Which service?",
        "Azure Arc",
        ("Azure Migrate", "Azure Stack", "Azure Lighthouse"),
        "Arc projects non-Azure machines into Azure so policy, monitoring, and governance apply to them.",
    ),
    Question(
        "governance",
        "Which service provides personalised recommendations on cost, security, reliability, and performance?",
        "Azure Advisor",
        ("Azure Monitor", "Azure Service Health", "Microsoft Purview"),
        "Advisor analyses your resources and recommends improvements across those pillars.",
    ),
    Question(
        "governance",
        "Where do you check whether an Azure outage is affecting your specific resources?",
        "Azure Service Health",
        ("Azure Monitor", "Azure Advisor", "Microsoft Defender for Cloud"),
        "Service Health reports incidents and planned maintenance scoped to the services and regions you actually use.",
    ),
    Question(
        "governance",
        "Which language is purpose-built for Azure infrastructure as code, as a simpler alternative to ARM JSON templates?",
        "Bicep",
        ("Terraform", "PowerShell DSC", "YAML"),
        "Bicep is Microsoft's domain-specific language that compiles to ARM templates.",
    ),
    Question(
        "governance",
        "Which service governs and catalogues data across an organisation, including data outside Azure?",
        "Microsoft Purview",
        ("Azure Policy", "Azure Monitor", "Azure Arc"),
        "Purview handles data governance: discovery, classification, and lineage across the estate.",
    ),
    Question(
        "governance",
        "Which tool collects metrics and logs from Azure resources and can raise alerts on them?",
        "Azure Monitor",
        ("Azure Advisor", "Azure Service Health", "Azure Policy"),
        "Azure Monitor is the telemetry platform: metrics, logs, alerts, and workbooks.",
    ),
    Question(
        "governance",
        "Which browser-based shell lets you run Azure CLI or PowerShell without installing anything locally?",
        "Azure Cloud Shell",
        ("Azure Portal dashboard", "Azure Arc", "Azure DevOps"),
        "Cloud Shell is the hosted shell in the portal, offering both Bash with Azure CLI and PowerShell.",
    ),
]

TOPIC_LABELS = {
    "cloud": "Cloud concepts",
    "compute": "Compute",
    "networking": "Networking",
    "storage": "Storage",
    "identity": "Identity and security",
    "governance": "Governance, cost, and tools",
}

# --------------------------------------------------------------------------
# Presentation helpers
# --------------------------------------------------------------------------

USE_COLOR = sys.stdout.isatty()


def paint(text: str, code: str) -> str:
    return f"\033[{code}m{text}\033[0m" if USE_COLOR else text


def bold(text: str) -> str:
    return paint(text, "1")


def green(text: str) -> str:
    return paint(text, "32")


def red(text: str) -> str:
    return paint(text, "31")


def dim(text: str) -> str:
    return paint(text, "2")


def rule() -> str:
    return dim("-" * 68)


def ask(question: Question, number: int, total: int) -> str | None:
    """Show one question. Returns the chosen option, or None if skipped."""
    options = [question.correct, *question.wrong]
    random.shuffle(options)

    print()
    print(rule())
    label = TOPIC_LABELS.get(question.topic, question.topic)
    print(f"{bold(f'Question {number}/{total}')}  {dim(label)}")
    print()
    print(question.prompt)
    print()
    for index, option in enumerate(options, start=1):
        print(f"  {bold(str(index))}. {option}")
    print()

    while True:
        try:
            raw = input("Your answer (1-4, s to skip, q to quit): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return "__quit__"

        if raw in {"q", "quit"}:
            return "__quit__"
        if raw in {"s", "skip"}:
            return None
        if raw in {"1", "2", "3", "4"}:
            return options[int(raw) - 1]
        print(dim("  Enter 1, 2, 3, 4, s, or q."))


def run(questions: list[Question]) -> None:
    total = len(questions)
    correct = 0
    missed: list[Question] = []
    answered = 0

    print()
    print(bold(f"AZ-900 practice quiz - {total} questions"))
    print(dim("Answer with 1-4. s skips, q stops and scores what you did."))

    for number, question in enumerate(questions, start=1):
        choice = ask(question, number, total)

        if choice == "__quit__":
            print()
            print(dim("Stopping early."))
            break

        answered += 1
        print()
        if choice is None:
            print(dim(f"  Skipped. The answer was: {question.correct}"))
            missed.append(question)
        elif choice == question.correct:
            correct += 1
            print(green("  Correct."))
        else:
            missed.append(question)
            print(red("  Wrong."))
            print(f"  The answer is: {bold(question.correct)}")
        print(dim(f"  {question.why}"))

    summarise(correct, answered, missed)


def summarise(correct: int, answered: int, missed: list[Question]) -> None:
    print()
    print(rule())
    if answered == 0:
        print("No questions answered.")
        return

    percent = round(correct / answered * 100)
    verdict = green("on track") if percent >= 80 else red("keep drilling")
    print(f"{bold('Score')}: {correct}/{answered}  ({percent}%)  {verdict}")
    print(dim("The real exam passes at roughly 700/1000, so aim for 80% here."))

    if missed:
        print()
        print(bold("Review these:"))
        by_topic: dict[str, int] = {}
        for question in missed:
            by_topic[question.topic] = by_topic.get(question.topic, 0) + 1
        for topic, count in sorted(by_topic.items(), key=lambda item: -item[1]):
            label = TOPIC_LABELS.get(topic, topic)
            print(f"  {count:>2}  {label}")
        print()
        print(dim("Weakest area first. Re-run with --topic to drill just that one."))
    print()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Interactive AZ-900 practice quiz.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--topic",
        "-t",
        action="append",
        choices=sorted(TOPIC_LABELS),
        help="restrict to a topic; repeat the flag for several",
    )
    parser.add_argument(
        "--count",
        "-n",
        type=int,
        default=20,
        help="number of questions (default 20, 0 means all)",
    )
    parser.add_argument(
        "--list",
        "-l",
        action="store_true",
        help="list topics and question counts, then exit",
    )
    parser.add_argument("--seed", type=int, help="fix the shuffle for a repeatable round")
    args = parser.parse_args()

    if args.list:
        print()
        print(bold("Topics"))
        for key, label in TOPIC_LABELS.items():
            count = sum(1 for q in BANK if q.topic == key)
            print(f"  {key:<12} {label:<28} {count:>2} questions")
        print(f"\n  {'total':<12} {'':<28} {len(BANK):>2} questions\n")
        return 0

    if args.seed is not None:
        random.seed(args.seed)

    pool = [q for q in BANK if not args.topic or q.topic in args.topic]
    if not pool:
        print("No questions match that topic.", file=sys.stderr)
        return 1

    random.shuffle(pool)
    if args.count > 0:
        pool = pool[: args.count]

    run(pool)
    return 0


if __name__ == "__main__":
    sys.exit(main())
