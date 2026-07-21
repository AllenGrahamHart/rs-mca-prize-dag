# Audit

1. The coordinates `beta_e` are affine column coordinates relative to fixed
   scaled anchors, not merely projective points. This is why `(QC5)` is
   meaningful.
2. Both factors in every `p_ij` are nonzero: slopes and projective row
   classes are pairwise distinct.
3. Smoothness is inherited from the determinant quadric by the invertible
   anchor map; it is not inferred only from nonzero pair coefficients.
4. Support one is excluded by distinct projections. Support two is excluded
   by the proved minimum circuit arity.
5. The centroid is exactly `(-1,-1,-1,-1)`, with the sign fixed by
   `v_e=M_B beta_e` and `sum_i v_i=0`.
6. The converse retains the finite-slope and distinct-projection conditions;
   an arbitrary projective point on the full quadric is not silently treated
   as a selected block.
7. The atlas is coefficient-complete but supplies no support embedding count
   or cross-core owner.
8. No Modal or candidate-row computation is used.
