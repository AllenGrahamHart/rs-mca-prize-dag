#!/usr/bin/env python3
"""Replay the rank-five u=1 split-locator nonbasis bound."""

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
NODE = "xr_rank_five_u1_split_locator_nonbasis_bound"
DEPENDENCY = "xr_rank_five_extension_list_reduction"
CONSUMERS = ("xr_highcore_collision_count", "xr_lowcore_spread_heart")
PRIME = 101


def multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    output = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] = (output[i + j] + a * b) % PRIME
    return tuple(output)


def locator(points: tuple[int, ...]) -> tuple[int, ...]:
    output = (1,)
    for point in points:
        output = multiply(output, ((-point) % PRIME, 1))
    return output


def dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(a * b for a, b in zip(left, right)) % PRIME


def finite_fixtures() -> tuple[int, int, int]:
    domain = tuple(range(1, 11))
    functionals = (
        (3, 5, 7, 11, 13),
        (1, 0, 0, 0, 0),
        (0, 0, 0, 0, 1),
    )
    checked = 0
    peak = 0
    for functional in functionals:
        actual = sum(
            dot(functional, locator(points)) == 0
            for points in itertools.combinations(domain, 4)
        )
        bound = (comb(len(domain), 3) + 8 * 6) // 4
        if actual > bound:
            raise AssertionError((functional, actual, bound))

        degenerate = 0
        completions = 0
        for triple in itertools.combinations(domain, 3):
            cubic = locator(triple)
            padded = cubic + (0,)
            shifted = (0,) + cubic
            left = dot(functional, padded)
            right = dot(functional, shifted)
            if left == 0 and right == 0:
                degenerate += 1
            completions += sum(
                dot(functional, locator(tuple(sorted(triple + (x,))))) == 0
                for x in domain
                if x not in triple
            )
        if completions != 4 * actual:
            raise AssertionError((functional, completions, actual))
        if functional == functionals[0] and degenerate > len(domain) - 2:
            raise AssertionError((functional, degenerate))
        checked += 1
        peak = max(peak, actual)

    evaluation = tuple(pow(0, degree, PRIME) for degree in range(5))
    if sum(dot(evaluation, locator(points)) == 0 for points in itertools.combinations(domain, 4)):
        raise AssertionError("outside-domain evaluation should contain no locator")
    return checked, peak, len(domain)


def official_arithmetic() -> tuple[list[int], list[int], list[int]]:
    rows = ((773, 10), (901, 10), (965, 8))
    global_bounds = []
    local_bounds = []
    basis_floors = []
    for length, size in rows:
        global_bounds.append(
            (comb(length, 3) + (length - 2) * (length - 4)) // 4
        )
        local = (comb(size, 3) + (size - 2) * (size - 4)) // 4
        local_bounds.append(local)
        basis_floors.append(comb(size, 4) - local)
    if global_bounds != [19319011, 30576563, 37558043]:
        raise AssertionError(global_bounds)
    if local_bounds != [42, 42, 20] or basis_floors != [168, 168, 50]:
        raise AssertionError((local_bounds, basis_floors))
    return global_bounds, local_bounds, basis_floors


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
    fixtures, peak, toy_length = finite_fixtures()
    global_bounds, local_bounds, basis_floors = official_arithmetic()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = mutation_controls(dag)
    print(
        "XR_RANK_FIVE_U1_SPLIT_LOCATOR_NONBASIS_BOUND_PASS "
        f"fixtures={fixtures}:{toy_length}:{peak} "
        f"global={','.join(map(str, global_bounds))} "
        f"local={','.join(map(str, local_bounds))} "
        f"bases={','.join(map(str, basis_floors))} "
        f"mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
