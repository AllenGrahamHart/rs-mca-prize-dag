# Proof

The normal of `H_x` in the four cubic coefficients is

```text
(1,x,x^2,x^3).
```

Any four such normals are independent by the Vandermonde determinant, so
four hyperplanes meet at the unique cubic `I_Tq`. Five hyperplanes indexed
by `S` meet exactly when one cubic agrees with `q` on `S`, equivalently when
`[S]q=0`. The divided-difference clique bridge excludes this on every
five-subset of `A`. The arrangement is therefore simple.

We prove (SC) in the following general form. Let `m` affine hyperplanes be in
simple position in affine `r`-space, and evaluate a nonzero polynomial `F` of
degree `d<=m-r` on their `C(m,r)` vertices. Then

```text
wt(F) >= C(m-d,r).                                    (1)
```

For `r=1`, this is the usual fact that a degree-`d` polynomial has at most
`d` roots among `m` distinct points. Suppose `r>1`. Factor from `F` all `s`
defining linear forms of arrangement hyperplanes which divide it:

```text
F=(product_(j in J) l_j)G,       |J|=s<=d.
```

A vertex on one of those `s` hyperplanes is a zero of `F`; at a vertex
avoiding them the extracted factors are nonzero. We may therefore use the
reduced simple arrangement of `m'=m-s` hyperplanes and count the nonzero
values of `G`, whose degree is `e=d-s` and which is divisible by none of the
remaining hyperplane forms.

For each remaining hyperplane `H_i`, the restriction `G|H_i` is nonzero.
The other `m'-1` hyperplanes restrict to a simple arrangement in dimension
`r-1`. By induction, `G` is nonzero at at least

```text
C((m'-1)-e,r-1)=C(m-d-1,r-1)
```

vertices lying on `H_i`. Sum this over all `m'` choices of `i`. Every
nonzero vertex belongs to exactly `r` arrangement hyperplanes, so

```text
wt(F)=wt(G)
 >= (m-s)/r C(m-d-1,r-1)
 >= (m-d)/r C(m-d-1,r-1)
 = C(m-d,r).
```

This proves (1), and `r=4` proves (SC).

Sharpness follows by taking `F` to be the product of any `d` arrangement
hyperplane forms: it is nonzero exactly at the vertices avoiding those
hyperplanes, of which there are `C(m-d,4)`. For `d=h=m-4`, (SC) makes the
evaluation map injective. Its source and target both have dimension

```text
C(h+4,4)=C(m,4),
```

so it is an isomorphism.

Finally, the complements of the reused direction sets have exact sizes
`1,3,4`. A nonzero degree-`d` polynomial vanishing on every reused direction
would have all its nonzero evaluations in that complement. This contradicts
(SC) whenever `C(m-d,4)` is larger than the corresponding complement. The
largest such degrees are `4,4,2`, as claimed.
