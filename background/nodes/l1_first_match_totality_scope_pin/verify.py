#!/usr/bin/env python3
"""Verify finite first-owner totality and the L1 scope wiring."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_first_match_totality_scope_pin"
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    checks = 0

    # Exhaust every nonempty carrying-key assignment on small finite universes.
    for key_count in range(1, 4):
        nonempty_masks = range(1, 1 << key_count)
        for item_count in range(0, 5):
            for masks in itertools.product(nonempty_masks, repeat=item_count):
                owners = tuple((mask & -mask).bit_length() - 1 for mask in masks)
                cells = {
                    key: {item for item, owner in enumerate(owners) if owner == key}
                    for key in range(key_count)
                }
                flattened = set().union(*cells.values()) if cells else set()
                assert flattened == set(range(item_count))
                assert sum(len(cell) for cell in cells.values()) == item_count
                for left in range(key_count):
                    for right in range(left + 1, key_count):
                        assert cells[left].isdisjoint(cells[right])
                checks += 2 + key_count * (key_count - 1) // 2

    # Total-key fibers are the singleton-carrying-set specialization.
    for key_count in range(1, 5):
        for item_count in range(0, 6):
            for keys in itertools.product(range(key_count), repeat=item_count):
                fibers = {
                    key: {item for item, value in enumerate(keys) if value == key}
                    for key in range(key_count)
                }
                assert set().union(*fibers.values()) == set(range(item_count))
                assert sum(len(fiber) for fiber in fibers.values()) == item_count
                checks += 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (NODE, CONSUMER, "ev") in edges
    checks += 2

    base = ROOT / "background" / "nodes" / NODE
    statement = (base / "statement.md").read_text()
    contract = (base / "claim_contract.md").read_text()
    for marker in (
        "I=disjoint_union_chi C_chi",
        "payment theorem",
        "does not promote",
        "polynomial **aggregate payment**",
    ):
        assert marker in statement + contract
        checks += 1

    print(f"L1_FIRST_MATCH_TOTALITY_SCOPE_PIN_PASS checks={checks}")


if __name__ == "__main__":
    main()
