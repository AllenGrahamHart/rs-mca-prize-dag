# F3 h=8 reciprocal weighted homogeneity

Status: PROVED STRUCTURAL COMPILER, NOT AN h=8 CLOSURE.

This packet records the root-scaling grading preserved by the h=8 reciprocal
system.  It is meant to guide chart-local attacks away from dense fixed-point
expansions and toward weighted graph arguments.

## Weights

Assign locator weights

```text
c8,c9,c10,c11,c12,c13,c14,c15       ->  8,7,6,5,4,3,2,1
bar_c8,bar_c9,...                   -> -8,-7,-6,-5,-4,-3,-2,-1.
```

These are the weights induced by root scaling.  The support product `delta`
has weight `16`, and the reciprocal rows

```text
P_j = D_j delta * bar_c(16-j)
```

are homogeneous in this grading.

## Replayed Profile

The compiler verifies:

```text
P1,...,P7 weights: 15,14,13,12,11,10,9
```

All twenty-eight rank-one minors are weighted homogeneous, with pairwise weight
range:

```text
1..13.
```

The seven Hermitian unit rows have weight `0`.  The compiler proves this
without expanding the large unit rows: if `P_j` has weight `16-j`, then
`P_j*conjugate(P_j)` has weight `0`, and `c(16-j)*bar_c(16-j)` also has
weight `0`.

For chart `7`, the relevant variables have weights

```text
c9 -> 7,  bar_c9 -> -7.
```

## Consequence

The h=8 reciprocal system and chart-7 graph are compatible with the natural
root-scaling action.  A future chart-7 proof should preserve this grading and
the `P7` denominator structure rather than expanding the fixed-point equations
as dense ordinary polynomials.

The companion `F3_H8_CHART7_OFFICIAL_SCALING_ACTION.md` keeps this honest on
official rows: the available scaling group is finite, namely `mu_n`, not the
whole ambient multiplicative group.

This does not prove the h=8 chart empty.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_weighted_homogeneity.py
```

Expected digest:

```text
H8_WEIGHTED_HOMOGENEITY_PASS
```
