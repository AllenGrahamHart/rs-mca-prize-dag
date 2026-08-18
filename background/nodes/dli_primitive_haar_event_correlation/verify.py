#!/usr/bin/env python3
"""Exhaustive replay of the primitive Haar-event correlation identity."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction
from itertools import product
import math


FIXTURES = ((8, 4, 17), (16, 2, 17), (16, 4, 17), (16, 8, 17))
EXPECTED = {
    "fixtures": 4,
    "positive": 1,
    "rows": {
        "8|4|17": {"joint": 2, "nonprimitive": 2, "primitive": 0,
                    "terminal": 70, "blocks": [16, 36],
                    "ratio_num": 0, "ratio_den": 1},
        "16|2|17": {"joint": 224, "nonprimitive": 16, "primitive": 208,
                     "terminal": 3856, "blocks": [3856],
                     "ratio_num": 53248, "ratio_den": 58081},
        "16|4|17": {"joint": 4, "nonprimitive": 4, "primitive": 0,
                     "terminal": 5124, "blocks": [320, 3856],
                     "ratio_num": 0, "ratio_den": 1},
        "16|8|17": {"joint": 2, "nonprimitive": 2, "primitive": 0,
                     "terminal": 12870, "blocks": [256, 1296, 5124],
                     "ratio_num": 0, "ratio_den": 1},
    },
}


def primitive_root(q: int) -> int:
    factors: list[int] = []
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
    for g in range(2, q):
        if all(pow(g, (q - 1) // p, q) != 1 for p in factors):
            return g
    raise AssertionError("primitive root missing")


def fixture(n: int, t: int, q: int) -> dict[str, object]:
    m = t.bit_length() - 1
    zeta = pow(primitive_root(q), (q - 1) // n, q)
    block_counts = [0] * m
    terminal_count = 0
    joint_count = 0
    primitive_joint = 0
    nonprimitive_joint = 0

    for bits in product((0, 1), repeat=n):
        direct = all(
            sum(bits[i] * pow(zeta, r * i, q) for i in range(n)) % q == 0
            for r in range(1, t + 1)
        )

        level = list(bits)
        events: list[bool] = []
        for j in range(m):
            h = len(level)
            half = h // 2
            skew = [level[i] - level[i + half] for i in range(half)]
            zeta_j = pow(zeta, 1 << j, q)
            odd = range(1, t // (1 << j) + 1, 2)
            event = all(
                sum(skew[i] * pow(zeta_j, u * i, q) for i in range(half)) % q == 0
                for u in odd
            )
            events.append(event)
            level = [level[i] + level[i + half] for i in range(half)]

        zeta_m = pow(zeta, 1 << m, q)
        terminal = sum(level[i] * pow(zeta_m, i, q) for i in range(len(level))) % q == 0
        assert direct == (terminal and all(events))

        for j, event in enumerate(events):
            block_counts[j] += event
        terminal_count += terminal
        joint_count += direct
        primitive = any(bits[i] != bits[i + n // 2] for i in range(n // 2))
        primitive_joint += direct and primitive
        nonprimitive_joint += direct and not primitive

    ratio = Fraction(
        primitive_joint << (n * m),
        terminal_count * math.prod(block_counts),
    )
    probability_ratio = Fraction(primitive_joint, 1 << n) / (
        Fraction(terminal_count, 1 << n)
        * math.prod(Fraction(count, 1 << n) for count in block_counts)
    )
    assert ratio == probability_ratio
    assert joint_count == primitive_joint + nonprimitive_joint
    return {
        "joint": joint_count,
        "nonprimitive": nonprimitive_joint,
        "primitive": primitive_joint,
        "terminal": terminal_count,
        "blocks": block_counts,
        "ratio_num": ratio.numerator,
        "ratio_den": ratio.denominator,
    }


def build() -> dict[str, object]:
    rows = {f"{n}|{t}|{q}": fixture(n, t, q) for n, t, q in FIXTURES}
    result = {
        "fixtures": len(rows),
        "positive": sum(row["primitive"] > 0 for row in rows.values()),
        "rows": rows,
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
        next(iter(changed["rows"].values()))["joint"] += 1
        caught = 0
        try:
            assert changed == result
        except AssertionError:
            caught = 1
        assert caught == 1
        print("DLI_PRIMITIVE_HAAR_EVENT_CORRELATION_TAMPER_PASS mutations=1/1")
        return
    print(
        "DLI_PRIMITIVE_HAAR_EVENT_CORRELATION_PASS "
        f"fixtures={result['fixtures']} positive={result['positive']}"
    )


if __name__ == "__main__":
    main()
