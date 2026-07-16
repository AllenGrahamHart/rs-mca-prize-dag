#!/usr/bin/env python3
"""Replay the XR divided-difference clique bridge."""

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
NODE = "xr_rank_five_divided_difference_clique_bridge"
DEPENDENCY = "xr_rank_five_ratio_minor_dictionary"
CONSUMER = "xr_highcore_collision_count"
PRIME = 101


def inverse(value: int) -> int:
    return pow(value % PRIME, PRIME - 2, PRIME)


def interpolate(values: dict[int, int], x: int) -> int:
    total = 0
    for point, value in values.items():
        numerator = 1
        denominator = 1
        for other in values:
            if other == point:
                continue
            numerator = numerator * (x - other) % PRIME
            denominator = denominator * (point - other) % PRIME
        total += value * numerator * inverse(denominator)
    return total % PRIME


def divided_difference(values: dict[int, int], subset: tuple[int, ...]) -> int:
    total = 0
    for point in subset:
        denominator = 1
        for other in subset:
            if other != point:
                denominator = denominator * (point - other) % PRIME
        total += values[point] * inverse(denominator)
    return total % PRIME


def finite_fixture() -> tuple[int, int, int]:
    domain = tuple(range(1, 13))
    core = domain[:4]
    fibers = (domain[4:6], domain[6:8], domain[8:10])
    colors = (0, 7, 11)
    q = {x: pow(x, 4, PRIME) for x in domain}
    iq = {x: interpolate({t: q[t] for t in core}, x) for x in domain}
    direction = {x: (q[x] - iq[x]) % PRIME for x in domain}

    u = {x: 17 * direction[x] % PRIME for x in domain}
    for fiber, color in zip(fibers, colors):
        for x in fiber:
            u[x] = color * direction[x] % PRIME
    for x in core:
        u[x] = 0

    agreements = []
    for fiber, color in zip(fibers, colors):
        codeword = {x: color * direction[x] % PRIME for x in domain}
        agreement = {
            x for x in domain if (u[x] - codeword[x]) % PRIME == 0
        }
        if agreement != set(core) | set(fiber):
            raise AssertionError((agreement, fiber))
        agreements.append(agreement)

    checked = 0
    for agreement, color in zip(agreements, colors):
        for subset in itertools.combinations(sorted(agreement), 5):
            qdd = divided_difference(q, subset)
            if qdd == 0:
                raise AssertionError(("zero denominator", subset))
            if divided_difference(u, subset) * inverse(qdd) % PRIME != color:
                raise AssertionError(("wrong color", subset, color))
            checked += 1

    star_checks = 0
    for x in domain[4:]:
        subset = tuple(sorted(core + (x,)))
        phi = divided_difference(u, subset) * inverse(
            divided_difference(q, subset)
        ) % PRIME
        ratio = u[x] * inverse(direction[x]) % PRIME
        if phi != ratio:
            raise AssertionError((x, phi, ratio))
        star_checks += 1
    return len(agreements), checked, star_checks


def official_arithmetic() -> tuple[list[int], list[int]]:
    n = 1024
    budget = 8 * n**3
    rows = ((256, 5), (128, 5), (64, 3))
    deficits = []
    packing = []
    for k, h in rows:
        size = 4 + h
        labels = comb(n - k + 4, 4)
        bases = comb(size, 4)
        deficits.append(labels // (budget + 1))
        if bases - labels // (budget + 1) <= 0:
            raise AssertionError("empty reuse core")
        packing.append(comb(n - k + 4, 5) // comb(size, 5))
    if deficits != [1, 3, 4]:
        raise AssertionError(deficits)
    expected = [17901860650, 38621327680, 326943323437]
    if packing != expected:
        raise AssertionError(packing)
    if not all(value > budget for value in packing):
        raise AssertionError("packing route unexpectedly pays")
    return deficits, packing


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
    members, clique_checks, star_checks = finite_fixture()
    deficits, packing = official_arithmetic()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = mutation_controls(dag)
    print(
        "XR_RANK_FIVE_DIVIDED_DIFFERENCE_CLIQUE_BRIDGE_PASS "
        f"fixture={members}:{clique_checks}:{star_checks} "
        f"deficits={','.join(map(str, deficits))} "
        f"packing={','.join(map(str, packing))} "
        f"mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
