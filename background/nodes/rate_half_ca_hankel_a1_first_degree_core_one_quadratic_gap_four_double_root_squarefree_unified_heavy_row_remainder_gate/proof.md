# Proof

## Cubic quotient at every squarefree root

At correction roots disjoint from `g_*`, the separated heavy-quotient
theorem gives

```text
D_1|F_i,       deg(F_i/D_1)<=3.                    (1)
```

At roots shared with `g_*`, the shared third-jet vanishing theorem gives the
same conclusion, with local Smith type `[3]`. At roots of `g_*` outside
`S_B`, the specialized minimal-locator kernel gives the remaining supported
factor. Since `S_B` and `g_*` are squarefree, these local valuations combine
to give the global identities

```text
F_i=D_1C_i,
C_(i+1)=x_*C_i-(a_Q/a_D)S_Bh_i,
deg C_i<=3.                                         (2)
```

Evaluating the Pade syzygy at `x_*` therefore yields

```text
Lambda G(t,x_*)=g_*S_B^2T_3,
deg T_3<=3.                                         (3)
```

Cancel `J` in `(3)`. With

```text
Lambda=JLambda_0,       g_*S_B^2=JH,               (4)
```

one has `gcd(Lambda_0,H)=1`, so `Lambda_0|T_3`.
Writing `T_3=Lambda_0T_j` gives

```text
G(t,x_*)=HT_j,       deg T_j<=j.                   (5)
```

## Center-overlap cap

The exact source partition gives

```text
supp(b_0,b_1)=U,
S_gamma=supp b(gamma) subset U
                  for gamma in {alpha,beta,theta}. (6)
```

The fixed heavy point `x_*` lies outside `U`. Hence, if any center is a root
of `Q(t,x_*)`, then `x_*` is a padded rather than actual-support root at that
center. Such center roots are exactly roots of `g_*`, and their number is

```text
sum_(gamma in A)r_gamma<=1.                         (7)
```

Every center root of `S_B` is also a root of `Q(t,x_*)`, hence by `(6)` is
already among those roots of `g_*`. Therefore every center factor occurring
in `g_*S_B^2` is counted by `(7)`. Since `Lambda` is squarefree,

```text
j=deg gcd(Lambda,g_*S_B^2)<=1.                     (8)
```

This proves `(HUG2)` and the degree bound in `(HUG3)`.

## Exact correction orders

Fix a root `tau` of `S_B`. On the normalized curve, the divisor identities
give

```text
ord(X-x_*)=r_tau+3,
ord(P_F|_C)=r_tau+2.                               (9)
```

When `r_tau=1`, simplicity of the specialized root gives
`Q_X(tau,x_*)!=0`, so the supported and correction contacts are on the same
unique normalized branch; the orders in `(9)` genuinely add. The heavy row
is outside `U_0`, so `L_U0(x_*)` is a unit. Restricting the Pade syzygy to
the curve and then replacing the moving point by `x_*` changes the value
only in order `r_tau+3`. Thus

```text
ord_tau G(t,x_*)=r_tau+2-c_tau.                    (10)
```

By definition of `J`, the right side is also `ord_tau H`. Hence `T_j` is a
unit at every correction root. This proves nonvanishing and
`gcd(T_j,S_B)=1`.

Finally, the coefficient interpolation proof of the barycentric gate uses
only `(5)` and the row coefficient-MDS identities. It is unchanged by
shared roots, proving `(HUG6),(HUG7)`. QED.
