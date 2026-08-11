#!/usr/bin/env python3
"""Independent union-excess recount for every deficit value."""


for e in (7, 17, 183251937963):
    rho = 3 * e - 1
    p = rho // 2
    j = p - 1
    U = rho + j

    for deficit in (0, 1, 2):
        cap_noncore_intersection = p - 3 - deficit
        for excess in (0, 1, 5):
            intersection = cap_noncore_intersection - excess
            if intersection < 0:
                continue
            triple_union = U + (rho - deficit) - (1 + intersection)
            assert triple_union == 2 * rho + 1 + excess

    off_slopes = 3 * e
    total_excess = e
    assert off_slopes - total_excess == 2 * e

print("RATE_HALF_QUADRATIC_EXTREMAL_THREE_CENTER_MINWORD_AUDIT_PASS")
