# L1 Mersenne HNF m=8 order-one cubic three-two-one generic fully-proportional q-quotient router

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_coefficient_bivariate_compiler`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the generic `E_G!=0` coefficient chart of the fully
  proportional official `h=7` cubic `3+2+1` residue

Write the conic endpoint as

```text
F_b=a_2q^2+a_1q+a_0,

a_2=63(1575-247b^2),
a_1=9240b^2(9-b^2),
a_0=400b^2(9-b^2)(b^2+27).                         (FQR1)
```

Expand the coefficient compatibility polynomial only in `q`:

```text
Theta_*(b,q)=sum_(j=0)^6 theta_j(b)q^j.             (FQR2)
```

On `a_2!=0`, define denominator-cleared quotient remainders by

```text
u_1=1,       v_1=0,
u_2=-a_1,    v_2=-a_0,

u_j=-a_1u_(j-1)-a_2a_0u_(j-2),
v_j=-a_1v_(j-1)-a_2a_0v_(j-2),       3<=j<=6.      (FQR3)
```

Then

```text
a_2^(j-1)q^j = u_jq+v_j mod F_b.                   (FQR4)
```

Put

```text
rho_1=a_2^5theta_1
    +sum_(j=2)^6 a_2^(6-j)theta_j u_j,

rho_0=a_2^5theta_0
    +sum_(j=2)^6 a_2^(6-j)theta_j v_j.             (FQR5)
```

There is an exact polynomial congruence

```text
a_2^5Theta_*=rho_1q+rho_0 mod F_b.                 (FQR6)
```

Consequently the generic coefficient pair has the following exact disjoint
router.

1. If `a_2rho_1!=0`, reconstruct

```text
q=-rho_0/rho_1,
U(b):=a_2rho_0^2-a_1rho_0rho_1+a_0rho_1^2=0.       (FQR7)
```

2. If `a_2!=0` and `rho_1=0`, retain

```text
rho_0=0,       F_b=0.                              (FQR8)
```

3. If `a_2=0`, retain the already exact leading-coefficient chart

```text
b^2=1575/247,
q=-10(b^2+27)/231,
Theta_*(b,q)=0.                                    (FQR9)
```

The degree ledger is

```text
deg_b(rho_1)<=26,       deg_b(rho_0)<=28,
deg_b(U)<=58.                                       (FQR10)
```

On the first chart, substitute the reconstructed `(b,q)` into `D,Q_0,G_2,
H,Y`, every structural identity, the selected role-discriminant weld,
`P_4`, and all arithmetic-lift filters. The other charts retain the same
obligations. This is an exact quotient router, not a nonzero-resultant,
unit, emptiness, norm, Frobenius-converse, cyclotomic, exact-fiber, or
inner-lift verdict.
