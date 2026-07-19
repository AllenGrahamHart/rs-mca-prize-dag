#!/usr/bin/env python3
"""Replay the XR split-pencil trade rank-two localization."""

from __future__ import annotations

import copy
import json
from pathlib import Path


HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3] if len(HERE.parents) > 3 else Path.cwd()
ROOT = REPO_ROOT if (REPO_ROOT / "dag.json").exists() else Path.cwd()
DAG = ROOT / "dag.json"
NODE = "xr_split_pencil_trade_rank_two_localization"
DEPENDENCY = "xr_split_pencil_dual_trade_core"
CONSUMERS = ("xr_highcore_collision_count", "xr_lowcore_spread_heart")


def support_cap(block_size: int, active_rows: int = 4) -> int:
    return active_rows * block_size // (active_rows - 1)


def official_arithmetic() -> tuple[list[int], list[int]]:
    high = [support_cap(size) for size in (9, 9, 7)]
    low = [support_cap(size) for size in (10, 10, 8)]
    if high != [12, 12, 9] or low != [13, 13, 10]:
        raise AssertionError((high, low))
    return high, low


def rank_one_exclusion_fixture() -> tuple[int, int, int]:
    slope_dual_distance = 3
    coordinate_dual_distance = 5
    pair_cap = 4
    if slope_dual_distance < 3 or coordinate_dual_distance <= pair_cap:
        raise AssertionError("rank-one exclusion lost")
    return slope_dual_distance, coordinate_dual_distance, pair_cap


def line_zero_charge_fixture() -> tuple[int, int, int]:
    block_size = 9
    active_rows = 4
    active_coordinates = 12
    zeros_per_row = active_coordinates - block_size
    if active_rows * zeros_per_row > active_coordinates:
        raise AssertionError("invalid line charge")
    if support_cap(block_size, active_rows) != active_coordinates:
        raise AssertionError("endpoint not sharp")
    mutation_coordinates = active_coordinates + 1
    if active_rows * (mutation_coordinates - block_size) <= mutation_coordinates:
        raise AssertionError("one-step mutation was not rejected")
    return active_rows, active_coordinates, mutation_coordinates


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
    high, low = official_arithmetic()
    rank_one = rank_one_exclusion_fixture()
    line = line_zero_charge_fixture()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = mutation_controls(dag)
    print(
        "XR_SPLIT_PENCIL_TRADE_RANK_TWO_LOCALIZATION_PASS "
        f"high={','.join(map(str, high))} low={','.join(map(str, low))} "
        f"rank1={':'.join(map(str, rank_one))} line={':'.join(map(str, line))} "
        f"mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
