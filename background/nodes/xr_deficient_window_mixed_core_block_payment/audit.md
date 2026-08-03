# Audit

## Logical checks

- Core hyperplanes are counted only outside the direction code's common-zero
  set; the miss parameter `b` is retained until a lower bound safely drops it.
- The core subset has rank exactly `s-1`, so its intersection with the affine
  hull is a line.
- Active points lie in `D`, where the invariant residual prevents a zero error
  vector and makes the annihilator slope unique.
- The rational-direction fiber cap is `ell`, not one.  This loses exactly
  `r(ell-1)/2` possible point pairs.
- A zero quadratic is not counted as two roots.  It forces a constant selected
  slope and is disposed of by the already-proved same-ray interaction strip.
- The local budget is bounded below at `e=4`; no same-corner budget is used.

## Arithmetic checks

The verifier checks both sides of every threshold, all six cross-bounds by
integer cross multiplication, and the monotonic inequalities used between
the pins.  Lowering any `T` by one fails its affine threshold assertion.

## Residual risk

The mixed compiler pays only the first previously-unpaid affine dimension.
Its bound grows with dimension, so it must not be extrapolated to the residual
`11,11,10` layers.
