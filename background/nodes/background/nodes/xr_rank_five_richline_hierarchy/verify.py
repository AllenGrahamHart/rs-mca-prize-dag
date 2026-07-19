#!/usr/bin/env python3
"""Replay the rank-five rich-line peeling hierarchy."""

from __future__ import annotations

import copy
import itertools
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3] if len(HERE.parents) > 3 else Path.cwd()
ROOT = REPO_ROOT if (REPO_ROOT / "dag.json").exists() else Path.cwd()
DAG = ROOT / "dag.json"
NODE = "xr_rank_five_richline_hierarchy"
DEPENDENCY = "xr_rank_five_reuse_core"
CONSUMER = "xr_highcore_collision_count"


def label_multiplicities(family: list[frozenset[int]], rank: int) -> dict[tuple[int, ...], int]:
    counts: dict[tuple[int, ...], int] = {}
    for member in family:
        for label in itertools.combinations(sorted(member), rank):
            counts[label] = counts.get(label, 0) + 1
    return counts


def peel(
    family: list[frozenset[int]], rank: int, line_size: int, minimum: int
) -> list[frozenset[int]]:
    current = family[:]
    while current:
        counts = label_multiplicities(current, rank)
        degrees = [
            sum(
                counts[label] >= line_size
                for label in itertools.combinations(sorted(member), rank)
            )
            for member in current
        ]
        victim = next((index for index, degree in enumerate(degrees) if degree < minimum), None)
        if victim is None:
            return current
        current.pop(victim)
    return []


def finite_fixture() -> tuple[int, int]:
    family = [frozenset(member) for member in itertools.combinations(range(7), 5)]
    total_labels = comb(7, 4)
    budget = 20
    bases = comb(5, 4)
    line_size = 3
    minimum = bases - ((line_size - 1) * total_labels) // (budget + 1)
    if minimum <= 0:
        raise AssertionError("finite hierarchy fixture is vacuous")
    core = peel(family, 4, line_size, minimum)
    if not core or len(family) <= budget:
        raise AssertionError("finite hierarchy core")
    counts = label_multiplicities(core, 4)
    if min(
        sum(counts[label] >= line_size for label in itertools.combinations(sorted(member), 4))
        for member in core
    ) < minimum:
        raise AssertionError("finite hierarchy degree")
    return len(core), minimum


def official_hierarchy() -> tuple[list[list[int]], list[tuple[int, int]]]:
    n = 1024
    budget = 8 * n**3
    rows = ((256, 5), (128, 5), (64, 3))
    marks = (2, 3, 4, 8, 16, 32)
    expected = (
        [125, 123, 121, 115, 101, 74],
        [123, 120, 117, 104, 79, 28],
        [31, 27, 23, 6, 0, 0],
    )
    expected_last = ((74, 2), (40, 3), (9, 2))
    tables = []
    lasts = []
    for k, h in rows:
        bases = comb(4 + h, 4)
        labels = comb(n - k + 4, 4)

        def degree(line_size: int) -> int:
            return max(0, bases - ((line_size - 1) * labels) // (budget + 1))

        table = [degree(line_size) for line_size in marks]
        cap = (n - k) // h
        last = max(line_size for line_size in range(2, cap + 1) if degree(line_size) > 0)
        tables.append(table)
        lasts.append((last, degree(last)))
    if tuple(tables) != expected or tuple(lasts) != expected_last:
        raise AssertionError((tables, lasts))
    return tables, lasts


def validate_dag(data: dict[str, object]) -> None:
    nodes = {row["id"]: row for row in data["nodes"]}
    if nodes.get(NODE, {}).get("status") != "PROVED":
        raise AssertionError("node status")
    edges = {(row["from"], row["to"], row["kind"]) for row in data["edges"]}
    if (DEPENDENCY, NODE, "req") not in edges:
        raise AssertionError("dependency edge")
    if (NODE, CONSUMER, "ev") not in edges:
        raise AssertionError("consumer edge")


def mutation_controls(dag: dict[str, object]) -> int:
    mutations = []
    changed = copy.deepcopy(dag)
    next(row for row in changed["nodes"] if row["id"] == NODE)["status"] = "TARGET"
    mutations.append(changed)
    changed = copy.deepcopy(dag)
    changed["edges"] = [
        row for row in changed["edges"]
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
    fixture_size, fixture_minimum = finite_fixture()
    tables, lasts = official_hierarchy()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = mutation_controls(dag)
    print(
        "XR_RANK_FIVE_RICHLINE_HIERARCHY_PASS "
        f"fixture={fixture_size}:{fixture_minimum} "
        f"d3={','.join(str(table[1]) for table in tables)} "
        f"last={','.join(f'{line}:{degree}' for line, degree in lasts)} "
        f"mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
