# Proof

Reduce the proved global Padé identity modulo `L_U0`:

```text
Qbar B_src=Lambda G                  in A[z].      (1)
```

The source-multiplier theorem gives `B_src=J(z-varphi)`, with `J` a unit
of `A`, and `Lambda(varphi)=0`. Polynomial division by the monic factor
`z-varphi` gives

```text
Lambda(z)=(z-varphi)q_varphi(z),                  (2)
```

where every coefficient of the quadratic `q_varphi` lies in
`span_A{1,varphi,varphi^2}`. Substitution in `(1)` yields

```text
(z-varphi)J Qbar=(z-varphi)q_varphi G.            (3)
```

A monic polynomial is not a zero divisor in `A[z]`, even though `A` is a
product algebra. Cancelling it proves `(PPQ3)`. Every `X`-coefficient of
the right side belongs to `E_3`, so `J U_Q subset E_3`. The primitive
locator has `e+1` independent parameter coefficients; multiplication by
the unit `J` preserves dimension. This proves `(PPQ4)`.

Let `L=L_U0` have degree `R`. The standard residue identity is

```text
tau(P)=sum_(x in U_0)P(x)/L'(x)=0
                                      for deg P<=R-2. (4)
```

Since `d=R-n-2`, equation `(4)` gives `S_d subset S_n^perp`. The two
spaces have the same dimension:

```text
dim S_d=R-n-1=dim A-dim S_n.                      (5)
```

The residue pairing on the split algebra is nondegenerate, so `(5)` proves
`(PPQ5)`.

An element `E in E_3` lies in the right radical of `(PPQ6)` exactly when

```text
E/J in S_n^perp=S_d.                              (6)
```

Because `J` is a unit, `(6)` is equivalent to `E in E_3 intersect J S_d`,
proving `(PPQ7)`. Equations `(PPQ4)--(PPQ5)` also show directly that the
mandatory subspace `J U_Q` lies in this right radical, so `xi>=0`.

The source-multiplier theorem identifies the left radical of `(PPQ6)` with
the common interpolation kernel `K_cap`. Hence the rank of `(PPQ6)` equals
`rank T=n+1-kappa`. On the other hand, rank computed from the right radical
is

```text
dim E_3-dim(E_3 intersect J S_d)
 =3r-(e+1)-xi.                                    (7)
```

Equating the two expressions proves `(PPQ9)`. At `3r=n+5`, equation `(7)`
becomes `(PPQ10)`. QED.
