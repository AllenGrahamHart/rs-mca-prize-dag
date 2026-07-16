#!/usr/bin/env python3
"""Replay the rank-five collision-line reuse-core theorem."""

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
NODE = "xr_rank_five_reuse_core"
DEPENDENCY = "xr_rank_five_extension_list_reduction"
CONSUMERS = {"xr_highcore_collision_count", "xr_lowcore_spread_heart"}


def reused_labels(family: list[frozenset[int]], rank: int) -> list[int]:
    labels: dict[tuple[int, ...], int] = {}
    for member in family:
        for label in itertools.combinations(sorted(member), rank):
            labels[label] = labels.get(label, 0) + 1
    return [
        sum(labels[label] >= 2 for label in itertools.combinations(sorted(member), rank))
        for member in family
    ]


def peel(family: list[frozenset[int]], rank: int, minimum: int) -> list[frozenset[int]]:
    current = family[:]
    while current:
        reuse = reused_labels(current, rank)
        victim = next((index for index, count in enumerate(reuse) if count < minimum), None)
        if victim is None:
            return current
        current.pop(victim)
    return []


def finite_peeling_fixture() -> tuple[int, int]:
    family = [frozenset(member) for member in itertools.combinations(range(7), 5)]
    if max(len(left & right) for left, right in itertools.combinations(family, 2)) != 4:
        raise AssertionError("intersection fixture")
    total_labels = comb(7, 4)
    budget = 10
    bases = comb(5, 4)
    minimum = bases - total_labels // (budget + 1)
    core = peel(family, 4, minimum)
    if len(family) <= budget or not core:
        raise AssertionError("peeling fixture")
    if min(reused_labels(core, 4)) < minimum:
        raise AssertionError("core degree")
    if peel(family, 4, bases + 1):
        raise AssertionError("impossible mutation")
    return len(core), minimum


def official_arithmetic() -> tuple[list[int], list[int], list[int]]:
    n = 1024
    budget = 8 * n**3
    rows = ((256, 5), (128, 5), (64, 3))
    expected_core = [125, 123, 31]
    expected_unique = [116548571, 215520801, 1021697885]
    expected_caps = [153, 179, 320]
    cores = []
    unique = []
    caps = []
    for k, h in rows:
        length = n - k + 4
        bases = comb(4 + h, 4)
        labels = comb(length, 4)
        cores.append(bases - labels // (budget + 1))
        unique.append(labels // bases)
        caps.append((n - k) // h)
    if cores != expected_core or unique != expected_unique or caps != expected_caps:
        raise AssertionError((cores, unique, caps))
    if any(bound >= budget for bound in unique):
        raise AssertionError("P-B base branch not paid")
    return cores, unique, caps


def validate_dag(data: dict[str, object]) -> None:
    nodes = {row["id"]: row for row in data["nodes"]}
    if nodes.get(NODE, {}).get("status") != "PROVED":
        raise AssertionError("node status")
    edges = {(row["from"], row["to"], row["kind"]) for row in data["edges"]}
    if (DEPENDENCY, NODE, "req") not in edges:
        raise AssertionError("dependency edge")
    for consumer in CONSUMERS:
        if (NODE, consumer, "ev") not in edges:
            raise AssertionError((consumer, "consumer edge"))


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
    fixture_size, fixture_minimum = finite_peeling_fixture()
    cores, unique, caps = official_arithmetic()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = mutation_controls(dag)
    print(
        "XR_RANK_FIVE_REUSE_CORE_PASS "
        f"fixture={fixture_size}:{fixture_minimum} "
        f"cores={','.join(map(str, cores))} "
        f"unique={','.join(map(str, unique))} "
        f"caps={','.join(map(str, caps))} "
        f"mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
