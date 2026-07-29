# L1 Mersenne HNF m=8 order-one cubic three-two-one J-zero guard compiler

- **status:** PROVED
- **dependencies:**
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_j0_role_p4_compiler`,
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_common_quadratic_compiler`,
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_scaled_quadratic_core_compiler`,
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_coefficient_matrix_router`, and
  `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_j0_outer_lift_compiler`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** one retained eight-filter common root, one reconstructed `eta`
  branch, and one matched normalized color pair in the exceptional `J_*=0`
  cubic `3+2+1` chart

Retain all notation and denominator guards from the dependencies. In
particular,

```text
x=(b+15)/4,            A=6-2x=-(b+3)/2,
q=5bM/T,
d=3(eta R_j-S_j)/q,
S_c=S_j+qd/3=eta R_j,
lambda=1+eta^(-1).                                  (JGC1)
```

For a matched pair `(beta,gamma)` from the outer-lift compiler,

```text
eta=(beta-1)/(gamma-beta),
lambda=(gamma-1)/(beta-1).                          (JGC2)
```

Thus `eta*(eta+1)*lambda*(lambda-1)!=0`. Work in the scaled coordinate
`X=dW` and define

```text
Qhat(X)=X^2+(x+Y_j)X+V_j,
Ghat(X)=Qhat(X)(X-Y_j),
Fhat(X)=Ghat(X)+A Qhat(X)+S_c,
Lhat(X)=Fhat(X)Ghat(X).                             (JGC3)
```

These are exactly the scaled common-quadratic factors:

```text
Qhat(X)=d^2 Q(X/d),
Ghat(X)=d^3 G(X/d),
Fhat(X)=d^3 F(X/d),
Lhat(X)=d^6 L(X/d).                                (JGC4)
```

Moreover

```text
R_j=A Qhat(Y_j),
a=A/d,                 B=S_c/d^3,
Q(y)=Qhat(Y_j)/d^2,    lambda-1=eta^(-1),

a B (lambda-1) Q(y)=R_j^2/d^6.                    (JGC5)
```

Consequently the common-quadratic nonzero guard in (TQC2), (TQC7) is
automatic once `d*R_j!=0` and a normalized pair has been matched.

Put

```text
D_Q=disc_X(Qhat),       D_F=disc_X(Fhat).           (JGC6)
```

The exact identities

```text
disc(Ghat)=D_Q Qhat(Y_j)^2,
Res_X(Ghat,Fhat)=lambda S_c^3,

disc(Lhat)=D_F D_Q Qhat(Y_j)^2 lambda^2 S_c^6      (JGC7)
```

show that every squarefreeness and exact-fiber subresultant guard is
equivalent, on the already matched role branch, to

```text
D_Q*D_F!=0.                                         (JGC8)
```

Indeed the normalized color polynomial

```text
E=1+(beta-1)Fhat/S_c                               (JGC9)
```

then has exact gcd degrees

```text
deg gcd(Lhat,E-1)=3,
deg gcd(Lhat,E-beta)=2,
deg gcd(Lhat,E-gamma)=1.                           (JGC10)
```

The remaining split-root guard and scaled constant guard are simply

```text
Lhat(-1)!=0,                 K_6=Lhat(0)!=0.        (JGC11)
```

Therefore all named denominator, generic-chart, HNF, role, exact-fiber, and
split-root guards on this retained branch are decided by the finite ledger

```text
G_alg=
 b(b+3)D_*T q d(d+1)(q-d) Delta W K_6 R_j
 eta(eta+1),

G_fib=D_Q D_F,
G_split=Lhat(-1),

G_alg*G_fib*G_split!=0.                             (JGC12)
```

The official role constants `c_0` and `delta_Phi` are already proved units.
Every rational entry in (JGC12) is evaluated after reconstruction in the
proved field `K=F_(p^8)`; clearing its denominator is lossless because its
factors occur in `G_alg`. A failed entry rejects that candidate with a named
reason. A candidate passing (JGC12) still owes the norm and degree-six outer
congruence from the outer-lift compiler and the separate global inner lift.
No guard outcome, survivor, emptiness result, or critical close is asserted.
