# Proof

Let `A` be the affine span of the selected errors.  Choose `b in A` above
the syndrome intercept and choose a direction `q in A-A` with `Hq=y_1`.
Every selected error has a unique expression

```text
e_gamma=b+gamma q+w_gamma,       w_gamma in K,
```

where `K=(A-A) intersect ker H` has dimension four.  Every member of `A`
vanishes on `P_0`; consequently `b`, `q`, and every member of `K` vanish on
`P_0`.

Puncture those coordinates and put

```text
K_E=K|E,
C_E=K_E+<q|E>,
U_E=-b|E.
```

Puncturing loses no dimension from `K`, because its deleted coordinates are
already zero.  Also `q|E` is not in `K_E`: otherwise it would equal the
restriction of some `w in K`; both vectors vanish on `P_0`, so `q=w` on all
of `D`, contradicting `Hq=y_1!=0=Hw`.  Hence

```text
dim K_E=4,       dim C_E=5.
```

Associate to the selected slope `gamma` the codeword

```text
c_gamma=gamma q|E+w_gamma|E.
```

The equation `e_gamma(x)=0` on `E` is exactly
`c_gamma(x)=U_E(x)`.  Since every selected error has at least `k+h` zeros
and all `p` deleted coordinates are zeros, its codeword has at least

```text
k+h-p=4+h+u+v
```

agreements.  If two slopes are distinct, their codewords have distinct
images in `C_E/K_E`, because those images are `gamma(q+K_E)`.  Their
agreement-set intersection is their common error-zero set with `P_0`
deleted, and is therefore at most

```text
kappa-p = 4+u+v       when kappa=k,
kappa-p = 3+u+v       when kappa=k-1.
```

It remains to identify the subcode.  The flat-nullity factorization gives

```text
K=L_G W,       W subset F[X]_<4+u,       dim W=4,
```

where `G` is the full common evaluation-root set and `W` has no common root
on `D\G`.  The coordinates `G\P_0` survive the puncture and are zero on all
of `K_E`; there are exactly `v` of them.  On the other coordinates,
multiplication by the nonzero values of `L_G` is a coordinate scaling, so
deleting those `v` loops makes `K_E` monomially equivalent to the evaluation
of `W`.

Finally, if `u=0`, then `W` is a four-dimensional subspace of the
four-dimensional space `F[X]_<4`, hence equals that whole space.  If also
`v=0`, there are no loop coordinates and `K_E` is a generalized
Reed-Solomon code of dimension four.  This proves every assertion.
