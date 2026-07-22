# `A=1` distance-three Pade residual discriminant exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pade_aligned_residual_degree_four`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pullback_involution_absorption`

No degree-`1..4` aligned residual pencil from the all-deficient support
branch exists.

Indeed, write

```text
R(U,Z)=R_2(Z)U^2+R_1(Z)U+R_0(Z),       1<=deg_Z R<=4. (QPRD1)
```

The calibrated internal evaluations force

```text
R(U,xi_i)=c_iN_i(U)                               (QPRD2)
```

for every good involution pair, where `c_i` is nonzero and
`N_i(U)=(U-u_i)^2`. Consequently

```text
R_1(Z)^2-4R_2(Z)R_0(Z)=0,                          (QPRD3)
4R_2R=(2R_2U+R_1)^2.                               (QPRD4)
```

Every aligned specialization `R(u,Z)` is required to be split, squarefree,
and nonconstant. Equation `(QPRD4)` then forces all its roots to be roots of
`R_2`, so `R(u,Z)` is proportional to `R_2(Z)` for every aligned `u`. This
contradicts the calibrated projective distinctness of the complements.

Therefore simultaneous deficiency of every quartic support pair-crossing
matrix is impossible in an exact official design. The degree-two,
degree-four, antiweight, Laurent, and bounded-tail alternatives are all
closed; `CR-003-BT8` is retired.
