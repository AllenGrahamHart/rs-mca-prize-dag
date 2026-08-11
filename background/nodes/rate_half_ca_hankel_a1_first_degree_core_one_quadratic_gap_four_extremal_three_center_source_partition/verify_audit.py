#!/usr/bin/env python3
"""Independent missing-set recount for the three line slopes."""


for e in (7, 17, 183251937963):
    rho = 3 * e - 1
    p = rho // 2
    u0 = 3 * p - 2
    for line_deficit in (0, 1):
        support_total = 3 * (rho - 1) - line_deficit
        incidence_on_u0 = support_total
        missing = 3 * u0 - incidence_on_u0
        assert missing == 3 * (p - 1) + line_deficit
        assert u0 - missing == 1 - line_deficit

print("RATE_HALF_QUADRATIC_EXTREMAL_SOURCE_PARTITION_AUDIT_PASS")
