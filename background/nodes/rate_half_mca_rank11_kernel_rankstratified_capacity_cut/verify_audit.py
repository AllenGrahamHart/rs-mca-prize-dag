#!/usr/bin/env python3
"""Independent audit of the kernel rank-capacity interval."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "9fffc92c3682c65db6ac6c1f4b4fc7509c14516f41f2d9c7ebfe8750a7760312"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def fall(value: int, length: int) -> int:
    return prod(value - offset for offset in range(length))


def rise(value: int, length: int) -> int:
    return prod(value + offset for offset in range(length))


def cap_for_rank(p: dict[str, int], kprime: int, rank: int) -> int:
    d = 10 - rank
    if d == 9:
        records = p["rank9_record_cap"]
    else:
        j = kprime - rank
        a = Fraction(fall(p["n_offset"] + j, d + 1), (p["m_offset"] + j) * rise(p["m_offset"] + 1, d - 1))
        b = Fraction(fall(p["n_offset"] + d, d + 1), rise(p["m_offset"] + 1, d))
        q = max(a, b)
        records = q.numerator // q.denominator
    extras = kprime - 10
    extensions = comb(extras, d + 1) if extras >= d + 1 else 0
    return comb(p["n_offset"] + kprime, rank) * records * extensions


def comparison(p: dict[str, int], kprime: int) -> tuple[int, int]:
    demand_num = p["lane_density_numerator"] * p["residual_record_floor"] * comb(p["m_offset"] + kprime, 11)
    capacity_value = sum(cap_for_rank(p, kprime, rank) for rank in range(9, 0, -1))
    return demand_num, p["lane_density_denominator"] * capacity_value


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    p = json.loads(CONTRACT.read_text())["parameters"]
    checked = 0
    minimum_cross_gap = None
    for kprime in range(10, 4599):
        demand_num, capacity_num = comparison(p, kprime)
        gap = demand_num - capacity_num
        require(gap > 0, f"closed interval {kprime}")
        minimum_cross_gap = gap if minimum_cross_gap is None else min(minimum_cross_gap, gap)
        checked += 1
    wall_demand, wall_capacity = comparison(p, 4599)
    require(wall_demand < wall_capacity, "wall reversal")
    proof = (HERE / "proof.md").read_text()
    for pin in ("canonical rank basis", "C(n',r)", "K'=4598", "K'=4599"):
        require(pin in proof, f"proof pin {pin}")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_RANKSTRATIFIED_CAPACITY_CUT_AUDIT_PASS "
        f"checked={checked} min_cross_gap={minimum_cross_gap} proof_pins=4/4"
    )


if __name__ == "__main__":
    main()
