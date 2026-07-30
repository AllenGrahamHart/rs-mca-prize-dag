# KoalaBear m2 u2 colored source-resultant split compiler

- **status:** PROVED
- **scope:** every actual residual `Q=6,s=6,u=2` source component
- **dependencies:**
  `rate_half_kb_m2_r4_source_row_interpolation_compiler` and
  `rate_half_kb_m2_u2_universal_component_color_profile_cut`
- **consumer:** `rate_half_band_closure`

Let

```text
P_I(T)=product_(i in I)(T-alpha_i),
P_J(T)=product_(j in J)(T-alpha_j),
D_K(X)=psi^* product_(k in K)(T-alpha_k),
D_R(X)=B(X)/D_K(X).
```

Thus `deg D_K=10` and `deg D_R=14`. For an actual source equation
`H(T,X)`, let `C_H(X)` be the product of the four simple pole roots whose
pole-graph edges are colored by `H`. Then `C_H` is a squarefree binary
quartic dividing the degree-twelve pullback over `L^c`, and

```text
Res_T(P_J,H) ~ D_K^2 C_H,                           (KBCR-1)
C_H Res_T(P_I,H) ~ D_R^2.                          (KBCR-2)
```

Here `~` means equality up to a nonzero scalar. If `E_j=bZ_j` is the
two-point pole divisor attached to `j in J`, then

```text
c_j=4-d_j=deg gcd(C_H,E_j).                        (KBCR-3)
```

Hence the three surviving `K`-fiber profiles are recovered directly from
one quartic divisor. Equations `(KBCR-1)--(KBCR-2)` are equivalent to the
`I/J` split of the complete-source square product; they do not assert that
an admissible `C_H` or source component exists.

No component, stabilizer type, owner, payment, row, or Prize result is
closed.

## Falsifier

An actual residual degree-two component whose colored pole divisor is not
a squarefree quartic in the `L^c` pullback, whose two partial row resultants
violate `(KBCR-1)--(KBCR-2)`, or whose left colored degrees violate
`(KBCR-3)`.
