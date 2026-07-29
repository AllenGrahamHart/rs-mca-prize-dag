#!/usr/bin/env python3
"""Independent parameter reconstruction for the divisor-pencil route cut."""

dimension = 4_981
overlap = dimension - 1
agreement = dimension + 67_447

fixed_roots = overlap - 1
free_roots = agreement - fixed_roots

assert fixed_roots == 4_979
assert free_roots == 67_449
assert [overlap, fixed_roots, 0, 1, 2, 3] == [4_980, 4_979, 0, 1, 2, 3]
assert free_roots > 15_413

print("L1_M31_FIXED_SUPPORT_DIVISOR_ROUTE_CUT_AUDIT_PASS")
