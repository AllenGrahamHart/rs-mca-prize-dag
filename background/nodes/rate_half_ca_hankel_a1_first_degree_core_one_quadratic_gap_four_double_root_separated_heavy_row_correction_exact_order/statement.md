# `A=1` quadratic separated heavy-row correction exact order

- **status:** PROVED
- **closure:** exact correction-root valuations and coprimality of the overlap polynomial
- **consumer:** `rate_half_band_crossing_location`

Retain the separated double-root extremal profile and write

```text
J=gcd(Lambda,g_*S_B^2),       j=deg J<=3,
H=g_*S_B^2/J,
G(t,x_*)=H(t)T_j(t),          deg T_j<=j.           (HCE1)
```

For a projective root `tau` of the squarefree quadratic `S_B`, put

```text
c_tau=ord_tau Lambda in {0,1}.                      (HCE2)
```

Then the fixed heavy row has exact order

```text
ord_tau G(t,x_*)=2-c_tau=ord_tau H.                 (HCE3)
```

Consequently

```text
T_j(tau)!=0,
gcd(T_j,S_B)=1.                                     (HCE4)
```

For every connected-weld candidate which passes the coefficient and
barycentric remainder gates, the same exact orders hold for `R_lambda`.

## Scope

The theorem controls only correction roots. It does not constrain the free
roots of `T_j` away from `S_B`, prove that a connected-weld candidate passes,
or exclude a nonzero passing remainder. Nonreduced correction and roots
shared by `S_B` and `g_*` remain outside the separated hypotheses.
