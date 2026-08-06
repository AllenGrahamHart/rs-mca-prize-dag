# WCL `(1,5)` hard-tail factor campaign - preregistration

- **date:** 2026-08-06
- **consumer:** `dli_wcl_slot_1_5_emptiness`
- **easy inventory:** COMPLETE, 2,296,920/2,296,920 rows
- **inventory SHA-256:**
  `98f5a0b35ceb420519ed58589047f921ef962d9eb19efe36c1f5917ac02c131a`
- **hard-tail scope:** exactly 194 cases and 194 distinct norms

## Decision

Compile the hard-tail manifest from every one of the 35,890 validated easy
summaries, then factor exactly the 194 distinct retained norms.  This stage
does not aggregate the millions of easy factors and does not claim WCL
closure.  It replaces the original serial manifest reader with bounded
parallel I/O and uses a tail-only aggregate so that the stale prefix
`distinct_primes.txt` cannot contaminate the result.

Each tail worker gives PARI/GP at most 300 seconds, requires every returned
factor to pass `isprime`, checks the exact factor product, and records all
factors below `2^256` with `v_2(p-1)>=41`.  Atomic per-norm checkpoints make
preemption and partial completion reusable.

## Predictions and outcomes

**P1.**  The manifest contains exactly 194 distinct norms and reproduces the
inventory custody count.

**P2.**  At least 150 norms factor completely within 300 seconds.  Any
remainder is an explicit next-stage ECM/primality obligation, not evidence.

**P3.**  No completely factored tail contains an official-gate prime.  Any
such prime is a candidate falsifier and stops closure work pending direct
finite-field reconstruction.

`COMPLETE` pays the primary hard-tail factor stage only.  `PARTIAL` retains
the missing norm list.  Neither changes the DAG until a complete easy+tail
aggregate and independent replay pass.

## Resource ceiling

The manifest compiler uses one two-CPU, 4-GiB container with 96 I/O threads
and a 900-second cap.  At most 100 factor containers use one CPU, 2 GiB,
420-second function caps, and 300-second GP caps.  One tail-only aggregate
uses two CPUs, 4 GiB, and 900 seconds.  Historical sizes put expected cost
below `$1.50`; conservative campaign ceiling is `$3`.  No retry or expanded
timeout is authorized automatically, and the app stops when the client exits.

```text
tools/ramguard modal -- modal run \
  experiments/prize_resolution/dli_wcl_weight5_recursive_norm_tail_modal.py \
  --external-full --factor-only
```

App `ap-9R3y73LE4xoHSDpoqUXGoN` completed and stopped normally.  The manifest
matches all 35,890 easy batches and contains exactly 194 distinct norms.  GP
completely factors 193; tail index 191 reaches the 300-second cap.  The 193
complete rows contain 399 distinct primes, no official-gate factor, and
maximum `v_2(p-1)=17`.  The compact partial has SHA-256
`026fbd0d5665bc855bfcdd56f54b33bbea2b2a563aa98c79daf6e4f042ac0f4b`.
The sole remaining norm is routed to `TAIL191_PREREG.md`; no broad retry is
authorized.
