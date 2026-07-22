# `A=1` distance-three quartic support antiweight absorption

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_internal_slice_lambda_cube_kernel`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_degree_two_three_subgroup_reduction`

Retain an exact official design for which every support pair-crossing matrix
is deficient. Then the global smooth antiweight alternative is not a
separate survivor once the actual internal-slice quartics are restored.
Every such design satisfies at least one of:

1. one fixed antipodal or constant-product involution contains at least
   `e-40` exceptional pairs; or
2. one separable degree-four base-field rational map contains at least
   `e-148` exceptional pairs.

More precisely, on the global antiweight branch let `P_l` be the actual
quartic supplied by the internal-slice identity and put

```text
r_l=P_l/D_l^2.                                      (QAW1)
```

At most two indices have `P_l` proportional to `D_l^2`. The remaining
nonconstant `r_l` generate a proper common subfield `F_p(psi)` of
`F_p(X)`, with `deg psi` equal to two, three, or four. Degree three is
impossible; degree two captures at least `e-6` pairs and is dihedral;
degree four captures at least `e-1` pairs.

Thus the exact support frontier has only the bounded-tail dihedral and
degree-four branches. This theorem does not exclude either one.
