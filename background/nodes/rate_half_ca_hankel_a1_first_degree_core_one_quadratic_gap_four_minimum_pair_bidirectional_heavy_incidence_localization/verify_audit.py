#!/usr/bin/env python3
"""Independent replay of the category and missing-incidence algebra."""


def ceil_div(a, b):
    return -((-a) // b)


for e in (13, 127, 183251937963):
    T = 3 * e + 3
    for R in range(5):
        n = R + 6
        generic = ceil_div((R + 3) * e - 2, R + 5)
        for arm, cap in (("double", 1), ("two", 2)):
            if arm == "double" and R > 2:
                continue
            if cap == 1:
                localized = ceil_div((R + 1) * e - 6, R + 2)
            else:
                localized = ceil_div(2 * (R + 2) * e - 8, 2 * R + 7)
            g = max(generic, localized)
            used = g + 1 + n * (e - g)
            slack = T - used
            assert slack == (R + 5) * g - (R + 3) * e + 2
            assert slack >= 0

            forced_line_deficit = max(0, e - 6 - cap * slack)
            assert 3 * g + forced_line_deficit <= 3 * e - 2

print("RATE_HALF_QUADRATIC_BIDIRECTIONAL_HEAVY_LOCALIZATION_AUDIT_PASS")
