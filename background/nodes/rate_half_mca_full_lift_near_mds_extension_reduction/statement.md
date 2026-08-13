# Full-lift near-MDS extension reduction

- **status:** PROVED
- **scope:** the full-lift branch of a pair-noncontained shortened MCA
  family with explanation affine rank `K`

Let `C=RS[F,D,K]` have length `N`, let `m>K`, and suppose the selected
explanations have affine rank `K` while the lifted pairs
`(gamma,c_gamma)` have affine rank `K+1`.  Put

```text
W=C+span{r_1},       e=min_(b in C) wt(r_1-b),       t=N-m.
```

Then `r_1 notin C`, `dim W=K+1`, and the generalized Hamming weights of
`W` are exactly

```text
d_1(W)=e,
d_j(W)=N-K+j-1       for 2<=j<=K+1.                 (NM1)
```

The selected errors `r_gamma-c_gamma` lie in one affine coset of `W`, have
weight at most `t`, have full affine rank `K+1`, and determine their slopes
uniquely.  On every selected maximal zero set, restriction of `W` is
injective; this is equivalent to same-support pair noncontainment.

Thus the full-lift MCA residual is a full-affine-rank sparse-list problem in
a codimension-one RS extension whose only non-MDS generalized weight is
`d_1=e`.  Applying the corrected proper-subspace compiler gives

```text
|Z| <= floor(
  N^(K+1)_falling /
  (max(1,e-t) * product_(i=1)^K (m-K+i))
).                                                       (NM2)
```

At the best possible endpoint `e=N-K`, `(NM2)` is still

```text
KoalaBear:   743896698428332665 > 274980728111395087;
Mersenne-31:          219426634 >          16777215.
```

Therefore another weight-hierarchy or ordered-basis replay cannot close the
full-lift cells through this compiler.  The missing input must exploit
additional structure of the one-dimensional RS extension or improve the
row-sharp affine-list count.

## Nonclaims

This node does not prove that every possible generalized-weight argument is
optimal, classify the extension `W`, pay either middle-support interval, or
close a deployed row.
