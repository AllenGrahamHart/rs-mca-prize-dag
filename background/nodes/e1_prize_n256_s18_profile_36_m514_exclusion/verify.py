#!/usr/bin/env python3
"""Verify the profile-(3,6) cofactor-514 exclusion."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_profile_36_m514_exclusion"
PARENT = "e1_prize_n256_s18_profile_36_energy_adaptive_product_windows"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
EXPECTED_RETAINED = {
    "3": 6836, "4": 350, "5": 11490, "6": 8216, "7": 114212,
    "8": 24048, "9": 357190, "10": 134638, "11": 1248752,
}
EXPECTED_ORBITS = {
    "3": 692, "4": 23, "5": 725, "6": 496, "7": 6930,
    "8": 1728, "9": 23227, "10": 9043, "11": 80332,
}
EXPECTED_COUNTS = {
    "orbits": 123196,
    "sign_assignments": 3942272,
    "xor_probes": 922886080,
    "triple_candidates": 883718,
    "exact_sign_tests": 7069744,
    "root_tests": 1536,
    "geometry7": 0,
    "geometry8": 4,
    "geometry9": 0,
    "geometry10": 8,
    "geometry11": 0,
    "mod257_7": 0,
    "mod257_8": 2,
    "mod257_9": 0,
    "mod257_10": 6,
    "mod257_11": 0,
}
MAX_QUOTIENT = 76286518954257624881921953724462535222876321872384746739394244519622714858497


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def odd_chord_mask(support: tuple[int, ...]) -> int:
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


def census_counts(packet: dict) -> Counter[str]:
    counts: Counter[str] = Counter()
    for row in packet["rows"]:
        assert row["returncode"] == 0 and not row["stderr"]
        for line in row["stdout"].splitlines():
            if not line.startswith("PASS "):
                continue
            for key, value in re.findall(r"([a-z_0-9]+)=([0-9]+)", line):
                counts[key] += int(value)
    return counts


def candidates(
    packet: dict,
) -> list[tuple[int, int, tuple[tuple[int, int], ...], tuple[int, ...]]]:
    found = []
    pattern = r"CANDIDATE E=(\d+) q=(\d+) state=([^\n]+?) roots=([^\n]+)"
    for row in packet["rows"]:
        for energy_value, odd_weight, encoded, roots in re.findall(
            pattern, row["stdout"]
        ):
            state = tuple(
                (int(position), int(coefficient))
                for position, coefficient in re.findall(r"(\d+):(-?\d+),", encoded)
            )
            root_indices = tuple(int(value) for value in re.findall(r"(\d+),", roots))
            found.append((int(energy_value), int(odd_weight), state, root_indices))
    return sorted(found)


def autocorrelation(state: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    values = [0] * 64
    for index, (left, left_value) in enumerate(state):
        for right, right_value in state[index + 1 :]:
            delta = right - left
            if delta < 64:
                values[delta] += left_value * right_value
            elif delta > 64:
                values[128 - delta] -= left_value * right_value
    return tuple(values)


def main() -> None:
    node_dir = ROOT / "background/nodes" / NODE
    pin = json.loads((node_dir / "source_pin.json").read_text())
    for key in (
        "parent_statement", "parent_proof", "atlas_source", "atlas",
        "base_engine", "engine", "launcher", "primary", "audit",
        "norm_source", "norm",
    ):
        assert sha256(ROOT / pin[f"{key}_file"]) == pin[f"{key}_sha256"]

    atlas = json.loads((ROOT / pin["atlas_file"]).read_text())
    assert atlas["examined"] == 10009125 and atlas["mu_one"] == 5005539
    assert atlas["retained"] == EXPECTED_RETAINED
    assert atlas["orbit_weights"] == EXPECTED_ORBITS
    orbits = [tuple(orbit) for orbit in atlas["orbits"]]
    assert len(orbits) == atlas["affine_orbits"] == 123196
    assert len(set(orbits)) == len(orbits)
    for orbit in orbits:
        assert len(orbit) == 6 and orbit == tuple(sorted(orbit))
        assert orbit[:2] == (0, 1) and sum(orbit) % 2 == 1
        assert 3 <= odd_chord_mask(orbit).bit_count() <= 11
    for orbit in orbits[::997]:
        assert canonical(orbit) == orbit

    primary = json.loads((ROOT / pin["primary_file"]).read_text())
    audit = json.loads((ROOT / pin["audit_file"]).read_text())
    assert primary["engine"] == "hash-pairs" and audit["engine"] == "sorted-pairs"
    assert primary["orbit_file_sha256"] == audit["orbit_file_sha256"] == pin["atlas_sha256"]
    primary_counts = census_counts(primary)
    audit_counts = census_counts(audit)
    for key, value in EXPECTED_COUNTS.items():
        assert primary_counts[key] == audit_counts[key] == value

    primary_candidates = candidates(primary)
    assert primary_candidates == candidates(audit) and len(primary_candidates) == 8
    for energy_value, odd_weight, state, roots in primary_candidates:
        assert len(state) == 9
        assert sum(abs(value) == 1 for _, value in state) == 6
        assert sum(abs(value) == 2 for _, value in state) == 3
        correlation = autocorrelation(state)
        assert sum(value * value for value in correlation) == energy_value
        singleton_support = tuple(position for position, value in state if abs(value) == 1)
        assert odd_chord_mask(singleton_support).bit_count() == odd_weight
        assert (energy_value, odd_weight) in {(8, 4), (10, 6)}
        assert len(roots) == 1
        unit = 2 * roots[0] + 1
        assert sum(
            value * pow(3, unit * position, 257) for position, value in state
        ) % 257 == 0

    norms = json.loads((ROOT / pin["norm_file"]).read_text())
    assert norms["complete"] is True and norms["agreement"] is True
    assert norms["source_sha256"] == pin["norm_source_sha256"]
    assert norms["primary_sha256"] == pin["primary_sha256"]
    assert norms["audit_sha256"] == pin["audit_sha256"]
    assert norms["candidates"] == len(primary_candidates) == 8
    assert norms["census_counts"] == EXPECTED_COUNTS
    norm_states = []
    for row in norms["rows"]:
        state = tuple((int(position), int(value)) for position, value in row["state"])
        norm = int(row["norm"])
        assert row["flint_pari_agree"] is True and row["valuation"] == 1
        assert norm % 514 == 0 and int(row["quotient"]) == norm // 514
        assert row["quotient_relation"] == "below" and norm // 514 < P_MIN
        norm_states.append(state)
    assert len({int(row["norm"]) for row in norms["rows"]}) == 4
    assert max(int(row["quotient"]) for row in norms["rows"]) == MAX_QUOTIENT
    assert sorted(norm_states) == sorted(row[2] for row in primary_candidates)

    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    for text in ("m=514", "123196", "seven"):
        assert text in statement.lower()
    for text in ("922886080", "7069744", str(MAX_QUOTIENT)):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (PARENT, NODE, "req") in edges
    assert all((NODE, target, "ev") in edges for target in TARGETS)

    print(
        "E1_PRIZE_N256_S18_PROFILE_36_M514_EXCLUSION_PASS "
        "orbits=123196 geometry=12 factor257=8 distinct_norms=4"
    )


if __name__ == "__main__":
    main()
