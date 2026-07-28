#!/usr/bin/env python3
"""Verify the profile-(3,6) cofactor-64 exclusion."""

from __future__ import annotations

from collections import Counter
import hashlib
from math import isqrt
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_profile_36_m64_exclusion"
PARENT = "e1_prize_n256_s18_profile_36_energy_adaptive_product_windows"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
B_PRIZE = 317494674775468773183020924238786383963
CHORD_WEIGHTS = set(range(2, 16))

PRIMITIVE_WEIGHTS = {
    "2": 64, "3": 448, "4": 16, "5": 128, "6": 176, "7": 2080,
    "8": 416, "9": 5856, "10": 2080, "11": 24672, "12": 1360,
    "13": 32544, "14": 4080, "15": 48960,
}
PRIMITIVE_ORBITS = {
    "2": 16, "3": 56, "4": 2, "5": 8, "6": 22, "7": 130,
    "8": 52, "9": 366, "10": 260, "11": 1570, "12": 170,
    "13": 2034, "14": 510, "15": 3060,
}
IMPRIMITIVE_WEIGHTS = {
    "3": 48, "4": 128, "5": 816, "6": 928, "7": 4736,
    "8": 2848, "9": 12096, "10": 4896, "11": 18896, "12": 3360,
    "13": 14096, "14": 2176, "15": 6656,
}
IMPRIMITIVE_ORBITS = {
    "3": 3, "4": 8, "5": 51, "6": 58, "7": 296, "8": 178,
    "9": 756, "10": 306, "11": 1181, "12": 210, "13": 881,
    "14": 136, "15": 416,
}

