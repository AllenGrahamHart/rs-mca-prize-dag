# Proof

Assume the uniform corank-two record cap `M_2<=84416263`.  For each row
`K'`, let `x_d` be the residual-normalized number of
rank-`10-d` incidences, `1<=d<=9`.  Build the inherited individual
ambient/support caps, replacing the first two record factors by

```text
M_1=8147918,  M_2=84416263.
```

Impose all 28 multi-step shadow inequalities.  On every replay row, the
exact optimizer has two cap roots, `x_1=A_1` and `x_2=A_2`, and the seven
tight tree edges

```text
(2,3), (2,4), (2,6), (2,8), (3,5), (2,7), (2,9),
```

where each pair is `(step,source)` and joins `source-step` to `source`.
Equivalently, the components are

```text
1 -> 3,
2 -> 4 -> 6 -> 8,
2 -> 5 -> 7 -> 9.
```

All nine coranks are positive.  Both shared resources are strict, every
nonroot individual cap is strict, and 17 of the 28 hierarchy rows are exact
equalities.

For a tree edge `(t,d)`, write its inequality as
`R_(t,d)x_d <= q_(t,d)x_(d-t)`.  Starting at the leaves, assign

```text
h_(t,d)=(1+sum_child qh)/R_(t,d).
```

The two root cap prices are `1+sum_child qh`.  Every multiplier is positive,
and the resulting dual objective equals the primal tree allocation.  Weak
duality therefore proves exact optimality without either slack shared
resource.

Conditional on the assumed cap, the pinned exact Modal replay checks this
primal-dual certificate, all
individual caps, both shared resources, and all 28 hierarchy rows on every
`K'` in `377674<=K'<=568339`.  All 64 bounded workers and all `190666`
rows completed.  Demand is strictly above capacity through `568338`; at
`568339` the sign reverses.  An independent verifier recomputes each pinned
endpoint from direct tree-path products.  The replay proves the implication;
it does not prove the uniform cap premise.
