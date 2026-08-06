# WCL `(1,5)` full independent easy-batch replay - preregistration

- **date:** 2026-08-06
- **consumer:** `dli_wcl_slot_1_5_emptiness`
- **pricing-pilot SHA-256:**
  `928b644d878aea22465248a5a4371dfe2c7b71397555126fbd7ada15a086044c`
- **scope:** all 35,890 batches and 2,296,920 affine-Galois classes
- **exclusion:** retained hard-tail factorization is not paid here

## Decision

Run the pricing pilot's independent direct-resultant, FLINT-primality, and
trial-division replay over every easy batch.  Partition the exact contiguous
batch interval into 100 disjoint groups.  Each group writes an atomic prefix
checkpoint every 64 batches, stops voluntarily before 380 seconds, and can
resume only its unverified suffix.  The aggregate must prove exact disjoint
coverage and bind every primary candidate/factor digest through per-group and
global custody digests.

The replay independently requires:

1. every representative key and timeout norm matches the pinned source;
2. direct `Res(P,X^256+1)` reproduces every primary candidate digest;
3. every shard entry passes FLINT primality;
4. trial division by the batch shard leaves remainder one on every resolved
   row and reproduces every primary factor digest and factor-record count;
5. exactly 194 retained timeout rows remain for the separately named hard
   tail.

Any mismatch is a candidate falsifier and stops promotion.  A clean result
pays the complete easy-factor replay but cannot promote
`dli_wcl_slot_1_5_emptiness` until the hard-tail packet, including tail 191,
has the same independent treatment.

## Predictions and gates

**P1.**  All 35,890 batches and 2,296,920 rows pass with exactly 194 retained
timeouts and no custody gap, overlap, digest mismatch, or factor remainder.

**P2.**  All 6,177,403 shard-prime occurrences pass FLINT primality, and the
aggregate reproduces 6,528,119 factor records.

**P3.**  Every group completes inside 380 seconds.  The pilot projects about
18,715 CPU-seconds before larger-group startup amortization.  At current
Modal unit rates this is expected below `$0.50`; the conservative metered
ceiling is `$1`.  No retry beyond checkpoint resume is authorized.

`COMPLETE` banks an independent executable certificate for the easy census.
`PARTIAL` banks exact completed prefixes and missing group suffixes.  `FAIL`
records the first counterexample.  No status changes occur automatically.

## Resource ceiling

At most 100 Modal workers use one CPU, 2 GiB, and a 420-second hard cap.  One
aggregate uses one CPU, 1 GiB, and 180 seconds.  The client runs detached; all
proof-relevant data is written to the existing audit volume before return.

```text
tools/ramguard modal -- modal run --detach \
  notes/pilots_20260806/wcl15_finish/full_batch_replay_modal.py
```

## Outcome

Initial app `ap-0OBpQSj0V7998tTvkzixwx` completed 99 groups and stopped group
78 voluntarily at 380 seconds, leaving exactly 15 batches.  Authorized
checkpoint-resume app `ap-y5FDRVADCUfOqoflndTSDg` computed only that suffix
while returning the other 99 certificates from cache.

The final result is `COMPLETE`: 100/100 groups, 35,890/35,890 batches,
2,296,920/2,296,920 rows, 6,177,403 FLINT primality checks, 6,528,119 factor
records, 194 retained timeout rows, no duplicate or missing batch, and no
failure.  Global custody digest is
`975220600606e8f9fac4de09d7d350121ea04ea3de23b9e492fb0651b331e033`;
partition digest is
`3be1a3d950949d3d579ed88d26fdf5dbd9fac10e23920a2cb3dc3de15d563d27`;
compact-result SHA-256 is
`04dc6160585c122a9022b922d867bde6d64967a16a41359d6c327c4f03dd5c6c`.

P1 and P2 pass exactly.  P3 passes operationally through its specified
checkpoint resume: no invocation crossed the voluntary 380-second cap, while
group 78's cumulative two-invocation time is 384.354 seconds.  Total worker
time is 17,865.481 seconds, below the pilot projection.  Independent
primality used 9,810.365 seconds, direct resultants 756.147, and trial
division 53.267.  The complete easy-factor replay is banked; no DAG status
changes until the 194 hard tails are independently discharged.
