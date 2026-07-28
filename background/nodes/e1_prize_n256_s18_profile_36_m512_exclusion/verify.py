#!/usr/bin/env python3
"""Verify the profile-(3,6) cofactor-512 exclusion."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_profile_36_m512_exclusion"
PARENT = "e1_prize_n256_s18_profile_36_bounded_product_windows"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
EXPECTED = {
    "orbits": 2912,
    "sign_assignments": 93184,
    "triple_candidates": 438120,
    "exact_sign_tests": 3504960,
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
        assert row["returncode"] == 0 and not row["stderr"]
        for key, value in re.findall(r"([a-z_0-9]+)=([0-9]+)", row["stdout"]):
            counts[key] += int(value)
    return counts


def parse_candidates(result: dict) -> list[tuple[int, tuple[tuple[int, int], ...]]]:
    found = []
    for row in result["rows"]:
        for energy, encoded in re.findall(r"CANDIDATE E=(\d+) state=([^\n]+)", row["stdout"]):
            state = tuple(
                (int(position), int(coefficient))
                for position, coefficient in re.findall(r"(\d+):(-?\d+),", encoded)
            )
            found.append((int(energy), state))
    return sorted(found)


def autocorrelation_energy(state: tuple[tuple[int, int], ...]) -> int:
    values = [0] * 64
    for index, (left, left_value) in enumerate(state):
        for right, right_value in state[index + 1 :]:
            delta = right - left
            if delta < 64:
                values[delta] += left_value * right_value
            elif delta > 64:
                values[128 - delta] -= left_value * right_value
    return sum(value * value for value in values)


def main() -> None:
    node_dir = ROOT / "background/nodes" / NODE
    pin = json.loads((node_dir / "source_pin.json").read_text())
    for key in (
        "parent_statement", "parent_proof", "orbit_classifier", "orbit",
        "base_engine", "radius_engine", "radius_launcher", "primary_result",
        "audit_result", "norm_launcher", "norm_result",
    ):
        assert sha256(ROOT / pin[f"{key}_file"]) == pin[f"{key}_sha256"]

    residue_patterns = []
    for weight in (2, 4, 6):
        for residues in combinations(range(16), weight):
            if multiplicity(residues) == 9:
                residue_patterns.append(residues)
    assert len(residue_patterns) == 16
    assert all(len(pattern) == 4 for pattern in residue_patterns)
    assert all(any((right - left) % 2 for left, right in combinations(pattern, 2)) for pattern in residue_patterns)

    orbit_data = json.loads((ROOT / pin["orbit_file"]).read_text())
    assert orbit_data["examined"] == 10009125 and orbit_data["mu9"] == 46592
    assert orbit_data["orbit_weights"] == {
        "6": 8, "7": 48, "8": 64, "9": 208, "10": 136,
        "11": 656, "12": 64, "13": 368, "14": 208, "15": 1152,
    }
    orbits = [tuple(orbit) for orbit in orbit_data["orbits"]]
    assert len(orbits) == orbit_data["affine_orbits"] == 2912
    for orbit in orbits:
        assert multiplicity(orbit) == 9 and 6 <= odd_chords(orbit).bit_count() <= 15
        assert canonical(orbit) == orbit

    primary = json.loads((ROOT / pin["primary_result_file"]).read_text())
    audit = json.loads((ROOT / pin["audit_result_file"]).read_text())
    assert primary["engine"] == "pair-radius-plus-third"
    assert audit["engine"] == "triple-radius"
    assert primary["orbit_file_sha256"] == audit["orbit_file_sha256"] == pin["orbit_sha256"]
    primary_counts = parse_counts(primary)
    audit_counts = parse_counts(audit)
    for key, value in EXPECTED.items():
        assert primary_counts[key] == audit_counts[key] == value
    assert primary_counts["xor_probes"] == 2198607872
    assert audit_counts["xor_probes"] == 18021376
    for energy in range(2, 18):
        expected = 2 if energy in (15, 17) else 0
        assert primary_counts[f"energy{energy}"] == audit_counts[f"energy{energy}"] == expected
    candidates = parse_candidates(primary)
    assert candidates == parse_candidates(audit) and len(candidates) == 4
    for energy, state in candidates:
        assert autocorrelation_energy(state) == energy
        singleton_support = tuple(position for position, value in state if abs(value) == 1)
        assert multiplicity(singleton_support) == 9

    norms = json.loads((ROOT / pin["norm_result_file"]).read_text())
    assert norms["complete"] is True and norms["agreement"] is True
    assert norms["candidates"] == len(candidates) == 4
    assert norms["primary_sha256"] == pin["primary_result_sha256"]
    assert norms["audit_sha256"] == pin["audit_result_sha256"]
    assert len({int(row["norm"]) for row in norms["rows"]}) == 2
    for row in norms["rows"]:
        norm = int(row["norm"])
        assert row["flint_pari_agree"] is True
        assert row["valuation"] == 9
        assert norm % 512 == 0 and int(row["quotient"]) == norm // 512
        assert row["quotient_relation"] == "below" and norm // 512 < P_MIN

    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    for text in ("m=512", "four normalized", "eight"):
        assert text in statement.lower()
    for text in ("2198607872", "3504960", "Norm(F)/512"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (PARENT, NODE, "req") in edges
    assert all((NODE, target, "ev") in edges for target in TARGETS)

    print(
        "E1_PRIZE_N256_S18_PROFILE_36_M512_EXCLUSION_PASS "
        f"orbits={len(orbits)} candidates={len(candidates)} distinct_norms=2"
    )


if __name__ == "__main__":
    main()
