# Claim contract

## Inputs

- The residual owner-plane geometry and exact extension charge proved by
  `rate_half_mca_rank11_rank9_residual_petal_capacity_cut`.
- The same weighted rank-nine selector demand used by that parent node.

## Output

Exact convex packing sharpens the marked component capacity and excludes
rank nine for `15529<=K'<=15634`. Combined with the existing higher-row
cuts, the surviving rank-nine interval is `10<=K'<=15528`.

## Scope pins

- All coordinates and support sizes are residual-row quantities.
- Zero-sized petals contribute zero before any division or packing step.
- The partition optimization is an upper-bound relaxation; it does not
  assert that the maximizing partition is geometrically realizable.
- No conclusion is drawn for rank eight or for the remaining rank-nine
  interval.
