# Claim contract - L1 two-petal small-support anchor closure

## Inputs

- maximal-source threshold and the nonzero-numerator/background-root facts
  from `petal_reserve_rich_fiber_reduction`;
- the non-planted per-petal defect cap in the same core-defect reduction;
- the exact paid background-petal gate from `pma_b11_first_match_router`.

## Output

Every exact two-petal word with smaller support bounded by a fixed `A` enters
the B11 gate automatically. The singleton case is completely removed from
the unpaid mixed residual.

## Nonclaims

No uniform theorem for growing `A`, no count of three-petal profiles, no
power-map normalization, and no promotion of the L1 target is claimed.

## Falsifier

A valid maximal-chart word satisfying the threshold, `W!=0`, the per-petal
cap, `t=2`, and `z<=A`, but violating either `d<=ell+A-1` or `G_R<=2A`.
