# `A=1` quadratic separated double-root heavy-quotient cubic residual

- **status:** PROVED
- **closure:** exact `D_1` divisibility and type `[2]` on the separated correction locus
- **consumer:** `rate_half_band_crossing_location`

Retain the double-root arm of the quadratic `u=4` packet. Normalize

```text
Q(t,x_*)=a_Q g_*(t)S_B(t)^3,
D_1(t)=a_D g_*(t)S_B(t)^2,                          (HQC1)
```

with `a_Q,a_D!=0`.

Assume the separated-correction condition

```text
S_B is squarefree,       gcd(g_*,S_B)=1.             (HQC0)
```

Put `kappa=a_Q/a_D` and divide the fixed heavy row:

```text
U(t,X)=[Q(t,X)-Q(t,x_*)]/(X-x_*),
deg_X U<=d-1.                                       (HQC2)
```

For the contracted moment functional define

```text
h_i(t)=Phi_t(X^i),
F_i(t)=Phi_t(X^iU(t,X)).                            (HQC3)
```

There are homogeneous parameter forms `C_i(t)` of degree at most three
such that, for `0<=i<=d`,

```text
F_i=D_1 C_i.                                        (HQC4)
```

They satisfy the exact cubic recurrence

```text
C_(i+1)=x_* C_i-kappa S_B h_i       (0<=i<d),       (HQC5)
```

and the first component is the contracted Pade value

```text
P_F(t,x_*)=D_1(t)C_0(t).                            (HQC6)
```

Equivalently, if `u(t)` is the coefficient vector of `U(t,X)`, padded by
one zero to length `d+1`, and `C=(C_0,...,C_d)^T`, then

```text
M(t)u(t)=D_1(t)C(t),       deg_t C<=3.              (HQC7)
```

The Pade syzygy at the external heavy row becomes

```text
Lambda(t)G(t,x_*)
 =g_*(t)S_B(t)^2
   [a_Q S_B(t)B(t,x_*)-a_D L_U0(x_*)C_0(t)].        (HQC8)
```

At each of the two projective roots `tau` of `S_B`, the regular local Smith
block has exactly one positive invariant, of exponent two:

```text
Smith_tau(D_1)=[2].                                  (HQC9)
```

Thus the separated correction has Smith type `[2]`, not `[1,1]`.

## Scope

The cubic vector `C` is not proved to vanish or to violate the source
equations. `(HQC9)` narrows the separated correction mechanism to one local
chain but does not exclude that chain; the abstract marked-jet countermodel
has the same type `[2]`. The theorem makes no `D_1`-divisibility or Smith
claim when `S_B` is nonreduced or shares a root with `g_*`.
