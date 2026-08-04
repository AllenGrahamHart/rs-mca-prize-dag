#!/usr/bin/env python3
"""Verify the active-block nullity identity and official boundary pins."""


ROWS = (
    ("1/4", 2**33 + 1, 6),
    ("1/8", 2**33 + 1, 6),
    ("1/16", 2**32 + 1, 2),
)

checks = 0
for name, h, expected in ROWS:
    ell = (h - 4) // 7
    r = 2 * ell + 1
    d = h - r
    g_floor = 2 * r
    nullity_cap = d - ell - g_floor

    assert 7 * ell <= h - 4 < 7 * (ell + 1)
    assert nullity_cap == h - 7 * ell - 3 == expected
    assert nullity_cap == 3 * d - 2 * h - ell
    assert ell <= 3 * d - 2 * h - 1
    assert g_floor <= d - ell - 1

    # Moving one unit past the admissible ell boundary would make the
    # multiplier-space cap negative, so the floor endpoint is load-bearing.
    assert h - 7 * (ell + 1) - 3 < 0
    checks += 6

print(
    "XR_DEFICIENT_WINDOW_ACTIVE_BLOCK_NULLITY_PIN_PASS "
    f"rows={len(ROWS)} checks={checks}"
)
