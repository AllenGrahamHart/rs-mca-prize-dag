# xr_heavy_triangle_charge

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/e27_exceptional_pair_census.md']

## Statement

Configurations with sum of pairwise overlaps minus triple intersection > 2k: syzygies exist for dimension reasons (kernel of the sum map is forced positive: 3t > |union| - k). These are overlap-heavy — at least two near-k/2+ overlaps, one step below rung 2b's partial-forcing threshold. TASK: extend the graded tangent ledger (2b) across the boundary so heavy-triangle stagnations are charged by the same depth grading; the popular-core case with petal-petal contact reduces here too (non-sunflower popular cores stagnate only through petal contact — sunflowers are excluded by beta-1).

## Attack surface

shared ledger design with xr_partial_tangent_band; the dimension count above pins exactly which configurations need the charge

## Falsifier

a heavy triangle whose stagnation resists the graded charge at toys

## Ledger (migrated notes)

DECOMPOSED: beta-2a the pencil-degenerate case (derived codewords w_ij coincide) gives v agreement >= k+1 with one codeword — rung 2b VERBATIM, proved reduction (the w's are always affinely dependent; degeneracy = pencil collapse); beta-2b the generic case reduces to deep_link_staircase (every heavy triple contains a near-k partner pair).
