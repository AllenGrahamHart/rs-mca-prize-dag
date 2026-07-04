# strat_tree conditional proof

## Predicate node

- `stratification_partition_thm`

## Supporting proved nodes

- `m1_two_root_closure`
- `m1_rank_defect_nf`
- `common_code_line_budget`
- `thm_exactslack`
- `prop_collapse`

## Claim

The T0-T7 first-match stratification is a valid dedup convention once the
partition theorem holds.

## Proof

The supporting proved nodes supply the local normal forms used by the cases:
two-root packet closure, rank-defect normal form, common-code-line residual
budget, exact-slack image identity, and subgroup-symmetric collapse. These
identify the clauses that the T0-T7 tree tests.

The predicate `stratification_partition_thm` states that those clauses are
total and pairwise disjoint after first-match ordering. Therefore every pair
enters exactly one T0-T7 cell, and counting or charging by first match neither
misses nor double-counts any object.

Thus the stratification tree is a valid conditional dedup convention.

