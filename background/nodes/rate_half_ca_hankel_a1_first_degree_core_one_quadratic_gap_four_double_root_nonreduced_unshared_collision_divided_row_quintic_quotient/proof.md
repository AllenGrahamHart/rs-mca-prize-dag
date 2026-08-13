# Proof

The center-adjusted heavy-row theorem gives

```text
Q(t,x_*)=a_QJ_*g_off S_B^3,
G(t,x_*)=g_off S_BT_(2+d_A),
Lambda=J_*Lambda_0.                                (1)
```

Evaluate the Pade syzygy at `x_*`:

```text
Q(t,x_*)B(t,x_*)-Lambda(t)G(t,x_*)
 =L_U0(x_*)F_0(t).                                 (2)
```

Both terms on the left of `(2)` are divisible by
`J_*g_off S_B=g_*S_B`. The scalar `L_U0(x_*)` is nonzero, so

```text
F_0=g_*S_BC_0.                                     (3)
```

The source weights are parameter-linear and `U` has parameter degree at
most `e`, hence `deg F_0<=e+1`. Since `deg(g_*S_B)=e-4`, equation `(3)`
gives `deg C_0<=5`.

The kernel recurrence is

```text
F_(i+1)=x_*F_i-Q(t,x_*)h_i.                        (4)
```

Substitute `(1)` and `(3)` into `(4)` and divide by `g_*S_B`:

```text
C_(i+1)=x_*C_i-a_QS_B^2h_i.                       (5)
```

Because `deg S_B^2=4` and `deg h_i<=1`, induction gives
`deg C_i<=5` for every `i`. The entries of `M(t)u(t)` are the `F_i`, so
this proves `(DQQ3)--(DQQ5)`.

Cancel `J_*g_off S_B=g_*S_B` directly in `(2)` using `(1),(3)`. The result
is `(DQQ6)`. At `tau`, the first term vanishes, while
`Lambda_0(tau)T_(2+d_A)(tau)L_U0(x_*)` is nonzero. This proves the first
assertion in `(DQQ7)`. Evaluating recurrence `(DQQ4)` at `tau` gives the
second by induction. QED.
