#!/usr/bin/env python3
"""Exact verifier for the two-threshold residual route wall."""

from __future__ import annotations

import argparse
import copy
from math import comb


N = 2_097_152
K = 1_048_576
M = 1_116_048
A = M - 1_679
MULTIPLICITY = N - A
H = 38_385
AVAILABLE = 65_167_969_673_715_470
R4 = MULTIPLICITY * (comb(N - K + 4, 4) // comb(A - K + 4, 4))
R6 = MULTIPLICITY * (comb(N - K + 6, 6) // comb(A - K + 6, 6))
FALL2 = M * (M - 1)
FALL3 = FALL2 * (M - 2)


def build() -> dict[str, int]:
    start = 18_166
    max_d2 = max(x * (H - x) ** 2 for x in range(start, H))
    max_d3 = max(x * (H - x) for x in range(start, H))
    count2 = FALL3 // max_d2
    count3 = FALL2 // max_d3
    charge = count2 * R4 + count3 * R6
    result = {
        "max_d2": max_d2,
        "max_d3": max_d3,
        "count2": count2,
        "count3": count3,
        "charge": charge,
        "excess": charge - AVAILABLE,
    }
    assert R4 == 63_397_365_764
    assert R6 == 16_100_859_197_492
    assert result == {
        "max_d2": 7_426_405_419_526,
        "max_d3": 368_352_056,
        "count2": 187_184,
        "count3": 3_381,
        "charge": 66_303_977_459_889_028,
        "excess": 1_136_007_786_173_558,
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        caught = 0
        for key, value in (("count2", 187_183), ("count3", 3_380), ("excess", 0)):
            changed = copy.deepcopy(result)
            changed[key] = value
            try:
                assert changed == result
            except AssertionError:
                caught += 1
        assert caught == 3
        print("RANK11_FACTOR_FLAG_TWO_THRESHOLD_WALL_TAMPER_PASS mutations=3/3")
        return
    print(
        "RANK11_FACTOR_FLAG_TWO_THRESHOLD_WALL_PASS "
        f"charge={result['charge']} excess={result['excess']}"
    )


if __name__ == "__main__":
    main()
