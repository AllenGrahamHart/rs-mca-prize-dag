# Proof: general t-petal fixed joint-owner packing

For an exact candidate, let

```text
S=Z(G_H) disjoint_union R_H subset C disjoint_union Bkg.
```

The list threshold forces `|R_H|>=u`; hence `|S|>=d+v`. For two distinct
primitive candidates, the joint determinant degree budget gives

```text
|S_1 intersect S_2|
 =|Z(G_1) intersect Z(G_2)|+|R_1 intersect R_2|
 <=r.                                                  (1)
```

Every candidate in `F_Q` intersects the anchor marked set exactly in the
`q` roots of `Q`, by the joint-owner theorem. In particular, all members of
`F_Q` contain those `q` roots. Remove them from every `S`. The resulting
sets lie in a universe of size `N+b-q`, have size at least `d+v-q`, and any
two meet in at most `r-q` points by `(1)`.

Put `s=r-q+1`. No `s`-subset can lie in two different reduced marked sets.
Each reduced set contains at least `binom(d+v-q,s)` such subsets, while the
universe contains `binom(N+b-q,s)`. Double counting proves `(JP3)`.

The denominator is defined. If `u>=0`, then

```text
d+v-r=d+u-r=ell.
```

If `u<0`, then `d+v-r=d-r=t ell-d`. The list threshold
`t ell+|R_H|>=d+ell` and `|R_H|<=b` gives

```text
t ell-d>=ell-b>=1.
```

Thus `d+v-q>=r-q+1=s` in both cases.

If `q=r-c`, then `s=c+1`. The numerator binomial is at most
`n^(c+1)` and the denominator is at least one, proving `(JP4)`. Setting
`c=0` in the exact ratio gives `(JP5)`, and the displayed calculation gives
`(JP6)`. QED.
