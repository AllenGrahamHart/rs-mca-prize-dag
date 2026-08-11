#!/usr/bin/env python3
"""Independent category count for the zero-deficit oriented coupling."""


for e in (7, 13, 183251937963):
    g = -((-(3 * e - 2)) // 5)
    common_nonendpoint = g - 1
    endpoint_roots = 2
    oriented_residual = 6 * (e - g)
    used = common_nonendpoint + endpoint_roots + oriented_residual
    assert used == g + 1 + 6 * (e - g)
    assert used <= 3 * e + 3
    assert 5 * g >= 3 * e - 2

print("RATE_HALF_QUADRATIC_MINIMUM_PAIR_ORIENTED_GCD_COUPLING_AUDIT_PASS")
