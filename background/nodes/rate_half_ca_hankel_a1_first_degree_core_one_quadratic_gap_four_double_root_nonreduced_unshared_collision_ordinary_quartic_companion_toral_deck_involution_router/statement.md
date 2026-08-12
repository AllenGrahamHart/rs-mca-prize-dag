# `A=1` collision ordinary-quartic toral deck-involution router

- **status:** PROVED
- **closure:** shape C has a scaling or reciprocal deck involution
- **consumer:** `rate_half_band_crossing_location`

Retain shape C and its absolutely irreducible bidegree-`(4,6)` companion
`Q(t,X)`. On the official row put

```text
N=2^41,       H=mu_N,       e=(2^39+1)/3,
F_6=3e-14=2^39-13,          P>2^167.               (QDI1)
```

The divided off-diagonal resultant

```text
L_Q(X,Y)=Res_t(Q(t,X),Q(t,Y))/(X-Y)^4              (QDI2)
```

is nonzero and has bidegree at most `(20,20)`. Its reduced off-diagonal
locus contains at least

```text
P_6=ceil(30F_6/4)=4123168604063                    (QDI3)
```

distinct points of `H^2`.

The degree-six projection `Q=0 -> P^1_t` has at most five geometric
off-diagonal orbit components. The Corvaja--Zannier theorem and the exact
official margins force at least one of them to be a translate of a
one-dimensional subtorus. That component is necessarily the graph of a
nonidentity deck involution. More precisely, over the geometric closure its
action on the row coordinate has one of the forms

```text
sigma(X)=-X,             or             sigma(X)=k/X,
k in H.                                                (QDI4)
```

Consequently the companion has one of the quotient forms

```text
Q(t,X)=R(t,X^2),
Q(t,X)=X^3 R(t,X+k/X),                              (QDI5)
```

up to a nonzero scalar normalization, where `R(t,W)` has bidegree `(4,3)`.

## Scope

This theorem does not exclude shape C: both involution forms in `(QDI4)`
remain live. It does not address shape A. The next obstruction must couple
the cubic quotient in `(QDI5)` to the collision/source constraints or show
that neither involution can preserve the exact saturated row packet.
