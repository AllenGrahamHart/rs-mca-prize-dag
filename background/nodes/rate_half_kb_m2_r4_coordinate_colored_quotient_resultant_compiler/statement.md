# KoalaBear m2 r4 coordinate colored-quotient resultant compiler

- **status:** PROVED
- **scope:** every actual coordinate-order-two component
  `S=<tau x 1>` in the residual `(m,r,delta)=(2,4,2)` row
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_coefficient_normal_form` and
  `rate_half_kb_m2_u2_colored_source_resultant_split_compiler`
- **consumer:** `rate_half_band_closure`

Use the geometric coordinates

```text
tau(T)=-T,       b(X)=-X,       W=X^2.
```

The colored quartic is deck invariant and therefore

```text
C_H(X) ~ c(W),                                      (KBCQ-1)
```

where `c` is a squarefree quadratic divisor of the six-label quotient form
over `L^c`. Equivalently, the component's four colored edges are the two
complete edge pairs at two right pole-graph vertices.

Since `I,J` are `tau`-invariant, write

```text
P_S(T)=p_S(T^2),       deg p_S=3,       S in {I,J}.
```

For the positive and negative coordinate source forms define

```text
Phi_+(Y,W)=(A_2(W)Y+A_0(W))^2-WY B_1(W)^2,
Phi_-(Y,W)=W(B_2(W)Y+B_0(W))^2-Y A_1(W)^2.          (KBCQ-2)
```

Then

```text
R_S^epsilon(W):=Res_Y(p_S(Y),Phi_epsilon(Y,W))
               ~ Res_T(P_S(T),H(T,X)).             (KBCQ-3)
```

Let `K_5(W)` be the quotient form on `K` and `R_7(W)` the quotient form on
its seven-label complement. The universal colored-resultant split becomes
the explicit univariate system

```text
R_J^epsilon(W) ~ K_5(W)^2 c(W),
c(W) R_I^epsilon(W) ~ R_7(W)^2.                    (KBCQ-4)
```

If `xi` is the unique label in `I minus K`, then projectively
`K_5=P_I/(W-xi)` and `R_7=(W-xi)P_J` in an affine chart. The positive
system has the existing eight source coefficients and the negative system
has seven, plus the two-root choice encoded by `c`.

This compiler does not prove either system inconsistent. It deletes no
orientation, stabilizer type, owner, payment, row, or Prize result.

## Falsifier

An actual coordinate component with a colored divisor not descending as in
`(KBCQ-1)`, failure of either paired-root formula in `(KBCQ-2)--(KBCQ-3)`,
or violation of the specialized split `(KBCQ-4)`.