PRIMITIVE_COUNTS = {
    "orbits": 8256,
    "triple_syndromes": 2437501440,
    "distance_tests": 78000046080,
    "radius_matches": 5446358364,
    "exact_sign_tests": 43570866912,
    "low_energy_vectors": 3409506,
    "product_live_vectors": 2385026,
    "fixed_below": 2384994,
    "fixed_above": 32,
    "fixed_unresolved": 0,
}
IMPRIMITIVE_COUNTS = {
    "orbits": 4480,
    "triple_syndromes": 1322675200,
    "distance_tests": 42325606400,
    "radius_matches": 4733090268,
    "exact_sign_tests": 37864722144,
    "low_energy_vectors": 8730734,
    "product_live_vectors": 4806540,
    "fixed_below": 4806430,
    "fixed_above": 110,
    "fixed_unresolved": 0,
}
MINIMUM_LIVE_L1 = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 4, "7": 5,
    "8": 6, "9": 7, "10": 4, "11": 5, "12": 6, "13": 7,
    "14": 6, "15": 7, "16": 8, "17": 9, "18": 6, "19": 7,
    "20": 8, "21": 9, "22": 8, "23": 9, "24": 10, "25": 11,
    "26": 10, "27": 11, "28": 12, "29": 13, "30": 14,
    "31": 15, "32": 16, "33": 17, "34": 18, "35": 19,
    "36": 20, "37": 21, "38": 22, "39": 23, "40": 24,
    "41": 25, "42": 26, "43": 27, "44": 26, "45": 27,
    "46": 30,
}
Q_FRONTIERS = {
    "2": 34, "3": 35, "4": 36, "5": 37, "6": 38, "7": 39,
    "8": 44, "9": 45, "10": 42, "11": 43, "12": 44,
    "13": 45, "14": 46, "15": 43,
}
Q_RADII = {
    "2": 8, "3": 8, "4": 8, "5": 8, "6": 8, "7": 8,
    "8": 9, "9": 9, "10": 8, "11": 8, "12": 8,
    "13": 8, "14": 8, "15": 7,
}
HIGH_ENERGIES = {
    7: 4, 8: 8, 10: 12, 11: 10, 12: 20, 13: 12,
    14: 24, 15: 18, 16: 20, 17: 6, 18: 4, 19: 4,
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
    records = set()
    for energy in range(2, 66):
        def visit(magnitude: int, remaining: int, q: int, l1: int, classes: int) -> None:
            if magnitude == 1:
                count = remaining
                odd_weight = q + count
                if classes + count <= 36 and odd_weight in CHORD_WEIGHTS:
                    records.add(f"E{energy}q{odd_weight}L{l1 + count}")
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
        visit(isqrt(energy), energy, 0, 0, 0)
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


def witness_records(packet: dict) -> list[tuple[int, int, int, tuple[tuple[int, int], ...]]]:
    pattern = re.compile(r"WITNESS E=(\d+) q=(\d+) L=(\d+) state=([^\n]+)")
    records = []
    for row in packet["witnesses"]:
        match = pattern.fullmatch(row["record"])
        assert match
        state = tuple(
            (int(position), int(coefficient))
            for position, coefficient in re.findall(r"(\d+):(-?\d+),", match.group(4))
        )
        records.append((int(match.group(1)), int(match.group(2)), int(match.group(3)), state))
    return records


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
    assert product["records"] == 1092 and product["comparisons"] == 128228
    live = set(product["live"])
    excluded = set(product["excluded"])
    assert len(live) == 255 and len(excluded) == 837 and not live & excluded
    assert live | excluded == partition_records()
    assert product["max_live_energy"] == 46
    assert product["minimum_live_l1"] == MINIMUM_LIVE_L1
    assert product["q_frontiers"] == Q_FRONTIERS
    assert product["q_radii"] == Q_RADII

    primitive = json.loads((ROOT / pin["atlas_file"]).read_text())
    assert primitive["examined"] == 10009125 and primitive["mu_six"] == 122880
    assert primitive["weights"] == PRIMITIVE_WEIGHTS
    assert primitive["orbit_weights"] == PRIMITIVE_ORBITS
    primitive_orbits = [tuple(orbit) for orbit in primitive["orbits"]]
    assert len(primitive_orbits) == len(set(primitive_orbits)) == 8256
    for orbit in primitive_orbits:
        assert len(orbit) == 6 and orbit == tuple(sorted(orbit))
        assert orbit[:2] == (0, 1) and multiplicity(orbit) == 6
        assert odd_chord_mask(orbit).bit_count() in CHORD_WEIGHTS
    for orbit in primitive_orbits[::89]:
        assert canonical(orbit, 128) == orbit

    imprimitive = json.loads((ROOT / pin["imprimitive_atlas_file"]).read_text())
    assert imprimitive["examined"] == 557845
    assert imprimitive["mu_three_normalized"] == 71680
    assert imprimitive["weights"] == IMPRIMITIVE_WEIGHTS
    assert imprimitive["orbit_weights"] == IMPRIMITIVE_ORBITS
    imprimitive_orbits = [tuple(orbit) for orbit in imprimitive["orbits"]]
    assert len(imprimitive_orbits) == len(set(imprimitive_orbits)) == 4480
    for orbit in imprimitive_orbits:
        assert len(orbit) == 6 and orbit == tuple(sorted(orbit))
        assert orbit[:2] == (0, 2) and all(value % 2 == 0 for value in orbit)
        assert multiplicity(orbit) == 6
        assert multiplicity(tuple(value // 2 for value in orbit)) == 3
        assert odd_chord_mask(orbit).bit_count() in CHORD_WEIGHTS
    for orbit in imprimitive_orbits[::73]:
        assert canonical(tuple(value // 2 for value in orbit), 64) == tuple(
            value // 2 for value in orbit
        )

    primary = json.loads((ROOT / pin["primary_file"]).read_text())
    audit = json.loads((ROOT / pin["audit_file"]).read_text())
    imp_primary = json.loads((ROOT / pin["imprimitive_primary_file"]).read_text())
    imp_audit = json.loads((ROOT / pin["imprimitive_audit_file"]).read_text())
    for packet in (primary, audit, imp_primary, imp_audit):
        assert packet["complete"] is True
        assert all(row["returncode"] == 0 and not row["stderr"] for row in packet["rows"])
        assert packet["fixed_roots_sha256"] == pin["root_header_sha256"]
    assert primary["orbit_file_sha256"] == pin["atlas_sha256"]
    assert audit["orbit_file_sha256"] == pin["atlas_sha256"]
    assert imp_primary["orbit_file_sha256"] == pin["imprimitive_atlas_sha256"]
    assert imp_audit["orbit_file_sha256"] == pin["imprimitive_atlas_sha256"]
    assert primary["engine_sha256"] == pin["primary_engine_sha256"]
    assert audit["primary_engine_sha256"] == pin["primary_engine_sha256"]
    assert audit["engine_sha256"] == pin["audit_engine_sha256"]
    assert imp_primary["engine_sha256"] == pin["primary_engine_sha256"]
    assert imp_audit["primary_engine_sha256"] == pin["primary_engine_sha256"]
    assert imp_audit["engine_sha256"] == pin["audit_engine_sha256"]
    for key, expected in PRIMITIVE_COUNTS.items():
        assert primary["counts"][key] == expected
    for key, expected in IMPRIMITIVE_COUNTS.items():
        assert imp_primary["counts"][key] == expected
    for primary_packet, audit_packet in ((primary, audit), (imp_primary, imp_audit)):
        for key in (
            "exact_sign_tests", "low_energy_vectors", "product_live_vectors",
            "fixed_below", "fixed_above", "fixed_unresolved",
        ):
            assert audit_packet["counts"][key] == primary_packet["counts"][key]
        assert audit_packet["counts"]["unique_triples"] == primary_packet["counts"]["radius_matches"]
    assert primary["counts"]["screen_below"] == primary["counts"]["fixed_below"]
    assert primary["counts"]["screen_above"] == primary["counts"]["fixed_above"]
    assert imp_primary["counts"]["screen_below"] == imp_primary["counts"]["fixed_below"]
    assert imp_primary["counts"]["screen_above"] == imp_primary["counts"]["fixed_above"]

    roots = json.loads((ROOT / pin["root_result_file"]).read_text())
    assert roots == {
        "audit": "python-flint-arb-256-bit",
        "bits": 48,
        "checks": 16384,
        "complete": True,
        "generator": "mpmath-100-decimal",
        "header_sha256": pin["root_header_sha256"],
        "positions": 128,
        "roots": 64,
        "scaled_component_error_lt": 1,
        "schema": "e1-profile-36-mu6-m64-fixed-roots-v1",
        "source_sha256": pin["root_source_sha256"],
    }
    real = fixed_table(ROOT / pin["root_header_file"], "M64_FIXED_REAL")
    imaginary = fixed_table(ROOT / pin["root_header_file"], "M64_FIXED_IMAG")

    primitive_witnesses = json.loads((ROOT / pin["witness_file"]).read_text())
    imprimitive_witnesses = json.loads((ROOT / pin["imprimitive_witness_file"]).read_text())
    for packet, atlas_hash, count in (
        (primitive_witnesses, pin["atlas_sha256"], 32),
        (imprimitive_witnesses, pin["imprimitive_atlas_sha256"], 110),
    ):
        assert packet["complete"] is True and packet["witness_count"] == count
        assert packet["orbit_file_sha256"] == atlas_hash
        assert packet["engine_sha256"] == pin["primary_engine_sha256"]
        assert packet["fixed_roots_sha256"] == pin["root_header_sha256"]
        assert all(row["returncode"] == 0 and not row["stderr"] for row in packet["rows"])
    records = witness_records(primitive_witnesses) + witness_records(imprimitive_witnesses)
    assert len(records) == len(set(records)) == 142
    assert Counter(record[0] for record in records) == HIGH_ENERGIES
    scaled_ceiling = 64 * ((B_PRIZE + 1) * 2**128 - 1) * 2 ** (96 * 64)
    for energy_value, odd_weight, l1_norm, state in records:
        assert len(state) == 9 and len({position for position, _ in state}) == 9
        assert sum(abs(value) == 1 for _, value in state) == 6
        assert sum(abs(value) == 2 for _, value in state) == 3
        correlation = autocorrelation(state)
        assert sum(value * value for value in correlation) == energy_value
        assert sum(abs(value) for value in correlation) == l1_norm
        support = tuple(position for position, value in state if abs(value) == 1)
        assert multiplicity(support) == 6
        assert odd_chord_mask(support).bit_count() == odd_weight
        assert energy_value <= Q_FRONTIERS[str(odd_weight)]
        assert l1_norm >= MINIMUM_LIVE_L1[str(energy_value)]
        lower_product = 1
        for root in range(64):
            real_sum = sum(value * real[root][position] for position, value in state)
            imag_sum = sum(value * imaginary[root][position] for position, value in state)
            lower_real = max(abs(real_sum) - 12, 0)
            lower_imag = max(abs(imag_sum) - 12, 0)
            lower_product *= lower_real * lower_real + lower_imag * lower_imag
        assert lower_product > scaled_ceiling

    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    for text in ("m=64", "12736", "7191566", "five"):
        assert text in statement.lower()
    for text in ("10179448632", "81435589056", "7191424", "142"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (PARENT, NODE, "req") in edges
    assert all((NODE, target, "ev") in edges for target in TARGETS)

    print(
        "E1_PRIZE_N256_S18_PROFILE_36_M64_EXCLUSION_PASS "
        "orbits=12736 product_live=7191566 separated=7191566"
    )


if __name__ == "__main__":
    main()
