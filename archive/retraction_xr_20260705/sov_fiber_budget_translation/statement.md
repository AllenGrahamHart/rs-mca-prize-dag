# sov_fiber_budget_translation

- **status:** CONDITIONAL
- **closure:** proof

## Statement

The quantitative fiber bound supplied by `sov_obstruction_equidistribution`
is below the per-`h` active-core budget for every `h in (20,A]` at the
official-shape rows.

## Falsifier

A row or `h` value where the proved fiber bound is still too large for the
active-core budget used by `midlarge_h20_A`.

## Conditional decomposition

This node is conditional on `sov_obstruction_equidistribution`, whose statement
already includes the budget-small fiber bound.
