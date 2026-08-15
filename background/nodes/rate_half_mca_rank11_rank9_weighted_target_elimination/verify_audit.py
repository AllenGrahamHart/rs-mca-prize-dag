#!/usr/bin/env python3
"""Independent scope audit of the repaired rank-nine boundary."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "28cfa4f50ea4ffa9a61888148c3916b0638906117d6efdbd2a779d8f4a925d94"


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
    samples = [20617, 20618, 50000, 250000, 500000, 1048576]
    values = [ratio(p, k) for k in samples]
    require(values[0] < 1 < values[1], "adjacent crossing")
    require(all(a < b for a, b in zip(values, values[1:])), "sampled monotonicity")
    require(1048576 - 10 > 134944, "deleted core swallows original-row floor")
    require(1048576 - 20617 > 134944, "last-open deleted core")

    proof = (HERE / "proof.md").read_text()
    for pin in (
        "same `(record,T)` unit",
        "strictly increase",
        "J_deleted",
        "mixes two rows",
        "no row below",
    ):
        require(pin in proof, f"proof pin {pin}")
    require("134944<=|J|<m'" not in proof, "retracted inequality absent")
    print(
        "RATE_HALF_MCA_RANK11_RANK9_WEIGHTED_TARGET_ELIMINATION_AUDIT_PASS "
        f"samples={len(samples)} adjacent_crossing=20617/20618 "
        "scope_pins=5/5 reopened=10..20617"
    )


if __name__ == "__main__":
    main()
