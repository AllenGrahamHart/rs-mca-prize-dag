#!/usr/bin/env python3
"""Verify the prize N=256 profile-(4,2,0) cofactor-4 exclusion."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_m4_collision_exclusion"
PARENT = "e1_prize_n256_s18_m4_high_variance_exclusion"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
B_PRIZE = 317494674775468773183020924238786383963
MAX_BELOW = 107716387476569755844902778849041509815310757677547440774146432592221447900929
MIN_ABOVE = 110553665570163478885905819698234426068541015284212878175575978480389082393089
ENERGIES = list(range(5, 38, 4))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_region_counts() -> dict[str, dict[str, int]]:
    above = {9: 16, 13: 16, 17: 100, 21: 100, 25: 212, 29: 172, 33: 148, 37: 8}
    below = {21: 44, 25: 208, 29: 648, 33: 16936, 37: 2768}
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

    flint = json.loads((ROOT / pins["flint_result_file"]).read_text())
    pari = json.loads((ROOT / pins["pari_result_file"]).read_text())
    expected_counts = expected_region_counts()
    assert flint["complete"] is True and not flint["errors"]
    assert pari["complete"] is True and not pari["errors"]
    assert flint["returned_shards"] == pari["returned_shards"] == 32
    assert flint["row_count"] == pari["row_count"] == 21376
    assert flint["counts"] == pari["counts"] == expected_counts
    assert flint["fingerprint"] == pari["fingerprint"]
    assert pari["primary_match"] is True
    assert not flint["interval_rows"] and not pari["interval_rows"]
    assert len(flint["fingerprint"]) == 64
    assert sum(int(bucket["count"]) for bucket in flint["fingerprint"]) == 21376
    assert all(
        len(bucket[field]) == 64
        for bucket in flint["fingerprint"]
        for field in ("xor", "sum", "sum_square")
    )
    checks += 11 + 64 * 3

    lower = B_PRIZE * 2**128
    upper = (B_PRIZE + 1) * 2**128 - 1
    assert flint["prize_interval"] == [lower, upper]
    assert int(flint["maximum_below"]["candidate"]) == MAX_BELOW < lower
    assert int(pari["maximum_below"]["candidate"]) == MAX_BELOW
    assert int(flint["minimum_above"]["candidate"]) == MIN_ABOVE > upper
    assert int(pari["minimum_above"]["candidate"]) == MIN_ABOVE
    assert int(flint["maximum_below"]["norm"]) == 4 * MAX_BELOW
    assert int(flint["minimum_above"]["norm"]) == 4 * MIN_ABOVE
    assert sum(row["above"] for row in expected_counts.values()) == 772
    assert sum(row["below"] for row in expected_counts.values()) == 20604
    assert sum(sum(row.values()) for row in expected_counts.values()) == 21376
    checks += 10

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert all((NODE, target, "ev") in edges for target in TARGETS)
    checks += 3

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    proof = (ROOT / "background" / "nodes" / NODE / "proof.md").read_text()
    assert "all `21376` residual vectors" in statement
    assert "Every quotient `R/4` is" in statement
    assert "64 buckets" in proof
    checks += 3
    print(
        "E1_PRIZE_N256_S18_M4_COLLISION_EXCLUSION_PASS "
        f"rows={flint['row_count']} inside=0 checks={checks}"
    )


if __name__ == "__main__":
    main()
