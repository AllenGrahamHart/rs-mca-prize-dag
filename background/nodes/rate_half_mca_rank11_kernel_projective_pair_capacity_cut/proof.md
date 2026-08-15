# Proof

For every row `K'`, let `x_d` be the residual-normalized number of
rank-`10-d` incidences, `1<=d<=9`.  Build the nine inherited individual
ambient/support caps, replacing only the corank-one record factor by the
proved value

```text
M_1=8147918.
```

Impose all 28 multi-step shadow inequalities.  On every row from `18159`
through the first wall, the exact optimizer has two cap roots:

```text
x_1=A_1,                    x_2=A_2,
```

and seven tight tree edges

```text
1 --H_(3,2)--> 3 --H_(5,2)--> 5 --H_(7,2)--> 7 --H_(9,2)--> 9,
1 --H_(4,3)--> 4 --H_(6,2)--> 6 --H_(8,2)--> 8.
```

Every other count is the positive tree multiple of `x_1`.  Both shared
resources, full containment and rank-preserving nine-shadow, are strict.
All other individual caps are strict.  Of the 28 hierarchy rows, 22 are
tight: the seven displayed tree rows and fifteen exact cycle identities.

For a tree edge from `d-t` to `d`, write its inequality as

```text
R_(t,d) x_d <= q_(t,d) x_(d-t).
```

Starting at the leaves, assign the edge dual multiplier

```text
h_(t,d)=(1+sum_child q h)/R_(t,d).
```

The two root cap prices are `1+sum_child qh`.  All multipliers are positive,
and their dual objective equals the sum of the displayed primal allocation.
This proves exact optimality without invoking either slack shared resource.

The pinned exact Modal replay evaluates this primal-dual certificate, all
individual caps, both shared resources, and all 28 hierarchy rows on every
`K'` in `18159<=K'<=377674`.  It completed all 64 bounded workers and all
`359516` rows.  Demand is strictly above capacity through `377673`; the
integer gap there is the value in the statement.  At `377674` the sign
reverses by the displayed wall excess.  The independent verifier recomputes
the endpoint and wall optimum from direct tree-path products.
