#!/usr/bin/env python3
"""Replay the cubic block-tail energy nonimplication profiles."""

from __future__ import annotations

import copy
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3] if len(HERE.parents) > 3 else Path.cwd()
ROOT = REPO_ROOT if (REPO_ROOT / "dag.json").exists() else Path.cwd()
DAG = ROOT / "dag.json"
NODE = "f3_h3_cubic_block_tail_energy_fence"
DEPENDENCIES = {
    "f3_h3_quotient_block_identity",
    "f3_h3_identity_deficit_energy_close",
}
CONSUMERS = {"f3_h3_mobius_excess_half", "f3_h3_three_to_one_c36"}


def profile(exponent: int) -> tuple[int, dict[int, int]]:
    n = 1 << exponent
    mass = (n - 1) * (n - 2)
    counts: dict[int, int] = {}
    used = 0
    for level in range(3, exponent + 1):
        size = 1 << level
        count = 3 * n * n // (size**3)
        if count:
            counts[size] = count
            used += count * size * (size - 1)
    residual = mass - used
    if residual <= 0 or residual % 2:
        raise AssertionError(("residual", exponent, residual))
    counts[2] = residual // 2
    return n, counts


def check_profile(exponent: int) -> tuple[bool, Fraction]:
    n, counts = profile(exponent)
    mass = sum(count * size * (size - 1) for size, count in counts.items())
    if mass != (n - 1) * (n - 2):
        raise AssertionError(("mass", exponent, mass))

    worst = Fraction(0)
    for threshold in counts:
        tail = sum(count for size, count in counts.items() if size >= threshold)
        ratio = Fraction(tail * threshold**3, n * n)
        worst = max(worst, ratio)
        if ratio > 4:
            raise AssertionError(("tail", exponent, threshold, ratio))

    energy = (n - 1) ** 2 + sum(
        count * size * (size - 1) ** 2 for size, count in counts.items()
    )
    target = Fraction(145, 4) * (n - 1) ** 2
    return energy > target, worst


def profile_checks() -> tuple[int, tuple[int, ...], Fraction, int]:
    violations = []
    global_worst = Fraction(0)
    constant_mutations = 0
    for exponent in range(13, 42):
        violates, worst = check_profile(exponent)
        global_worst = max(global_worst, worst)
        if violates:
            violations.append(exponent)
            if worst > 3:
                constant_mutations += 1
    expected = tuple(range(22, 42))
    if tuple(violations) != expected:
        raise AssertionError((tuple(violations), expected))
    if constant_mutations != len(expected):
        raise AssertionError(("tail mutation", constant_mutations))
    return 29, expected, global_worst, constant_mutations


def validate_dag(data: dict[str, object]) -> None:
    nodes = {row["id"]: row for row in data["nodes"]}
    if nodes.get(NODE, {}).get("status") != "PROVED":
        raise AssertionError("node status")
    edges = {(row["from"], row["to"], row["kind"]) for row in data["edges"]}
    for dependency in DEPENDENCIES:
        if (dependency, NODE, "req") not in edges:
            raise AssertionError(("dependency", dependency))
    for consumer in CONSUMERS:
        if (NODE, consumer, "ev") not in edges:
            raise AssertionError(("consumer", consumer))


def dag_mutations(dag: dict[str, object]) -> tuple[int, int]:
    cases = []
    changed = copy.deepcopy(dag)
    next(row for row in changed["nodes"] if row["id"] == NODE)["status"] = "TARGET"
    cases.append(changed)
    for dependency in DEPENDENCIES:
        changed = copy.deepcopy(dag)
        changed["edges"] = [
            row
            for row in changed["edges"]
            if not (row["from"] == dependency and row["to"] == NODE)
        ]
        cases.append(changed)
    caught = 0
    for case in cases:
        try:
            validate_dag(case)
        except AssertionError:
            caught += 1
    if caught != len(cases):
        raise AssertionError((caught, len(cases)))
    return caught, len(cases)


def main() -> None:
    rows, violations, worst, mutations = profile_checks()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    caught, total = dag_mutations(dag)
    print(
        "F3_H3_CUBIC_BLOCK_TAIL_ENERGY_FENCE_PASS "
        f"rows={rows} violations={len(violations)} "
        f"first={violations[0]} last={violations[-1]} "
        f"worst_tail={worst} constant3_mutations={mutations} "
        f"dag_mutations={caught}/{total}"
    )


if __name__ == "__main__":
    main()
