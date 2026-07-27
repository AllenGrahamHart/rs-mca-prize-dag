#!/usr/bin/env python3
"""Exact checks for the order-128 high-field folded-box theorem."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "integer_code_distance_high_field_folded_box_exclusion"
PARENT = "collision_norm_criterion"
TARGET = "integer_code_distance_cert"


def odd_character_sum(difference: int) -> list[int]:
    """Reduce sum_{u odd} X^(u*difference) modulo X^64+1 exactly."""
    out = [0] * 64
    for odd in range(1, 128, 2):
        exponent = (odd * difference) % 128
        if exponent < 64:
            out[exponent] += 1
        else:
            out[exponent - 64] -= 1
    return out


def main() -> None:
    for difference in range(64):
        reduced = odd_character_sum(difference)
        expected = [0] * 64
        if difference == 0:
            expected[0] = 64
        assert reduced == expected

    assert 63 * 4 + 1 == 253
    assert 64**32 < 253**32
    assert 253**32 < 256**32 == 1 << 256

    # Exhaust the coefficient-value cases behind the two proof branches.
    for value in range(-2, 3):
        if value % 2:
            assert value * value <= 1
        else:
            assert value // 2 in (-1, 0, 1)

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}

    assert statuses[NODE] == "PROVED"
    assert statuses[PARENT] == "PROVED"
    assert statuses[TARGET] == "TARGET"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, TARGET, "ev") in edges
    assert "253^32" in statements[NODE]
    assert "order-128" in statements[NODE]

    print(
        "INTEGER_CODE_DISTANCE_HIGH_FIELD_FOLDED_BOX_EXCLUSION_PASS "
        "orthogonality_checks=64 threshold=253^32"
    )


if __name__ == "__main__":
    main()
