# dependency sub-DAG: single_obstruction_valueset

Promoted subclaims.

```text
sov_forced_root_recursion_algebra [PROVED]
    -> sov_forced_root_correctness

sov_active_core_obstruction_vanishing
    -> sov_forced_root_correctness

sov_forced_root_correctness [CONDITIONAL]
    -> sov_obstruction_equidistribution
    -> sov_fiber_budget_translation
    -> single_obstruction_valueset
    -> midlarge_h20_A

sov_first_obstruction_sensitivity [PROVED]
    -> sov_obstruction_equidistribution

sov_first_obstruction_value_distribution
    -> sov_obstruction_equidistribution
```

## sov_forced_root_correctness

Statement: the generalized forced square-root recursion correctly produces the
obstruction vector for every h in the intended band, and an active h-trade
forces all obstruction coordinates to vanish.

Status: gate-scripted, not replayed here except syntax.

## sov_obstruction_equidistribution

Statement: the first obstruction `O_{h-1}` has sufficiently small fibers on
anchored cores at official-shape rows.

Status: CONDITIONAL. Sensitivity is proved; the active leaf is
`sov_first_obstruction_value_distribution`, likely a character-sum or
norm-structure cancellation estimate.

## sov_fiber_budget_translation

Statement: the `O_{h-1}` zero fiber bound is numerically below the active-core
budget for every h in `(20,A]`.

Status: conditionally handled by `midlarge_h20_A`; it should be made explicit
once `SOV-EQDIST` has constants.
