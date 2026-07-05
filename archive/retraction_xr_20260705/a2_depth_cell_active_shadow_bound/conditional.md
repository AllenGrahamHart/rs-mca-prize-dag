# a2_depth_cell_active_shadow_bound conditional proof

## Predicate node

- `anchored_nontoral_pte_bound`

## Claim

The active depth-cell shadow in the graded tangent ledger is budget-bounded
once the anchored non-toral PTE bound holds.

## Proof

The raw depth-cell lattice is known to be too large; the statement only counts
active cells, namely cells actually occupied by post-strip aligned pairs. For
a fixed depth cell, the proved 2b forcing map puts the pair into a
tangent-depth normal form. After removing the paid tangent, quotient-with-tail,
and dihedral strata, any remaining active occupant determines a primitive
anchored non-toral same-top-`t` locator trade.

Fix the canonical first occupant of each active depth cell. The depth
parameter and bounded tail data are part of the cell label, so this canonical
choice maps active cells to the anchored non-toral PTE objects counted by
`anchored_nontoral_pte_bound`, with only the bounded multiplicity from the
graded depth/tail alphabet.

Thus `A_h^nt <= h n` bounds the active shadow by the same polynomial budget
after multiplying by the fixed depth/tail constant. This supplies the
occupancy column needed by the graded tangent ledger.
