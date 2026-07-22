# Claim contract

- **claim:** every support-wise nontrivial selected LineRay is transverse on
  its own error support, even if another joint explanation support exists;
  the all-LineRay selector theorem therefore pays mismatch selector rank at
  most three everywhere and rank four at RowC rate `1/4`.
- **status:** PROVED
- **dependency:** `xr_all_lineray_affine_core_bound`
- **consumers:** `xr_tangent_support_mismatch_bridge`,
  `xr_highcore_collision_count`, `xr_lowcore_spread_heart`
- **quantifiers:** every linear code with distance greater than `n-A`, every
  received pair, and every support-wise nontrivial selected ray; official-row
  arithmetic only for the printed rank thresholds.
- **excludes:** no claim for selector rank at least four on the five unpaid
  rows or rank at least five at RowC rate `1/4`; no chart-union enumeration.
- **falsifier:** a selected ray whose own zero mask is support-wise
  nontrivial but whose two endpoint syndromes both have lifts supported on
  the complementary error support.
