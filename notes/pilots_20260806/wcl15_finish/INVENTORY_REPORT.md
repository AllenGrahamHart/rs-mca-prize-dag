# WCL `(1,5)` persisted-census inventory

- **date:** 2026-08-06
- **verdict:** COMPLETE
- **DAG effect:** none

The bounded metadata audit found exactly 21,332 valid batch summaries out of
35,890 expected.  They cover 1,365,248 of 2,296,920 affine-Galois classes;
14,558 batches and 931,672 classes remain.  All valid summaries have their
matching prime shard.  There are no invalid summaries, extra indices,
duplicate indices, recorded official-gate factors, or missing prime shards.

The completed prefix records 111 unresolved cases with 111 distinct norms.
Among completely factored rows the maximum is

```text
max v_2(p-1) = 30 < 41.
```

The missing set consists of 47 interrupted holes below batch 21,379 followed
by the contiguous suffix 21,379--35,889.  This reproduces the campaign
ledger's custody account exactly.

The serial first attempt, app `ap-UTEn7QKVL578dJdILqaWrp`, stopped normally
with a valid partial after 1,325 summaries.  The preregistered parallel-I/O
retry, app `ap-glG3TjqDK6BZ7fnKLzf0qw`, checked all 21,332 summaries in
210.018416 seconds and stopped normally.  Inventory file SHA-256:

```text
52aaac5ba078999383d62b586007874772c1f5bef909e639d8b0fe4076df754d
```

This is route-pricing evidence, not an emptiness certificate.  Completion
still requires every missing easy batch, every hard-tail norm, compact
aggregation, and an independent exact replay.
