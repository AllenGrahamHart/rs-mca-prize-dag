# L1 Mersenne HNF m=8 order-one cubic three-two-one generic double-linear-d router

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_linear_d_router`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the generic `Delta!=0` arm of the official `h=7` cubic color
  profile `3+2+1`

Retain (GLD1)--(GLD10), and write `C` for the `h=7` conic. Define

```text
kappa=12q+366-176x,

B_1=-q(120D+1062+86q)-528R_0,
B_0=360DQ_0-360-1098q-191q^2+10q^3,

M_1=3B_1+q kappa(4x-21),
M_0=3B_0+12 kappa R_0.                              (GDL1)
```

The sixth coefficient, conic, and `P_4` obey the exact polynomial identity

```text
2(M_1d+M_0)
 =2160E_6+3qC+2(kappa-132d)P_4.                    (GDL2)
```

Consequently the complete generic coefficient and conic core is exactly

```text
P_4=0,
C_1d+C_0=0,
M_1d+M_0=0,
C=0,
Phi(R_D,S_D)=0,                                    (GDL3)
```

together with `Delta*W!=0` and every inherited saturation. All four
coefficients `C_1,C_0,M_1,M_0` lie in the parameter ring `(x,Y,q)`.

Put

```text
Omega=C_1M_0-M_1C_0.                               (GDL4)
```

Then (GDL3) has the following exact disjoint split.

1. If `C_1!=0`, reconstruct `d=-C_0/C_1` and retain
   `Omega=0`, together with the denominator-cleared `P_4,C,Phi` in
   `(x,Y,q)`.
2. If `C_1=0` and `M_1!=0`, retain `C_0=0`, reconstruct
   `d=-M_0/M_1`, and retain the denominator-cleared `P_4,C,Phi` in
   `(x,Y,q)`.
3. If `C_1=M_1=0`, retain

```text
C_1=M_1=C_0=M_0=P_4=C=Phi=0                       (GDL5)
```

   in `(x,Y,q,d)`.

On the two rational charts, also saturate the cleared numerators of
`d,q-d,Delta,W` and every inherited nonzero factor. The only generic chart
which still retains `d` is therefore the doubly singular coefficient locus
`C_1=M_1=0`. No unit, emptiness, norm, Frobenius-converse, cyclotomic,
exact-fiber, or inner-lift verdict is claimed.
