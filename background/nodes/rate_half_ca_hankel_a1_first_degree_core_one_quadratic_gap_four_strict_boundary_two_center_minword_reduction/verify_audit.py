#!/usr/bin/env python3
"""Independent union recount at the strict j=p boundary."""


for e in (7, 17, 183251937963):
    rho = 3 * e - 1
    p = rho // 2
    union = rho + p
    for deficit in (0, 1, 2):
        for excess in (0, 1, 5):
            inside = p - 2 - deficit - excess
            if inside < 0:
                continue
            triple_union = union + (rho - deficit) - (1 + inside)
            assert triple_union == 2 * rho + 1 + excess
    assert (3 * e + 1) - p == p + 2

print("RATE_HALF_QUADRATIC_STRICT_BOUNDARY_MINWORD_AUDIT_PASS")
