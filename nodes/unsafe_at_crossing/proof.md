# unsafe_at_crossing proof

## Claim

For each admissible row, the adjacent grid point below the safe radius has an
unsafe witness:

```text
B_C(a_safe - 1) > B*.
```

## Proof

The node statement splits the proof into two exhaustive cases.

In the collision-free case, the quotient-floor value-set family supplies the
unsafe witnesses. This is exactly the proved `qfloor_exact` branch.

In the collided case, the quotient-floor family may not directly give distinct
witnesses, but the FM locator mass crosses the v8-normalized threshold. The
proved `averaged_slope_conversion` converts that locator mass, after paid
fibers are excluded, into a pair `(u,v)` carrying at least `B*` distinct bad
slopes.

Since every admissible row is in one of these two cases, and both branches are
proved, the adjacent unsafe witness exists in every admissible row.
