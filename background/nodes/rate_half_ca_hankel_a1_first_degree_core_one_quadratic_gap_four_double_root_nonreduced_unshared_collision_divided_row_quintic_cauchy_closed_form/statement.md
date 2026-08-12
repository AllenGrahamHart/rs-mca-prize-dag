# `A=1` nonreduced collision divided-row quintic Cauchy closed form

- **status:** PROVED
- **closure:** the quintic vector is an automatic source Cauchy transform
- **consumer:** `rate_half_band_crossing_location`

Retain the unshared nonreduced collision and write

```text
L(X)=L_U0(X),       n_0=|U_0|=3p-2,
d=2p-1,             deg_X G<=p-3,
H_NR=g_*S_B,
G(t,x_*)=H_NR(t)T_2(t),
Q(t,x_*)=a_Qg_*(t)S_B(t)^3.                       (DCF1)
```

For `0<=i<=d`, define the source Cauchy moments

```text
D_i(t)=sum_(y in U_0) omega_y(t)y^i/(x_*-y),
h_i(t)=sum_(y in U_0) omega_y(t)y^i.              (DCF2)
```

Then `deg_t D_i<=1` and

```text
D_0=B(t,x_*)/L(x_*),
D_(i+1)=x_*D_i-h_i.                               (DCF3)
```

The divided-row quintic quotients have the exact closed form

```text
C_i(t)=-Lambda(t)x_*^iT_2(t)/L(x_*)
       +a_QS_B(t)^2D_i(t).                        (DCF4)
```

In particular, `(DCF4)` automatically gives

```text
deg_t C_i<=5,
C_(i+1)=x_*C_i-a_QS_B^2h_i,
C_i(tau)=x_*^i C_0(tau)!=0.                       (DCF5)
```

## Scope

This is a route fence. The degree-five quotient, its recurrence, and its
geometric correction value impose no condition beyond the source
interpolation identity and the heavy-row factorization. The theorem does
not make the collision feasible; it shows that excluding the collision
requires an additional scalar-weld or factor-geometric argument.
