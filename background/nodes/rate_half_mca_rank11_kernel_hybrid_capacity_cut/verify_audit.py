#!/usr/bin/env python3
"""Independent exact replay of the kernel hybrid capacity cut."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import prod
from pathlib import Path


HERE = Path(__file__).parent
CONTRACT_SHA256 = "ce3e5d908adba2db8ce0a12cd0f464d1d9b45b0602203f9f5a8adef7e0d51837"


def choose(n: int, r: int) -> int:
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return prod(range(n - r + 1, n + 1)) // prod(range(1, r + 1))


def fall(n: int, r: int) -> int:
    return prod(range(n - r + 1, n + 1))


def rise(n: int, r: int) -> int:
    return prod(range(n, n + r))


def local_cap(p: dict[str, int], k: int, d: int) -> int:
    if d == 9:
        return p["rank9_record_cap"]
    rank = 10 - d
    first = Fraction(fall(p["n_offset"] + k - rank, d + 1), (p["m_offset"] + k - rank) * rise(p["m_offset"] + 1, d - 1))
    second = Fraction(fall(p["n_offset"] + d, d + 1), rise(p["m_offset"] + 1, d))
    return int(first if first >= second else second)


def independent_terms(p: dict[str, int], k: int) -> list[tuple[int, int, str]]:
    rows = []
    for d in range(1, 10):
        rank = 10 - d
        extension = choose(k - 10, d + 1)
        ambient = choose(p["n_offset"] + k, rank) * local_cap(p, k, d) * extension // (d + 2)
        support = p["residual_record_floor"] * (choose(p["m_offset"] + k, rank) * extension // (d + 2))
        rows.append((ambient, support, "ambient" if ambient <= support else "record"))
    return rows


def independent_capacity(p: dict[str, int], k: int) -> int:
    return sum(min(a, r) for a, r, _ in independent_terms(p, k))


def independent_demand(p: dict[str, int], k: int) -> int:
    numerator = p["lane_density_numerator"] * p["residual_record_floor"] * choose(p["m_offset"] + k, 11)
    return -(-numerator // p["lane_density_denominator"])


def main() -> None:
    contract_path = HERE / "source_contract.json"
    if hashlib.sha256(contract_path.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise SystemExit("contract hash")
    p = json.loads(contract_path.read_text())["parameters"]
    checked = 0
    for k in range(10, 11773):
        if independent_demand(p, k) <= independent_capacity(p, k):
            raise SystemExit(f"capacity reversal at {k}")
        checked += 1
    branches = [choice for _, _, choice in independent_terms(p, 11772)]
    if branches != p["endpoint_branch_pattern"]:
        raise SystemExit("branch reconstruction")
    gap = independent_demand(p, 11772) - independent_capacity(p, 11772)
    wall_excess = independent_capacity(p, 11773) - independent_demand(p, 11773)
    if gap != p["endpoint_gap"] or wall_excess != p["wall_excess"]:
        raise SystemExit("boundary reconstruction")
    proof = (HERE / "proof.md").read_text()
    pins = ("nonincreasing in `R_actual`", "R_actual>=N_min", "per-corank minimum", "11,763 rows")
    if not all(pin in proof for pin in pins):
        raise SystemExit("proof pins")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_HYBRID_CAPACITY_CUT_AUDIT_PASS "
        f"checked={checked} branches=AARRRRRRR endpoint_gap={gap} "
        f"wall_excess={wall_excess} proof_pins={len(pins)}/{len(pins)}"
    )


if __name__ == "__main__":
    main()
