#!/usr/bin/env python3
"""Replay the XR u=1 augmented-paving scope and arithmetic fence."""

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
NODE = "xr_lowcore_u1_augmented_paving_scope_fence"
DEPENDENCIES = {
    "xr_rank_five_extension_list_reduction",
    "xr_rank_five_u1_split_locator_nonbasis_bound",
}
CONSUMER = "xr_lowcore_spread_heart"


def rank(matrix: list[list[int]], prime: int) -> int:
    rows = [[value % prime for value in row] for row in matrix]
    pivot_row = 0
    width = len(rows[0])
    for col in range(width):
        pivot = next((r for r in range(pivot_row, len(rows)) if rows[r][col]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = pow(rows[pivot_row][col], prime - 2, prime)
        rows[pivot_row] = [(scale * value) % prime for value in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row or not rows[row][col]:
                continue
            factor = rows[row][col]
            rows[row] = [
                (left - factor * right) % prime
                for left, right in zip(rows[row], rows[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def non_mds_witness() -> tuple[int, int, bool]:
    prime = 101
    domain = tuple(range(7))
    bad_set = (0, 1, 2, 3)

    def locator(value: int) -> int:
        answer = 1
        for root in bad_set:
            answer = answer * (value - root) % prime
        return answer

    rows = [[1, x, x * x, locator(x)] for x in domain]
    global_rank = rank(rows, prime)
    local_rank = rank([rows[x] for x in bad_set], prime)
    common_root = any(all(entry == 0 for entry in row) for row in rows)
    if (global_rank, local_rank, common_root) != (4, 3, False):
        raise AssertionError((global_rank, local_rank, common_root))
    return global_rank, local_rank, common_root


def official_arithmetic() -> tuple[list[int], int, int, int]:
    budget = 8 * 1024**3
    rows = ((773, 10), (901, 10), (965, 8))
    ceilings = [comb(length, 5) // comb(agreement, 5) for length, agreement in rows]
    expected = [9_009_204_611, 19_418_424_240, 123_242_307_467]
    if ceilings != expected or not all(value > budget for value in ceilings):
        raise AssertionError((ceilings, budget))

    ambient = comb(773, 5)
    local_charge = comb(10, 5)
    beta_threshold = local_charge * (budget + 1) - 1
    saving = ambient - beta_threshold
    if (ambient, local_charge, beta_threshold, saving) != (
        2_270_319_562_049,
        252,
        2_164_663_517_435,
        105_656_044_614,
    ):
        raise AssertionError((ambient, local_charge, beta_threshold, saving))
    if beta_threshold // local_charge != budget:
        raise AssertionError("threshold does not pay")
    if (beta_threshold + 1) // local_charge != budget + 1:
        raise AssertionError("threshold mutation does not fail")
    return ceilings, budget, beta_threshold, saving


def validate_dag(data: dict[str, object]) -> None:
    nodes = {row["id"]: row for row in data["nodes"]}
    if nodes.get(NODE, {}).get("status") != "PROVED":
        raise AssertionError("node status")
    edges = {(row["from"], row["to"], row["kind"]) for row in data["edges"]}
    for dependency in DEPENDENCIES:
        if (dependency, NODE, "req") not in edges:
            raise AssertionError(("dependency edge", dependency))
    if (NODE, CONSUMER, "ev") not in edges:
        raise AssertionError("consumer edge")


def dag_mutation_controls(dag: dict[str, object]) -> int:
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
    global_rank, local_rank, common_root = non_mds_witness()
    ceilings, budget, beta_threshold, saving = official_arithmetic()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = dag_mutation_controls(dag)
    print(
        "XR_LOWCORE_U1_AUGMENTED_PAVING_SCOPE_FENCE_PASS "
        f"ranks={global_rank}/{local_rank} common_root={int(common_root)} "
        f"ceilings={','.join(map(str, ceilings))} budget={budget} "
        f"beta_threshold={beta_threshold} saving={saving} "
        f"dag_mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
