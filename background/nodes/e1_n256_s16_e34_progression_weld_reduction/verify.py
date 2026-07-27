#!/usr/bin/env python3
"""Verify the E34 progression-weld reduction."""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e34_progression_weld_reduction"
HEAVY = "e1_n256_s16_e34_heavy_chord_template_reduction"
PARITY = "e1_n256_s16_e34_parity_profile_reduction"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")


def distance(left: int, right: int) -> int:
    delta = (right - left) % 128
    return min(delta, 128 - delta)


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    for key, value in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / value).read_bytes()).hexdigest() == pin[key + "_sha256"]

    forms = Counter()
    for heavy in combinations(range(128), 3):
        lengths = Counter(distance(left, right) for left, right in combinations(heavy, 2))
        if 64 in lengths or sorted(lengths.values()) != [1, 2]:
            continue
        t = next(length for length, count in lengths.items() if count == 2)
        assert 1 <= t <= 63 and t != 32
        forms[t] += 1
    assert sum(forms.values()) == 7936
    assert forms == Counter({t: 128 for t in range(1, 64) if t != 32})

    # Equal outer signs contribute eight. Two possible heavy-light chords and
    # one light-light chord cannot reduce that class to magnitude at most two.
    outputs = {
        abs(8 * sign + 2 * first + 2 * second + unit)
        for sign in (-1, 1)
        for first, second in product((-1, 0, 1), repeat=2)
        for unit in (-1, 0, 1)
    }
    assert min(outputs) == 3 and outputs.isdisjoint({0, 1, 2})

    support_count = math.comb(125, 4) - math.comb(121, 4)
    assert support_count == 1195965
    for t in forms:
        heavy = {0, t, (2 * t) % 128}
        repeated = {
            value
            for value in range(128)
            if value not in heavy and any(distance(value, h) == t for h in heavy)
        }
        outer_length = distance(0, (2 * t) % 128)
        weld = {
            value
            for value in range(128)
            if value not in heavy and any(distance(value, h) == outer_length for h in heavy)
        }
        expected = {(-2 * t) % 128, (3 * t) % 128, (-t) % 128, (4 * t) % 128}
        assert repeated == {(-t) % 128, (3 * t) % 128}
        assert weld == expected and len(weld) == 4 and not weld & heavy

    assert 62 * support_count * 2 * 16 == 2372794560

    representatives = (1, 2, 4, 8, 16)
    orbit_sizes = Counter()
    for t in forms:
        valuation = (t & -t).bit_length() - 1
        representative = 1 << valuation
        assert representative in representatives
        units = [
            unit
            for unit in range(1, 128, 2)
            if (unit * t) % 128 in (representative, (-representative) % 128)
        ]
        assert units
        unit = units[0]
        mapped_heavy = {(unit * value) % 128 for value in (0, t, 2 * t)}
        expected_heavy = {0, representative, 2 * representative}
        if mapped_heavy != expected_heavy:
            mapped_heavy = {(-value) % 128 for value in mapped_heavy}
        assert mapped_heavy == expected_heavy
        orbit_sizes[representative] += 1
    assert orbit_sizes == Counter({1: 32, 2: 16, 4: 8, 8: 4, 16: 2})
    assert len(representatives) * support_count * 2 * 16 == 191354400

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for node in (NODE, HEAVY, PARITY):
        assert nodes[node]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for dependency in (HEAVY, PARITY):
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges

    print(
        "E1_N256_S16_E34_PROGRESSION_WELD_REDUCTION_PASS "
        f"triples={sum(forms.values())} forms={len(forms)} "
        f"orbits={len(representatives)} supports_per_form={support_count} "
        "census_vectors=191354400 total_vectors=2372794560"
    )


if __name__ == "__main__":
    main()
