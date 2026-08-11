# Cycle 53: rate-half Haboeck audit harvest (2026-08-10)

## Source

Harvest canonical Fable commit `31aa1e684` (Round 32 bank 1) on top of the
newer Codex rate-half branch. The mathematical source remains the proved
Haboeck import and its upstream audit pin at
`przchojecki/rs-mca@93fba1be`.

## Certified content

The adversarial bank records 28 attacks with no mathematical kill. It checks
the support-wise MCA object identity, the load-bearing `d=k-1` convention,
both safe-side roundings, the complete `m=3..96` arithmetic ladder, the
all-`e` field scope, the exclusion of the unproved BCHKS25 linear refinement,
and the `CA<=MCA` far-branch consumer transport.

The consumer now records the complete safe staircase

```text
a_RH(q)<=a_(m(q)),
m(q)=max{m: Q_m*2^128<=q},
```

for `m=9..95`. The first strict improvement begins at
`log2(q)=232.650530...`; `m=94` covers every razor row, `m=95` applies above
its exact threshold, and `m=96` is unaffordable below `2^256`.

## Port audit and repairs

The canonical commit says a separate `REPORT.md` was persisted, but no such
file is present. The retained evidence is `FABLE_AUDIT.md` plus four replay
scripts; the consumer wording is corrected to that exact custody surface.

Two replay strings also described the pre-bank state: one printed the old
`232.650531` claim and one said the staircase was not recorded. Both are
corrected. More materially, `logcheck.py` labeled an inconclusive coarse
bracket as a negative comparison. It now uses an exact rational
`atanh`-series interval with a proved tail bound and certifies

```text
232.650530 < log2(Q_9*2^128) < 232.650531.
```

## Status

This certifies and broadens the safe-side bracket but supplies no adjacent
unsafe witness. `rate_half_band_crossing_location` remains `TARGET`; no
critical status changes.
