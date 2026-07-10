# F3 h=5 central finite-scheme payment

> **RETRACTED AT OFFICIAL ROWS (2026-07-10):** the Bezout arithmetic below
> (K = 19,840,464; Kn < n^3) is correct, but the fixed-scheme premise rests
> on reciprocal-system rows invalid at split primes — see
> F3_H5_CONJUGATION_GUARDRAIL_20260710.md and the witness replay
> audit_witness_check_20260710.py. Do not consume as an official-row payment.

Status: PROVED PAYMENT COMPILER; CENTRAL FINITENESS PREMISE DISCHARGED.

This packet weakens the remaining h=5 central-chart target.  The central chart
does not have to be proved empty in order to be harmless for the F3 floor.  It
is enough that, on each official row field, the saturated central weighted
slice fixed scheme is zero-dimensional with the already-recorded degree
bounds.  `F3_H5_CENTRAL_PROJECTIVE_INFINITY_EXCLUSION` now proves that
zero-dimensionality premise.

## Conditional Target

Let `H5-CENTRAL-SLICE-FINITE` mean:

```text
After reducing to the official row field and saturating by the central-chart
denominators, the fixed-point equations on the slice l5=bar_l5=1 define a
zero-dimensional scheme.
```

This is a row-wise finite-field statement.  The projective-infinity exclusion
controls bad reductions on official rows by checking that the leading-form
coefficients have no prime divisor in the official characteristic range.

## Bezout Payment

The central slice fixed-point skeleton gives degree bounds

```text
81, 72, 63, 54.
```

Therefore any zero-dimensional saturated row slice has geometric degree at
most

```text
K = 81 * 72 * 63 * 54 = 19840464.
```

The official central scaling action is free on every row `n=2^s`,
`13 <= s <= 41`, because `gcd(5,n)=1`.  A single algebraic scaling orbit can
contribute at most one free official `mu_n` orbit, hence at most `n` official
central-chart points.  Thus the central contribution is bounded by

```text
K n.
```

At the first official row,

```text
K = 19840464 < 2^26 = (2^13)^2.
```

So for every official row,

```text
K n < n^3.
```

## Finiteness Input

The projective-infinity exclusion derives the forced coordinate descent

```text
l9=0, then l7=0 or l8=0, then the remaining active coordinates are forced
to zero.
```

Both projective-infinity branches terminate at `l6=l7=l8=l9=0`, impossible in
projective space.  Therefore the central fixed scheme has no projective
infinity point and is zero-dimensional on official rows.

## Consequence

The finite-scheme route does not prove there are no h=5 central points.  It
proves that any such points are too sparse to threaten the direct `n^3`
budget.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_finite_scheme_payment.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_projective_infinity_exclusion.py
```

Expected digest:

```text
H5_CENTRAL_FINITE_SCHEME_PAYMENT_PASS
H5_CENTRAL_PROJECTIVE_INFINITY_EXCLUSION_PASS
```
