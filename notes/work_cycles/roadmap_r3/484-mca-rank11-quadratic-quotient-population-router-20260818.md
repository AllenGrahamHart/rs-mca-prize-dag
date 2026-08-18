# Cycle 484: quadratic quotient population router

## Result: PROVED aggregate forcing

One cyclic or dihedral quadratic pair type has a common core of size `m-2`.
Its disjoint two-point exceptions lie in a complement of size 981,106, so it
owns at most

```text
floor(981106/2)=490553
```

records. Applied to the 255,011,043-record synchronized residual, this gives
the exact tradeoff

```text
R_other >= max(0,255011043-490553q),
```

where `q` is the number of first-owned quotient types. In particular,

```text
519*490553=254597007<255011043,
520*490553=255087560>=255011043.
```

A quotient-only residual therefore requires at least 520 distinct chronology
keys carrying cyclic or dihedral factor-through maps.

## Audit

The primary verifier reconstructs the cap, the integer threshold, and nine
selected quotient/nonquotient tradeoff rows. The independent audit checks
the disjoint-exception and first-owner hypotheses. Nine mutations are
rejected. No Modal computation was used.

## Burn-down

```text
starting local pin:       b55269f73
canonical prize pin:      0dd5b3244
upstream main pin:        93fba1be3
critical target attacked: rate_half_band_crossing_location
DAG delta:                +1 PROVED node, +4 edges
critical status delta:    none
route delta:              one quotient pencil -> 520-type aggregate target
compute spend:            none
next action:              cross-type compatibility or chronology charge
```

## Nonclaims

- no upper bound below 520 quotient types;
- no aggregate quotient payment;
- no shifted or nonquadratic split-pencil payment;
- no high-complexity payment, rank-eleven closure, or MCA closure.
