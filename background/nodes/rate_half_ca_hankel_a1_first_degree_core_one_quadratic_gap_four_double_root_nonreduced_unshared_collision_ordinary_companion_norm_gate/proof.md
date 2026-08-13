# Proof

The factor-saturation theorem gives, for every `x in U_0`,

```text
Q(t,x)=lambda_x product_(delta in A_x(Q))(t-delta),
lambda_x!=0,       A_x(Q) subset Gamma,
|A_x(Q)|=m.                                        (1)
```

The roots in `(1)` are distinct. At an incident point `(delta,x)`, the
all-excess factorization writes

```text
G(delta,X)=zeta_delta A_delta H_delta R_delta.     (2)
```

Here `x` is a simple root of `A_delta`, while `H_delta(x)` and
`R_delta(x)` are nonzero. Distinct factors have disjoint row roots, so the
other factors of `G` are nonzero at `(delta,x)`. Therefore

```text
partial_X Q(delta,x)!=0.                          (3)
```

Exactly the `m` factors indexed by `A_x(Q)` vanish simply at `x` in the
product `N_Q`. Hence

```text
ord_(X=x)N_Q=m                                    (4)
```

for every `x in U_0`. The rows are distinct, so `(4)` proves the
factorization in `(OCN2)`. Every specialization `Q(delta,X)` is nonzero by
the factor-saturation theorem. Thus `N_Q` is nonzero and its degree is at
most `3en`; subtracting `Rm` gives

```text
deg S_Q<=3en-Rm.                                  (5)
```

For `d_A=1`, `R=3p-2`, `2p=3e-1`, and an ordinary factor has
`n=3m/2`. Direct substitution in `(5)` gives `7m/2`. Equation `(4)` also
says that the quotient after removing `L_0^m` is nonzero at every root of
`L_0`, proving `(OCN3)`.

The shape classification gives the complete heavy-row record of an
ordinary companion:

```text
(m,n;r,b,t;ell)=(2,3;1,1,0;2)
             or (4,6;2,2,0;4).                   (6)
```

Thus `Q(t,x_*)` has exactly `r=m/2` distinct roots in `Gamma`, plus the
collision root `tau` of order `b=m/2`, and no other projective root. For
each of those `r` supported heavy-row roots `delta`, the factor
`Q(delta,X)` vanishes at `x_*`. Therefore

```text
(X-x_*)^r divides N_Q.                            (7)
```

No vertical simplicity is inferred here. Factorwise Bezout length one is
two-dimensional transversality and does not by itself force
`partial_XQ(delta,x_*)` to be nonzero.

Since `x_* notin U_0`, the factor `L_0^m` is a unit at `x_*`. Equation
`(7)` proves `(OCN4)`, and `(OCN5)` follows from the degree cap.

Finally divide `N_Q` by `(X-x)^m` and evaluate at a classified row. The
incident factors contribute their derivatives by `(3)` and every
nonincident factor is nonzero. Therefore

```text
[N_Q/(X-x)^m]_(X=x)=D_x(Q).                       (9)
```

Likewise

```text
[L_0^mS_Q/(X-x)^m]_(X=x)=L_0'(x)^mS_Q(x).        (10)
```

Comparison proves `(OCN7)`. The official and symbolic rows have
`R>14`, so the degree bound makes interpolation unique. QED.
