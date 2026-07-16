#!/usr/bin/env python3
"""Replay the growing-window dyadic near-coset owner and absorption."""

from __future__ import annotations

from math import comb


def miss_window(n: int, exponent: int) -> int:
    return n // (32 * exponent)


def exact_owner_count(n: int, k: int, max_defect: int) -> int:
    total = 0
    scale = 1
    while scale <= n:
        if scale >= k - max_defect:
            for e in range(max_defect + 1):
                q = max(0, k - scale + e)
                if q <= n - scale:
                    total += (
                        (n // scale)
                        * comb(scale, e)
                        * comb(n - scale, q)
                    )
        scale *= 2
    return total


def main() -> None:
    checks = 0
    n_min = 1 << 13

    if not (1 << 7) < 15**2:
        raise AssertionError("growing-window exponent comparison")
    checks += 1

    # Doubling the miss window would make this certificate fail. This guards
    # the constant 32 rather than merely replaying a favorable inequality.
    if (1 << 13) < 15**2:
        raise AssertionError("mutation: denominator 16 must be rejected")
    checks += 1

    smallest_window = None
    for exponent in range(13, 45):
        n = 1 << exponent
        n_half = n // 2
        max_defect = miss_window(n, exponent)
        smallest_window = (
            max_defect
            if smallest_window is None
            else min(smallest_window, max_defect)
        )

        if max_defect < 19:
            raise AssertionError((exponent, max_defect))
        if not 3 * exponent * max_defect <= 3 * n // 32:
            raise AssertionError((exponent, max_defect, "window exponent"))
        if not 3 * exponent <= n // 64:
            raise AssertionError((exponent, "prefactor absorption"))
        checks += 3

        for denominator in (2, 4, 8, 16):
            k = n // denominator
            h = k // 2 + 1
            m = min(h, n_half - 1 - h)
            r = n // 32
            if not r <= m <= (n_half - 1) // 2:
                raise AssertionError((exponent, denominator, r, m))
            if not n_half - 1 > 15 * r:
                raise AssertionError((exponent, denominator, "factor lower"))

            scales = [
                1 << i
                for i in range(exponent + 1)
                if (1 << i) >= k - max_defect
            ]
            if len(scales) > exponent + 1:
                raise AssertionError((exponent, denominator, scales))
            for scale in scales:
                max_q = max(0, k - scale + max_defect)
                if max_q > 2 * max_defect:
                    raise AssertionError(
                        (exponent, denominator, scale, max_defect, max_q)
                    )
            checks += 4

    # Exact smallest-row comparisons independently cover every rate.
    for denominator in (2, 4, 8, 16):
        n = n_min
        exponent = 13
        k = n // denominator
        max_defect = miss_window(n, exponent)
        n_half = n // 2
        owner = exact_owner_count(n, k, max_defect)
        q2 = comb(n_half - 1, k // 2 + 1)
        if not owner < q2:
            raise AssertionError((denominator, max_defect, owner, q2))
        checks += 1

    # The growing owner contains the four-defect index-two specialization.
    n = n_min
    k = n // 2
    max_defect = miss_window(n, 13)
    scale = n // 2
    index_two = (n // scale) * sum(
        comb(scale, e) * comb(n - scale, max(0, k - scale + e))
        for e in range(5)
    )
    if exact_owner_count(n, k, max_defect) < index_two:
        raise AssertionError("index-two subsumption")
    checks += 1

    print(
        "PMA_DYADIC_NEAR_COSET_OWNER_PASS "
        f"checks={checks} rows={32 * 4} smallest_window={smallest_window} "
        "smallest_exact=4"
    )


if __name__ == "__main__":
    main()
