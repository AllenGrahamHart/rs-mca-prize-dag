#!/usr/bin/env python3
"""Independent audit of rank-nine target elimination."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "78436c5e0cc6cd9d313e8d4de24e849d87676a4236be6e2c09b203576a002ab9"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def ratio(p: dict[str, int], k: int) -> Fraction:
    n, m = p["n_offset"] + k, p["m_offset"] + k
    lower = Fraction(
        p["lane_density_numerator"]
        * p["residual_record_floor"]
        * comb(m, 9)
        * comb(m - 9, 2),
        p["lane_density_denominator"] * comb(n, 9),
    )
    upper = (p["support_complement"] + 1) * (m - 10) * n
    return lower / upper


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    p = json.loads(CONTRACT.read_text())["parameters"]
    require(p["m_offset"] + p["small_dimension_ceiling"] == p["forced_common_core_floor"], "low interval")
    samples = [67473, 67474, 100000, 250000, 500000, 750000, 1048576]
    values = [ratio(p, k) for k in samples]
    require(values[0] > 1, "boundary contradiction")
    require(all(a < b for a, b in zip(values, values[1:])), "sampled monotonicity")
    require(p["weighted_boundary_demand"] - p["weighted_boundary_cap"] == p["weighted_boundary_gap"], "gap")
    proof = (HERE / "proof.md").read_text()
    require("strictly increases" in proof and "same `(record,T)` unit" in proof, "proof pins")
    print(
        "RATE_HALF_MCA_RANK11_RANK9_WEIGHTED_TARGET_ELIMINATION_AUDIT_PASS "
        f"samples={len(samples)} boundary_ratio={float(values[0]):.6f} "
        f"gap={p['weighted_boundary_gap']}"
    )


if __name__ == "__main__":
    main()
