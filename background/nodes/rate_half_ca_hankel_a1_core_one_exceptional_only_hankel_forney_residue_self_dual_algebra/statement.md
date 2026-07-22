# `A=1` exceptional Forney-residue self-dual algebra

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_exceptional_split_incidence_self_dual_frame`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_forney_numerator_normal_form`

Write `Phi` for the Forney numerator called `F` in `(QFN3)--(QFN5)`, and
work in the squarefree exceptional algebra

```text
R_A=F_field[X]/(A),       dim R_A=2e.                (HFR1)
```

The classes of `q_1`, `Phi`, and `B_T` are units. Define

```text
p_i=q_(i+1)q_1^(-1) in R_A,       0<=i<e,
U_q=span{p_0,...,p_(e-1)},        p_0=1,
C=q_1 Phi B_T^(-1) in R_A.                           (HFR2)
```

For a class `H`, put

```text
tau_A(H)=sum_(a in R_A-roots) H(a)/A'(a)
        =[X^(2e-1)] rem_A(H),                         (HFR3)
<H,K>_C=tau_A(CHK).                                   (HFR4)
```

Then `(HFR4)` is nondegenerate and

```text
dim U_q=e,       U_q=U_q^(perp C).                   (HFR5)
```

Equivalently, the normalized split-incidence columns have constant term one
and self-dual weights

```text
mu_a=C(a)/A'(a)
    =q_1(a)Phi(a)/(A'(a)B_T(a)).                     (HFR6)
```

Let `U_q^2` denote the span of all products of two elements of `U_q`. Then

```text
U_q^2 subset ker(tau_A(C dot)),       dim U_q^2<=2e-1. (HFR7)
```

If equality holds, the functional `tau_A(C dot)`, and therefore the class
`C`, is uniquely determined up to scalar by `U_q`. If
`dim U_q^2<=2e-2`, the frame lies in the separately detectable degenerate
product-space branch. This exact dichotomy incorporates the Forney weights;
it does not yet exclude either branch at the official value of `e`.
