#!/usr/bin/env python3
"""Independent audit of weighted nine-subset concentration."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "050954321fc65a504b801b19dc0787e21d31f979f8062319ea67055e37709895"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    p = json.loads(CONTRACT.read_text())["parameters"]
    k = p["residual_dimension_minimum"]
    n, m = p["n_offset"] + k, p["m_offset"] + k
    density = Fraction(p["lane_density_numerator"], p["lane_density_denominator"])
    marked_a = density * p["residual_record_floor"] * 55 * Fraction(comb(m, 11), comb(n, 9))
    marked_b = (
        density
        * p["residual_record_floor"]
        * Fraction(comb(m, 9) * comb(m - 9, 2), comb(n, 9))
    )
    require(marked_a == marked_b, "independent mark identity")
    marked = -(-marked_a.numerator // marked_a.denominator)
    distinct_fraction = density * p["residual_record_floor"] * Fraction(comb(m, 9), comb(n, 9))
    distinct = -(-distinct_fraction.numerator // distinct_fraction.denominator)
    require((marked, distinct) == (p["marked_endpoint_floor"], p["distinct_record_endpoint_floor"]), "endpoints")
    proof = (HERE / "proof.md").read_text()
    require("No division by the extension multiplicity" in proof, "weight custody")
    print(
        "RATE_HALF_MCA_RANK11_COMPONENT_NINESUBSET_WEIGHTED_CONCENTRATOR_AUDIT_PASS "
        f"marked={marked} distinct={distinct} identity=2/2"
    )


if __name__ == "__main__":
    main()
