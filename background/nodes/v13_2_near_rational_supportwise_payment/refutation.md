# Refutation

Take `F=F_17`, the smooth dyadic multiplicative subgroup

```text
D=mu_8=(1,2,4,8,16,15,13,9),
C=RS[F_17,D,4].
```

Set

```text
m=5,    w=m-K=1,
u=(0,0,0,0,0,0,1,1),
v=(0,0,0,0,0,0,1,2).
```

All source hypotheses hold:

```text
n-3w=8-3=5=m,       2w=2<=n-K=4.
```

At the two distinct finite slopes `z=16` and `z=8`, respectively,

```text
u+16v=(0,0,0,0,0,0,0,16),
u+ 8v=(0,0,0,0,0,0,9, 0).
```

Each word is at Hamming distance one from the zero codeword, has nonzero
agreement census at `m=5`, and has a shifted-lattice vector `(W,0)` of
shifted degree one, where `W=X-9` or `W=X-13`. Hence `d1<=w` at both
slopes.

Nevertheless both slopes are support-wise MCA-bad. At `z=16`, use the
five-point support with indices `{0,1,2,3,6}`; at `z=8`, use indices
`{0,1,2,3,7}`. The corresponding line word is zero on the support, so the
zero codeword explains it. On either support, a degree-below-four polynomial
explaining `u` would vanish at four distinct domain points and equal one at
the fifth. This is impossible, so no codeword pair explains `(u,v)` on that
same support. This is exactly the support-wise MCA condition.

The pair does have the common zero-codeword explanation on the first six
coordinates. That fact coexists with the two bad supports and exposes the
invalid existential-support inference. The counterexample therefore lies on
a smooth dyadic domain, at rate `1/2`, and at equality in `n-3w>=m`.
