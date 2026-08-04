#!/usr/bin/env python3
"""Verify the two-block slack identities and official boundary pins."""


def check_general(h: int, d: int, ell: int) -> int:
    r = h - d
    sigma = d - ell - 1 - 2 * r
    if sigma < 0 or sigma >= r:
        return 0

    checks = 0
    for g in range(2 * r, 2 * r + sigma + 1):
        for e in range(2 * r, g + 1):
            assert e <= g <= d - ell - 1
            assert e // r == 2
            assert e - 2 * r <= sigma
            assert g - 2 * r <= sigma
            assert d - ell - g <= sigma + 1
            checks += 5
    return checks


checks = 0
for h in range(12, 96):
    for d in range((h + 1) // 2, h - 1):
        for ell in range(1, d):
            checks += check_general(h, d, ell)

ROWS = (
    ("1/4", 2**33 + 1, 5, 6),
    ("1/8", 2**33 + 1, 5, 6),
    ("1/16", 2**32 + 1, 1, 2),
)

for name, h, expected_sigma, expected_cofactor_space in ROWS:
    ell = (h - 4) // 7
    r = 2 * ell + 1
    d = h - r
    sigma = d - ell - 1 - 2 * r
    assert sigma == h - 7 * ell - 4 == expected_sigma
    assert sigma < r
    assert d - ell - 2 * r == expected_cofactor_space
    assert 2 * r + sigma == d - ell - 1
    checks += 4

# Mutating the boundary by one unit destroys the printed exact slack.
h = 2**33 + 1
ell = (h - 4) // 7
assert h - 7 * (ell + 1) - 4 != 5
checks += 1

print(
    "XR_DEFICIENT_WINDOW_TWO_BLOCK_KERNEL_SLACK_ROUTER_PASS "
    f"rows={len(ROWS)} checks={checks}"
)
