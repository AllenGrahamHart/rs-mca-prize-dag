# conditional proof: r2_clean_rates

- **status:** CONDITIONAL
- **closure:** proof

## Predicate node

- `xr_clean_residual_any_gate`

## Evidence/support nodes

- `xr_globalness_from_ledger`
- `xr_small_set_engine`
- `xr_radius_arithmetic`

## Claim

Conditional on `xr_clean_residual_any_gate`, the clean-rate R2 obligation holds:
at each clean-rate decision candidate, every pair `(u,v)` has

```text
R_post(u, v; A) <= 16 n^3.
```

## Proof

The active form of this node is the compiled integer-budget target, not the
older KLLM/globalness route.  The proved budget audit converts the clean-rate
safe-side obligation to the exact per-pair residual inequality above, and that
conversion is already part of the `xr_clean_residual_any_gate` packet through
its `xr_target_budget_audit` input.

The predicate `xr_clean_residual_any_gate` states precisely the required
post-strip residual bound at the clean-rate candidates, with dihedral and
extension columns counted inside `R_post`.  Therefore granting that gate gives
the conclusion of `r2_clean_rates` directly.

The older `xr_globalness_from_ledger`, `xr_small_set_engine`, and
`xr_radius_arithmetic` inputs remain evidence for the route history and for
rate-half/globalness work, but they are not additional logical predicates of
this clean-rate assembly step.

## Ledger

WEAKENING 2026-07-06: the three older XR support inputs were demoted from
requirements to evidence.  The sole live clean-rate R2 premise is now
`xr_clean_residual_any_gate`.  The exact-exponent caveat remains: the gate's
open child must supply a budget-compatible `16 n^3` residual bound, not merely
an unspecified polynomial.
