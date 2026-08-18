# Audit

1. The high-margin cap is maximized over every affine subrank `0..4` and
   both endpoints of the full shortened-dimension interval.
2. The low pair count uses agreement `m-11`, not the exact-support value
   `m`.
3. The determinant argument is applied to correction matrices after the
   fixed affine anchor is removed.
4. A nonzero quadratic is charged at two slopes even in characteristic two;
   the official characteristic is in any event odd.
5. One-dimensional rank-one pair pencils are assigned canonically to the
   left orientation, preventing double ownership by the two rulings through
   their point.
6. The per-ruling cap is recomputed at correction dimension two; the older
   exact-support cap `R_2` is not silently substituted.
7. Zero correction is removed before identifying the selected ruling with
   an original projective factor.
8. Right-ruling synchronization is only within each `Pq`; different values
   of `[q]` are not merged.
9. No coefficient-field descent or upstream fixed-cell hypothesis is
   inferred from the ruling classification.
