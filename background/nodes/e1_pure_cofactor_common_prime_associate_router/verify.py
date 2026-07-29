#!/usr/bin/env python3
"""Verify wiring and source custody for the pure-cofactor associate router."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_pure_cofactor_common_prime_associate_router"
TARGET = "e1_official_low_square_mass_pair_budget"
EDGE_CAP = 65127585921474870475467050631501738502567
PROFILE_WEIGHT = 1386246316188473270092082114587711840
SUPPLIERS = (
    "e1_pair_feasible_prime_field_reduction",
    "e1_low_square_mass_weighted_kernel_dictionary",
    "e1_prize_n256_s18_profile_36_cofactor_windows",
    "e1_prize_n256_s18_profile_36_m1538_exclusion",
    "e1_prize_n256_s18_profile_36_m1024_exclusion",
    "e1_prize_n256_s18_profile_36_m1028_exclusion",
    "e1_prize_n256_s18_profile_36_m512_exclusion",
    "e1_prize_n256_s18_profile_36_m514_exclusion",
    "e1_prize_n256_s18_profile_36_m256_exclusion",
    "e1_prize_n256_s18_profile_36_m64_exclusion",
    "e1_prize_n256_s18_profile_36_m32_exclusion",
    "e1_prize_n256_s18_profile_36_m16_one_division_exclusion",
    "e1_prize_n256_s18_profile_36_m16_two_divisions_exclusion",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    checks = 0
    pins = json.loads((Path(__file__).with_name("source_pin.json")).read_text())
    for key, value in pins.items():
        if key.endswith("_file"):
            prefix = key[:-5]
            assert digest(ROOT / value) == pins[f"{prefix}_sha256"]
            checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[TARGET]["status"] == "TARGET"
    for supplier in SUPPLIERS:
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    assert (NODE, TARGET, "ev") in edges
    assert (NODE, TARGET, "req") not in edges
    checks += 4

    statement = (Path(__file__).with_name("statement.md")).read_text()
    assert "m in {2,4,8,16}" in statement
    assert "unit associates" in statement
    contract = (Path(__file__).with_name("claim_contract.md")).read_text()
    assert "arbitrary algebraic unit" in contract
    assert "cyclotomic-unit subgroup is not proved" in contract
    assert "not a count" in statement
    assert [2013 // 2**mu for mu in range(1, 5)] == [1006, 503, 251, 125]
    assert "floor(18^64/(2^mu p))" in statement
    assert "sqrt(128 D_(mu,p))" in statement
    assert "rank `63`" in statement
    assert "kernel exactly the 256" in statement
    assert 2 * EDGE_CAP // PROFILE_WEIGHT == 93962
    assert PROFILE_WEIGHT * 93962 <= 2 * EDGE_CAP
    assert PROFILE_WEIGHT * 93963 > 2 * EDGE_CAP
    assert 367 * 256 == 93952 < 93962 < 94208 == 368 * 256
    assert "T_36(p,r)<=367" in statement
    assert "not sufficient" in statement
    checks += 16

    print(
        "E1_PURE_COFACTOR_COMMON_PRIME_ASSOCIATE_ROUTER_PASS "
        f"suppliers={len(SUPPLIERS)} checks={checks}"
    )


if __name__ == "__main__":
    main()
