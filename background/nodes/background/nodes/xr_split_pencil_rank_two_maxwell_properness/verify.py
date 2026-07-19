#!/usr/bin/env python3
"""Replay the XR rank-two Maxwell properness theorem."""

from __future__ import annotations

import copy
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3] if len(HERE.parents) > 3 else Path.cwd()
ROOT = REPO_ROOT if (REPO_ROOT / "dag.json").exists() else Path.cwd()
DAG = ROOT / "dag.json"
NODE = "xr_split_pencil_rank_two_maxwell_properness"
DEPENDENCIES = {
    "xr_split_pencil_trade_rank_two_support_atlas",
    "xr_split_pencil_maxwell_core_extraction",
}
CONSUMERS = ("xr_highcore_collision_count", "xr_lowcore_spread_heart")

ZERO_SETS = (
    ({0}, {1}, {2}, {3}),
    ({0}, {1, 2}, {3, 4}, {5, 6}),
    ({0, 1}, {2, 3}, {4, 5}, {6, 7}),
    ({0}, {1}, {2}, {3}, {4}),
    ({0}, {1}, {2}, {3}, {4}, {5}),
)
ACTIVE = (6, 7, 8, 6, 6)
EXPECTED = {
    (7, 3): (8, 2, 4, 9, 10),
    (8, 4): (12, 6, 8, 14, 16),
    (9, 5): (16, 10, 12, 19, 22),
    (10, 6): (20, 14, 16, 24, 28),
}


def sharp_blocks(profile: int, block_size: int) -> list[set[object]]:
    active = ACTIVE[profile]
    supports = [set(range(active)) - zeros for zeros in ZERO_SETS[profile]]
    blocks = [support.copy() for support in supports]
    needs = [block_size - len(support) for support in supports]

    for left, right in itertools.combinations(range(len(blocks)), 2):
        slack = 4 - len(supports[left] & supports[right])
        for slot in range(slack):
            if needs[left] == 0 or needs[right] == 0:
                raise AssertionError("insufficient extras for sharp sharing")
            label = ("shared", left, right, slot)
            blocks[left].add(label)
            blocks[right].add(label)
            needs[left] -= 1
            needs[right] -= 1

    for row, need in enumerate(needs):
        for slot in range(need):
            blocks[row].add(("private", row, slot))
    return blocks


def table_replay() -> dict[tuple[int, int], tuple[int, ...]]:
    got: dict[tuple[int, int], tuple[int, ...]] = {}
    for (block_size, parity_rows), expected in EXPECTED.items():
        deficits = []
        for profile in range(5):
            blocks = sharp_blocks(profile, block_size)
            if any(len(block) != block_size for block in blocks):
                raise AssertionError("block size")
            if any(len(a & b) > 4 for a, b in itertools.combinations(blocks, 2)):
                raise AssertionError("pair cap")
            union = set().union(*blocks)
            deficit = 2 * len(union) - 8 - parity_rows * len(blocks)
            deficits.append(deficit)
        got[(block_size, parity_rows)] = tuple(deficits)
        if tuple(deficits) != expected:
            raise AssertionError(((block_size, parity_rows), deficits, expected))
    if min(value for row in got.values() for value in row) != 2:
        raise AssertionError("global deficit floor")
    return got


def validate_dag(data: dict[str, object]) -> None:
    nodes = {row["id"]: row for row in data["nodes"]}
    if nodes.get(NODE, {}).get("status") != "PROVED":
        raise AssertionError("node status")
    edges = {(row["from"], row["to"], row["kind"]) for row in data["edges"]}
    for dependency in DEPENDENCIES:
        if (dependency, NODE, "req") not in edges:
            raise AssertionError(("dependency edge", dependency))
    for consumer in CONSUMERS:
        if (NODE, consumer, "ev") not in edges:
            raise AssertionError(("consumer edge", consumer))


def mutation_controls(dag: dict[str, object]) -> int:
    mutations = []
    changed = copy.deepcopy(dag)
    next(row for row in changed["nodes"] if row["id"] == NODE)["status"] = "TARGET"
    mutations.append(changed)
    for dependency in DEPENDENCIES:
        changed = copy.deepcopy(dag)
        changed["edges"] = [
            row
            for row in changed["edges"]
            if not (row["from"] == dependency and row["to"] == NODE)
        ]
        mutations.append(changed)
    caught = 0
    for mutation in mutations:
        try:
            validate_dag(mutation)
        except AssertionError:
            caught += 1
    if caught != len(mutations):
        raise AssertionError((caught, len(mutations)))
    return caught


def main() -> None:
    table = table_replay()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = mutation_controls(dag)
    print(
        "XR_SPLIT_PENCIL_RANK_TWO_MAXWELL_PROPERNESS_PASS "
        f"rows={len(table)} profiles={sum(map(len, table.values()))} "
        f"minimum={min(value for row in table.values() for value in row)} "
        f"mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
