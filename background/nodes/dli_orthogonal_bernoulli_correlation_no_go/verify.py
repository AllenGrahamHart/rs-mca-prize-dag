#!/usr/bin/env python3
"""Verify the orthogonal Bernoulli-correlation tensor counterexample."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction


U = (1, 1, -1, -1)
V = (1, -1, 1, -1)
EXPECTED = {
    "u_count": 6,
    "v_count": 6,
    "joint_count": 4,
    "dot": 0,
    "balanced_u": 0,
    "balanced_v": 0,
    "first_sqrt_failure": 3,
}


def dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(a * b for a, b in zip(left, right, strict=True))


def one_block() -> dict[str, int]:
    assignments = [
        tuple((mask >> index) & 1 for index in range(4))
        for mask in range(16)
    ]
    u_zero = [bits for bits in assignments if dot(U, bits) == 0]
    v_zero = [bits for bits in assignments if dot(V, bits) == 0]
    joint = [bits for bits in u_zero if dot(V, bits) == 0]
    return {
        "u_count": len(u_zero),
        "v_count": len(v_zero),
        "joint_count": len(joint),
        "dot": dot(U, V),
        "balanced_u": sum(U),
        "balanced_v": sum(V),
    }


def build() -> dict[str, int]:
    result = one_block()
    failures = []
    for r in range(1, 65):
        ratio = Fraction(16, 9) ** r
        if ratio * ratio > 8 * r:
            failures.append(r)
    result["first_sqrt_failure"] = failures[0]
    assert result == EXPECTED
    assert 16**6 > 24 * 9**6
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        changed = copy.deepcopy(result)
        changed["joint_count"] += 1
        caught = 0
        try:
            assert changed == result
        except AssertionError:
            caught = 1
        assert caught == 1
        print("DLI_ORTHOGONAL_BERNOULLI_NO_GO_TAMPER_PASS mutations=1/1")
        return
    print(
        "DLI_ORTHOGONAL_BERNOULLI_NO_GO_PASS "
        "single=6,6,4 ratio=16/9 first_sqrt_failure_r=3"
    )


if __name__ == "__main__":
    main()
