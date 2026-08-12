# `A=1` nonreduced collision divided-row quintic quotient

- **status:** PROVED
- **closure:** all divided-row moments have one common degree-`e-4` divisor and quintic quotients
- **consumer:** `rate_half_band_crossing_location`

Retain the unshared nonreduced exact collision and put

```text
H_NR=g_*S_B,       deg H_NR=e-4,
Q(t,x_*)=a_Qg_*S_B^3.                              (DQQ1)
```

For the canonical divided row

```text
U(t,X)=[Q(t,X)-Q(t,x_*)]/(X-x_*),
F_i(t)=Phi_t(X^iU(t,X)),                            (DQQ2)
```

there are homogeneous parameter forms `C_i` of degree at most five such
that

```text
F_i=H_NR C_i       (0<=i<=d).                      (DQQ3)
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

Let `T_2` be the nonzero quadratic residual of the outside row. The exact
Pade relation is

```text
a_QS_B^2B(t,x_*)-Lambda(t)T_2(t)
 =L_U0(x_*)C_0(t).                                 (DQQ6)
```

Consequently

```text
C_0(tau)=-Lambda(tau)T_2(tau)/L_U0(x_*)!=0,
C_i(tau)=x_*^iC_0(tau).                            (DQQ7)
```

## Scope

The quintic vector is not proved incompatible with the source equations.
The result gives a bounded six-coefficient replacement for the full
degree-`e+1` divided-row image; it does not restore `D_1=g_*S_B^2`
divisibility.
