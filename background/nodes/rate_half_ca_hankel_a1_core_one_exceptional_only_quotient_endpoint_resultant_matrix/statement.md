# `A=1` exceptional quotient endpoint resultant matrix

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_endpoint_resultant_profile`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_factor_descent`

Retain the sharp endpoint and write

```text
P_X=A H,       P=z P_ord,       QV+P_XW=P,
deg A=2e,       deg H=6e+6.                              (QRM1)
```

Put

```text
alpha=(e-1)/2,       beta=3(e+1)/2,
gamma=(3e+1)/2,      delta=9(e+1)/2.                    (QRM2)
```

All four exponents are integers. In the flat endpoint profile, up to four
nonzero field scalars, the resultant matrix is

```text
                         Q                         V
A       z^(2e) P_ord^alpha              P_ord^gamma
H              P_ord^beta       z^(6e+6) P_ord^delta. (QRM3)
```

In the swapped endpoint profile, put

```text
L(z)=(z-z_min)/(z-z_max).
```

Then the four entries in `(QRM3)` acquire respectively the factors

```text
                         Q          V
A                        L        L^(-1)
H                     L^(-1)        L.                 (QRM4)
```

Every displayed rational expression means its equivalent identity after
clearing the one printed linear factor already dividing `P_ord`. Thus
`(QRM3)--(QRM4)` are polynomial identities.

The matrix is compatible in both directions:

```text
Res(A,Q)Res(A,V)=P^(2e),
Res(H,Q)Res(H,V)=P^(6e+6),
Res(P_X,Q)=z^(2e)P_ord^r,
Res(P_X,V)=z^(6e+6)P_ord^(6e+5),                       (QRM5)
```

up to nonzero scalars. This is the complete sharp-endpoint resultant ledger;
it does not exclude either matrix profile.
