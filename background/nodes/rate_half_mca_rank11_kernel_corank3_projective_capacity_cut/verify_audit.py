#!/usr/bin/env python3
"""Independent endpoint and custody audit for the corank-three cut."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
ROOT = Path(__file__).resolve().parents[3]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def record_cap(kprime: int, d: int, p: dict[str, object]) -> int:
    if d <= 3:
        return int(p[f"projective_corank{d}_record_cap"])
    if d == 9:
        return int(p["rank9_record_cap"])
    rank = 10 - d
    shortened = kprime - rank
    n0, m0 = int(p["n_offset"]), int(p["m_offset"])
    return int(max(
        Fraction(
            falling(n0 + shortened, d + 1),
            (m0 + shortened) * rising(m0 + 1, d - 1),
        ),
        Fraction(falling(n0 + d, d + 1), rising(m0 + 1, d)),
    ))


def caps(kprime: int, p: dict[str, object]) -> list[Fraction]:
    nprime = int(p["n_offset"]) + kprime
    mprime = int(p["m_offset"]) + kprime
    residual = int(p["residual_record_floor"])
    answer = []
    for d in range(1, 10):
        extension = comb(kprime - 10, d + 1)
        ambient = Fraction(
            comb(nprime, 10 - d) * record_cap(kprime, d, p) * extension // (d + 2),
            residual,
        )
        support = Fraction(comb(mprime, 10 - d) * extension // (d + 2))
        answer.append(min(ambient, support))
    return answer


def ratio(kprime: int, step: int, source: int, p: dict[str, object]) -> Fraction:
    raising = Fraction(
        comb(source + 2, step) * comb(int(p["m_offset"]) + source, step),
        comb(kprime - source - 11 + step, step),
    )
    return Fraction(comb(9 - source + step, step), raising)


def direct_row(kprime: int, p: dict[str, object]) -> dict[str, object]:
    limits = caps(kprime, p)
    allocation = [Fraction(0) for _ in range(9)]
    allocation[0], allocation[1], allocation[2] = limits[0], limits[1], limits[2]
    allocation[3] = ratio(kprime, 2, 4, p) * limits[1]
    for source in range(5, 10):
        allocation[source - 1] = ratio(kprime, source - 3, source, p) * limits[2]
    require(all(0 < value <= limit for value, limit in zip(allocation, limits)), "caps")

    tight = []
    for step in range(2, 9):
        for source in range(step + 1, 10):
            left = allocation[source - 1]
            right = ratio(kprime, step, source, p) * allocation[source - step - 1]
            require(left <= right, "hierarchy")
            if left == right:
                tight.append([step, source])
    require(tight == p["tight_hierarchy_rows"], "tight rows")

    optimum = sum(allocation, Fraction(0))
    mprime = int(p["m_offset"]) + kprime
    demand = Fraction(
        int(p["lane_density_numerator"]) * comb(mprime, 11),
        int(p["lane_density_denominator"]),
    )
    scaled_demand = int(p["residual_record_floor"]) * demand
    integer_demand = -(-scaled_demand.numerator // scaled_demand.denominator)
    scaled_capacity = int(p["residual_record_floor"]) * optimum
    integer_capacity = scaled_capacity.numerator // scaled_capacity.denominator
    return {
        "optimum_numerator": optimum.numerator,
        "optimum_denominator": optimum.denominator,
        "integer_demand": integer_demand,
        "integer_capacity": integer_capacity,
        "signed_gap": integer_demand - integer_capacity,
        "tight": tight,
    }


def expected(p: dict[str, object], prefix: str, wall: bool = False) -> dict[str, object]:
    return {
        "optimum_numerator": p[f"{prefix}_optimum_numerator"],
        "optimum_denominator": p[f"{prefix}_optimum_denominator"],
        "integer_demand": p[f"{prefix}_demand_ceiling"],
        "integer_capacity": p[f"{prefix}_capacity"],
        "signed_gap": -p["wall_excess"] if wall else p[f"{prefix}_gap"],
        "tight": p["tight_hierarchy_rows"],
    }


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p, evidence = data["parameters"], data["evidence"]
    endpoint_specs = (
        (p["replay_minimum"], "replay_start", False),
        (p["closed_dimension_maximum"], "endpoint", False),
        (p["first_open_dimension"], "wall", True),
    )
    for kprime, prefix, wall in endpoint_specs:
        require(direct_row(kprime, p) == expected(p, prefix, wall), f"endpoint {kprime}")

    result = json.loads((ROOT / evidence["result"]).read_text())
    require(result["complete"] is True and result["error"] is None, "completion")
    require(result["tree"] == p["dual_forest"], "forest")
    require(result["checked_rows"] == p["checked_rows_including_wall"], "row count")
    cursor = p["replay_minimum"]
    checked = 0
    endpoints = []
    for chunk in sorted(result["chunks"], key=lambda item: item["start"]):
        require(chunk["start"] == cursor, "chunk continuity")
        require(chunk["checked"] == chunk["end"] - chunk["start"], "chunk width")
        cursor = chunk["end"]
        checked += chunk["checked"]
        endpoints.extend(chunk["endpoint_rows"])
    require(cursor == p["first_open_dimension"] + 1, "final cursor")
    require(checked == p["checked_rows_including_wall"], "complete rows")
    require(sorted(endpoints, key=lambda item: item["kprime"]) == result["endpoint_rows"], "endpoint custody")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_CORANK3_PROJECTIVE_CAPACITY_CUT_AUDIT_PASS "
        f"checked={checked} endpoints={len(endpoints)} chunks={len(result['chunks'])}"
    )


if __name__ == "__main__":
    main()
