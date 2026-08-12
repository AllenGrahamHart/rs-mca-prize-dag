# Cycle 192: rate-half shape-A pure-split component floor (2026-08-12)

The exact sums `sum a_delta=e` and `sum r_delta=e-7` force at least `e+7`
off-line slopes with zero excess and zero padding. On each such slope, the
entire degree-`n=(3e-7)/2` shape-A fiber splits into distinct classified
rows.

The unique large factor is absolutely irreducible: any Frobenius-conjugate
geometric factors would have to share all `|U_0|(e-2)` rational grid points,
far above their pairwise Bezout intersection. Its divided off-diagonal
resultant therefore contains at least

```text
75557863727701029814224
```

distinct official subgroup pairs. Since the degree-`n` cover has at most
`n-1` off-diagonal fiber-product components, one component contains at
least

```text
n+14=274877906955
```

such points. This does not trigger the companion torus argument: the large
factor's component bidegree remains macroscopic. The next geometric target
is a component-subdegree bound; the alternative remains a direct coupling
to the source or concentrated excess norm.

```text
start:                   d54687e6b
result:                  NARROWED, exact shape-A component point floor
DAG delta:               +1 PROVED node, +3 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: candidate Lane-T PR #1161 extension
delta-star movement:     none
compute:                 exact local replay only; no Modal spend
next route action:       bound component subdegree or couple pairs to source
```
