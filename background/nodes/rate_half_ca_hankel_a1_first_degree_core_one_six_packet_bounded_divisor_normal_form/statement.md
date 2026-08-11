# `A=1` core-one six-packet bounded-divisor normal form

- **status:** PROVED
- **closure:** distinguished-row radical, adjugate tail, and contact divisor
- **consumer:** `rate_half_band_crossing_location`

Retain any of the six core-one scalar-residual packets. Use the packet
coordinates

```text
u=Delta-I_H,       v=Delta-O,       0<=I_0<=u,
c=2+u+I_0,         d_*=e-c,       Delta=e-2.          (SBN1)
```

Let `x_*` be the unique heavy root of the residual linear form and let
`P_*` be the squarefree locator of the `d_*` supported slopes on that row.
Then, up to nonzero scalars,

```text
Qbar(U,V;x_*)=P_* K_c,              deg K_c=c<=6;
D=P_* E_(c-2),                      deg E_(c-2)=c-2<=4;
N_F(U,V;x_*)=P_* C_(c+1),           deg C_(c+1)<=c+1<=7,
                                      C_(c+1)!=0.     (SBN2)
```

Here `D` is the core-one middle-Hankel adjugate factor.

Let `R_*` be the reduced divisor on `C` formed by the `d_*` distinguished
incidences, and let `R_0` be the reduced divisor of the `I_0` ordinary heavy
incidences. There are effective divisors

```text
Z_c=V_(x_*)-R_*,       deg Z_c=c,
E_u,                   deg E_u=u<=2,                 (SBN3)
```

such that

```text
div(s_F)=R_*+R_0+E_u.                                 (SBN4)
```

Consequently every packet satisfies the bounded degree-two Picard relation

```text
O_C(rho+2,-e-1)=O_C(Z_c-R_0-E_u),
deg(Z_c-R_0-E_u)=c-I_0-u=2.                           (SBN5)
```

Thus all official-size data outside the squarefree locator `P_*` is carried
by divisors or polynomial tails of degree at most seven.

## Scope

The theorem does not assert that the signed divisor in `(SBN5)` is
effective, nor does it exclude any of the six packets. The first packet has
`R_0=E_u=0` and recovers the effective two-point normal form.
