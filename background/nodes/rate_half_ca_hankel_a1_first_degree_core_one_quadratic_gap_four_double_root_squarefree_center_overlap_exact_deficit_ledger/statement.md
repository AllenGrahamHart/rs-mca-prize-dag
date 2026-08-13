# `A=1` quadratic squarefree center-overlap exact-deficit ledger

- **status:** PROVED
- **closure:** exact identification of the heavy-row overlap degree with the center deficit
- **consumer:** `rate_half_band_crossing_location`

Retain the squarefree unified heavy-row setup. For the three assigned
centers `A={alpha,beta,theta}`, put

```text
d_A=sum_(gamma in A) r_gamma in {0,1},
J=gcd(Lambda,g_*S_B^2),       j=deg J.              (HED1)
```

Then, up to one nonzero scalar,

```text
J=gcd(Lambda,g_*),       j=d_A.                    (HED2)
```

Consequently the complete squarefree passing remainder has exactly one of
the following two profiles:

```text
d_A=0:
  J=1,
  R_lambda=G(t,x_*)=c g_*S_B^2,       c!=0;

d_A=1:
  J=ell_(gamma_0),
  R_lambda=G(t,x_*)=(g_*S_B^2/ell_(gamma_0))T_1,
  T_1!=0,       deg T_1<=1,       gcd(T_1,S_B)=1,   (HED3)
```

where `gamma_0` is the unique center with `r_(gamma_0)=1`. Thus the
constant and affine alternatives are controlled by the existing endpoint
deficit bit; there is no independent overlap parameter.

## Scope

The theorem does not exclude either profile. In the `d_A=1` case it does
not assert that `T_1` has degree exactly one or that it is nonzero at the
center unless that center is also a correction root.
