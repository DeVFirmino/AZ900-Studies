# File movement and migration tools

Moving data into, out of, and across Azure is a common exam scenario. Know **which tool fits the job** rather than every command-line switch.

## Tool comparison

| Tool | Primary purpose | Exam clue |
|---|---|---|
| AzCopy | Command-line copy of blobs and files at scale | Scriptable bulk transfer to or from Azure Storage |
| Azure Storage Explorer | GUI to browse and manage storage accounts | Interactive upload, download, and management |
| Azure File Sync | Sync on-premises Windows Server file shares with Azure Files | Hybrid file share with cloud tiering |
| Azure Migrate | Discovery, assessment, and migration planning for servers, databases, and apps | Migrate workloads to Azure with guidance |
| Azure Data Box | Physical appliance for very large offline transfers | Too much data or too slow a link for online transfer |

## AzCopy

AzCopy is a command-line utility optimized for high-performance transfer of blob and file data.

Use AzCopy when the scenario mentions:

- automated bulk copy;
- scheduled transfers;
- moving large datasets to storage accounts or between them.

## Azure Storage Explorer

Storage Explorer is a free GUI for working with blobs, files, queues, and tables across subscriptions.

Use Storage Explorer when the scenario mentions:

- browsing containers and shares visually;
- ad hoc upload or download;
- developers or operators who prefer a desktop tool.

## Azure File Sync

Azure File Sync keeps a local Windows Server file share in sync with an Azure Files share. Frequently used files can remain local while less-used files tier to cloud.

Use File Sync when the scenario mentions:

- hybrid file access with low latency locally;
- cloud-backed file shares across branch offices;
- tiering infrequently used files to Azure.

## Azure Migrate

Azure Migrate is the central hub for discovering and assessing on-premises servers, databases, and applications before moving them to Azure.

Use Azure Migrate when the scenario mentions:

- inventory and readiness assessment;
- migrating VMs, databases, or applications;
- choosing the right migration path with Azure guidance.

Azure Migrate is about **workload migration**, not everyday file copying.

## Azure Data Box

Data Box devices move very large datasets through an offline physical shipment when network transfer is impractical.

Use Data Box when the scenario mentions:

- terabytes or petabytes of data;
- limited bandwidth;
- one-time or periodic bulk offline transfer.

## Scenario

A media company must upload 200 TB of video to Blob Storage, but the datacenter uplink would take months.

**Best fit:** **Azure Data Box**.

## Scenario

Users at a branch office need fast access to shared files, but older files should live in Azure to save local disk space.

**Best fit:** **Azure File Sync** with cloud tiering.

## Exam clues

- Bulk scripted storage copy → **AzCopy**.
- GUI storage management → **Storage Explorer**.
- Hybrid Windows file share sync → **File Sync**.
- Assess and migrate servers to Azure → **Azure Migrate**.
- Huge offline transfer → **Data Box**.

## Official references

- [Transfer data with AzCopy](https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-v10)
- [Azure File Sync overview](https://learn.microsoft.com/azure/storage/file-sync/file-sync-introduction)
- [Azure Migrate overview](https://learn.microsoft.com/azure/migrate/migrate-services-overview)
- [Azure Data Box overview](https://learn.microsoft.com/azure/databox/data-box-overview)
