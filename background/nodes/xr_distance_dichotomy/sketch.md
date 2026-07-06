# Sketch: XR distance dichotomy

Status: PROVABLE.

## Predicate nodes

- `xr_ledger_qpower`
- `xr_radius_arithmetic`
- `xr_anticode_toolkit`
- `xr_globalness_from_ledger`
- `exchange_ledger_gen_t`

## Proof route

Fix a post-strip pair and classify every residual aligned support by its
exchange-distance behavior relative to the current family.

Close pairs are those inside the ledger reach.  The generalized exchange
ledger and the q-power ledger give one fresh q-factor per step through the
usable range, so this region is suppressed by the close-pair accounting.

Far-only sets have no close-pair witnesses at the relevant scale.  The
`xr_anticode_toolkit` supplies the Johnson/Delsarte anticode bound for such
distance-separated locator families, giving the required combinatorial loss.

The remaining case is link-dense: many supports share the top-core/link
structure that defeats the far-only anticode split.  This is exactly the
structured branch, and `xr_globalness_from_ledger` identifies that mass with
the paid tangent/globalness ledger.  This predicate is therefore a required
input, not merely evidence.

`xr_radius_arithmetic` proves that these regimes cover the corridor scales with
the necessary overlap.  Hence the per-scale split is exhaustive and the XR
distance assembly follows from the listed green inputs.
