# WCL `(1,5)` independent batch-replay pricing pilot - preregistration

- **date:** 2026-08-06
- **consumer:** `dli_wcl_slot_1_5_emptiness`
- **easy vocabulary result SHA-256:**
  `25597e973edb63c822af4a8b8b71506e4ecf68f629046aabcdda19ea6d535a31`
- **scope:** 128 fixed batches, at most 8,192 rows, 16 checkpointed groups
- **purpose:** correctness cross-check and full-replay pricing only

## Fixed sample

The selector includes batches `0,1,2,24924,35887,35888,35889`, where 24924
contains hard-tail class 1,595,149.  It fills the remaining positions by
successive SHA-256 draws from the literal seed
`wcl15-independent-batch-replay-pilot-v1`, reducing the first eight digest
bytes modulo 35,890 and rejecting repeats, until exactly 128 sorted indices
are fixed.  The code returns and binds the resulting selector digest.

## Independent replay

For each sampled batch, reconstruct the 64 representative keys from the
pinned binary file.  Compute every norm as the direct FLINT resultant with
`X^256+1`, rather than using the primary recursive norm algorithm.  Test every
stored shard factor with FLINT primality, rather than primary PARI `isprime`.
Recover each resolved row's complete factorization by trial division against
the sorted batch shard.  Require exact reproduction of the primary candidate
and factor digests, factor-record count, resolved-row count, and every retained
timeout norm.

Each of 16 disjoint eight-batch groups writes an atomic checkpoint before the
aggregate runs.  A timeout or client interruption therefore returns reusable
partial evidence.  Any digest mismatch, composite shard entry, or nontrivial
factor remainder is a candidate falsifier and stops full-replay planning.

## Predictions and gates

**P1.**  All 128 candidate and factor digests reproduce exactly.

**P2.**  Every sampled shard factor passes FLINT primality and every resolved
norm divides to one, with no unexplained factor.

**P3.**  Linear scaling of summed worker time puts a complete 35,890-batch
replay below 7,200 CPU-seconds and below 300 seconds idealized wall time at
100 containers.  Passing P1/P2 but missing P3 banks correctness evidence and
routes the full replay to an external or redesigned request.

This pilot cannot change a DAG status.  Even a clean, cheap projection only
authorizes writing a separate full-replay preregistration; it does not launch
that fleet.

## Resource ceiling

At most 16 Modal containers use one CPU, 2 GiB, and a 420-second hard cap.
The compact aggregate uses one CPU, 1 GiB, and 120 seconds.  Expected cost is
below `$0.25`; conservative ceiling is `$1`.  No automatic retry, sample
extension, or full replay is authorized.

```text
tools/ramguard modal -- modal run --detach \
  notes/pilots_20260806/wcl15_finish/batch_replay_pilot_modal.py
```
