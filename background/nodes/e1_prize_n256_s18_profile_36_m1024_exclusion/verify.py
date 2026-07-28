#!/usr/bin/env python3
"""Verify the profile-(3,6) cofactor-1024 exclusion."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_profile_36_m1024_exclusion"
PARENT = "e1_prize_n256_s18_profile_36_sharp_product_window"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
EXPECTED = {
    "orbits": 68,
    "sign_assignments": 2176,
    "targets": 194816,
    "triple_candidates": 606,
    "exact_sign_tests": 4848,
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def multiplicity(support: tuple[int, ...], limit: int = 16) -> int:
    for derivative in range(limit):
        if sum((derivative & ~exponent) == 0 for exponent in support) % 2:
            return derivative
    return limit


def odd_chords(support: tuple[int, ...]) -> int:
    mask = 0
    for index, left in enumerate(support):
        for right in support[index + 1 :]:
            delta = right - left
            if delta == 64:
                continue
            lag = delta if delta < 64 else 128 - delta
            mask ^= 1 << lag
    return mask


def canonical(support: tuple[int, ...]) -> tuple[int, ...]:
    return min(
        tuple(sorted(unit * ((value - origin) % 128) % 128 for value in support))
        for origin in support
        for unit in range(1, 128, 2)
    )


def parse_counts(result: dict) -> Counter[str]:
    counts: Counter[str] = Counter()
    for row in result["rows"]:
        assert row["returncode"] == 0 and not row["stderr"] and row["mu"] == 10
        for key, value in re.findall(r"([a-z_]+)=([0-9]+)", row["stdout"]):
            counts[key] += int(value)
    return counts


def main() -> None:
    node_dir = ROOT / "background/nodes" / NODE
    pin = json.loads((node_dir / "source_pin.json").read_text())
    for key in (
        "parent_statement", "parent_proof", "orbit_classifier", "orbit",
        "exact_engine", "modal_launcher", "primary_result", "audit_result",
    ):
        assert sha256(ROOT / pin[f"{key}_file"]) == pin[f"{key}_sha256"]

    residue_patterns = []
    for weight in (2, 4, 6):
        for residues in combinations(range(16), weight):
            if multiplicity(residues) == 10:
                residue_patterns.append(residues)
    assert len(residue_patterns) == 8
    assert all(len(pattern) == 4 for pattern in residue_patterns)
    assert all(
        any((right - left) % 4 == 2 for left, right in combinations(pattern, 2))
        for pattern in residue_patterns
    )

    orbit_data = json.loads((ROOT / pin["orbit_file"]).read_text())
    assert orbit_data["examined"] == 10009125
    assert orbit_data["multiplicity_counts"]["10"] == 32256
    target = orbit_data["targets"]["10"]
    assert target["retained"] == {"2": 32, "3": 112, "4": 96, "5": 336, "6": 224}
    orbits = [tuple(orbit) for orbit in target["orbits"]]
    assert len(orbits) == target["affine_orbits"] == 68
    assert len(set(orbits)) == len(orbits)
    for orbit in orbits:
        assert multiplicity(orbit) == 10
        assert 2 <= odd_chords(orbit).bit_count() <= 6
        assert canonical(orbit) == orbit

    primary = json.loads((ROOT / pin["primary_result_file"]).read_text())
    audit = json.loads((ROOT / pin["audit_result_file"]).read_text())
    assert primary["engine"] == "pair-xor-plus-third"
    assert audit["engine"] == "triple-xor"
    assert primary["multiplicities"] == audit["multiplicities"] == [10]
    assert primary["orbit_file_sha256"] == audit["orbit_file_sha256"] == pin["orbit_sha256"]
    primary_counts = parse_counts(primary)
    audit_counts = parse_counts(audit)
    for key, value in EXPECTED.items():
        assert primary_counts[key] == audit_counts[key] == value
    assert primary_counts["xor_probes"] == EXPECTED["targets"] * 122
    assert audit_counts["xor_probes"] == EXPECTED["targets"]

    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    for text in ("m=1024", "{2,3,4,5,6}", "ten"):
        assert text in statement.lower()
    for text in ("10009125", "194816", "4848"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (PARENT, NODE, "req") in edges
    assert all((NODE, target_node, "ev") in edges for target_node in TARGETS)

    print(
        "E1_PRIZE_N256_S18_PROFILE_36_M1024_EXCLUSION_PASS "
        f"orbits={len(orbits)} targets={EXPECTED['targets']} candidates={EXPECTED['triple_candidates']}"
    )


if __name__ == "__main__":
    main()
