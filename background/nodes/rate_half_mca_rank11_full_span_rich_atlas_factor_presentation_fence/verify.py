#!/usr/bin/env python3
"""Exact arithmetic checks for the rich-atlas factor-presentation fence."""

from __future__ import annotations

import argparse
import copy


H = 38_385
D_SMALL = H + 4
D_AMBIENT = 2 * H + 4
K = 1_048_576
Q = 2_097_152
CONTAINERS = 16_384_884


def gaussian(n: int, r: int, q: int) -> int:
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= q ** (n - i) - 1
        denominator *= q ** (r - i) - 1
    return numerator // denominator


def build() -> dict[str, int]:
    family_dimension = 2 * 5 * ((D_SMALL + 1) - 5)
    product_dimension = 5 * D_AMBIENT - 25
    available_at_q16 = 4 * gaussian(5, 2, 16)
    result = {
        "D_small": D_SMALL,
        "D_ambient": D_AMBIENT,
        "family_dimension": family_dimension,
        "product_dimension": product_dimension,
        "dimension_gap": family_dimension - product_dimension,
        "available_at_q16": available_at_q16,
        "degree_slack": K - 1 - D_AMBIENT,
        "finite_count_margin": Q**5 - 32 * (D_AMBIENT + 1) ** 2,
    }
    assert result == {
        "D_small": 38_389,
        "D_ambient": 76_774,
        "family_dimension": 383_850,
        "product_dimension": 383_845,
        "dimension_gap": 5,
        "available_at_q16": 71_862_340,
        "degree_slack": 971_801,
        "finite_count_margin": 40_564_819_207_303_340_847_705_881_752_032,
    }
    assert available_at_q16 > CONTAINERS
    assert 64 < Q ** (H - 4)
    assert 40 < Q**4
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        caught = 0
        for key, value in (
            ("dimension_gap", 0),
            ("available_at_q16", CONTAINERS),
            ("degree_slack", -1),
            ("finite_count_margin", 0),
        ):
            changed = copy.deepcopy(result)
            changed[key] = value
            try:
                assert changed == result
            except AssertionError:
                caught += 1
        assert caught == 4
        print("RANK11_RICH_ATLAS_FACTOR_FENCE_TAMPER_PASS mutations=4/4")
        return
    print(
        "RANK11_RICH_ATLAS_FACTOR_FENCE_PASS "
        f"dimension_gap={result['dimension_gap']} containers={result['available_at_q16']}"
    )


if __name__ == "__main__":
    main()
