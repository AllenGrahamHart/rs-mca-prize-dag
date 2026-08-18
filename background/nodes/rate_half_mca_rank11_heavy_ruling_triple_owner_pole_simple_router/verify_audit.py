#!/usr/bin/env python3
"""Independent audit of the triple-owner pole-simple router."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "ce7ac51d33075bca9d5913e1b127a8ed598cd2a6b30bd50894fd2b8b975ae1f5"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256
    data = json.loads(CONTRACT.read_text())
    mass, q4 = data["orientation_mass"], data["pair_type_cap"]
    low = 2 * q4
    triple = mass - low
    capacity = data["rank_two_pair_type_cap"] * data["fixed_pair_multiplicity"]
    total = capacity + low
    gap = mass - total
    dense = (triple + q4 - 1) // q4
    assert (low, triple, capacity, total, gap, dense) == (
        116722,
        322359637,
        236448715,
        236565437,
        85910922,
        5524,
    )
    for t in range(1, data["maximum_additional_pair_types"] + 1):
        anchor = data["seed_size"] - data["records_per_additional_pair"] * t
        assert anchor >= 20
        assert data["records_per_additional_pair"] - 1 >= 2
    surplus = data["agreement_excess"] - 2 * data["pair_core_margin"] + 1
    assert surplus == 67451
    assert data["maximum_common_poles"] == 0
    assert data["maximum_supports_per_denominator_root"] == 1
    assert (
        data["denominator_degree_maximum"]
        * data["maximum_supports_per_denominator_root"]
        == data["maximum_denominator_root_support_incidences"]
        == 67472
    )
    proof = Path(__file__).with_name("proof.md").read_text().lower()
    assert "every represented pair contributes three" in proof
    assert "at most one\nselected support" in proof
    assert "does not make `q` root-free" in Path(__file__).with_name("audit.md").read_text().lower()
    print(
        "RANK11_TRIPLE_OWNER_POLE_SIMPLE_AUDIT_PASS "
        f"mass={triple} gap={gap} dense={dense} root_surplus={surplus}"
    )


if __name__ == "__main__":
    main()
