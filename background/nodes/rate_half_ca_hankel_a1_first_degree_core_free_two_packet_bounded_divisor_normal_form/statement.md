# `A=1` core-free two-packet bounded-divisor normal form

- **status:** PROVED
- **closure:** two distinguished row radicals, regular determinant, and contact divisor
- **consumer:** `rate_half_band_crossing_location`

Retain either core-free residual-degree-two packet. Let `x_1,x_2` be the
two distinguished heavy roots, let

```text
c_i=e-d_(x_i),       c_1+c_2=2+I_0,
I_0 in {0,1},       Delta=2e-1,                       (CFN1)
```

and let `P_i` be the squarefree locator of the supported slopes on row
`x_i`. Then

```text
Qbar(U,V;x_i)=P_i K_i,       deg K_i=c_i<=2;
N_F(U,V;x_i)=P_i C_i,        deg C_i<=c_i+1<=3,        (CFN2)
```

where `C_1,C_2` are not both zero.

Let `D_reg` be the homogeneous determinant of the regular Kronecker block,
of degree `Delta`. If `I_0=1`, let `L_0` be the slope of the unique ordinary
heavy incidence. Then

```text
D_reg=P_1P_2 L_0^(2I_0) E_(1-I_0),
deg E_(1-I_0)=1-I_0.                                  (CFN3)
```

Thus the first packet has one unallocated determinant root; the second has
none.

Let `R_i` be the reduced incidence divisor on row `x_i`, let `R_0` be the
ordinary heavy-incidence divisor of degree `I_0`, and put

```text
Z_i=V_(x_i)-R_i,       deg Z_i=c_i.
```

There is an effective divisor `E_1` of degree one such that

```text
div(s_F)=R_1+R_2+R_0+E_1.                             (CFN4)
```

Consequently both packets satisfy the signed degree-one Picard relation

```text
O_C(rho+3,-e-1)=O_C(Z_1+Z_2-R_0-E_1),
deg(Z_1+Z_2-R_0-E_1)=1.                               (CFN5)
```

All residual data has degree at most three.

## Scope

The theorem does not assert that the degree-one line bundle in `(CFN5)` is
effective, and it does not exclude either packet.
