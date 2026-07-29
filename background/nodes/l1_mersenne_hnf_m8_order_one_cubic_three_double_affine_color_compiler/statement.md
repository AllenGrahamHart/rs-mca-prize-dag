# L1 Mersenne HNF m=8 order-one cubic three-double affine-color compiler

- **status:** PROVED
- **dependencies:** `l1_mersenne_hnf_m8_order_one_cubic_three_double_linear_remainder_reduction`, `l1_mersenne_hnf_m8_cubic_three_two_one_role_polynomial_compiler`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the h=7 cubic color profile `2+2+2`

Retain the role polynomial `Lambda_321(lambda)` from (RPC3), and put

```text
A(lambda)=lambda^2-lambda+1,
B(lambda)=(lambda+1)(2lambda-1)(lambda-2).           (TAC1)
```

For two indeterminates `P,Q`, define the homogeneous color resultant

```text
K_8(P,Q)=Res_lambda(
  Lambda_321(lambda),
  27 A(lambda)^3 Q^2+B(lambda)^2 P^3).              (TAC2)
```

Every three-distinct-color packet satisfies

```text
K_8(P,Q)=0.                                          (TAC3)
```

Over characteristic zero, the primitive squarefree part of (TAC2), viewed
as a binary form in `P^3,Q^2`, has degree seven. Its seven factors correspond
to the seven oriented cyclic gap types

```text
(1,1,6),
(1,2,5), (1,5,2),
(1,3,4), (1,4,3),
(2,2,4),
(2,3,3).                                            (TAC4)
```

More explicitly, for `T=-27Q^2/P^3`, the seven color values have polynomial

```text
Theta_8(T)=(T+50)(T^2-224T-578)(T^2-4T+54)
           (125T^2-2404T+13448),                    (TAC5)

Phi_8(P,Q)=P^21 Theta_8(-27Q^2/P^3).                (TAC6)
```

The expression in (TAC6) is homogeneous in `P^3,Q^2`, including on `P=0`,
and is proportional to the primitive squarefree radical of (TAC2).
Reduction to an official characteristic may merge factors; it cannot create
a new color type. The full resultant (TAC2) remains the
characteristic-independent equation.

To impose (TAC3) without restoring the individual double-fiber parameters,
use the notation of (TDF2)--(TDF3) and (TSC1)--(TSC2). Put

```text
f(T)=T^3-2UT^2+(U^2+V)T-UV,
R(T)=T^3-s_1T^2+s_2T-s_3,

Res_T(R(T),Z-f(T))=Z^3-E_1Z^2+E_2Z-E_3,             (TAC7)

P=E_2-E_1^2/3,
Q=E_3-E_1E_2/3+2E_1^3/27.                           (TAC8)
```

The three roots represented by (TAC7) are `f(u_1),f(u_2),f(u_3)`.
Equations (TSC2) make `P,Q` explicit rational polynomials in the existing
variables `(U,s_2,r,d)`, hence in `(x,b,q,d)` after (TLR1). Thus (TAC3),
equivalently (TAC6),
adds one exact symmetric color equation to (TLR3), (TLR5), (TLR7), and
(TLR8), with no assignment or color-role enumeration.

On the generic locus (off (TLR9)), eliminate `b` using (TLR5). The retained
core consists of the conic, the substituted `D_b`, the compatibility of
`M_5,M_6`, and the substituted affine-color equation: four equations in
`(x,q,d)`. No unit or emptiness verdict is asserted here.
