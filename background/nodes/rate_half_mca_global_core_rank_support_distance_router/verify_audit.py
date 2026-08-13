#!/usr/bin/env python3
"""Independent audit of surviving rank/support-router gates."""

rows = (
    (1048576, 4337, 1044239, (981108, 981153, 981861, 992852), 992852,
     743896698428332665, 274980728111395087),
    (1048576, 4334, 1044242, (981144, 981363, 984779, 1037876), 1037876,
     219426634, 16777215),
)
if any(R - j != e or any(not threshold < e for threshold in walls)
       or drop != walls[-1] or not ceiling > budget
       for R, j, e, walls, drop, ceiling, budget in rows):
    raise ValueError("support conversion")
print("RATE_HALF_MCA_GLOBAL_CORE_RANK_SUPPORT_REPLACEMENT_TARGET_AUDIT_PASS gates=2 replacement_walls=8 top_splits=2 full_lift_ceilings=2")
