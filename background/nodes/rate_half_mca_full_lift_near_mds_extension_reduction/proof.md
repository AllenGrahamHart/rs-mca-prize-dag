# Proof

Pair noncontainment implies `r_1 notin C`: if `r_1` were a codeword, then on
any selected agreement support `r_1` would explain the direction and
`c_gamma-gamma r_1` would explain the base.  Hence `W=C+span{r_1}` has
dimension `K+1`.

Interpolation on any `K` coordinates gives a codeword agreeing with `r_1`
there, so `e<=N-K`.  A nonzero word of `W` is either a nonzero word of `C`,
of weight at least `N-K+1`, or a nonzero scalar multiple of `r_1-b` for some
`b in C`, of weight at least `e`.  A nearest `b` attains `e`, proving
`d_1(W)=e`.

Fix `2<=j<=K+1` and a `j`-dimensional subspace `A<=W`.  If `A<=C`, the MDS
weight hierarchy gives

```text
|supp(A)|>=N-K+j.
```

Otherwise `dim(A intersect C)=j-1`.  A `(j-1)`-dimensional RS subcode has at
most `K-j+1` common zero coordinates, so

```text
|supp(A)|>=N-K+j-1.
```

The generalized Singleton bound for the `[N,K+1]` code `W` is the reverse
inequality `d_j(W)<=N-K+j-1`.  This proves `(NM1)`.

The selected error differences are the images of the lifted differences
under

```text
(a,u) -> a r_1-u.
```

This map is an isomorphism from `F direct_sum C` to `W`, so full lifted rank
gives error affine rank `K+1`.  It also shows that two equal errors have the
same slope, because `r_1 notin C`.

Let `S_gamma` be a selected maximal zero set.  If a nonzero
`a r_1-u in W` vanished on `S_gamma`, then `a=0` would contradict the RS
root bound because `|S_gamma|>=m>K`.  If `a!=0`, the codeword
`b=a^(-1)u` would agree with `r_1` on `S_gamma`, while
`c_gamma-gamma b` would agree with the base there.  This is precisely a
same-support pair containment.  The converse is immediate, proving the
restriction equivalence.

Finally, the full-explanation corrected compiler has `q=K`, so its two
numerators coincide and its denominator is

```text
max(1,e-t) * product_(i=1)^K (m-K+i).
```

This is `(NM2)`.  Exact integer substitution at `e=N-K` gives the two
displayed deployed bounds.
