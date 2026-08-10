# Clean-endpoint Picard--Forney contact exclusion

- **status:** PROVED
- **closure:** exact boundary contact and vanishing cohomology
- **consumer:** `rate_half_band_crossing_location`

Retain the integral clean-endpoint curve

```text
C:Q(z;X)=0,       (deg_X Q,deg_z Q)=(rho,m),
rho=4m-1,         N=16m,       T=4m+1,       m>3.     (PFC1)
```

Let `P(z;X)` be the canonical Forney numerator and homogenize it as a
section of `O_C(rho-1,m+1)`. If `H_X` is the divisor cut out by
`X=infinity`, then

```text
div_C(P)>=(2rho+2)H_X.                                (PFC2)
```

Consequently there is a nonzero section of

```text
L_F=O_C(-rho-3,m+1),       deg L_F=m-1.               (PFC3)
```

The clean Picard theorem also supplies a point `P_* in C` with

```text
O_C(P_*)=O_C(N,-T).                                   (PFC4)
```

The official arithmetic gives

```text
L_F^4 tensor O_C(P_*)
 =O_C(4(-rho-3)+N,4(m+1)-T)
 =O_C(-8,3).                                          (PFC5)
```

But

```text
H^0(C,O_C(-8,3))=0       for m>3.                    (PFC6)
```

Equations `(PFC3)--(PFC5)` would produce a nonzero section of the space in
`(PFC6)`, a contradiction. Therefore the strict `A=3`, `e=m`, `O=0`
endpoint branch does not exist. In particular, every surviving endpoint
failure has positive root-omission defect `O>=1`.

## Scope

This excludes the clean branch on the official row `m=2^37`. It does not
exclude the remaining `1<=O<=m-1` defect strata and does not by itself locate
the adjacent unsafe MCA numerator.
