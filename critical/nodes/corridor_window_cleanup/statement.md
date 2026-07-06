# corridor_window_cleanup

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/proof_sketch/s2_paid_ledger.md']

## Statement

For each rate and each corridor grid point: the per-point boundary windows (the finite residual charts) tighten by exact per-point evaluation; deliverable = the cleaned per-point bounds as a table, with the grid-step fraction each rate recovers. Evidence-gated: a finite per-point computation (the window_m5_charts material, made propositional).

## Attack surface

finite enumeration per corridor point; the chart machinery exists

## Falsifier

a corridor point whose cleaned window widens rather than tightens

## Ledger (migrated notes)

COMPUTED (agent, verifier PASS; falsifier passed — no point widens): recovers 0.633 / 0.099 / 0.370 grid steps at rates 1/4 / 1/8 / 1/16. The eater-partition modeling choice ([tau*,cap] -> (ii)) is stated openly in the note; the boundary numbers are banked.
