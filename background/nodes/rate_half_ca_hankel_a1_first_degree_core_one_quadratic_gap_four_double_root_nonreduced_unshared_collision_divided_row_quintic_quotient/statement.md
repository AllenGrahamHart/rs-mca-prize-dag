# `A=1` nonreduced collision divided-row quintic quotient

- **status:** PROVED
- **closure:** all divided-row moments have one common degree-`e-4` divisor and quintic quotients
- **consumer:** `rate_half_band_crossing_location`

Retain the unshared nonreduced exact collision and put

```text
J_*=gcd(Lambda,g_*),       Lambda_0=Lambda/J_*,
g_off=g_*/J_*,
H_mom=g_*S_B,              deg H_mom=e-4,
Q(t,x_*)=a_Qg_*S_B^3,
G(t,x_*)=g_off S_BT_(2+d_A).                      (DQQ1)
```

For the canonical divided row

```text
U(t,X)=[Q(t,X)-Q(t,x_*)]/(X-x_*),
F_i(t)=Phi_t(X^iU(t,X)),                            (DQQ2)
```

there are homogeneous parameter forms `C_i` of degree at most five such
that

```text
F_i=H_mom C_i       (0<=i<=d).                     (DQQ3)
```

They satisfy the exact recurrence

```text
C_(i+1)=x_*C_i-a_QS_B^2h_i       (0<=i<d),         (DQQ4)
```

where `h_i=Phi_t(X^i)` is parameter-linear. In vector form, with `u` the
coefficient vector of `U` padded to length `d+1`,

```text
M(t)u(t)=g_*(t)S_B(t)C(t),       deg_t C<=5.       (DQQ5)
```

The center-adjusted Pade relation is

```text
a_QS_B^2B(t,x_*)-Lambda_0(t)T_(2+d_A)(t)
 =L_U0(x_*)C_0(t).                                 (DQQ6)
```

Consequently

```text
C_0(tau)=-Lambda_0(tau)T_(2+d_A)(tau)/L_U0(x_*)!=0,
C_i(tau)=x_*^iC_0(tau).                            (DQQ7)
```

## Scope

The quintic vector is not proved incompatible with the source equations.
The moment divisor remains the full `g_*S_B` in both deficit profiles even
though the fixed heavy row contains only `(g_*/J_*)S_B`. The result does
not restore `D_1=g_*S_B^2` divisibility.
