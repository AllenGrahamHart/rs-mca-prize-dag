#!/usr/bin/env python3
"""Independent audit of the rank-eight weighted capacity crossing."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "569188006da1752dc9013db7947f3ade77fdc330eb947f57589f16d3e6ad74b1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def ceiling(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    p = json.loads(CONTRACT.read_text())["parameters"]
    rows = []
    for kprime in (p["last_open_dimension"], p["first_closed_dimension"]):
        nprime = p["n_offset"] + kprime
        mprime = p["m_offset"] + kprime
        lower = Fraction(
            55 * p["component_ppb"] * p["record_floor"] * comb(mprime, 11),
            p["ppb_denominator"] * comb(nprime, 9),
        )
        upper = (nprime - mprime + 1) * (nprime - 9) * (nprime - 10) // 2
        rows.append((ceiling(lower), upper, lower > upper))
    require(rows[0] == (p["last_open_demand"], p["last_open_cap"], False), "last row")
    require(rows[1] == (p["first_closed_demand"], p["first_closed_cap"], True), "first row")
    for index in range(11):
        kprime = p["first_closed_dimension"]
        nprime = p["n_offset"] + kprime
        mprime = p["m_offset"] + kprime
        require(
            Fraction(mprime + 1 - index, nprime + 1 - index)
            > Fraction(mprime - index, nprime - index),
            f"monotone factor {index}",
        )
    proof = (HERE / "proof.md").read_text()
    for pin in ("C(n',9)C(n'-9,2)=55C(n',11)", "strictly increases", "37995"):
        require(pin in proof, f"proof pin {pin}")
    print(
        "RATE_HALF_MCA_RANK11_RANK8_WEIGHTED_CAPACITY_CUT_AUDIT_PASS "
        f"last_gap={rows[0][1]-rows[0][0]} first_gap={rows[1][0]-rows[1][1]} "
        "monotone_factors=11/11 proof_pins=3/3"
    )


if __name__ == "__main__":
    main()
