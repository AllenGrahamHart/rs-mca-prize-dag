# `A=1` core-free cubic gap-one regular-factor pin

- **status:** PROVED
- **closure:** three exact regular determinants and one linear residual
- **consumer:** `rate_half_band_crossing_location`

Retain one of the four core-free cubic double-plus-simple packets in
`(DGN2)`. For every supported parameter slope `gamma`, write

```text
Qbar_gamma=Q_min,gamma R_gamma,
c_gamma=deg R_gamma,
C_tot=sum_gamma c_gamma.                             (CRF1)
```

Let `L_gamma` be a homogeneous linear form cutting out `gamma`, with
repetitions recorded through the exponents, and put

```text
P_C=product_gamma L_gamma^c_gamma.                   (CRF2)
```

Let `D_0` be the degree-`Delta=2e-1` regular Kronecker determinant from
`(MHD2)`. If `w=Delta-C_tot`, then there are a nonzero scalar `a` and a
nonzero homogeneous binary form `E_w` of degree `w` such that

```text
D_0=a P_C E_w.                                      (CRF3)
```

In the order of the four rows of `(DGN2)`, this specializes to

```text
packet                    w       regular determinant
no ordinary, no extra     1       D_0=a P_C E_1
no ordinary, extra simple 0       D_0=a P_C
no ordinary, extra double 0       D_0=a P_C
one ordinary incidence    0       D_0=a P_C.         (CRF4)
```

Thus the last three packets have no regular rank-drop slope or
multiplicity beyond the supported excess-recurrence divisor. For every
domain mark `x`, the bordered Hankel determinant is exactly

```text
det M_0[x]=a P_C E_w Q(U,V;x).                       (CRF5)
```

Here `E_0=1` by convention.

## Scope

The linear form `E_1` is not located. It may vanish at an already supported
slope, so no coprimality or new-slope assertion is made. The theorem does
not identify `E_1` with a contact correction, prove squarefreeness of
`D_0`, or exclude any packet.
