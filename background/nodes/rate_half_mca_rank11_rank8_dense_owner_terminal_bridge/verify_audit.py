#!/usr/bin/env python3
"""Independent audit of the rank-eight dense-owner bridge."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "c77779cfc39566264dbfa48bfe4081eb6c46a4913c579e21e1bcf204de13da67"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def ceiling(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    p = json.loads(CONTRACT.read_text())["parameters"]
    signed_rows = []
    for kprime in (p["last_unforced_dimension"], p["first_forced_dimension"]):
        nprime = p["n_offset"] + kprime
        mprime = p["m_offset"] + kprime
        lower = Fraction(
            55 * p["component_ppb"] * p["record_floor"] * comb(mprime, 11),
            p["ppb_denominator"] * comb(nprime, 9),
        )
        pairs = (nprime - 9) * (nprime - 10) // 2
        signed_rows.append((ceiling(lower), pairs, ceiling(lower) - 200631 * pairs, lower - 200631 * pairs))
    require(signed_rows[0][2] == -p["last_unforced_deficit"], "last rounded sign")
    require(signed_rows[0][3] <= 0, "last raw sign")
    require(signed_rows[1][2] == p["first_forced_excess"], "first rounded sign")
    require(signed_rows[1][3] > 0, "first raw sign")
    require(1 + 981104 // 5 == p["delta5_record_cap"] < p["owner_record_target"], "deficiency cut")
    proof = (HERE / "proof.md").read_text()
    for pin in ("sum_p t_p q_p", "200631*Q", "C(m',11)/C(n',11)", "delta>=5", "chronology"):
        require(pin in proof, f"proof pin {pin}")
    print(
        "RATE_HALF_MCA_RANK11_RANK8_DENSE_OWNER_TERMINAL_BRIDGE_AUDIT_PASS "
        f"last_deficit={-signed_rows[0][2]} first_excess={signed_rows[1][2]} "
        "proof_pins=5/5"
    )


if __name__ == "__main__":
    main()
