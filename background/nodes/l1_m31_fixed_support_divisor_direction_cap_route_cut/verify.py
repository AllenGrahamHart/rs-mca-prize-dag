#!/usr/bin/env python3
"""Static arithmetic replay for the one-root-swap divisor pencil."""

m = 72_428
t = 4_980
degrees = [t, t - 1, 0, 1, 2, 3]

assert len(set(degrees)) == 6
directions = m - (t - 1)
assert directions == 67_449
assert directions > 15_413

print(
    "L1_M31_FIXED_SUPPORT_DIVISOR_ROUTE_CUT_PASS "
    f"dimension={len(degrees)} directions={directions}"
)
