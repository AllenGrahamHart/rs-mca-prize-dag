# Proof

The two uniform parents prove `M_2<=84416263` and `M_3<=983902549`.
For each row `K'`, let `x_d` be the residual-normalized number of
rank-`10-d` incidences, `1<=d<=9`.  Build the inherited individual
ambient/support caps, replacing the first three record factors by

```text
M_1=8147918,  M_2=84416263,  M_3=983902549.
```

Impose all 28 multi-step shadow inequalities.  On every replay row, the
exact optimizer has three cap roots, `x_1=A_1`, `x_2=A_2`, and `x_3=A_3`,
and the six-edge forest

```text
(2,4), (2,5), (3,6), (4,7), (5,8), (6,9),
```

where each pair is `(step,source)` and joins `source-step` to `source`.
Equivalently, the components are

```text
1,
2 -> 4,
3 -> 5, 3 -> 6, 3 -> 7, 3 -> 8, 3 -> 9.
```

All nine coranks are positive.  Both shared resources are strict, every
nonroot individual cap is strict, and 12 of the 28 hierarchy rows are exact
equalities.  The six additional equalities follow from exact path identities
among the multi-step coefficients.

For a forest edge `(t,d)`, write its inequality as
`R_(t,d)x_d <= q_(t,d)x_(d-t)`.  Starting at the leaves, assign

```text
h_(t,d)=(1+sum_child qh)/R_(t,d).
```

The three root cap prices are `1+sum_child qh`.  Every multiplier is
positive, and the resulting dual objective equals the primal forest
allocation.  Weak duality therefore proves exact optimality without either
slack shared resource.

The pinned exact Modal replay checks this primal-dual certificate, all
individual caps, both shared resources, and all 28 hierarchy rows on every
`K'` in `568339<=K'<=796599`.  All 64 bounded workers and all `228261`
rows completed.  Demand is strictly above capacity through `796598`; at
`796599` the sign reverses.  An independent verifier recomputes each pinned
endpoint from direct forest products.
