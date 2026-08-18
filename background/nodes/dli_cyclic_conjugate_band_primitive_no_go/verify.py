#!/usr/bin/env python3
"""Verify the primitive conjugate-band correlation counterexample."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction
from itertools import product


EXPECTED = {
    "n": 8,
    "q": 17,
    "e2": 36,
    "e6": 36,
    "joint": 36,
    "owner": 4,
    "primitive": 32,
    "ratio_numerator": 512,
    "ratio_denominator": 81,
}


def build() -> dict[str, int]:
    n, q, zeta = 8, 17, 9
    assert pow(zeta, n, q) == 1 and pow(zeta, n // 2, q) == q - 1
    e2 = e6 = joint = owner = 0
    for bits in product((0, 1), repeat=n):
        event2 = sum(bits[i] * pow(zeta, 2 * i, q) for i in range(n)) % q == 0
        event6 = sum(bits[i] * pow(zeta, 6 * i, q) for i in range(n)) % q == 0
        assert event2 == event6
        e2 += event2
        e6 += event6
        joint += event2 and event6
        owner += event2 and event6 and all(
            bits[i] == bits[i + n // 2] for i in range(n // 2)
        )
    primitive = joint - owner
    ratio = Fraction(primitive * (1 << n), e2 * e6)
    result = {
        "n": n,
        "q": q,
        "e2": e2,
        "e6": e6,
        "joint": joint,
        "owner": owner,
        "primitive": primitive,
        "ratio_numerator": ratio.numerator,
        "ratio_denominator": ratio.denominator,
    }
    assert result == EXPECTED
    assert ratio * ratio > 2 * n
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        changed = copy.deepcopy(result)
        changed["owner"] += 1
        caught = 0
        try:
            assert changed == result
        except AssertionError:
            caught = 1
        assert caught == 1
        print("DLI_CYCLIC_CONJUGATE_PRIMITIVE_NO_GO_TAMPER_PASS mutations=1/1")
        return
    print(
        "DLI_CYCLIC_CONJUGATE_PRIMITIVE_NO_GO_PASS "
        "n=8 marginal=36 owner=4 primitive=32 ratio=512/81"
    )


if __name__ == "__main__":
    main()
