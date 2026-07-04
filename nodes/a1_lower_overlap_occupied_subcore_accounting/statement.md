# a1_lower_overlap_occupied_subcore_accounting

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/a1_staircase_cap_assembly.md']

## Statement

Count the subcores simultaneously occupied by aligned partners at lower overlaps — the accounting layer above the proved per-subcore cap. Consumers: the assembled staircase (A1) and the graded tangent ledger bound (A2) — one machinery, two clients. E33's occupancy data calibrates (observed: totals stayed linear).

## Attack surface

sum the proved per-subcore cap over an occupancy-bounded family; the occupancy bound is a packing count over the (k-1)-subcore lattice

## Falsifier

toy occupancy exceeding the budget (E33's scan + an occupancy histogram column)

## Ledger (migrated notes)

OCC-1 (#28, 19/19): CONDITIONAL/RESIDUE — the E33 occupancy column is benign but DIRECT formal-lattice packing is under-specified; the bound must be on ACTIVE occupied subcores (the shadow), not the formal lattice. Same pattern as OCC-2 and everything else in this program: raw/formal fails, active/post-strip holds.
