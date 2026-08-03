#!/usr/bin/env python3
"""Exact official arithmetic for the low-affine-span SL-2 payment."""

from math import comb


ROWS = (
    ("1/4", 2**41, 2**39, 2**33 + 1, 9,
     13211041760784548301820, 3791568976987080033655707,
     3288278229349592331945250),
    ("1/8", 2**41, 2**38, 2**33 + 1, 9,
     53137761854335542656230, 17801150181942642789226202,
     3288278229349592331945250),
    ("1/16", 2**41, 2**37, 2**32 + 1, 8,
     71421853205846145996360, 51352312252010783557476583,
     3288278229349592331945250),
)


def cap(a, b, s):
    return comb(a + s, s) // comb(b + s, s)


checks = 0
for name, n, k, h, paid_s, paid_pin, next_pin, budget_pin in ROWS:
    R = n - k
    d0 = (2 * h + 3) // 3
    assert 3 * d0 >= 2 * h + 2 > 3 * (d0 - 1)
    ell0 = 1
    e0 = 2 * (h - d0)
    assert e0 <= d0 - ell0 - 1
    a0 = R + ell0 - e0
    b0 = d0 + ell0
    budget = (17 * n * n - 25 * (n - 4)) // 25
    corner_budget = (17 * n * n - 25 * (n - e0)) // 25
    assert cap(a0, b0, paid_s) == paid_pin < budget == budget_pin
    assert cap(a0, b0, paid_s + 1) == next_pin > corner_budget >= budget
    assert h + 7 <= R - 2 * h  # ell+j <= R-2h for ell<=h-3,j<=10.
    for s in range(1, paid_s + 1):
        assert cap(a0, b0, s) <= budget
    checks += 7 + paid_s

# Bounded exact check of the discrete monotonic algebra independent of the
# official magnitudes.
for R in range(80, 101, 5):
    for h in range(8, 13):
        if R - 2 * h < h + 7:
            continue
        d0 = (2 * h + 3) // 3
        for d in range(d0, h - 1):
            for ell in range(1, d - 2 * (h - d)):
                emin = 2 * (h - d)
                if emin > d - ell - 1:
                    continue
                for s in range(1, 11):
                    assert cap(R + ell - emin, d + ell, s) <= cap(
                        R + 1 - 2 * (h - d0), d0 + 1, s
                    )
                    checks += 1

print(f"XR_DEFICIENT_WINDOW_LOW_AFFINE_SPAN_PAYMENT_PASS checks={checks}")
