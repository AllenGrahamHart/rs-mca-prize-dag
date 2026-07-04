# a2_depth_cell_active_shadow_bound

- **status:** TARGET
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/occ2_depth_cell_residual_occupancy.md']

## Statement

The graded ledger's quantitative bound must count ACTIVE depth cells (those actually occupied by post-strip pairs — the shadow), not the formal cell lattice, which is already super-linear at every clean row (OCC-2's verified negative). Statement: the active shadow is budget-bounded; E33/P-A-style occupancy data says active objects are rare throughout this program.

## Attack surface

the same rarity-counting shape as A-i: activity requires an alignment event, which is suppressed; count expected active cells directly

## Falsifier

a toy row with super-budget ACTIVE depth cells (extend the OCC-2 audit with the activity filter)

## Ledger (migrated notes)

ACT-SHADOW (#36): active depth cells max 10, max depth mass 60 <= n^2 = 256 at toys — no falsifier; the active-shadow statements are empirically solid and are instances of the same rarity count as the final estimate.
