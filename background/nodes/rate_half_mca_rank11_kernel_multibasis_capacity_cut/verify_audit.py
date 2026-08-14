#!/usr/bin/env python3
"""Independent exact replay of the kernel multi-basis capacity cut."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import prod
from pathlib import Path


HERE = Path(__file__).parent
CONTRACT_SHA256 = "47cd5f4ee795bc82161711e65e1fdbfd70cc86d0947854a4ed9aa320508b8a64"


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
    bound = first if first >= second else second
    return bound.numerator // bound.denominator


def independent_capacity(p: dict[str, int], k: int) -> int:
    total = 0
    for d in range(1, 10):
        decorated = choose(p["n_offset"] + k, 10 - d) * local_cap(p, k, d) * choose(k - 10, d + 1)
        total += decorated // (d + 2)
    return total


def independent_demand(p: dict[str, int], k: int) -> int:
    numerator = p["lane_density_numerator"] * p["residual_record_floor"] * choose(p["m_offset"] + k, 11)
    return -(-numerator // p["lane_density_denominator"])


def main() -> None:
    contract_path = HERE / "source_contract.json"
    if hashlib.sha256(contract_path.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise SystemExit("contract hash")
    data = json.loads(contract_path.read_text())
    p = data["parameters"]
    if p["basis_multiplicities"] != [d + 2 for d in range(1, 10)]:
        raise SystemExit("multiplicity reconstruction")
    checked = 0
    for k in range(10, 11642):
        if independent_demand(p, k) <= independent_capacity(p, k):
            raise SystemExit(f"capacity reversal at {k}")
        checked += 1
    end_gap = independent_demand(p, 11641) - independent_capacity(p, 11641)
    wall_excess = independent_capacity(p, 11642) - independent_demand(p, 11642)
    if end_gap != p["endpoint_gap"] or wall_excess != p["wall_excess"]:
        raise SystemExit("boundary reconstruction")
    proof = (HERE / "proof.md").read_text()
    pins = ("d+2", "integer floors", "11,632 rows", "comparison reverses")
    if not all(pin in proof for pin in pins):
        raise SystemExit("proof pins")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_MULTIBASIS_CAPACITY_CUT_AUDIT_PASS "
        f"checked={checked} endpoint_gap={end_gap} wall_excess={wall_excess} "
        f"proof_pins={len(pins)}/{len(pins)}"
    )


if __name__ == "__main__":
    main()
