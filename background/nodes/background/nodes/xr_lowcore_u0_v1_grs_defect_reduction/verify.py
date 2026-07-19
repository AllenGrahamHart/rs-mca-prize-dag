#!/usr/bin/env python3
"""Replay the XR low-core one-loop GRS defect reduction."""

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
NODE = "xr_lowcore_u0_v1_grs_defect_reduction"
DEPENDENCY = "xr_rank_five_extension_list_reduction"
CONSUMER = "xr_lowcore_spread_heart"
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

    agreement_sets = []
    for fiber, color in zip(fibers, colors):
        codeword = {x: color * direction[x] % PRIME for x in domain}
        agreement_sets.append(
            {x for x in domain if (u[x] - codeword[x]) % PRIME == 0}
        )
    if any(len(left & right) != 4 for left, right in itertools.combinations(agreement_sets, 2)):
        raise AssertionError("pair cap fixture")

    loop_received = 7
    loop_agreements = sum(color == loop_received for color in colors)
    if loop_agreements != 1:
        raise AssertionError(loop_agreements)

    clique_checks = 0
    for agreement, color in zip(agreement_sets, colors):
        for subset in itertools.combinations(sorted(agreement), 5):
            qdd = divided_difference(q, subset)
            if qdd == 0:
                raise AssertionError(("zero denominator", subset))
            phi = divided_difference(u, subset) * inverse(qdd) % PRIME
            if phi != color:
                raise AssertionError((subset, phi, color))
            clique_checks += 1
    return len(agreement_sets), loop_agreements, clique_checks


def official_arithmetic() -> list[tuple[int, ...]]:
    n = 1024
    budget = 8 * n**3
    rows = ((772, 10), (900, 10), (964, 8))
    expected = [
        (1, 209, 207, 123, 2, 63, 105, 97650, 5),
        (3, 207, 204, 67, 2, 35, 103, 52530, 5),
        (4, 66, 62, 17, 4, 10, 33, 1782, 3),
    ]
    output = []
    for length, size in rows:
        labels = comb(length, 4)
        bases = comb(size, 4)
        external = size - 4
        line_cap = (length - 4) // external
        candidates = []
        last = None
        for line_size in range(2, line_cap + 1):
            degree = bases - ((line_size - 1) * labels) // budget
            if degree > 0:
                last = (line_size, degree)
                candidates.append(
                    (
                        degree * (line_size - 1) * comb(external, 2),
                        line_size,
                        degree,
                    )
                )
        collisions, best_line, best_degree = max(candidates)
        complement = labels // budget
        rigidity = max(
            d for d in range(external + 1) if comb(size - d, 4) > complement
        )
        output.append(
            (
                complement,
                bases - labels // budget,
                bases - (2 * labels) // budget,
                last[0],
                last[1],
                best_line,
                best_degree,
                collisions,
                rigidity,
            )
        )
    if output != expected:
        raise AssertionError(output)
    return output


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
    members, loop_agreements, clique_checks = finite_fixture()
    official = official_arithmetic()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = mutation_controls(dag)
    print(
        "XR_LOWCORE_U0_V1_GRS_DEFECT_REDUCTION_PASS "
        f"fixture={members}:{loop_agreements}:{clique_checks} "
        f"official={';'.join(','.join(map(str, row)) for row in official)} "
        f"mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
