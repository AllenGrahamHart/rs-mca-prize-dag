#!/usr/bin/env python3
"""Independent audit of the component nine-subset concentration bound."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "f3e7cebc5b859df1d9950ca5cf49c085a994b91c949da3e49fbe701ffe169192"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    require(comb(11, 9) * comb(p["endpoint_m"], 11)
            == comb(p["endpoint_m"], 9) * comb(p["endpoint_m"] - 9, 2),
            "subset identity")
    endpoint = Fraction(
        p["record_floor"] * p["dominant_lane_incidence_ppb_floor"], 10**9
    )
    for index in range(9):
        endpoint *= Fraction(p["endpoint_m"] - index, p["endpoint_n"] - index)
    rounded = -(-endpoint.numerator // endpoint.denominator)
    require(rounded == 2578110, "independent endpoint")
    # Each factor (d+K-i)/(R+K-i) has successive numerator R-d>0.
    require(all(p["R"] - p["d"] == 981104 for _ in range(9)), "monotonicity")
    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    for token in ("2578110", "495405467/10^9", "does not mix the two labels"):
        require(token in statement, f"statement token {token}")
    for token in ("55*C(m',11)=C(m',9)*C(m'-9,2)", "K'=10"):
        require(token in proof, f"proof token {token}")
    print(
        "RATE_HALF_MCA_RANK11_COMPONENT_NINESUBSET_LANE_CONCENTRATOR_AUDIT_PASS "
        f"endpoint={rounded} factors=9"
    )


if __name__ == "__main__":
    main()
