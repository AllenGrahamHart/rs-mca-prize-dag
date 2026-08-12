# `A=1` collision ordinary-companion complete shape exclusion

- **status:** PROVED
- **closure:** shapes B, C, and D are impossible; only shape A remains
- **consumer:** `rate_half_band_crossing_location`

Retain shape C and the deck involution `sigma` on its absolutely
irreducible bidegree-`(4,6)` companion `Q(t,X)`. On the official row put

```text
N=2^41,       H=mu_N,       e=(2^39+1)/3,
F_6=3e-14=2^39-13.                                  (OCX1)
```

Every one of the `F_6` full six-row slopes contributes thirty ordered
off-diagonal row pairs. Exactly six lie on the graph of `sigma`; after
removing that graph, the other at most four geometric fiber-product
components therefore contain at least

```text
P_res=24F_6/4=6F_6=3298534883250                  (OCX2)
```

distinct points of `H^2`. Each component image has bidegree at most
`(20,20)`. The Corvaja--Zannier bound and the exact official margins

```text
64*17280000*N^2 < P_res^3,
4*4800*N^2 < 2^167 P_res                           (OCX3)
```

force a second translated-subtorus component carrying an `H^2` point.
Degree comparison makes it the graph of a deck transformation

```text
eta(X)=cX       or       eta(X)=c/X,       c in H, (OCX4)
```

distinct from both the identity and `sigma`.

The deck group has order dividing six. Since `H` is a `2`-group, a
nonidentity scaling deck transformation has order two. Comparing `(OCX4)`
with either `sigma(X)=-X` or `sigma(X)=k/X` shows that the two distinct
involutions either coincide or generate a Klein four subgroup. Both are
impossible: the component is distinct, and four does not divide six.
Thus shape C does not occur.

The proved quadratic-companion exclusion already removes shapes B and D.
Consequently the four-shape factorwise Bezout classification leaves only

```text
shape A: Q_L has record
(m,n;r,b,t;ell)=(e-2,(3e-7)/2;e-7,2,3;4),          (OCX5)
```

with no ordinary companion.

## Scope

This theorem closes the ordinary-companion alternatives, not the remaining
irreducible shape A. The next obstruction must act directly on its unique
large odd factor or on the source/collision equations that produce it.
