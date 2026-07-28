#!/usr/bin/env python3
"""Verify the profile-(3,6) cofactor-256 exclusion."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_profile_36_m256_exclusion"
PARENT = "e1_prize_n256_s18_profile_36_energy_adaptive_product_windows"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
CHORD_WEIGHTS = {1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
EXPECTED_WEIGHTS = {
    "1": 16, "3": 288, "5": 256, "6": 128, "7": 3584,
    "8": 384, "9": 8480, "10": 3712, "11": 26208, "12": 1920,
    "13": 8064, "14": 10240, "15": 24576,
}
EXPECTED_ORBITS = {
    "1": 4, "3": 32, "5": 24, "6": 8, "7": 236, "8": 24,
    "9": 608, "10": 296, "11": 1648, "12": 152, "13": 504,
    "14": 848, "15": 1536,
}
EXPECTED_COUNTS = {
    "orbits": 5920,
    "sign_assignments": 189440,
    "third_queries": 23111680,
    "bucket_hits": 2061796568,
    "radius_matches": 12206580,
    "triple_candidates": 2833260,
    "exact_sign_tests": 22666080,
    "low_energy_vectors": 70,
    "live_candidates": 54,
    "live_E13": 8,
    "live_E15": 6,
    "live_E17": 12,
    "live_E19": 28,
}
MAX_QUOTIENT = 67404590334226659516226521627034983611828304342200684420570670966820124685313


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
    records = set()
    for energy in range(2, 24):
        for fours in range(energy // 16 + 1):
            for threes in range((energy - 16 * fours) // 9 + 1):
                for twos in range(
                    (energy - 16 * fours - 9 * threes) // 4 + 1
                ):
                    ones = energy - 16 * fours - 9 * threes - 4 * twos
                    odd_weight = ones + threes
                    if odd_weight not in CHORD_WEIGHTS:
                        continue
                    l1_norm = ones + 2 * twos + 3 * threes + 4 * fours
                    records.add(f"E{energy}q{odd_weight}L{l1_norm}")
    return records


def candidates(
    packet: dict,
) -> list[tuple[int, int, int, tuple[tuple[int, int], ...]]]:
    found = []
    pattern = re.compile(
        r"CANDIDATE E=(\d+) q=(\d+) L=(\d+) state=([^\n]+)"
    )
    for row in packet["rows"]:
        assert row["returncode"] == 0 and not row["stderr"]
        for energy, odd_weight, l1_norm, encoded in pattern.findall(row["stdout"]):
            state = tuple(
                (int(position), int(coefficient))
                for position, coefficient in re.findall(r"(\d+):(-?\d+),", encoded)
            )
            found.append((int(energy), int(odd_weight), int(l1_norm), state))
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
        "parent_statement", "parent_proof", "product_source", "product",
        "atlas_source", "atlas", "base_engine", "engine", "launcher",
        "primary", "audit", "norm_source", "norm",
    ):
        assert sha256(ROOT / pin[f"{key}_file"]) == pin[f"{key}_sha256"]

    product = json.loads((ROOT / pin["product_file"]).read_text())
    assert product["source_sha256"] == pin["product_source_sha256"]
    assert product["comparisons"] == 27176
    live = set(product["live"])
    excluded = set(product["excluded"])
    assert len(live) == len(excluded) == 45 and not live & excluded
    assert live | excluded == partition_records()
    assert max(int(re.match(r"E(\d+)", row).group(1)) for row in live) == 20
    assert all(
        row in excluded
        for row in partition_records()
        if int(re.match(r"E(\d+)", row).group(1)) >= 21
    )

    atlas = json.loads((ROOT / pin["atlas_file"]).read_text())
    assert atlas["examined"] == 10009125 and atlas["mu_eight"] == 87856
    assert atlas["weights"] == EXPECTED_WEIGHTS
    assert atlas["orbit_weights"] == EXPECTED_ORBITS
    orbits = [tuple(orbit) for orbit in atlas["orbits"]]
    assert len(orbits) == atlas["affine_orbits"] == 5920
    assert len(set(orbits)) == len(orbits)
    for orbit in orbits:
        assert len(orbit) == 6 and orbit == tuple(sorted(orbit))
        assert orbit[:2] == (0, 1) and multiplicity(orbit) == 8
        assert odd_chord_mask(orbit).bit_count() in CHORD_WEIGHTS
    for orbit in orbits[::97]:
        assert canonical(orbit) == orbit

    primary = json.loads((ROOT / pin["primary_file"]).read_text())
    audit = json.loads((ROOT / pin["audit_file"]).read_text())
    assert primary["engine"] == "hash-blocks"
    assert audit["engine"] == "sorted-blocks"
    assert primary["orbit_file_sha256"] == audit["orbit_file_sha256"] == pin["atlas_sha256"]
    assert primary["engine_sha256"] == audit["engine_sha256"] == pin["engine_sha256"]
    assert primary["counts"] == audit["counts"] == EXPECTED_COUNTS
    assert primary["candidate_lines"] == audit["candidate_lines"] == 54

    primary_candidates = candidates(primary)
    assert primary_candidates == candidates(audit)
    assert len(primary_candidates) == len(set(primary_candidates)) == 54
    for energy_value, odd_weight, l1_norm, state in primary_candidates:
        assert len(state) == 9 and len({position for position, _ in state}) == 9
        assert sum(abs(value) == 1 for _, value in state) == 6
        assert sum(abs(value) == 2 for _, value in state) == 3
        correlation = autocorrelation(state)
        assert sum(value * value for value in correlation) == energy_value
        assert sum(abs(value) for value in correlation) == l1_norm
        singleton_support = tuple(position for position, value in state if abs(value) == 1)
        assert multiplicity(singleton_support) == 8
        assert odd_chord_mask(singleton_support).bit_count() == odd_weight
        assert f"E{energy_value}q{odd_weight}L{l1_norm}" in live

    norms = json.loads((ROOT / pin["norm_file"]).read_text())
    assert norms["complete"] is True and norms["agreement"] is True
    assert norms["source_sha256"] == pin["norm_source_sha256"]
    assert norms["primary_sha256"] == pin["primary_sha256"]
    assert norms["audit_sha256"] == pin["audit_sha256"]
    assert norms["candidate_lines"] == norms["unique_candidates"] == 54
    assert norms["relations"] == {"below": 54}
    assert norms["energies"] == {"13": 8, "15": 6, "17": 12, "19": 28}
    assert norms["max_quotient"] == MAX_QUOTIENT
    norm_candidates = []
    for row in norms["rows"]:
        state = tuple((int(position), int(value)) for position, value in row["state"])
        norm = int(row["norm"])
        quotient = int(row["quotient"])
        assert row["flint_pari_agree"] is True and row["valuation"] == 8
        assert norm % 256 == 0 and quotient == norm // 256
        assert row["quotient_relation"] == "below" and quotient < P_MIN
        norm_candidates.append(
            (int(row["energy"]), int(row["odd_weight"]), int(row["l1_norm"]), state)
        )
    assert sorted(norm_candidates) == primary_candidates
    assert max(int(row["quotient"]) for row in norms["rows"]) == MAX_QUOTIENT

    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    for text in ("m=256", "5920", "54", "six"):
        assert text in statement.lower()
    for text in ("2061796568", "22666080", str(MAX_QUOTIENT)):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (PARENT, NODE, "req") in edges
    assert all((NODE, target, "ev") in edges for target in TARGETS)

    print(
        "E1_PRIZE_N256_S18_PROFILE_36_M256_EXCLUSION_PASS "
        "orbits=5920 candidates=54 max_quotient_below_prize=1"
    )


if __name__ == "__main__":
    main()
