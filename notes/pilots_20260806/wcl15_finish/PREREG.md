# WCL `(1,5)` finish inventory - preregistration

- **date:** 2026-08-06
- **consumer:** `dli_wcl_slot_1_5_emptiness`
- **status at open:** written before the inventory app is launched

## Decision

Audit the persisted Modal volume for the interrupted exact recursive-norm
campaign.  This is metadata work only: do not recompute a norm, factor an
integer, repair a batch, or launch the residual fleet.

The inventory must validate every present batch summary against the pinned
run ID, representative digest, batch index and bounds, and check that its
corresponding prime shard exists.  It must return:

- valid, invalid, missing, and extra batch indices;
- exact covered-row and resolved-row counts;
- unresolved-case and distinct unresolved-norm counts;
- the maximum recorded `v_2(p-1)` and every recorded official-gate case;
- compact missing-index ranges suitable for a resumable launcher.

## Predictions and falsifiers

**P1.**  About 21,332 of 35,889 expected batches remain valid, covering the
ledgered 1,365,248 rows.

**P2.**  No stored batch records a prime with `v_2(p-1)>=41`.

**P3.**  Every valid batch has its prime shard.  Any missing shard means the
existing aggregation route is incomplete even before the residual fleet.

The inventory is `PARTIAL` if its self-timer fires.  Corrupt summaries,
digest drift, duplicate indices, extra files, or a recorded high-gate factor
are route-changing findings and must be printed rather than repaired.

## Resource ceiling

One Modal container, one CPU, 1 GiB RAM, `max_containers=1`, 270-second
function timeout, and an internal 240-second partial-output timer.  Expected
cost is below `$0.02`.  The app is stopped when `modal run` exits.  No full
campaign is authorized by this preregistration.

```text
tools/ramguard modal -- modal run \
  notes/pilots_20260806/wcl15_finish/inventory_modal.py
```
