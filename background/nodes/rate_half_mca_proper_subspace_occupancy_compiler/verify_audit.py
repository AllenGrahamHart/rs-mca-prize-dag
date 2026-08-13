#!/usr/bin/env python3
"""Independent rational audit of the proper-subspace occupancy walls."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import product as cartesian_product
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent


def falling(value: int, length: int) -> int:
    result = 1
    for offset in range(length):
        result *= value - offset
    return result


def full_bound(R: int, d: int, K: int, q: int, L: int) -> int:
    N, m = R + K, d + K
    middle = prod(d + offset for offset in range(1, q))
    values = []
    for z in range(K - q + 1):
        for g in range(z + 1):
            values.append(Fraction(falling(N - z, q + 1), (m - g) * middle * L))
    return max(values).numerator // max(values).denominator


def first_factor(R: int, d: int, K: int, q: int, budget: int) -> int:
    low, high = 1, 1
    while full_bound(R, d, K, q, high) > budget:
        high *= 2
    while low < high:
        middle = (low + high) // 2
        if full_bound(R, d, K, q, middle) <= budget:
            high = middle
        else:
            low = middle + 1
    return low


def exhaustive_rank_one_toy() -> int:
    p, N, K, m = 3, 3, 1, 2
    words = list(cartesian_product(range(p), repeat=N))
    code = [(constant,) * N for constant in range(p)]
    checks = 0
    for base in words:
        for direction in words:
            e = min(
                sum(value != constant for value in direction)
                for constant in range(p)
            )
            options: list[list[int | None]] = []
            for slope in range(p):
                received = tuple(
                    (base[x] + slope * direction[x]) % p for x in range(N)
                )
                candidates: list[int | None] = [None]
                for explanation, word in enumerate(code):
                    support = tuple(
                        x for x in range(N) if received[x] == word[x]
                    )
                    if len(support) < m:
                        continue
                    contained = any(
                        all(
                            base[x] == first and direction[x] == second
                            for x in support
                        )
                        for first in range(p)
                        for second in range(p)
                    )
                    if not contained:
                        candidates.append(explanation)
                options.append(candidates)
            corrected = full_bound(N - K, m - K, K, 1, max(1, e - (N - m)))
            for choice in cartesian_product(*options):
                selected = [value for value in choice if value is not None]
                if len(selected) < 2 or len(set(selected)) < 2:
                    continue
                if len(selected) > corrected:
                    raise ValueError("rank-one toy violation")
                checks += 1
    return checks


def main() -> None:
    contract = json.loads((HERE / "source_contract.json").read_text())
    regression = contract["regression"]
    regression_bound = full_bound(99, 20, 1, 1, 1)
    if regression_bound != regression["corrected_bound"] or regression_bound == 23:
        raise ValueError("regression")

    endpoint_checks = 0
    wall_checks = 0
    for row in contract["rows"]:
        R, d, K, budget = (row[key] for key in ("R", "d", "K", "budget"))
        factors = [first_factor(R, d, K, q, budget) for q in range(1, K + 1)]
        if factors[row["unconditional_through_q"] - 1] != 1:
            raise ValueError("unconditional endpoint")
        if row["unconditional_through_q"] < K and factors[row["unconditional_through_q"]] == 1:
            raise ValueError("first conditional rank")
        for wall in row["walls"]:
            q, L = wall["q"], wall["minimum_L"]
            if factors[q - 1] != L:
                raise ValueError("factor")
            if full_bound(R, d, K, q, L) != wall["bound"]:
                raise ValueError("wall bound")
            if full_bound(R, d, K, q, L - 1) != wall["previous_bound"]:
                raise ValueError("adjacent wall")
            wall_checks += 1
        unpaid = row["unpaid"]
        if factors[unpaid["q"] - 1] != unpaid["required_L"]:
            raise ValueError("unpaid factor")
        if full_bound(R, d, K, unpaid["q"], d) != unpaid["maximum_L_bound"]:
            raise ValueError("unpaid maximum")
        endpoint_checks += sum(
            (K - q + 1) * (K - q + 2) // 2 for q in range(1, K + 1)
        )

    toy_checks = exhaustive_rank_one_toy()
    if toy_checks != 540:
        raise ValueError("toy census")
    print(
        "RATE_HALF_MCA_PROPER_SUBSPACE_OCCUPANCY_COMPILER_AUDIT_PASS "
        f"zero_normal_cases={endpoint_checks} walls={wall_checks} "
        f"regression={regression_bound} toy_selections={toy_checks}"
    )


if __name__ == "__main__":
    main()
