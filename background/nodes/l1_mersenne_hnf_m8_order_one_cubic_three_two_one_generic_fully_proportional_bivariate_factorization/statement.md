# L1 Mersenne HNF m=8 order-one cubic three-two-one generic fully-proportional bivariate factorization

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_parameter_reduction`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the `F_N=0` endpoint of the generic fully proportional official
  `h=7` cubic `3+2+1` role packets

Retain (FPR1)--(FPR5), and put

```text
z=b^2.                                               (FBF1)
```

The conic endpoint factors exactly as

```text
F_N=24F_b(z,q),                                      (FBF2)

F_b(z,q)=63(1575-247z)q^2
          +9240z(9-z)q
          +400z(9-z)(z+27).                         (FBF3)
```

The inherited `b*q!=0` saturation and (FBF3) imply

```text
z!=0,9.                                             (FBF4)
```

There are two exact coefficient charts.

1. If `1575-247z!=0`, retain the quadratic (FBF3). Its discriminant is

```text
Disc_q(F_b)=302400z(9-z)
              (-200z^2+4239z-14175).               (FBF5)
```

2. If `1575-247z=0`, the linear coefficient is nonzero and (FBF3)
   reconstructs

```text
z=1575/247,
q=-10(z+27)/231.                                    (FBF6)
```

Every fixed denominator and coefficient in these formulas is a unit on the
four official characteristics. The complete proportional endpoint still
retains the four coefficient-zero equations, the `R_0,S_0`
reconstructions, the selected role-discriminant weld, `P_4=0`, and all
generic and arithmetic saturations.

This is an exact bivariate factorization, not a square-condition verdict:
the discriminant in (FBF5) lives in the ambient quadratic field. No unit,
emptiness, norm, Frobenius-converse, cyclotomic, exact-fiber, or inner-lift
verdict is claimed.
