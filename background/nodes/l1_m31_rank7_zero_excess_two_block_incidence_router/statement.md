# M31 rank-seven zero-excess two-block incidence router

- **status:** PROVED
- **closure:** proof with two independent exact-arithmetic replay sources
- **consumer:** `l1_mixed_petal_amplification` and the M31 LIST stress-row
  upper route
- **upstream source:** `przchojecki/rs-mca` source packet commit `b9665145`

## Fixed source class

Use the normalized-label class left by the M31 rank-seven proper-`G`
route cut. Put

```text
g       = 354972       planted-root domain size
E       = 698585       external domain after deleting S
N       = 1053557      g+E
k       = 4981         residual polynomial dimension
t       = 4980         k-1
m       = 72428        exact combined agreement weight
M0      = 2157929      forbidden proper-G zero-excess mass
```

For each distinct zero-excess proper member `i`, let

```text
A_i = Z(Q_i)                         subset of Z(P)
B_i = Z(H_i) minus S                 subset of E0 minus S
q_i = |A_i|,       |B_i| = m-q_i.
```

Then every pair of distinct members satisfies the exact two-block
intersection bound

```text
|A_i intersect A_j| + |B_i intersect B_j| <= t.       (TB1)
```

## Tail and mean conclusions

For every such family:

```text
# {i : q_i <= 4980}  <= 40,
# {i : q_i >= 67448} <= 7.                              (TB2)
```

If `M` is the family size and `Q=sum_i q_i`, then

```text
(N Q - M m g)^2
  <= g E (M N (m-t) + M^2 (N t-m^2)),                 (TB3)

N t-m^2 = 898676.
```

In particular, if `M>=M0`, then

```text
23945 < Q/M < 24860.                                  (TB4)
```

A violating class therefore has at least

```text
2157929-40-7 = 2157882                                 (TB5)
```

members in `4981<=q_i<=67447`. Every one has a different proper locator
`G_i`, equivalently a different complement `Q_i`. Thus the missing theorem
is not a sum of nineteen near-maximal fixed-`G` slices: it is a collective
middle-band census of more than 2.15 million distinct locators whose mean
complement degree is pinned near `24403`.

## Scope

This is an exact source-bound route reduction. It does not bound the middle
band, pay `Q=147595`, produce a v4 atom, treat ranks at least eight, or close
the M31 LIST row or either Prize problem.
