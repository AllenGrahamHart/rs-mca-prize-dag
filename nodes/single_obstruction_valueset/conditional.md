# conditional: single_obstruction_valueset

## Predicate nodes

- `sov_forced_root_correctness`
- `sov_obstruction_equidistribution`
- `sov_fiber_budget_translation`

## Claim

Conditional on the three predicates, the first obstruction `O_{h-1}` has
small enough fibers on anchored cores to supply the active-core bound needed
by `midlarge_h20_A`.

## Proof

The predicate `sov_forced_root_correctness` identifies the generalized
forced-root obstruction vector and proves that an active `h`-core forces the
relevant obstruction coordinates to vanish.

The predicate `sov_obstruction_equidistribution` proves the main value-set
statement: the map `O_{h-1}` has sufficiently small fibers on anchored cores
at official-shape rows.

The predicate `sov_fiber_budget_translation` checks that the resulting fiber
bound is below the per-`h` active-core budget used by the mid/large-h
certification.

Therefore every active core lies in a fiber of `O_{h-1}` whose size is within
budget, proving the statement of `single_obstruction_valueset`.
