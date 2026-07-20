# Audit - L1 bounded-mark affine split-pencil compiler

## Checked axes

1. Differences of monic degree-`d` locators have degree at most `d-1`.
2. Equal missing syndromes plus the retained equations give every full-petal
   equation.
3. The leading coefficient makes the homogenized sum direct and identifies
   its monic hyperplane exactly.
4. Sparse-petal equations may be retained as fixed equations; only dense
   holes enter the missing syndrome.
5. Exact-defect coprimality gives `gcd(JF,JW)=J`, not merely divisibility by
   `J`.
6. The orientation-plus-exceptions encoding counts sparse occupancy and dense
   holes with the same polarized currency.
7. The polynomial pre-factor is not presented as a cell bound.
8. The per-chart compiler is not presented as a non-intrinsic chart census.

## Remaining attack

Prove a uniform split/saturated-point bound for the one-direction affine
extensions, or map every such cell injectively to an existing
base-field-normalized split-pencil/profile owner. Separately bound canonical
first-match source charts. Growing polarity remains a separate branch.
