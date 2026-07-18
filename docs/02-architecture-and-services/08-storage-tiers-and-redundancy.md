# Storage tiers and redundancy

Azure Storage pricing and durability depend on **how often data is accessed** and **how many copies are kept**. These two decisions appear constantly on AZ-900.

## Access tiers for blob storage

| Tier | Access pattern | Cost pattern |
|---|---|---|
| Hot | Frequent reads and writes | Higher storage cost, lower access cost |
| Cool | Infrequent access for at least 30 days | Lower storage cost, higher access cost |
| Cold | Infrequent access for at least 90 days | Lower storage cost than cool, higher retrieval cost |
| Archive | Rare access for at least 180 days; rehydration required | Lowest storage cost, highest retrieval latency and cost |

**Exam clue:** rarely accessed backups or compliance archives → **Cool**, **Cold**, or **Archive**, depending on how rarely the data is read and how quickly it must be available again.

Archive is offline-style storage. Plan time for rehydration before the data can be read again.

## Redundancy options

Redundancy determines how Azure copies data inside and across facilities.

| Option | Copies | Protects against |
|---|---|---|
| LRS (Locally redundant storage) | 3 copies in one physical location in the primary region | Hardware failure within that location |
| ZRS (Zone-redundant storage) | 3 copies across availability zones in a region | Zone failure within a region |
| GRS (Geo-redundant storage) | 6 copies: 3 in the primary region and 3 in a geographically distant secondary region | Region-wide disaster; secondary access requires failover unless read access is enabled |
| GZRS | ZRS in primary plus replication to secondary region | Zone failure and regional disaster recovery design |
| RA-GRS / RA-GZRS | Geo-redundant with read access to secondary | Read from secondary region before a full failover in supported scenarios |

### Fast rules

- Lowest cost, single datacenter acceptable → **LRS**.
- Need zone resilience for storage in one region → **ZRS**.
- Need secondary region copy for disaster recovery → **GRS** or **GZRS**.
- Need to read from secondary before failover → **RA-GRS** or **RA-GZRS**.

Redundancy does not replace an application disaster-recovery design. It protects stored data copies according to the selected option.

When a primary region has an Azure region pair, geo-redundant storage commonly uses that paired region. Because newer Azure regions can be nonpaired, the reliable exam-level description is **a geographically distant secondary region**, not always "the paired region."

## Scenario

Regulatory backups must survive a full regional outage and remain readable from the secondary region during an investigation.

**Best fit:** **RA-GRS** or **RA-GZRS**, depending on whether zone redundancy is also required in the primary region.

## Scenario

Development test files can be recreated easily and cost must stay minimal.

**Best fit:** **LRS** with **Cool** or **Hot** tier based on access frequency.

## Exam clues

- Cheapest redundancy → **LRS**.
- Zone failure inside one region → **ZRS** or **GZRS**.
- Secondary region for disaster recovery → **GRS**, **GZRS**, **RA-GRS**, or **RA-GZRS**.
- Rarely accessed long-term backup → **Archive** tier.

## Check yourself

**Statement:** Archive tier blobs can be read instantly without rehydration.

**Answer:** False. Archive data must be rehydrated to hot or cool before normal read access.

## Official references

- [Azure Storage redundancy](https://learn.microsoft.com/azure/storage/common/storage-redundancy)
- [Access tiers for blob data](https://learn.microsoft.com/azure/storage/blobs/access-tiers-overview)
