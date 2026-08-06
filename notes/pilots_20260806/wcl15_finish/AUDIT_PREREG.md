# WCL `(1,5)` independent factor-vocabulary audit - preregistration

- **date:** 2026-08-06
- **consumer:** `dli_wcl_slot_1_5_emptiness`
- **primary inventory SHA-256:**
  `98f5a0b35ceb420519ed58589047f921ef962d9eb19efe36c1f5917ac02c131a`
- **primary scope:** 35,890 batches, 2,296,920 classes, 194 hard tails
- **audit stage:** easy-factor vocabulary only

## Decision

Independently read every primary batch summary and its corresponding prime
shard.  Reject any custody mismatch, noncanonical shard, count mismatch, or
disagreement in the batch maximum prime size or `v_2(p-1)`.  Form the exact
global union of easy factors, write it in sorted canonical form to a separate
audit path, and return only compact counts and SHA-256 digests.

This stage does not trust the stale primary aggregate, recompute norms, or
claim that shard entries are prime.  It prices the next independent replay:
the vocabulary size and bit-length distribution determine whether one global
primality pass is sensible or whether certification must be sharded.

## Predictions and decision gates

**P1.**  All 35,890 summary/shard pairs pass custody and local-summary checks.

**P2.**  The independently reconstructed vocabulary contains no factor below
`2^256` with `v_2(p-1) >= 41`; any exception is a candidate falsifier and
halts promotion work.

**P3.**  The scan completes in under 300 seconds.  A complete vocabulary of
at most one million factors authorizes a bounded sharded primality/replay
design.  A larger vocabulary is banked but requires explicit repricing before
any broad follow-up.

`COMPLETE` pays only the vocabulary/custody layer.  It cannot promote the WCL
node.  Promotion still requires independent norm replay, factor-product
reconstruction, primality certification, and the remaining 269-bit tail.

## Resource ceiling

One Modal container uses two CPUs, 8 GiB, and a 900-second hard cap.  It uses
96 bounded I/O threads but no worker fleet.  Expected cost is below `$0.25`;
the authorized ceiling is `$1`.  No retry or follow-up fleet is authorized by
this preregistration.

```text
tools/ramguard modal -- modal run \
  notes/pilots_20260806/wcl15_finish/prime_vocabulary_inventory_modal.py
```

## Operational null run

App `ap-8BYMKPa1sEwm7704oy8pjj` was canceled before producing an output after
the WSL client missed its Modal heartbeat for 88 seconds.  Modal killed the
remote input when the local client disconnected; no result file was written,
so this is not an experimental outcome.  One detached replacement using the
identical committed code and resource ceiling is authorized.  Its result is
retrieved from the separately named audit path on the volume; no second
mathematical retry is authorized.

```text
tools/ramguard modal -- modal run --detach \
  notes/pilots_20260806/wcl15_finish/prime_vocabulary_inventory_modal.py
```

The detached replacement was stopped manually after a delayed progress feed
made the initial throughput appear too slow.  At cancellation it had actually
validated 8,000/35,890 batches and accumulated 1,041,988 distinct factors.
It wrote no complete result.  This partial observation falsifies P3's
one-million size prediction and therefore blocks any automatic broad
primality/replay follow-up.  The observed post-startup rate nevertheless puts
the complete inventory inside the existing 900-second cap.  One final run of
the identical code is authorized solely to finish and bank the inventory;
after that, completion or failure is terminal for this design.

## Outcome

Final app `ap-QctfVdgXi0IsLhxDIMLR0j` completed in 186.861 seconds and
stopped normally.  It validated all 35,890 summary/shard pairs and counted
6,177,403 shard records, 6,528,119 factor records, and 4,443,651 distinct
easy factors.  The vocabulary SHA-256 is
`1abfdfddbb9a168522b9413292cff6064308f9d7a0706b1f5cf34329a0d8bc3a`;
the compact local result SHA-256 is
`25597e973edb63c822af4a8b8b71506e4ecf68f629046aabcdda19ea6d535a31`.
No official-gate factor was found; maximum `v_2(p-1)` is 30 and maximum
factor size is 262 bits.

P1 and P2 pass.  P3's runtime prediction passes, but its one-million size
prediction is falsified by a factor of 4.44.  The custody/vocabulary layer is
banked.  No broad primality or batch-replay campaign is authorized without a
new sharded design and cost estimate.
