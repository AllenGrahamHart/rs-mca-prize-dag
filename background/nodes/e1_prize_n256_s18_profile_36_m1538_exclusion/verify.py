#!/usr/bin/env python3
"""Verify the profile-(3,6) cofactor-1538 exclusion certificate."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_profile_36_m1538_exclusion"
PARENT = "e1_prize_n256_s18_profile_36_cofactor_windows"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
EXPECTED = {
    "orbits": 1969,
    "sign_assignments": 63008,
    "targets": 2216832,
    "triple_candidates": 16970,
    "exact_sign_tests": 135760,
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def folded_lag(left: int, right: int) -> int:
    delta = abs(right - left)
    return min(delta, 128 - delta)


def odd_chords(support: tuple[int, ...]) -> int:
    mask = 0
    for index, left in enumerate(support):
        for right in support[index + 1 :]:
            lag = folded_lag(left, right)
            if lag != 64:
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
        for key, value in re.findall(r"([a-z_]+)=([0-9]+)", row["stdout"]):
            counts[key] += int(value)
    return counts


def autocorrelation(state: dict[int, int]) -> list[int]:
    values = [0] * 64
    support = sorted(state)
    for index, left in enumerate(support):
        for right in support[index + 1 :]:
            delta = right - left
            product = state[left] * state[right]
            if delta < 64:
                values[delta] += product
            elif delta > 64:
                values[128 - delta] -= product
    return values


def main() -> None:
    node_dir = ROOT / "background/nodes" / NODE
    pin = json.loads((node_dir / "source_pin.json").read_text())
    for key in (
        "parent_statement",
        "parent_proof",
        "orbit_classifier",
        "orbit",
        "exact_engine",
        "modal_launcher",
        "primary_result",
        "audit_result",
    ):
        assert sha256(ROOT / pin[f"{key}_file"]) == pin[f"{key}_sha256"]

    orbit_data = json.loads((ROOT / pin["orbit_file"]).read_text())
    assert orbit_data["examined"] == 10009125
    assert orbit_data["mu_one"] == 5005539
    assert orbit_data["retained"] == {
        "1": 297,
        "2": 18,
        "3": 6836,
        "4": 350,
        "5": 11490,
        "6": 8216,
    }
    orbits = [tuple(orbit) for orbit in orbit_data["orbits"]]
    assert len(orbits) == orbit_data["affine_orbits"] == 1969
    assert len(set(orbits)) == len(orbits)

    orbit_q = Counter()
    for orbit in orbits:
        assert len(orbit) == 6 and orbit[0] == 0
        assert sum(orbit) % 2 == 1
        assert canonical(orbit) == orbit
        q = odd_chords(orbit).bit_count()
        assert 1 <= q <= 6
        orbit_q[q] += 1

    primary = json.loads((ROOT / pin["primary_result_file"]).read_text())
    audit = json.loads((ROOT / pin["audit_result_file"]).read_text())
    assert primary["engine"] == "pair-xor-plus-third"
    assert audit["engine"] == "triple-xor"
    assert primary["orbit_file_sha256"] == audit["orbit_file_sha256"] == pin["orbit_sha256"]
    assert primary["passed"] == audit["passed"] == 24

    primary_counts = parse_counts(primary)
    audit_counts = parse_counts(audit)
    for key, value in EXPECTED.items():
        assert primary_counts[key] == audit_counts[key] == value
    assert primary_counts["xor_probes"] == EXPECTED["targets"] * 122
    assert audit_counts["xor_probes"] == EXPECTED["targets"]
    assert EXPECTED["sign_assignments"] == EXPECTED["orbits"] * 32
    assert EXPECTED["exact_sign_tests"] == EXPECTED["triple_candidates"] * 8

    targets_per_sign = {1: 248, 2: 492, 3: 8, 4: 16, 5: 32, 6: 64}
    assert sum(orbit_q[q] * targets_per_sign[q] * 32 for q in orbit_q) == EXPECTED["targets"]

    sharp_state = {
        5: -1,
        16: 1,
        27: -2,
        36: -1,
        38: 1,
        69: -2,
        80: -2,
        102: 1,
        122: 1,
    }
    singleton_sum = sum(position for position, value in sharp_state.items() if abs(value) == 1)
    assert singleton_sum % 2 == 1
    assert sum(value * value for value in autocorrelation(sharp_state)) == 8

    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    for text in ("1538=2*769", "{2,3,4,5,6}", "Eleven"):
        assert text in statement
    for text in ("10009125", "270453504", "135760", "energy-eight"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (PARENT, NODE, "req") in edges
    assert all((NODE, target, "ev") in edges for target in TARGETS)

    print(
        "E1_PRIZE_N256_S18_PROFILE_36_M1538_EXCLUSION_PASS "
        f"orbits={len(orbits)} targets={EXPECTED['targets']} candidates={EXPECTED['triple_candidates']}"
    )


if __name__ == "__main__":
    main()
