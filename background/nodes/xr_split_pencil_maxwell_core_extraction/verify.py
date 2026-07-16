#!/usr/bin/env python3
"""Replay the XR split-pencil Maxwell-core extraction."""

from __future__ import annotations

import copy
import json
from pathlib import Path


HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3] if len(HERE.parents) > 3 else Path.cwd()
ROOT = REPO_ROOT if (REPO_ROOT / "dag.json").exists() else Path.cwd()
DAG = ROOT / "dag.json"
NODE = "xr_split_pencil_maxwell_core_extraction"
DEPENDENCY = "xr_grs_split_pencil_rank_certificate"
CONSUMERS = ("xr_highcore_collision_count", "xr_lowcore_spread_heart")


def row_bound(length: int, block_size: int) -> tuple[int, int]:
    constraints = block_size - 4
    core_size = (2 * length + constraints - 9) // constraints
    private_cap = (constraints - 1) // 2
    return core_size, private_cap


def official_arithmetic() -> tuple[list[int], list[int], list[int], list[int]]:
    high = [row_bound(*row) for row in ((772, 9), (900, 9), (964, 7))]
    low = [row_bound(*row) for row in ((772, 10), (900, 10), (964, 8))]
    high_sizes = [row[0] for row in high]
    low_sizes = [row[0] for row in low]
    high_private = [row[1] for row in high]
    low_private = [row[1] for row in low]
    if high_sizes != [308, 359, 640]:
        raise AssertionError(high_sizes)
    if low_sizes != [256, 299, 480]:
        raise AssertionError(low_sizes)
    if high_private != [2, 2, 1] or low_private != [2, 2, 1]:
        raise AssertionError((high_private, low_private))
    return high_sizes, low_sizes, high_private, low_private


def finite_minimal_fixture() -> tuple[int, int, int, int]:
    domain = set(range(6))
    blocks = [domain - {omitted} for omitted in range(4)]
    constraints = 1
    union = set().union(*blocks)
    excess = constraints * len(blocks) - (2 * len(union) - 8)
    if excess != 0:
        raise AssertionError(excess)
    for index in range(len(blocks)):
        proper = blocks[:index] + blocks[index + 1 :]
        proper_union = set().union(*proper)
        if constraints * len(proper) > 2 * len(proper_union) - 9:
            raise AssertionError((index, proper_union))
        private = blocks[index] - set().union(*proper)
        if excess + 2 * len(private) > constraints - 1:
            raise AssertionError((index, private))
    left_nullity_floor = excess + 1
    return len(blocks), len(union), excess, left_nullity_floor


def validate_dag(data: dict[str, object]) -> None:
    nodes = {row["id"]: row for row in data["nodes"]}
    if nodes.get(NODE, {}).get("status") != "PROVED":
        raise AssertionError("node status")
    edges = {(row["from"], row["to"], row["kind"]) for row in data["edges"]}
    if (DEPENDENCY, NODE, "req") not in edges:
        raise AssertionError("dependency edge")
    for consumer in CONSUMERS:
        if (NODE, consumer, "ev") not in edges:
            raise AssertionError(("consumer edge", consumer))


def mutation_controls(dag: dict[str, object]) -> int:
    mutations = []
    changed = copy.deepcopy(dag)
    next(row for row in changed["nodes"] if row["id"] == NODE)["status"] = "TARGET"
    mutations.append(changed)
    changed = copy.deepcopy(dag)
    changed["edges"] = [
        row
        for row in changed["edges"]
        if not (row["from"] == DEPENDENCY and row["to"] == NODE)
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
    high, low, high_private, low_private = official_arithmetic()
    fixture = finite_minimal_fixture()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = mutation_controls(dag)
    print(
        "XR_SPLIT_PENCIL_MAXWELL_CORE_EXTRACTION_PASS "
        f"high={','.join(map(str, high))} low={','.join(map(str, low))} "
        f"private={','.join(map(str, high_private))}:{','.join(map(str, low_private))} "
        f"fixture={':'.join(map(str, fixture))} mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
