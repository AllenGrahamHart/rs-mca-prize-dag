#!/usr/bin/env python3
"""Replay the XR split-pencil dual-trade normal form."""

from __future__ import annotations

import copy
import json
from pathlib import Path


HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3] if len(HERE.parents) > 3 else Path.cwd()
ROOT = REPO_ROOT if (REPO_ROOT / "dag.json").exists() else Path.cwd()
DAG = ROOT / "dag.json"
NODE = "xr_split_pencil_dual_trade_core"
DEPENDENCY = "xr_split_pencil_maxwell_core_extraction"
CONSUMERS = ("xr_highcore_collision_count", "xr_lowcore_spread_heart")
PRIME = 101


def inverse(value: int) -> int:
    return pow(value % PRIME, PRIME - 2, PRIME)


def dual_word(points: tuple[int, ...], values: list[int]) -> list[int]:
    result = []
    for index, point in enumerate(points):
        denominator = 1
        for other_index, other in enumerate(points):
            if index != other_index:
                denominator = denominator * (point - other) % PRIME
        result.append(values[index] * inverse(denominator) % PRIME)
    return result


def block_dual_fixture() -> tuple[int, int]:
    points = (2, 5, 9, 14, 20, 27, 35)
    polynomial = [(x * x + 3 * x + 7) % PRIME for x in points]
    word = dual_word(points, polynomial)
    for degree in range(4):
        moment = sum(value * pow(x, degree, PRIME) for x, value in zip(points, word)) % PRIME
        if moment:
            raise AssertionError((degree, moment))
    weight = sum(value != 0 for value in word)
    if weight < 5:
        raise AssertionError(weight)
    return len(points), weight


def slope_dual_fixture() -> tuple[int, int]:
    slopes = (3, 11, 24, 40, 63)
    polynomial = [(2 * slope * slope + 5 * slope + 9) % PRIME for slope in slopes]
    word = dual_word(slopes, polynomial)
    moments = [
        sum(value * pow(slope, degree, PRIME) for slope, value in zip(slopes, word)) % PRIME
        for degree in range(2)
    ]
    if moments != [0, 0]:
        raise AssertionError(moments)
    active = sum(value != 0 for value in word)
    if active < 3:
        raise AssertionError(active)
    return len(slopes), active


def low_degree_exclusion() -> int:
    slopes = (1, 7)
    determinant = (slopes[1] - slopes[0]) % PRIME
    if determinant == 0:
        raise AssertionError("distinct-slope determinant vanished")
    return 2


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
    block = block_dual_fixture()
    slope = slope_dual_fixture()
    degree_floor = low_degree_exclusion()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = mutation_controls(dag)
    print(
        "XR_SPLIT_PENCIL_DUAL_TRADE_CORE_PASS "
        f"block={block[0]}:{block[1]} slope={slope[0]}:{slope[1]} "
        f"degree_floor={degree_floor} mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
