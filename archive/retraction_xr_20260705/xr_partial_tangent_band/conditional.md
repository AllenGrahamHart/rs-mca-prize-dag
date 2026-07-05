# xr_partial_tangent_band conditional proof

## Predicate nodes

- `a1_lower_overlap_occupied_subcore_accounting`
- `a2_depth_cell_active_shadow_bound`

## Evidence node not used as a predicate

- `a2_depth_cell_residual_occupancy` is refuted; it is the raw formal-lattice
  count that the active-shadow statement replaces.

## Claim

The partial tangent band is bounded once the active occupied-subcore accounting
and active depth-cell shadow bound hold.

## Proof

For two aligned supports at distinct slopes with core `r = k + d`,
`1 <= d <= t - 2`, subtracting the alignment identities gives
`(z_1 - z_2)v = c_1 - c_2` on the core. Hence `v` agrees with a codeword on
`k + d` points and the pair lies in a tangent-depth-`d` cell. This is the
proved forcing map recorded in the node ledger.

The graded ledger charges a band pair by its depth cell. The complementarity
identity `d + s = t` says that the tangent depth and the qx13 fresh-codimension
defect exactly partition the available cost, so every pair in the band is
either charged in its depth cell or upgraded toward the cascade boundary.

It remains only to sum the charged cells without using the refuted raw
cell-lattice count. The predicate
`a2_depth_cell_active_shadow_bound` supplies the replacement: only active
post-strip cells are counted, and their shadow is budget-bounded. The predicate
`a1_lower_overlap_occupied_subcore_accounting` supplies the corresponding
lower-overlap occupancy budget, so summing the per-cell ledger over occupied
subcores stays inside the polynomial budget.

Therefore the 2b band bound follows conditionally from the two active
occupancy predicates. The refuted formal residual occupancy is not part of the
claim; it is precisely why the active-shadow formulation is required.
