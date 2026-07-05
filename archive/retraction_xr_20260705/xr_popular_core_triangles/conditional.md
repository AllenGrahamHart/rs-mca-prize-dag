# Conditional proof: popular-core triangles

Status: CONDITIONAL on `xr_heavy_triangle_charge` and
`xr_light_triangle_eliminant`.

The concentrated-budget branch is partitioned by the exact heavy/light divider
from the node statement:

```text
sum r - triple > 2k     heavy
sum r - triple <= 2k    light
```

The sunflower subcase is already proved by `xr_sunflower_rank_additive`, which
shows that sunflower families do not create rank stagnation and are capped by
the support-cancellation/dual-weight argument.

For non-sunflower concentrated budgets, the remaining cases are exactly the
heavy and light triangle branches.  Thus the popular-core triangle node follows
once `xr_heavy_triangle_charge` covers the heavy side and
`xr_light_triangle_eliminant` covers the light side.
