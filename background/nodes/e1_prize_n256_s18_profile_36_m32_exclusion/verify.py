#!/usr/bin/env python3
"""Verify the profile-(3,6) cofactor-32 exclusion."""

from __future__ import annotations

from collections import Counter
import hashlib
from math import isqrt
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_profile_36_m32_exclusion"
PARENT = "e1_prize_n256_s18_profile_36_energy_adaptive_product_windows"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
B_PRIZE = 317494674775468773183020924238786383963
CHORD_WEIGHTS = set(range(3, 16))
ORBIT_WEIGHTS = {
    "3": 1, "4": 6, "5": 41, "6": 24, "7": 300, "8": 148,
    "9": 1430, "10": 480, "11": 4061, "12": 358,
    "13": 4097, "14": 904, "15": 7990,
}
RAW_WEIGHTS = {key: 16 * value for key, value in ORBIT_WEIGHTS.items()}
Q_FRONTIERS = {
    "3": 55, "4": 56, "5": 57, "6": 58, "7": 55, "8": 56,
    "9": 57, "10": 58, "11": 59, "12": 60,
    "13": 57, "14": 58, "15": 59,
}
Q_RADII = {
    "3": 13, "4": 13, "5": 13, "6": 13, "7": 12, "8": 12,
    "9": 12, "10": 12, "11": 12, "12": 12,
    "13": 11, "14": 11, "15": 11,
}
PRIMARY_COUNTS = {
    "orbits": 19840,
    "triple_syndromes": 5857561600,
    "distance_tests": 187441971200,
    "radius_matches": 84923111400,
    "exact_sign_tests": 679384891200,
    "low_energy_vectors": 339892636,
    "product_live_vectors": 239131808,
    "fixed_below": 239131588,
    "fixed_above": 220,
    "fixed_unresolved": 0,
}
HIGH_ENERGIES = {
    9: 4, 11: 2, 12: 4, 13: 14, 14: 4, 15: 22, 16: 28,
    17: 48, 18: 8, 19: 26, 20: 28, 21: 24, 23: 4, 24: 4,
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def multiplicity(support: tuple[int, ...]) -> int:
    for derivative in range(16):
        if sum((derivative & ~exponent) == 0 for exponent in support) % 2:
            return derivative
    return 16


def odd_chord_mask(support: tuple[int, ...]) -> int:
    mask = 0
    for index, left in enumerate(support):
        for right in support[index + 1 :]:
            delta = right - left
            if delta == 64:
                continue
            lag = delta if delta < 64 else 128 - delta
            mask ^= 1 << (lag - 1)
    return mask


def canonical(support: tuple[int, ...]) -> tuple[int, ...]:
    return min(
        tuple(sorted(unit * ((value - origin) % 128) % 128 for value in support))
        for origin in support
        for unit in range(1, 128, 2)
    )


def partition_records() -> set[str]:
    records: set[str] = set()
    for energy_value in range(2, 86):
        def visit(magnitude: int, remaining: int, q: int, l1: int, classes: int) -> None:
            if magnitude == 1:
                count = remaining
                odd_weight = q + count
                if classes + count <= 36 and odd_weight in CHORD_WEIGHTS:
                    records.add(f"E{energy_value}q{odd_weight}L{l1 + count}")
                return
            square = magnitude * magnitude
            for count in range(min(remaining // square, 36 - classes) + 1):
                visit(
                    magnitude - 1,
                    remaining - count * square,
                    q + (count if magnitude % 2 else 0),
                    l1 + count * magnitude,
                    classes + count,
                )
        visit(isqrt(energy_value), energy_value, 0, 0, 0)
    return records


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


def fixed_table(path: Path, name: str) -> list[list[int]]:
    text = path.read_text()
    marker = f"{name}[64][128] = {{"
    start = text.index(marker) + len(marker)
    end = text.index("\n};", start)
    values = [int(value) for value in re.findall(r"-?\d+", text[start:end])]
    assert len(values) == 64 * 128
    return [values[index * 128 : (index + 1) * 128] for index in range(64)]


def parse_witness(record: str) -> tuple[int, int, int, tuple[tuple[int, int], ...]]:
    match = re.fullmatch(r"WITNESS E=(\d+) q=(\d+) L=(\d+) state=(.+)", record)
    assert match
    state = tuple(
        (int(position), int(coefficient))
        for position, coefficient in re.findall(r"(\d+):(-?\d+),", match.group(4))
    )
    return int(match.group(1)), int(match.group(2)), int(match.group(3)), state


def main() -> None:
    node_dir = ROOT / "background/nodes" / NODE
    pin = json.loads((node_dir / "source_pin.json").read_text())
    for key, value in pin.items():
        if key.endswith("_file"):
            prefix = key[:-5]
            assert sha256(ROOT / value) == pin[f"{prefix}_sha256"]

    product = json.loads((ROOT / pin["product_file"]).read_text())
    assert product["complete"] is True
    assert product["source_sha256"] == pin["product_source_sha256"]
    assert product["header_sha256"] == pin["product_header_sha256"]
    assert product["energy_range"] == [2, 85]
    assert product["records"] == 1834 and product["comparisons"] == 173683
    live = set(product["live"])
    excluded = set(product["excluded"])
    assert len(live) == 474 and len(excluded) == 1360 and not live & excluded
    assert live | excluded == partition_records()
    assert product["max_live_energy"] == 60
    assert product["q_frontiers"] == Q_FRONTIERS
    assert product["q_radii"] == Q_RADII

    atlas = json.loads((ROOT / pin["atlas_file"]).read_text())
    assert atlas["examined"] == 10009125 and atlas["mu_five"] == 317440
    assert atlas["affine_orbits"] == 19840
    assert atlas["weights"] == RAW_WEIGHTS
    assert atlas["orbit_weights"] == ORBIT_WEIGHTS
    orbits = [tuple(orbit) for orbit in atlas["orbits"]]
    assert len(orbits) == len(set(orbits)) == 19840
    for orbit in orbits:
        assert len(orbit) == 6 and orbit == tuple(sorted(orbit))
        assert orbit[:2] == (0, 1) and multiplicity(orbit) == 5
        assert odd_chord_mask(orbit).bit_count() in CHORD_WEIGHTS
    for orbit in orbits[::127]:
        assert canonical(orbit) == orbit

    primary = json.loads((ROOT / pin["primary_file"]).read_text())
    audit = json.loads((ROOT / pin["audit_file"]).read_text())
    assert primary["complete"] is True and audit["complete"] is True
    assert primary["completed_batches"] == primary["expected_batches"] == 1240
    assert audit["completed_batches"] == audit["expected_batches"] == 1654
    assert all(row["valid"] and row["returncode"] == 0 and not row["stderr"] for row in primary["rows"])
    assert all(row["valid"] and row["returncode"] == 0 and not row["stderr"] for row in audit["rows"])
    assert primary["orbit_file_sha256"] == audit["orbit_file_sha256"] == pin["atlas_sha256"]
    assert primary["engine_sha256"] == audit["primary_engine_sha256"] == pin["primary_engine_sha256"]
    assert audit["audit_engine_sha256"] == pin["audit_engine_sha256"]
    assert audit["primary_result_sha256"] == pin["primary_sha256"]
    assert primary["product_header_sha256"] == audit["product_header_sha256"] == pin["product_header_sha256"]
    assert primary["fixed_roots_sha256"] == audit["fixed_roots_sha256"] == pin["root_header_sha256"]
    for key, expected in PRIMARY_COUNTS.items():
        assert primary["counts"][key] == expected
    assert audit["counts"]["orbits"] == PRIMARY_COUNTS["orbits"]
    assert audit["counts"]["sign_assignments"] == 32 * PRIMARY_COUNTS["orbits"]
    assert audit["counts"]["triple_syndromes"] == PRIMARY_COUNTS["distance_tests"]
    for key in (
        "radius_matches", "exact_sign_tests", "low_energy_vectors",
        "product_live_vectors", "fixed_below", "fixed_above", "fixed_unresolved",
    ):
        assert audit["counts"][key] == PRIMARY_COUNTS[key]
    assert primary["counts"]["screen_below"] == PRIMARY_COUNTS["fixed_below"]
    assert primary["counts"]["screen_above"] == PRIMARY_COUNTS["fixed_above"]
    assert primary["counts"]["screen_near"] == 0
    assert sum(value for key, value in audit["counts"].items() if key.startswith("live_E")) == PRIMARY_COUNTS["product_live_vectors"]
    audit_high = {
        int(key.removeprefix("above_E")): value
        for key, value in audit["counts"].items() if key.startswith("above_E")
    }
    assert audit_high == HIGH_ENERGIES

    hash_audit = json.loads((ROOT / pin["hash_audit_file"]).read_text())
    assert hash_audit["complete"] is True and hash_audit["representatives"] == 13
    assert {row["odd_weight"] for row in hash_audit["rows"]} == CHORD_WEIGHTS
    for row in hash_audit["rows"]:
        assert row["returncode"] == 0 and not row["stderr"]
        counts = dict(re.findall(r"\b([a-z_]+)=([0-9]+)(?=\s|$)", row["stdout"]))
        assert int(counts["exact_sign_tests"]) == 8 * int(counts["unique_triples"])
        assert int(counts["product_live_vectors"]) == int(counts["fixed_below"]) + int(counts["fixed_above"])
        assert int(counts["fixed_unresolved"]) == 0

    roots = json.loads((ROOT / pin["root_result_file"]).read_text())
    assert roots["complete"] is True and roots["checks"] == 16384
    assert roots["audit"] == "python-flint-arb-256-bit"
    assert roots["scaled_component_error_lt"] == 1
    assert roots["header_sha256"] == pin["root_header_sha256"]
    assert roots["source_sha256"] == pin["root_source_sha256"]
    real = fixed_table(ROOT / pin["root_header_file"], "M64_FIXED_REAL")
    imaginary = fixed_table(ROOT / pin["root_header_file"], "M64_FIXED_IMAG")

    assert primary["witnesses"] == [
        witness for row in primary["rows"] for witness in row["witnesses"]
    ]
    records = [parse_witness(record) for record in primary["witnesses"]]
    assert len(records) == len(set(records)) == 220
    assert Counter(record[0] for record in records) == HIGH_ENERGIES
    scaled_ceiling = 32 * ((B_PRIZE + 1) * 2**128 - 1) * 2 ** (96 * 64)
    for energy_value, odd_weight, l1_norm, state in records:
        assert len(state) == 9 and state == tuple(sorted(state))
        assert len({position for position, _ in state}) == 9
        assert sum(abs(value) == 1 for _, value in state) == 6
        assert sum(abs(value) == 2 for _, value in state) == 3
        correlation = autocorrelation(state)
        assert sum(value * value for value in correlation) == energy_value
        assert sum(abs(value) for value in correlation) == l1_norm
        support = tuple(position for position, value in state if abs(value) == 1)
        assert multiplicity(support) == 5
        assert odd_chord_mask(support).bit_count() == odd_weight
        assert f"E{energy_value}q{odd_weight}L{l1_norm}" in live
        lower_product = 1
        for root in range(64):
            real_sum = sum(value * real[root][position] for position, value in state)
            imag_sum = sum(value * imaginary[root][position] for position, value in state)
            lower_real = max(abs(real_sum) - 12, 0)
            lower_imag = max(abs(imag_sum) - 12, 0)
            lower_product *= lower_real * lower_real + lower_imag * lower_imag
        assert lower_product > scaled_ceiling

    statement = (node_dir / "statement.md").read_text().lower()
    proof = (node_dir / "proof.md").read_text()
    for text in ("m=32", "19,840", "239,131,808", "four"):
        assert text in statement
    for text in ("84923111400", "679384891200", "239131588", "220"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (PARENT, NODE, "req") in edges
    assert all((NODE, target, "ev") in edges for target in TARGETS)

    print(
        "E1_PRIZE_N256_S18_PROFILE_36_M32_EXCLUSION_PASS "
        "orbits=19840 product_live=239131808 separated=239131808"
    )


if __name__ == "__main__":
    main()
