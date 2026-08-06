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

## Outcome

App `ap-ghDRZvjFIf7BFrEw2AM46h` completed and stopped normally.  All 16
groups and 128 batches passed: 8,152 actual rows, 21,762 independently tested
shard primes, 23,091 factor records, and four retained timeout rows.  Every
candidate digest, factor digest, timeout norm, factor product, and FLINT
primality check agreed.  Selector digest is
`90fcc2b4f17e6dba7c0b8f6038bcf18baf327e828d6e4b51454d72cdec01bf14`;
compact-result SHA-256 is
`928b644d878aea22465248a5a4371dfe2c7b71397555126fbd7ada15a086044c`.

P1 and P2 pass.  P3 fails its CPU gate: measured worker time projects to
18,714.830 CPU-seconds, versus the preregistered 7,200-second ceiling.  The
idealized 100-container wall projection is 187.148 seconds and the slowest
eight-batch group took 7.304 seconds.  Of 66.746 worker-seconds, independent
primality used 35.549, direct resultants 2.714, and trial division 0.190.
The pilot is banked as correctness evidence.  A full audit requires a fresh
grouped/checkpointed design and explicit sub-`$1` pricing; it is not launched
under this preregistration.
