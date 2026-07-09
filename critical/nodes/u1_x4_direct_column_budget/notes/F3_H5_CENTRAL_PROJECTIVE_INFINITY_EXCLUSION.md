# F3 h=5 central projective-infinity exclusion

Status: PROVED PROJECTIVE-INFINITY EXCLUSION FOR THE CENTRAL SLICE.

This packet upgrades the central infinity flag from a route guide into the
missing zero-dimensionality criterion for the weighted central fixed scheme.
It does not assert that the central chart is empty.  It proves the weaker fact
needed by the finite-scheme payment compiler: the saturated central slice has
no positive-dimensional affine component on official rows.

## Statement

Work on the central weighted slice `l5=bar_l5=1`, after the already-proved
central graph reduction.  Let `F_i(l6,l7,l8,l9)=0` be the four fixed equations
for the composed central graph.

For every official row characteristic, the highest-degree projective-infinity
system for these four equations has no nonzero solution.

Consequently the projective closure of the central fixed scheme misses the
hyperplane at infinity.  Since a positive-dimensional affine component would
meet infinity after projective closure, the central fixed scheme is
zero-dimensional over every official row.

## Descent Certificate

The replay derives the branch tree from the actual leading monomial equations.
At each branch, a projective-infinity point must make every listed monomial
vanish, so it must enter one of the forced coordinate subbranches:

```text
zero=-              top supports=l9       forced l9=0
zero=l9             top supports=l7*l8    forced l7=0 or l8=0
zero=l7,l9          top supports=l8       forced l8=0
zero=l7,l8,l9       top supports=l6       forced l6=0
zero=l8,l9          top supports=l6       forced l6=0
zero=l6,l8,l9       top supports=l7       forced l7=0
```

Both paths terminate at

```text
l6=l7=l8=l9=0,
```

which is forbidden in projective space.  The replay also checks that the
coefficients in these leading forms remain nonzero in every official row
characteristic; the largest prime divisor appearing in the leading
coefficients is `19`.

## Consequence

Combined with `F3_H5_CENTRAL_FINITE_SCHEME_PAYMENT`, this proves the central
finite-scheme target used by the current T4 h=5 route:

```text
central projective-infinity exclusion
  => row-wise saturated central-slice zero-dimensionality
  => Bezout central payment K*n < n^3 on official rows.
```

This still relies on the earlier h=5 structural reduction and chart-local
recovery packets for reducing the h=5 norm-gate frontier to this central
slice.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_projective_infinity_exclusion.py
```

Expected digest:

```text
H5_CENTRAL_PROJECTIVE_INFINITY_EXCLUSION_PASS
```
