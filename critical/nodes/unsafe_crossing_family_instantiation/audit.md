# Audit

Date: 2026-07-26.

The former `unsafe_at_crossing` proof treated “collision-free” and “collided”
as an exhaustive sufficient split. The predicates are exhaustive, but the
supplier conclusions are not:

- `qfloor_exact` applies only when its prime-field and norm-threshold
  hypotheses are proved at the row and endpoint;
- `averaged_slope_conversion` applies to any supplied family only after its
  exact occupancy quantity is computed, and prize unsafety requires the
  strict inequality `nu(A)>B*`;
- “collided” alone supplies neither post-paid ownership nor that inequality.

The 2026-07-27 tangent-floor audit adds a valid low-field `V` supplier. Its
negative envelope verdict concerns only the theorem's guaranteed `n-a`
slopes; it is not a converse and does not upper-bound that line's full bad set.

The old verifier checked dependency labels and statuses, not these premises.
This node records the missing row-instantiation theorem explicitly.
