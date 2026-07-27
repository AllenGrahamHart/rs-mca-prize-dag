#!/usr/bin/env python3
"""Verify the E34 nonquarter-diameter weld reduction."""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e34_nonquarter_diameter_weld_reduction"
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

    normal_forms = Counter()
    for heavy in combinations(range(128), 3):
        antipodal = [
            (left, right)
            for left, right in combinations(heavy, 2)
            if distance(left, right) == 64
        ]
        if not antipodal:
            continue
        assert len(antipodal) == 1
        left, right = antipodal[0]
        third = next(value for value in heavy if value not in (left, right))
        t = min(distance(left, third), distance(right, third))
        if t == 32:
            continue
        assert 1 <= t <= 31
        normal_forms[t] += 1
    assert sum(normal_forms.values()) == 7936
    assert normal_forms == Counter({t: 256 for t in range(1, 32)})

    support_count = None
    for t in range(1, 32):
        heavy = {0, 64, t}
        first = {128 - t, 64 - t, 64 + t, 2 * t}
        second = {64 - t, 64 + t, 128 - t, 64 + 2 * t}
        common = {64 - t, 64 + t, 128 - t}
        unique = {2 * t, 64 + 2 * t}
        assert first & second == common
        assert (first ^ second) == unique
        assert len(common | unique) == 5
        assert not (common | unique) & heavy

        # Check the exact disjunction on every occupancy pattern of the five
        # special positions; other support positions cannot supply a weld.
        special = sorted(common | unique)
        for mask in range(1 << 5):
            light = {special[i] for i in range(5) if mask & (1 << i)}
            both_welds = bool(light & first) and bool(light & second)
            reduced = bool(light & common) or unique <= light
            assert both_welds == reduced

        count = math.comb(125, 4) - math.comb(122, 4) + math.comb(120, 2)
        assert count == 915125
        support_count = count if support_count is None else support_count
        assert count == support_count

    assert 31 * support_count * 4 * 16 == 1815608000

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
        "E1_N256_S16_E34_NONQUARTER_DIAMETER_WELD_REDUCTION_PASS "
        f"triples={sum(normal_forms.values())} forms={len(normal_forms)} "
        f"supports_per_form={support_count} vectors=1815608000"
    )


if __name__ == "__main__":
    main()
