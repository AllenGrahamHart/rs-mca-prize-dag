#!/usr/bin/env python3
"""Verify W2 qcore counts, endpoint arithmetic, and scope mutations."""

from __future__ import annotations

from fractions import Fraction
from math import comb


CLEAN = (
    (1, 4, 256),
    (1, 8, 256),
    (1, 16, 512),
)


def main() -> None:
    edge = 1 << 128
    for numerator, denominator, quotient_order in CLEAN:
        h = quotient_order * numerator // denominator
        count = comb(quotient_order - 1, h)
        if count <= edge:
            raise AssertionError((numerator, denominator, count))

        # A representative official order; the proof is n-uniform because
        # quotient_order and h are fixed by the rate.
        n = 1 << 41
        k = n * numerator // denominator
        scale = n // quotient_order
        sigma = scale - 1
        if k % scale or k // scale != h or not (1 <= sigma < scale):
            raise AssertionError((numerator, denominator, scale, sigma))
        if sigma + k - scale != k - 1:
            raise AssertionError("degree endpoint")

        agreement = k + sigma
        closed_radius = Fraction(n - agreement, n)
        if closed_radius != 1 - Fraction(agreement, n):
            raise AssertionError("closed-radius conversion")

    # Invalid endpoint mutation: sigma=M makes the constructed polynomial
    # degree k, not <k.
    n = 1 << 41
    scale = n // 256
    k = n // 4
    if scale + k - scale != k:
        raise AssertionError("sigma=M mutation was not detected")

    # Rate 1/2 is intentionally outside W2.
    if comb(127, 64) >= edge:
        raise AssertionError("rate-half scope mutation")

    # Integer/floor equivalence at both integral and nonintegral thresholds.
    for field_size in ((1 << 256) - 189, 17**32):
        threshold = Fraction(field_size, 1 << 128)
        least = field_size // (1 << 128) + 1
        if not (least > threshold and least - 1 <= threshold):
            raise AssertionError((field_size, least, threshold))

    print(
        "WW_LOWER_WITNESSES_PASS "
        "clean_rates=3 endpoint=closed mutation=sigma=M rate_half=excluded"
    )


if __name__ == "__main__":
    main()
