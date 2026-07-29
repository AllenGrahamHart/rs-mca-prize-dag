# L1 Mersenne HNF m=8 order-one cubic three-two-one generic fully-proportional coefficient bivariate compiler

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_coefficient_router`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** denominator clearing for the coefficient router in the generic
  fully proportional official `h=7` cubic `3+2+1` residue

Retain (FCR1)--(FCR8). Define the bivariate polynomials

```text
L_*=135b(b^2+6b+105+8q)-6P,
F_*=D_*K_*-30bQ_*,
J_*=150bQ_*-3D_*^2-5PD_*,
X_*=Q_*-24D_*q^2,

Theta_*=5E_GD_*^2L_*-6J_*F_*.                     (FBC1)
```

They clear every denominator in (FCR4)--(FCR7):

```text
L_G=L_*,
F_G=F_*/(600b),
J_G=J_*/(5D_*),
Theta_G=Theta_*/(18000bD_*).                       (FBC2)
```

Hence the coefficient router has the following exact polynomial form.

1. On `E_G!=0`, retain

```text
F_b(b^2,q)=0,       Theta_*(b,q)=0,
G_2=-F_*/(600bE_G),
H=ell-G_2,          Y=(ell-2G_2)/A-x.              (FBC3)
```

2. On `E_G=0` and `J_*!=0`, retain

```text
F_b(b^2,q)=0,       E_G=0,       X_*=0,
G_2=-D_*^2L_*/(720bJ_*),
H=ell-G_2,          Y=(ell-2G_2)/A-x.              (FBC4)
```

3. The only coefficient chart retaining `G_2` is

```text
F_b(b^2,q)=E_G=X_*=J_*=L_*=0.                      (FBC5)
```

The degree ledger is

```text
deg(D_*,K_*,E_G,L_*)<=3,       deg(Q_*)<=5,
deg(F_*),deg(J_*)<=6,          deg(Theta_*)<=12,
deg_q(F_b)=2,                  deg_q(Theta_*)<=6.   (FBC6)
```

All formulas are over the official base field and use only inherited units.
After the reconstructions, substitute into every retained structural
identity, role-discriminant equation, `P_4`, and arithmetic-lift filter.
This is an exact polynomial compiler, not a unit, resultant, emptiness,
norm, Frobenius-converse, cyclotomic, exact-fiber, or inner-lift verdict.
