# F3 h=5 reciprocal weighted homogeneity

Status: PROVED STRUCTURAL COMPILER, NOT AN h=5 CLOSURE.

This packet records a grading preserved by the h=5 reciprocal system.  It is
meant to guide the next central-chart attack away from large fixed-point
expansions and toward a weighted/projective graph argument.

## Weights

Assign locator weights

```text
l5,l6,l7,l8,l9       ->  5, 4, 3, 2, 1
bar_l5,bar_l6,...    -> -5,-4,-3,-2,-1.
```

These are the weights induced by root scaling.  The support product `delta`
has weight `10`, and the reciprocal rows

```text
P_j = D_j delta * bar_l(10-j)
```

are homogeneous in this grading.

## Replayed Profile

The compiler verifies:

```text
P1,P2,P3,P4 weights: 9,8,7,6
```

All ten rank-one minors are weighted homogeneous:

```text
C12,C13,C14,C15 weights: 7,6,5,4
C23,C24,C25     weights: 5,4,3
C34,C35         weights: 3,2
C45             weight:  1
```

The four Hermitian unit rows have weight `0`:

```text
N1,N2,N3,N4 weights: 0,0,0,0.
```

## Consequence

The central chart graph and its unit constraints are compatible with the
natural root-scaling action.  The next central-chart proof should preserve
this grading, for example by choosing a weighted affine chart or by working in
the weighted projective quotient, rather than expanding the fixed-point
equations as ordinary dense polynomials.

This does not prove the central chart is empty.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_weighted_homogeneity.py
```

Expected digest:

```text
H5_WEIGHTED_HOMOGENEITY_PASS
```
