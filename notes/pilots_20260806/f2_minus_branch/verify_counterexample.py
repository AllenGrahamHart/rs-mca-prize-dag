#!/usr/bin/env python3
"""Verify the omitted p == -1 mod 2^41 official F2 branch."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
N = 1 << 41
P = (1 << 61) - 1
Q = P * P


def v2(value: int) -> int:
    result = 0
    while value % 2 == 0:
        value //= 2
        result += 1
    return result


def lucas_lehmer(exponent: int) -> int:
    modulus = (1 << exponent) - 1
    state = 4
    for _ in range(exponent - 2):
        state = (state * state - 2) % modulus
    return state


def main() -> None:
    assert lucas_lehmer(61) == 0
    assert Q < 1 << 256
    assert (Q - 1) % N == 0
    assert P % N == N - 1
    assert pow(P, 2, N) == 1
    assert P % N != 1
    actual_order = 2

    ep = v2(P - 1)
    old_formula = 1 << (41 - ep)
    assert ep == 1
    assert old_formula == 1 << 40
    assert old_formula != actual_order

    intersection = math.gcd(N, P - 1)
    assert intersection == 2
    antipodal_classes = N // 2
    assert antipodal_classes == 1 << 40
    assert antipodal_classes > 4

    manifest = json.loads(
        (ROOT / "background/nodes/f2_admissible_direct_sum_grs_reduction/node.json").read_text()
    )
    assert manifest["node"]["status"] == "PROVED"
    assert "every official" in manifest["node"]["statement"].lower()
    print(
        "F2_MINUS_BRANCH_COUNTEREXAMPLE_PASS "
        f"p={P} q_bits={Q.bit_length()} order={actual_order} "
        f"old_order={old_formula} classes={antipodal_classes} lucas_lehmer=0"
    )


if __name__ == "__main__":
    main()
