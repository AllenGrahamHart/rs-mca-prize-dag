# `A=1` quadratic gap-four Pade regular-factor identity

- **status:** PROVED
- **closure:** exact contracted Pade resultant and correction-quartic factorization
- **consumer:** `rate_half_band_crossing_location`

Retain the core-one quadratic `u=4` packet. Put

```text
d=rho-1,       n_0=|U_0|,       L(X)=L_U0(X),
a(t)=lc_X Q(t,X),       Lambda(t)=product_(gamma in A)ell_gamma(t).
                                                               (PRI1)
```

Let the contracted moment functional be

```text
Phi_t(h)=sum_(x in U_0)omega_x(t)h(x),
```

so that its symmetric Hankel matrix is `M_1(t)` and its primitive kernel
polynomial is `Q(t,X)`. Define

```text
B(t,X)=sum_(x in U_0)omega_x(t)L(X)/(X-x),

P_F(t,X)=sum_(x in U_0)omega_x(t)
                 [Q(t,X)-Q(t,x)]/(X-x).             (PRI2)
```

Then `deg_X P_F<=d-1` and the split biform satisfies the exact Pade
syzygy

```text
Q B-Lambda G=L P_F.                                 (PRI3)
```

If

```text
adj M_1=D_1 q q^T,       deg D_1=e-2,
```

then, for one nonzero base-field scalar `c_F`,

```text
Res_X^(d,d-1)(Q,P_F)=c_F a^(2d+1)D_1.              (PRI4)
```

The normalized factor `D_1` cuts out the parameter pushforward of the
contracted Forney-contact divisor:

```text
div(D_1)=pi_* div(s_F).                              (PRI5)
```

Consequently the previously unallocated regular quartic is no longer
anonymous. In the double-root arm,

```text
D_1=c g_* S_B^2,       E_4=c' S_B^2.               (PRI6)
```

In the two-simple arm,

```text
D_1=c G_1G_2S_1S_2,       E_4=c' S_1S_2.           (PRI7)
```

All constants displayed in `(PRI6)--(PRI7)` are nonzero. Equalities are
identities of homogeneous binary forms and remain valid when correction
forms share roots with supported factors.

## Scope

The theorem identifies the quartic but does not exclude either root arm.
In particular, a square regular quotient in the double-root arm and a
linear-times-cubic quotient in the two-simple arm are not ruled out by
determinant degree alone.
