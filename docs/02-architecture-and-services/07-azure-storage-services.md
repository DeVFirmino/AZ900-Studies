# Azure Storage services and account types

Azure Storage provides durable cloud data services for objects, files, queues, tables, and disks. AZ-900 tests **which storage type fits a workload** and **which account kind supports it**.

## Core storage services

| Service | Stores | Typical use |
|---|---|---|
| Blob Storage | Unstructured objects such as images, video, backups, logs, and documents | Data lake, app uploads, static content, backup targets |
| Azure Files | Managed file shares using SMB or NFS | Lift-and-shift file shares, shared config, legacy apps needing a file share |
| Queue Storage | Large numbers of messages | Decouple application components asynchronously |
| Table Storage | NoSQL key-value data | Simple structured data at scale |
| Azure Disks | Block storage for VMs | OS and data disks for Azure Virtual Machines |

**Exam rules:**

- objects such as images, video, backups → **Blob Storage**;
- managed SMB/NFS share → **Azure Files**.

## Storage account

A storage account is the container that holds your Azure Storage data services. Every blob, file share, queue, and table belongs to a storage account.

When creating a storage account, important choices include:

- account type or performance tier;
- replication option;
- access tier defaults for blobs;
- public access and networking settings.

## Common account types

| Account type | Typical exam note |
|---|---|
| Standard general-purpose v2 | Default choice for blobs, files, queues, and tables |
| Premium block blobs | Low-latency, high-transaction blob workloads |
| Premium file shares | High-performance file shares |
| Premium page blobs | Legacy page blob scenarios; disks use Azure Managed Disks for VMs |

For most AZ-900 questions, **general-purpose v2** is the standard answer unless the scenario calls out premium performance.

## Blob types

| Blob type | Best for |
|---|---|
| Block blobs | Text and binary data, files, streaming objects, documents |
| Append blobs | Logging with append operations |
| Page blobs | Random read/write patterns in page-sized blocks; legacy VHD-style scenarios |

Most object-storage scenarios on the exam map to **block blobs**.

## Scenario

A mobile app uploads photos and videos that must be stored as objects and served globally.

**Best fit:** **Blob Storage** in a general-purpose v2 account, often with a hot or cool tier depending on access frequency.

## Scenario

An on-premises application expects a UNC path to a shared Windows file share in Azure.

**Best fit:** **Azure Files**.

## Exam clues

- Unstructured object data → **Blob**.
- Shared file share → **Azure Files**.
- Messages between app tiers → **Queue Storage**.
- VM disk → **Azure Managed Disks**, backed by storage designed for VMs rather than a user-managed blob file share.

## Official references

- [Azure Storage overview](https://learn.microsoft.com/azure/storage/common/storage-introduction)
- [Storage account overview](https://learn.microsoft.com/azure/storage/common/storage-account-overview)
- [Describe Azure storage services — Microsoft Learn](https://learn.microsoft.com/training/modules/describe-azure-storage-services/2-describe-storage-services)
