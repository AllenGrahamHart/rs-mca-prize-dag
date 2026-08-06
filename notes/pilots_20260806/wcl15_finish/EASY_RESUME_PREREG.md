# WCL `(1,5)` easy-census resume - preregistration

- **date:** 2026-08-06
- **consumer:** `dli_wcl_slot_1_5_emptiness`
- **starting pin:** `66762875`
- **inventory:** COMPLETE, SHA-256
  `52aaac5ba078999383d62b586007874772c1f5bef909e639d8b0fe4076df754d`

## Decision

Resume the exact recursive-norm census in bounded waves, scheduling only
batch indices declared missing by the independently banked inventory.  Wave
1 contains the first 5,000 missing batches in increasing order: the 47
interrupted holes below index 21,379 followed by the first 4,953 indices of
the contiguous suffix.  It covers at most 320,000 new affine-Galois classes.

The worker algorithm and checkpoint schema are unchanged.  Each batch
reconstructs 64 pinned representatives, computes each exact cyclotomic norm
by recursive quadratic descent, gives PARI/GP at most 60 seconds per norm,
checks every returned factor for primality and exact product, filters
`q<2^256` and `v_2(q-1)>=41`, and atomically writes a summary plus prime
shard.  A timed-out factor is retained as an explicit hard-tail norm.

## Predictions and outcomes

**P1.**  All 5,000 batches complete with zero cache hits and zero client
errors, adding 320,000 rows.

**P2.**  The unresolved rate remains below `2e-4`, so the wave adds fewer
than 64 hard-tail norms.

**P3.**  No completely factored row reaches the official split gate.  A
recorded gate factor is a candidate falsifier and stops further waves pending
direct reconstruction.

`COMPLETE` authorizes a fresh metadata inventory, not another wave
automatically.  `PARTIAL` retains every atomic checkpoint and requires an
inventory before retry.  Neither outcome changes the DAG until the full easy
census, hard tails, aggregation, and independent replay all pass.

## Resource ceiling

At most 100 Modal containers; each batch uses two CPUs, 2 GiB RAM, a
2,100-second function cap, two factor threads, and a 60-second cap per norm.
Historical metering was about `$3.03` for 21,332 batches; Wave 1 is expected
below `$0.75` and has a conservative ceiling of `$1.25`.  The app is stopped
when the client exits.  No aggregation or hard-tail work is launched.

```text
tools/ramguard modal -- modal run \
  experiments/prize_resolution/dli_wcl_weight5_recursive_norm_full_modal.py \
  --external-full --resume-missing --max-missing-batches 5000
```

Wave-2 app `ap-OhRBjzWUFxlkiyknJAjQnj` completed and stopped normally.  It
returned 5,000/5,000 batches, 320,000 rows, 319,993 fully factored rows,
seven hard tails, no cache hit, client error, or gate factor, and maximum
`v_2(p-1)=27`.  Maximum batch time was 157.261801 seconds.  Compact result
SHA-256 is
`6bc6f5a46670cb3fcf98acf3bb7aee7af4bc63fe441603135fb904364247f0e2`.

One post-Wave-2 inventory is authorized under the same metadata-only
96-thread, one-CPU, 1-GiB, 420/390-second and sub-`$0.03` ceiling.  It must
complete before the final suffix is authorized.

Post-Wave-2 inventory app `ap-ecfcmrOq5GeVzA86bat8zG` completed and stopped
normally.  It validates 31,332 batches and 2,005,248 rows, with 131 distinct
hard tails, no custody error or gate factor, and missing suffix
31,332--35,889.  Inventory SHA-256 is
`0d99871c28c6d716e3a2542fd0b003a1c1fbf63e3f7b7522257681129e8b4801`.

## Final easy-wave authorization

Process all 4,558 remaining batches, indices 31,332--35,889, covering exactly
291,672 rows (the last batch has 24 rows).  Predictions P1--P3 and all worker
caps remain unchanged.  Expected cost is below `$0.70`, conservative ceiling
`$1.20`; no aggregation or hard-tail stage.  A final complete metadata
inventory is mandatory before the easy census can be called complete.

```text
tools/ramguard modal -- modal run \
  experiments/prize_resolution/dli_wcl_weight5_recursive_norm_full_modal.py \
  --external-full --resume-missing --max-missing-batches 4558
```

## Packaging-only first launch

App `ap-Zz4V2PkJVwGCxmOICMrEov` was stopped immediately after its workers
crash-looped during module import.  Modal relocates a packaged source file to
`/root`, so computing the local repository path as `Path(__file__).parents[2]`
raised `IndexError` before any worker read a representative, computed a norm,
or wrote a checkpoint.  The correction makes the inventory a local-entrypoint
relative path; remote workers no longer inspect it.  One retry of the exact
same 5,000-batch wave is authorized under the unchanged resource ceiling.

## Wave 1 result and post-wave inventory

Corrected app `ap-qYbLkmB7CKxnSWjPttlp1d` completed and stopped normally.
All 5,000 batches returned: 320,000 rows, 319,987 fully factored rows, 13
explicit hard tails, zero client errors, zero gate factors, maximum
`v_2(p-1)=26`, and maximum batch time 101.878462 seconds.  One batch was a
cache hit because its atomic checkpoint appeared after the inventory pin.
The compact result has SHA-256
`ba210ccadf33b43801c8d740966a6215f581d8db7e0be5fbefe780c206aad43c`.

One fresh metadata inventory is authorized before any further wave.  It uses
the identical validation logic with at most 96 I/O threads, one CPU, 1 GiB,
one container, a 420-second function cap, and a 390-second partial-output
timer.  Expected cost is below `$0.03`.  It computes no norm or factor.  A
partial result stops the resume decision; no wave is inferred from arithmetic
subtraction alone.

Post-wave inventory app `ap-9RWWVhxlPTB2FfXKAYCCQI` completed and stopped
normally.  It validates 26,332 batches and 1,685,248 rows, with 124 distinct
hard tails, no custody error or gate factor, and exactly 9,558 missing batches
forming the contiguous suffix 26,332--35,889.  The new inventory SHA-256 is
`d948248a8c5ef50f1d5c9dcb1722217a2458cdb6282c62b5315042b643d6f030`.

## Wave 2 authorization

Run the identical missing-only worker on the first 5,000 entries of the new
inventory: batch indices 26,332--31,331, exactly 320,000 classes.  Predictions
P1--P3 and all worker caps are unchanged.  Expected cost remains below
`$0.75`, conservative ceiling `$1.25`; no aggregation or hard-tail stage.
`COMPLETE` again requires a fresh metadata inventory before the final suffix.

```text
tools/ramguard modal -- modal run \
  experiments/prize_resolution/dli_wcl_weight5_recursive_norm_full_modal.py \
  --external-full --resume-missing --max-missing-batches 5000
```
