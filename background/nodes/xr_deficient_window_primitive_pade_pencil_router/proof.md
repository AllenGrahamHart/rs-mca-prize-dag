# Proof

Write a syzygy as a polynomial pair `(A,B)` of component degrees `<d`.
The pointwise rational-direction theorem gives, for every maximal pair,

```text
A(x)E(x)+B(x)E'(x)=0                         (1)
```

at every `x in H`.

## Kernel projective rank one

Choose one counted pair and let `T` be its full joint error support.
Maximality gives `|T|=r'=R-d`. For two syzygies `(A,B),(C,D)`, equation
`(1)` says that at each `x in T` the two row vectors

```text
(A(x),B(x)),       (C(x),D(x))
```

both annihilate the same nonzero error vector. Hence

```text
Delta(X)=A(X)D(X)-B(X)C(X)
```

vanishes on all `r'` points of `T`. But `deg Delta<=2d-2`. On every
official row and every `d<=h-2`,

```text
r'-(2d-2)=R-3d+2 >= R-3h+8 >0.               (2)
```

Therefore `Delta=0` identically. Every two kernel syzygies are
projectively proportional over `F(X)`.

Fix a nonzero syzygy and divide its components by their monic gcd,
writing it as `S_0(P,Q)` with `gcd(P,Q)=1`. If `(A,B)` is any other
syzygy, determinant zero gives `AQ=BP`. Coprimality implies
`A=SP,B=SQ` for a polynomial `S`. Thus `(PP1)` holds for a linear
multiplier space `W`. The tangent gate makes both primitive components
nonzero and nonproportional, so `ell>=1`.

## Forced roots and dimensions

Since `P,Q` are coprime, they have no common root. Consequently `x in H`
is a common root of every pair `(SP,SQ)` exactly when every multiplier
`S in W` vanishes at `x`. The locator of `G_d` therefore divides every
multiplier. A nonzero multiplier has degree `<d-ell`, so

```text
ell+g<=d-1.
```

After dividing all multipliers by that locator, they lie in the
`d-ell-g` dimensional polynomial space. Since multiplication by `(P,Q)`
is injective,

```text
dim K_d=dim W<=d-ell-g,
```

proving `(PP2)`.

## Primitive direction and affine family

For `x notin G_d`, choose `S in W` with `S(x)!=0`. Applying `(1)` to
`(SP,SQ)` and cancelling the nonzero scalar `S(x)` proves `(PP3)`.

For a counted pair put `c_{f,g}=Pf+Qg`. On `H\G_d`, `(PP3)` says that
`c_{f,g}` agrees with the fixed received function `Pu+Qv`. Also

```text
deg c_{f,g}<k+ell.
```

By `(PP2)`,

```text
n-g-(k+ell)=R-(g+ell)>=R-d+1=r'+1>0.
```

Thus any two such polynomials agree on more points than their degree and
are equal. Fix a base member `(f_0,g_0)`. Every other member satisfies

```text
P(f-f_0)+Q(g-g_0)=0.
```

Coprimality gives a unique polynomial `tau` with

```text
f-f_0=Q tau,       g-g_0=-P tau.
```

The degree-`<k` constraints imply `deg tau<k-ell`, proving `(PP4)`.

For two distinct parameters, a point in both full joint cores is a
common zero of `Q(tau_1-tau_2)` and `P(tau_1-tau_2)`. Coprimality makes
it a zero of `tau_1-tau_2`, a nonzero polynomial of degree at most
`k-ell-1`. This proves the core-intersection cap.

Finally, if `g>=2(h-d)`, `(PP2)` yields

```text
ell<=d-1-2(h-d)=3d-2h-1.
```

Since `ell>=1`, `3d>=2h+2`, which is `(PP5)`. QED.
