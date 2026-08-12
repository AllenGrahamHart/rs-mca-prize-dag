#!/usr/bin/env python3
"""Replay the four-root factor-slack thresholds and profile compression."""


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def least_with_parity(numerator, denominator, parity):
    value = (numerator + denominator - 1) // denominator
    if value % 2 != parity:
        value += 1
    return value


checks = 0
for e in range(7, 80, 2):
    total = e - 2
    for d_a, q in ((0, 9), (1, 7)):
        large = least_with_parity(3 * e - 8, q - 2, 1)
        huge = least_with_parity(6 * e - 8, q - 2, 0)
        require((q - 2) * large >= 3 * e - 8, "large threshold")
        require((q - 2) * (large - 2) < 3 * e - 8, "large predecessor")
        require((q - 2) * huge >= 6 * e - 8, "huge threshold")
        require((q - 2) * (huge - 2) < 6 * e - 8, "huge predecessor")
        checks += 4
        if d_a == 1:
            require(2 * large + 1 > total, "profile II survived")
            require(huge + 1 > total, "profile III survived")
            checks += 2

official = 183251937963
require(least_with_parity(3 * official - 8, 7, 1) == 78536544841, "official d0 large")
require(least_with_parity(6 * official - 8, 7, 0) == 157073089682, "official d0 huge")
require(least_with_parity(3 * official - 8, 5, 1) == 109951162777, "official d1 large")
require(least_with_parity(6 * official - 8, 5, 0) == 219902325554, "official d1 huge")
checks += 4

for q, chi, coefficient in ((9, -1, 3), (9, -2, 6), (7, -1, 3), (7, -2, 6)):
    e = 101
    threshold = least_with_parity(coefficient * e - 8, q - 2, 1 if chi == -1 else 0)
    sigma_twice = 3 * e * chi + q * threshold
    require(sigma_twice >= 2 * threshold - 8, "factor slack inequality")
    checks += 1

print(f"RATE_HALF_COLLISION_FACTOR_UNSUPPORTED_ROOT_BUDGET_PASS checks={checks}")
