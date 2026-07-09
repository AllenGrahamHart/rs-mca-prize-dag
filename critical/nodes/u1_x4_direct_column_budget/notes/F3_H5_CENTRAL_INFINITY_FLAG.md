# F3 h=5 central infinity flag

Status: INITIAL-FORM ROUTE GUIDE, NOT CENTRAL-SLICE FINITENESS AND NOT
`T4-H5-NORM-GATE`.

This packet probes the new finite-scheme route without expanding the four
fixed-point numerators.  It works with the sparse central graph

```text
G: (l6,l7,l8,l9) -> (G6,G7,G8,G9)
```

on the weighted slice `l5=bar_l5=1`, and records the dominant initial forms of
the fixed equations

```text
l_i - G_i(G(l6,l7,l8,l9)) = 0.
```

## Sparse Graph Form

Using auxiliary variables, the fixed scheme can be written as eight sparse
graph equations:

```text
m_i - G_i(l) = 0,
l_i - G_i(m) = 0.
```

The replay verifies that these equations have term counts

```text
11,14,19,23,11,14,19,23
```

and degrees

```text
6,7,8,9,6,7,8,9.
```

This is the right object for future finite-scheme work.  Directly expanding
`G(G(l))` remains the wrong primitive.

## Dominant Boundary Flag

The first ordinary leading forms of the four fixed equations are nonzero
scalar multiples of

```text
l9^54, l9^63, l9^72, l9^81.
```

Thus the naive ordinary-degree boundary is contained in `l9=0`.

After restricting to that boundary, the induced dominant fixed forms are
nonzero scalar multiples of

```text
l7^6 l8^18,
l7^7 l8^21,
l7^8 l8^24,
l7^9 l8^27.
```

So the first boundary splits into the two coordinate branches `l7=0` and
`l8=0`.  The replay then checks both branches:

```text
l7=l9=0  => dominant forms force l8=0,
l8=l9=0  => dominant forms force l6=0,
l7=l8=l9=0 => dominant forms force l6=0,
l6=l8=l9=0 => dominant forms force l7=0.
```

All displayed dominant coefficients are units in official row characteristics,
because their numerator and denominator prime factors are all below the first
official possible row prime.

## Role

This is not a proof that the saturated central slice is zero-dimensional.  The
ordinary projective boundary and the displayed coordinate-flag initial forms
do not cover every possible valuation at infinity, and they do not control bad
reductions by themselves.

The value is narrower: any future proof of
`H5-CENTRAL-SLICE-FINITE` should preserve the sparse graph and can use this
flag as a checked boundary skeleton.  A successful proof still needs a
complete valuation, Groebner, resultant, or saturation argument over the
official row fields.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_infinity_flag.py
```

Expected digest:

```text
H5_CENTRAL_INFINITY_FLAG_PASS
```
