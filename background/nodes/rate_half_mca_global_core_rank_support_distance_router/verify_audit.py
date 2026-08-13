#!/usr/bin/env python3
"""Independent audit of surviving rank/support-router gates."""

rows = (
    (1048576, 4337, 1044239, (981108, 981153, 981861, 992852)),
    (1048576, 4334, 1044242, (981144, 981363, 984779, 1037876)),
)
if any(R - j != e or any(not threshold < e for threshold in walls)
       for R, j, e, walls in rows):
    raise ValueError("support conversion")
print("RATE_HALF_MCA_GLOBAL_CORE_RANK_SUPPORT_REPLACEMENT_TARGET_AUDIT_PASS gates=2 replacement_walls=8")
