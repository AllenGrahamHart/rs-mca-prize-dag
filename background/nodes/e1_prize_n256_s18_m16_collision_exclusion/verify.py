#!/usr/bin/env python3
"""Verify the prize N=256 profile-(4,2,0) cofactor-16 exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_m16_collision_exclusion"
PARENT = "e1_prize_n256_s18_m16_high_variance_exclusion"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
ENERGIES = list(range(5, 54, 4))
ENERGY_COUNTS = [0, 16, 16, 164, 208, 644, 1204, 15628, 3616, 29868, 35120, 415944, 37904]
B_PRIZE = 317494674775468773183020924238786383963
MAX_BELOW = 104797259883500113680505745049174573490076600644557179823872590464045041710081
MIN_ABOVE = 109148549668884138628080445927205579649397021264609510361461809939220006348801


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_region_counts() -> dict[str, dict[str, int]]:
    above = {9: 16, 13: 16, 17: 144, 21: 76, 25: 56}
    below = {
        17: 20,
        21: 132,
        25: 588,
        29: 1204,
        33: 15628,
        37: 3616,
        41: 29868,
        45: 35120,
        49: 415944,
        53: 37904,
    }
    return {
        str(energy): {
            "below": below.get(energy, 0),
            "inside": 0,
            "above": above.get(energy, 0),
        }
        for energy in ENERGIES
    }


def main() -> None:
    checks = 0
    pins = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    for key, value in pins.items():
        if key.endswith("_file"):
            assert digest(ROOT / value) == pins[key[:-5] + "_sha256"]
            checks += 1

    primary_census = json.loads(
        (ROOT / pins["primary_census_result_file"]).read_text()
    )
    audit_census = json.loads(
        (ROOT / pins["audit_census_result_file"]).read_text()
    )
    assert primary_census["complete"] is True and not primary_census["errors"]
    assert audit_census["complete"] is True and not audit_census["errors"]
    assert primary_census["totals"] == audit_census["totals"]
    assert primary_census["totals"]["combination_count"] == math.comb(126, 4)
    assert primary_census["totals"]["signed_vector_count"] == 32 * math.comb(126, 4)
    assert primary_census["totals"]["energy_counts"][:13] == ENERGY_COUNTS
    assert sum(ENERGY_COUNTS) == 540332
    checks += 7

    flint = json.loads((ROOT / pins["flint_result_file"]).read_text())
    pari = json.loads((ROOT / pins["pari_result_file"]).read_text())
    expected_counts = expected_region_counts()
    assert flint["complete"] is True and not flint["errors"]
    assert pari["complete"] is True and not pari["errors"]
    assert flint["row_count"] == pari["row_count"] == 540332
    assert flint["counts"] == pari["counts"] == expected_counts
    assert flint["fingerprint"] == pari["fingerprint"]
    assert pari["primary_match"] is True
    assert not flint["interval_rows"] and not pari["interval_rows"]
    assert len(flint["fingerprint"]) == 64
    assert sum(int(bucket["count"]) for bucket in flint["fingerprint"]) == 540332
    assert all(
        len(bucket[field]) == 64
        for bucket in flint["fingerprint"]
        for field in ("xor", "sum", "sum_square")
    )
    checks += 10 + 64 * 3

    lower = B_PRIZE * 2**128
    upper = (B_PRIZE + 1) * 2**128 - 1
    assert flint["prize_interval"] == [lower, upper]
    assert int(flint["maximum_below"]["candidate"]) == MAX_BELOW < lower
    assert int(pari["maximum_below"]["candidate"]) == MAX_BELOW
    assert int(flint["minimum_above"]["candidate"]) == MIN_ABOVE > upper
    assert int(pari["minimum_above"]["candidate"]) == MIN_ABOVE
    assert sum(row["above"] for row in expected_counts.values()) == 308
    assert sum(row["below"] for row in expected_counts.values()) == 540024
    checks += 7

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert all((NODE, target, "ev") in edges for target in TARGETS)
    checks += 3

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    proof = (ROOT / "background" / "nodes" / NODE / "proof.md").read_text()
    assert "all `540332` residual vectors" in statement
    assert "Every quotient `R/16` is outside" in statement
    assert "64-bucket" in proof
    checks += 3
    print(
        "E1_PRIZE_N256_S18_M16_COLLISION_EXCLUSION_PASS "
        f"rows={flint['row_count']} inside=0 checks={checks}"
    )


if __name__ == "__main__":
    main()
