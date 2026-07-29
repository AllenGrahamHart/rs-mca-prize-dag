# L1 Mersenne HNF m=8 order-one cubic three-two-one generic fully-proportional exceptional-E quadratic router

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_coefficient_bivariate_compiler`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the `E_G=0` coefficient chart of the fully proportional official
  `h=7` cubic `3+2+1` residue

Retain (FBC1)--(FBC6) and (FQR1). The exceptional coefficient is the
quadratic

```text
E_G=e_2q^2+e_1q+e_0,

e_2=-720b,
e_1=240b^2-1902b-630,
e_0=-40b(b^2-6b+27).                               (FEQ1)
```

Define

```text
S_1=a_2e_1-e_2a_1,
S_0=a_2e_0-e_2a_0.                                 (FEQ2)
```

Then

```text
a_2E_G-e_2F_b=S_1q+S_0.                           (FEQ3)
```

On `a_2!=0`, the exceptional coefficient endpoint has the following exact
split.

1. If `S_1!=0`, reconstruct

```text
q=-S_0/S_1,
V(b):=a_2S_0^2-a_1S_0S_1+a_0S_1^2=0.             (FEQ4)
```

   Since `deg_q X_*<=3`, put

```text
X_E(b):=S_1^3 X_*(b,-S_0/S_1).                    (FEQ5)
```

   This is a polynomial, and the complete exceptional coefficient equations
   `F_b=E_G=X_*=0` are exactly

```text
V(b)=X_E(b)=0,       q=-S_0/S_1.                  (FEQ6)
```

   The existing `J_*` split then either reconstructs `G_2` or retains its
   cleared `J_*=L_*=0` specialization.

2. If `S_1=0`, retain

```text
S_0=0,       F_b=0,       X_*=0.                  (FEQ7)
```

   These equations recover `E_G=0` by (FEQ3); no component is discarded.

If `a_2=0`, retain the fixed chart

```text
b^2=1575/247,       q=-10(b^2+27)/231,
E_G=X_*=0.                                             (FEQ8)
```

The degree ledger is

```text
deg_b(S_1)<=5,       deg_b(S_0)<=7,
deg_b(V)<=16,        deg_b(X_E)<=23.                (FEQ9)
```

Every chart retains the reconstructed structural variables, selected role
packet, `P_4`, all saturations, and arithmetic-lift filters. This is an exact
exceptional router, not a nonzero-resultant, unit, emptiness, norm,
Frobenius-converse, cyclotomic, exact-fiber, or inner-lift verdict.
