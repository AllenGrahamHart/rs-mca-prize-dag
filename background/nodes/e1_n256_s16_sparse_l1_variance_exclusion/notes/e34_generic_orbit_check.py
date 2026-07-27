#!/usr/bin/env python3
"""Check the two E34 generic-heavy orbit classifiers."""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
PRIMARY = HERE / "e34_generic_orbit_classifier.cpp"
AUDIT = HERE / "e34_generic_orbit_audit.cpp"
PACKET = HERE / "e34_generic_orbit_result.json"


def distance(left: int, right: int) -> int:
    delta = (right - left) % 128
    return min(delta, 128 - delta)


def weld(heavy: list[int], length: int) -> set[int]:
    return {
        light
        for light in range(128)
        if light not in heavy and any(distance(light, h) == length for h in heavy)
    }


def main() -> None:
    packet = json.loads(PACKET.read_text())
    assert packet["schema"] == "e1-e34-generic-orbit-classifier-v1"
    assert packet["complete"] is True and packet["errors"] == []
    assert packet["primary_source_sha256"] == hashlib.sha256(PRIMARY.read_bytes()).hexdigest()
    assert packet["audit_source_sha256"] == hashlib.sha256(AUDIT.read_bytes()).hexdigest()
    primary = packet["results"]["primary"]
    audit = packet["results"]["audit"]
    for result in (primary, audit):
        assert result["complete"] is True
        assert result["generic_triples"] == 325376
        assert result["orbits"] == 57
        assert result["orbits"] == len(result["rows"])
    assert primary["rows"] == audit["rows"]
    assert sum(row["heavy_triples"] for row in primary["rows"]) == 325376

    for row in primary["rows"]:
        heavy = row["heavy"]
        assert heavy[0] == 0 and len(set(heavy)) == 3
        lengths = sorted(distance(left, right) for i, left in enumerate(heavy) for right in heavy[i + 1 :])
        assert lengths == row["lengths"] and len(set(lengths)) == 3 and 64 not in lengths
        welds = [weld(heavy, length) for length in lengths]
        assert [len(values) for values in welds] == row["weld_sizes"]
        assert [
            len(welds[0] & welds[1]),
            len(welds[0] & welds[2]),
            len(welds[1] & welds[2]),
        ] == row["pair_intersections"]
        assert len(welds[0] & welds[1] & welds[2]) == row["triple_intersection"]
        union = welds[0] | welds[1] | welds[2]
        assert len(union) == row["union_size"]
        supports = math.comb(125, 4)
        supports -= sum(math.comb(125 - len(values), 4) for values in welds)
        supports += sum(
            math.comb(125 - len(welds[i] | welds[j]), 4)
            for i, j in ((0, 1), (0, 2), (1, 2))
        )
        supports -= math.comb(125 - len(union), 4)
        assert supports == row["supports"]
        assert row["census_vectors"] == 64 * supports

    census_vectors = sum(row["census_vectors"] for row in primary["rows"])
    shapes = Counter(
        (
            tuple(row["weld_sizes"]),
            tuple(row["pair_intersections"]),
            row["triple_intersection"],
            row["union_size"],
            row["supports"],
        )
        for row in primary["rows"]
    )
    assert shapes == Counter(
        {
            ((4, 4, 4), (1, 1, 1), 0, 9, 66405): 52,
            ((3, 4, 4), (2, 1, 1), 0, 7, 72486): 4,
            ((3, 4, 3), (2, 1, 2), 0, 5, 58325): 1,
        }
    )
    assert census_vectors == 243285056
    print(
        "E1_E34_GENERIC_ORBIT_CHECK_PASS "
        f"orbits={primary['orbits']} triples=325376 census_vectors={census_vectors}"
    )


if __name__ == "__main__":
    main()
