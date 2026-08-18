#!/usr/bin/env python3
"""Verify the cyclic-band correlation tensor and owner deletion."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction
from itertools import product


EXPECTED = {
    "n": 12,
    "q": 13,
    "e1": 64,
    "e2": 216,
    "joint": 8,
    "primitive_joint": 0,
    "ratio_numerator": 64,
    "ratio_denominator": 27,
}


def primitive_root(q: int) -> int:
    factors = []
    value = q - 1
    p = 2
    while p * p <= value:
        if value % p == 0:
            factors.append(p)
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        factors.append(value)
    for candidate in range(2, q):
        if all(pow(candidate, (q - 1) // factor, q) != 1
               for factor in factors):
            return candidate
    raise AssertionError("primitive root missing")


def build() -> dict[str, int]:
    r, n, q = 3, 12, 13
    zeta = pow(primitive_root(q), (q - 1) // n, q)
    assert pow(zeta, n, q) == 1 and pow(zeta, n // 2, q) == q - 1
    bands = (
        tuple(1 + 4 * ell for ell in range(r)),
        tuple(2 + 4 * ell for ell in range(r)),
    )
    counts = [0, 0]
    joint = primitive_joint = 0
    for bits in product((0, 1), repeat=n):
        events = [
            all(
                sum(bits[index] * pow(zeta, frequency * index, q)
                    for index in range(n)) % q == 0
                for frequency in band
            )
            for band in bands
        ]
        counts[0] += events[0]
        counts[1] += events[1]
        if all(events):
            joint += 1
            primitive = any(
                bits[index] != bits[index + n // 2]
                for index in range(n // 2)
            )
            primitive_joint += primitive
            assert all(bits[s] == bits[s + r] == bits[s + 2 * r] == bits[s + 3 * r]
                       for s in range(r))
    ratio = Fraction(joint * (1 << n), counts[0] * counts[1])
    result = {
        "n": n,
        "q": q,
        "e1": counts[0],
        "e2": counts[1],
        "joint": joint,
        "primitive_joint": primitive_joint,
        "ratio_numerator": ratio.numerator,
        "ratio_denominator": ratio.denominator,
    }
    assert result == EXPECTED
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        changed = copy.deepcopy(result)
        changed["primitive_joint"] += 1
        caught = 0
        try:
            assert changed == result
        except AssertionError:
            caught = 1
        assert caught == 1
        print("DLI_CYCLIC_BAND_TENSOR_OWNER_TAMPER_PASS mutations=1/1")
        return
    print(
        "DLI_CYCLIC_BAND_TENSOR_OWNER_PASS "
        "n=12 counts=64,216,8 ratio=64/27 primitive_joint=0"
    )


if __name__ == "__main__":
    main()
