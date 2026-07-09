# F3 h=5 central finite-scheme payment

Status: PROVED CONDITIONAL PAYMENT COMPILER, NOT `T4-H5-NORM-GATE`.

This packet weakens the remaining h=5 central-chart target.  The central chart
does not have to be proved empty in order to be harmless for the F3 floor.  It
is enough to prove that, on each official row field, the saturated central
weighted-slice fixed scheme is zero-dimensional with the already-recorded
degree bounds.

## Conditional Target

Let `H5-CENTRAL-SLICE-FINITE` mean:

```text
After reducing to the official row field and saturating by the central-chart
denominators, the fixed-point equations on the slice l5=bar_l5=1 define a
zero-dimensional scheme.
```

This is a row-wise finite-field statement.  A characteristic-zero finiteness
claim is not by itself enough unless it also controls bad reductions modulo
the official row primes.

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

## Consequence

The h=5 central residual can now be attacked by either of the following:

- prove central-chart emptiness, as before;
- prove the weaker row-wise saturated zero-dimensionality statement above;
- or keep using a scalable finite-row certificate family.

The finite-scheme route would not prove there are no h=5 central points.  It
would prove that they are too sparse to threaten the direct `n^3` budget.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_finite_scheme_payment.py
```

Expected digest:

```text
H5_CENTRAL_FINITE_SCHEME_PAYMENT_PASS
```
