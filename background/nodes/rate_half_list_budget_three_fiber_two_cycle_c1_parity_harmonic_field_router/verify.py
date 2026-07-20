#!/usr/bin/env python3
"""Exact checks for the c=1 parity harmonic field router."""

from __future__ import annotations

from math import isqrt


PRIME = 1009
STEP = 1 << 40
K_MIN = 29_058_991
K_MAX = 33_554_432


def square_root(value: int, modulus: int = PRIME) -> int:
    for candidate in range(modulus):
        if candidate * candidate % modulus == value % modulus:
            return candidate
    raise AssertionError("expected square")


def trace_iterate(value: int, levels: int, modulus: int = PRIME) -> int:
    for _ in range(levels):
        value = (value * value - 2) % modulus
    return value


def main() -> None:
    lower_square = 3 * (1 << 128)
    lower = isqrt(lower_square)
    if lower * lower < lower_square:
        lower += 1
    upper = 1 << 65
    computed_min = (lower - 1 + STEP - 1) // STEP
    computed_max = (upper - 1 + STEP - 1) // STEP
    assert (computed_min, computed_max) == (K_MIN, K_MAX)
    assert K_MAX - K_MIN == 4_495_441

    l_order = 1 << 39
    assert 4 * l_order * l_order < 3 * (1 << 128)
    assert (2 * l_order) ** 2 < 3 * (1 << 128)

    iota = square_root(-1)
    zeta = square_root(iota)
    theta = (1 + iota) * pow(zeta, -1, PRIME) % PRIME
    assert theta * theta % PRIME == 2

    h_p = (4 - 3 * iota) * pow(5, -1, PRIME) % PRIME
    assert (h_p + pow(h_p, -1, PRIME)) % PRIME == (
        8 * pow(5, -1, PRIME)
    ) % PRIME

    h_r_roots = [
        value
        for value in range(1, PRIME)
        if (
            value * value
            + 3 * (1 + iota) * value
            + iota
        )
        % PRIME
        == 0
    ]
    assert len(h_r_roots) == 2
    for root in h_r_roots:
        scaled = root * pow(zeta, -1, PRIME) % PRIME
        trace = (scaled + pow(scaled, -1, PRIME)) % PRIME
        assert trace == (-3 * theta) % PRIME
        assert trace_iterate(trace, 1) == 16

    # A small exact-order control for the trace recurrence itself. The
    # official fixed traces are deliberately not assumed to survive.
    modulus = 17
    assert trace_iterate(0, 2, modulus) == 2
    assert trace_iterate(0, 1, modulus) != 2

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_PARITY_HARMONIC_FIELD_PASS "
        f"k_min={K_MIN} k_max={K_MAX} candidates={K_MAX-K_MIN} "
        "field_degree=2 traces=2"
    )


if __name__ == "__main__":
    main()
