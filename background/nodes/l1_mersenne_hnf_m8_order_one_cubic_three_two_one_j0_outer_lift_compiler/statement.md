# L1 Mersenne HNF m=8 order-one cubic three-two-one J-zero outer-lift compiler

- **status:** PROVED
- **dependencies:**
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_j0_role_p4_compiler`,
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_factor_reduction`,
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_official_frobenius_role_split`,
  `l1_mersenne_hnf_order_one_frobenius_gate`, and
  `l1_mersenne_hnf_m8_order_one_cubic_coefficient_field_degree_eight_router`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** a retained eight-filter common root in one official
  `h=7`, cubic `3+2+1`, exceptional-`J_*=0` role packet

Let `p` be one of the four official characteristics and put

```text
n=8(p+1),                 K=F_(p^8).                 (OLC1)
```

The coefficient-field router puts `b` in `K`. The role compiler puts
`eta` in `F_(p^2)`, hence in `K`, and reconstructs `q,d,x,Y,G_2,V,R,S`
in `K` after every inherited denominator guard is checked. Here

```text
S=S_j+qd/3,       eta=S/R,       lambda=1+eta^(-1). (OLC2)
```

For the retained role root, enumerate the normalized ordered color pairs

```text
T(eta)={(beta,gamma) in (mu_8\{1})^2:
        beta!=gamma,
        eta=(beta-1)/(gamma-beta)}.                 (OLC3)
```

The official Frobenius-role split proves that this set is nonempty for an
actual role root. It is obtained by checking at most `7*6=42` pairs in
`F_(p^2)`; if several pairs represent the same role value, retain all of
them.

Reconstruct the unscaled common-quadratic data in `K` by

```text
g_1=x/d,       y=Y/d,       g_2=G_2/d^2,
u=g_1+y,       v=V/d^2,     a=(6-2x)/d,
B=S/d^3,

Q(W)=W^2+uW+v,
G(W)=Q(W)(W-y),
F(W)=G(W)+aQ(W)+B,
L(W)=F(W)G(W).                                     (OLC4)
```

For `(beta,gamma) in T(eta)`, define the normalized cubic color polynomial

```text
E_(beta,gamma)(W)=1+(beta-1)F(W)/B.                 (OLC5)
```

The common-quadratic identities give

```text
E=1       on the three roots of F,
E=beta    on the two roots of Q,
E=gamma   at W=y.                                  (OLC6)
```

Consequently, after the inherited exact-fiber and nonzero guards are
checked,

```text
L(W) divides E_(beta,gamma)(W)^8-1.                (OLC7)
```

The complete outer arithmetic replay for this candidate is therefore:

```text
zeta=d^(p+1),                 zeta^8=1,

W^(p+1)=tau E_(beta,gamma)(W) mod L(W)
for some tau in mu_8 and some (beta,gamma) in T(eta). (OLC8)
```

If (OLC8) holds, then with

```text
P(W)=(W+1/d)L(W),
```

one has

```text
P(W) divides W^n-1.                                (OLC9)
```

Moreover `c=d+1` automatically satisfies

```text
c^p=1+zeta/d.                                      (OLC10)
```

Thus the norm, exact color-fiber, assignment-preserving pointwise
Frobenius, and full outer cyclotomic obligations reduce to inherited guard
checks, at most 42 normalized roles, eight global colors `tau`, one norm
test, and one degree-six modular-power congruence. No degree-`n` polynomial
is constructed.

This is an exact outer-lift compiler. It does not assert that any common
root or role branch passes its guards or (OLC8), and it does not construct
or discharge the separate global inner lift.
