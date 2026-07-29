#!/usr/bin/env python3
"""Verify wiring and source custody for the pure-cofactor associate router."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_pure_cofactor_common_prime_associate_router"
TARGET = "e1_official_low_square_mass_pair_budget"
SUPPLIERS = (
    "e1_pair_feasible_prime_field_reduction",
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
    assert "arbitrary cyclotomic unit" in statement
    assert "not a count" in statement
    assert [2013 // 2**mu for mu in range(1, 5)] == [1006, 503, 251, 125]
    assert "floor(18^64/(2^mu p))" in statement
    checks += 5

    print(
        "E1_PURE_COFACTOR_COMMON_PRIME_ASSOCIATE_ROUTER_PASS "
        f"suppliers={len(SUPPLIERS)} checks={checks}"
    )


if __name__ == "__main__":
    main()
