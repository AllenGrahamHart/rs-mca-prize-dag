#!/usr/bin/env python3
"""Verify the twice-divided profile-(3,6) cofactor-16 exclusion."""

from __future__ import annotations

from collections import Counter
import hashlib
from itertools import combinations
from math import isqrt
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_profile_36_m16_two_divisions_exclusion"
PARENT = "e1_prize_n256_s18_profile_36_energy_adaptive_product_windows"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
B_PRIZE = 317494674775468773183020924238786383963
CHORD_WEIGHTS = set(range(1, 16))
ORBIT_WEIGHTS = {
    "1": 8, "2": 1, "3": 52, "4": 23, "5": 101, "6": 124,
    "7": 214, "8": 144, "9": 163, "10": 43, "11": 28,
    "12": 1, "13": 1,
}
Q_FRONTIERS = {
    "1": 73, "2": 70, "3": 71, "4": 72, "5": 73, "6": 74,
    "7": 75, "8": 76, "9": 77, "10": 78, "11": 79,
    "12": 80, "13": 89, "14": 86, "15": 87,
}
Q_RADII = {
    "1": 18, "2": 17, "3": 17, "4": 17, "5": 17, "6": 17,
    "7": 17, "8": 17, "9": 17, "10": 17, "11": 17,
    "12": 17, "13": 19, "14": 18, "15": 18,
}
PRIMARY_COUNTS = {
    "orbits": 903,
    "triple_syndromes": 266601720,
    "distance_tests": 8531255040,
    "radius_matches": 7422374296,
    "exact_sign_tests": 59378994368,
    "low_energy_vectors": 497496976,
    "product_live_vectors": 205513652,
    "fixed_below": 205486644,
    "fixed_above": 27008,
    "fixed_unresolved": 0,
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


def canonical(support: tuple[int, ...], modulus: int) -> tuple[int, ...]:
    return min(
        tuple(sorted(unit * ((value - origin) % modulus) % modulus for value in support))
        for origin in support
        for unit in range(1, modulus, 2)
    )


def partition_records() -> set[str]:
    records: set[str] = set()
    for energy_value in range(2, 109):
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
    assert product["energy_range"] == [2, 108]
    assert product["maximum_classes"] == 36
    assert product["chord_inequality"] == "4L<=E+117"
    assert product["chord_excluded"] == 41
    assert product["records"] == 3685 and product["comparisons"] == 295256
    live = set(product["live"])
    excluded = set(product["excluded"])
    assert len(live) == 967 and len(excluded) == 2718 and not live & excluded
    assert live | excluded == partition_records()
    assert product["max_live_energy"] == 89
    assert product["q_frontiers"] == Q_FRONTIERS
    assert product["q_radii"] == Q_RADII

    atlas = json.loads((ROOT / pin["atlas_file"]).read_text())
    assert atlas["affine_orbits"] == 49919
    assert {
        branch: packet["affine_orbits"]
        for branch, packet in atlas["branches"].items()
    } == {"primitive": 39936, "one_division": 9080, "two_divisions": 903}
    branch = atlas["branches"]["two_divisions"]
    assert branch["modulus"] == 32 and branch["lift"] == 4
    assert branch["quotient_multiplicity"] == 1
    assert branch["examined"] == 27405 and branch["matching"] == 13755
    assert branch["orbit_weights"] == ORBIT_WEIGHTS
    orbits = [tuple(orbit) for orbit in branch["orbits"]]
    assert len(orbits) == len(set(orbits)) == 903

    enumerated: set[tuple[int, ...]] = set()
    matching = 0
    for tail in combinations(range(2, 32), 4):
        quotient = (0, 1) + tail
        if multiplicity(quotient) != 1:
            continue
        matching += 1
        enumerated.add(canonical(quotient, 32))
    assert matching == 13755 and len(enumerated) == 903
    quotients = {tuple(value // 4 for value in orbit) for orbit in orbits}
    assert quotients == enumerated
    for orbit in orbits:
        assert len(orbit) == 6 and orbit == tuple(sorted(orbit))
        assert all(value % 4 == 0 for value in orbit)
        assert multiplicity(orbit) == 4
        assert odd_chord_mask(orbit).bit_count() in set(map(int, ORBIT_WEIGHTS))

    primary = json.loads((ROOT / pin["primary_file"]).read_text())
    audit = json.loads((ROOT / pin["audit_file"]).read_text())
    assert primary["complete"] is True and audit["complete"] is True
    assert primary["branch"] == audit["branch"] == "two_divisions"
    assert primary["completed_batches"] == primary["expected_batches"] == 301
    assert audit["completed_batches"] == audit["expected_batches"] == 301
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
    assert sum(audit_high.values()) == PRIMARY_COUNTS["fixed_above"]
    assert min(audit_high) == 6 and max(audit_high) == 36

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
    assert len(records) == len(set(records)) == PRIMARY_COUNTS["fixed_above"]
    assert Counter(record[0] for record in records) == audit_high
    scaled_ceiling = 16 * ((B_PRIZE + 1) * 2**128 - 1) * 2 ** (96 * 64)
    orbit_set = set(orbits)
    for energy_value, odd_weight, l1_norm, state in records:
        assert len(state) == 9 and state == tuple(sorted(state))
        assert len({position for position, _ in state}) == 9
        assert sum(abs(value) == 1 for _, value in state) == 6
        assert sum(abs(value) == 2 for _, value in state) == 3
        correlation = autocorrelation(state)
        assert sum(value * value for value in correlation) == energy_value
        assert sum(abs(value) for value in correlation) == l1_norm
        support = tuple(position for position, value in state if abs(value) == 1)
        assert support in orbit_set and multiplicity(support) == 4
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

    # Hostile metadata mutation: exact autocorrelation replay rejects it.
    first_energy, _, _, first_state = records[0]
    first_correlation = autocorrelation(first_state)
    assert sum(value * value for value in first_correlation) != first_energy + 1

    statement = (node_dir / "statement.md").read_text().lower()
    proof = (node_dir / "proof.md").read_text()
    for text in ("twice-divided", "903", "205,513,652", "remain open"):
        assert text in statement
    for text in ("7422374296", "59378994368", "205486644", "27008"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (PARENT, NODE, "req") in edges
    assert all((NODE, target, "ev") in edges for target in TARGETS)

    print(
        "E1_PRIZE_N256_S18_PROFILE_36_M16_TWO_DIVISIONS_EXCLUSION_PASS "
        "orbits=903 product_live=205513652 separated=205513652 witnesses=27008"
    )


if __name__ == "__main__":
    main()
