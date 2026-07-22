# Proof

Use the flat-nullity notation

```text
g=|G_0|=k-a-u,       p=|P_0|=g-v=k-a-u-v,
```

where `G_0` is the global root set of the kernel slice and `P_0` is the
persistent root set of the affine family. At a coordinate of `G_0\P_0`, a
selected error value is a nonzero affine function of its slope and vanishes
at at most one slope. Delete the union of those exceptional slopes. Its size
is at most `v`, and no retained selected error vanishes on `G_0\P_0`.

Divide the kernel by the locator of `G_0` and puncture `G_0`. The flat-nullity
factorization gives an `a`-dimensional subspace

```text
W subset F[X]_{<a+u}
```

with no common root on a domain of size `n-g=R+a+u=N`. A retained selected
error has at least

```text
k+h-p=a+h+u+v=m
```

zeros there, and two residual zero sets meet in at most
`k-p=a+u+v=kappa` points.

The restriction of `W` to every full residual zero set has rank `a`. Write
the affine extension as

```text
e_gamma=b+gamma q+w_gamma,       w_gamma in W.        (1)
```

The direction `q` is not in `W` on the full zero set: otherwise `(1)` also
puts `b` in `W` there, and lifting those explanations together with `P_0`
gives the tangent-paid common `k+h`-point explanation. Choose a deterministic
`m`-subset containing a `W` basis and one witness to `q notin W`; fill any
remaining positions in the ambient order. This preserves full rank,
nondegeneracy, and the pair cap, proving `(GC1)`.

Let `B=8n^3`. On the prize rows, even after deleting `v<=k` exceptional
slopes,

```text
h(B+1-v)>2N-2kappa=2(R-v).                            (2)
```

Choose an inclusion-minimal nonempty subfamily satisfying

```text
h|G|>=2|union G|-2kappa.                              (3)
```

Writing equality with excess `e` gives `(GC2)`. Minimality gives
`e+2p_A<=h-1` for each block-private count, hence `0<=e<=h-1`. One block
would force `h>=2h`. Two blocks have union at least `kappa+2h`, so `(3)`
would force `2h>=4h`. Therefore `t>=3`.

For each block `A`, choose a full-row-rank parity check of `W|A`. It has
`m-a=h+u+v` rows. Stack those checks in the two syndrome columns as in the
uniform compiler. Evaluation of `W` is injective on the core union because
each block contains a basis, so the two copies of `W` give `2a` independent
right-kernel directions. The pair `(b,q)` gives one further direction by the
chosen nondegeneracy witness. The stack rank is at most

```text
2|V|-(2a+1).
```

Its left kernel consequently has dimension at least

```text
(h+u+v)t-[2|V|-(2a+1)]
 =(u+v)(t-2)+e+1,                                    (4)
```

which proves `(GC3)`. Every left relation gives block rows `lambda_A` with

```text
sum_A lambda_A=0,       sum_A gamma_A lambda_A=0.     (5)
```

At an active coordinate, one nonzero coefficient cannot satisfy the first
equation, and two at distinct slopes cannot satisfy both. The active degree
is at least three.

Suppose a trade has matrix rank one. Write its nonzero block rows as
`lambda_i=alpha_i lambda`. Their common support `S=supp(lambda)` is contained
in every active block. Evaluating `(5)` at any point of `S` gives `(GC4)` and
shows that at least three rows are active.

The vector `lambda` is a nonzero linear dependence among the coordinate
columns of `W` indexed by `S`. Its support therefore contains a matroid
circuit. Choose the lexicographically first one and call it `C`. The punctured
matroid has no loops, and its rank is `a`, so `2<=|C|<=a+1`.

Restrict `(1)` to `C` for two distinct active slopes. In the one-dimensional
quotient `F^C/(W|C)`, it gives

```text
[b]+gamma_i[q]=0,       [b]+gamma_j[q]=0.
```

Subtracting and using `gamma_i!=gamma_j` gives `[q]=0`, then `[b]=0`. This is
`(GC5)`. The circuit is canonical by construction.

Conversely, the rank-one description before circuit selection is exact: any
common nonzero dual vector `lambda` and nonzero coefficient vector satisfying
`(GC4)` obey both equations in `(5)`. Finally, when `u=0`, the polynomial
space is all `F[X]_{<a}`, whose coordinate matroid is uniform. Every circuit
has size `a+1`, and the previously proved locator cancellation gives the
stronger `(S,Q,alpha)` normal form. QED.
