# Attack surface

## Route 1: strip-free raw aggregate

Let `N_h^raw` count every F-4-minimal, non-full-fiber x83 norm-gate record in
the same record convention, before applying any of the five deletion strips.
Deletion is monotone, so

```text
N_h^strip <= N_h^raw.
```

Consequently the stronger theorem

```text
sum_(h=4)^H_max N_h^raw <= 14n^3              (RAW-NG)
```

implies NG-COUNT. This is the preferred interface because it is independent of
the two currently non-operational U2 and DLI/skew strip definitions.

## Route 2: width cap

Prove that no raw primitive norm-gate record exists above an explicit
`H*(row)`, then sum exact per-width bounds. The first-moment vacancy curve
`H_vac=8..16` is evidence only. Do not claim zero: the model predicts
p-specific events below the vacancy threshold.

## Route 3: norm-divisor aggregate

The x83 keys are cyclotomic integers. A p-specific event forces the row prime
to divide at least one nonzero cleared norm. A viable proof must aggregate
this divisibility over supports or torsion components; the existing
per-support norm bound is too weak by itself.

The target counts records, not raw support pairs or moments. Every proposed
bound must include the exact pairs-to-records and anchoring convention.
