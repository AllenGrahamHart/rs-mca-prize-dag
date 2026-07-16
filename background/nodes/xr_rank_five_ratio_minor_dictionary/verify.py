#!/usr/bin/env python3
"""Replay the rank-five ratio-fiber and maximal-minor dictionary."""

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
NODE = "xr_rank_five_ratio_minor_dictionary"
DEPENDENCY = "xr_rank_five_richline_hierarchy"
CONSUMER = "xr_highcore_collision_count"
PRIME = 101


def determinant(matrix: list[list[int]]) -> int:
    work = [[entry % PRIME for entry in row] for row in matrix]
    value = 1
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column]), None
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            value = -value
        pivot_value = work[column][column]
        value = value * pivot_value % PRIME
        inverse = pow(pivot_value, PRIME - 2, PRIME)
        for row in range(column + 1, len(work)):
            scale = work[row][column] * inverse % PRIME
            for other in range(column, len(work)):
                work[row][other] = (
                    work[row][other] - scale * work[column][other]
                ) % PRIME
    return value % PRIME


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
        total += value * numerator * pow(denominator % PRIME, PRIME - 2, PRIME)
    return total % PRIME


def finite_fixture() -> tuple[int, int, int]:
    domain = tuple(range(1, 13))
    core = domain[:4]
    agreement = set(domain[:6])
    first_fiber = set(domain[6:8])
    second_fiber = set(domain[8:10])
    q = {x: pow(x, 4, PRIME) for x in domain}
    interpolated = {x: interpolate({t: q[t] for t in core}, x) for x in domain}
    residual_direction = {x: (q[x] - interpolated[x]) % PRIME for x in domain}
    z = {x: 0 for x in agreement}
    for x in first_fiber:
        z[x] = 7 * residual_direction[x] % PRIME
    for x in second_fiber:
        z[x] = 11 * residual_direction[x] % PRIME
    z[domain[10]] = 17 * residual_direction[domain[10]] % PRIME
    z[domain[11]] = 18 * residual_direction[domain[11]] % PRIME

    codewords = (
        {x: 0 for x in domain},
        {x: 7 * residual_direction[x] % PRIME for x in domain},
        {x: 11 * residual_direction[x] % PRIME for x in domain},
    )
    agreement_sets = [
        {x for x in domain if (z[x] - codeword[x]) % PRIME == 0}
        for codeword in codewords
    ]
    if agreement_sets != [agreement, set(core) | first_fiber, set(core) | second_fiber]:
        raise AssertionError(agreement_sets)
    if any(len(left & right) != 4 for left, right in itertools.combinations(agreement_sets, 2)):
        raise AssertionError("pair cap fixture")

    vandermonde = [[pow(x, degree, PRIME) for x in core] for degree in range(4)]
    vandermonde_det = determinant(vandermonde)
    if not vandermonde_det:
        raise AssertionError("Vandermonde fixture")
    zeros = 0
    identities = 0
    for x, y in itertools.combinations(domain[4:], 2):
        columns = core + (x, y)
        matrix = [
            [pow(point, degree, PRIME) for point in columns] for degree in range(4)
        ]
        matrix.append([q[point] for point in columns])
        matrix.append([z[point] for point in columns])
        left = determinant(matrix)
        right = vandermonde_det * (
            residual_direction[x] * z[y] - residual_direction[y] * z[x]
        ) % PRIME
        if left != right:
            raise AssertionError((x, y, left, right))
        identities += 1
        if left == 0:
            zeros += 1
    if zeros != 3:
        raise AssertionError("heavy-fiber minors")
    return len(agreement_sets), identities, zeros


def official_bounds() -> list[tuple[int, int, int]]:
    n = 1024
    budget = 8 * n**3
    rows = ((256, 5), (128, 5), (64, 3))
    expected = [(39, 62, 23560), (22, 60, 12600), (5, 19, 228)]
    results = []
    for k, h in rows:
        bases = comb(4 + h, 4)
        labels = comb(n - k + 4, 4)
        line_cap = (n - k) // h
        candidates = []
        for line_size in range(2, line_cap + 1):
            degree = bases - ((line_size - 1) * labels) // (budget + 1)
            if degree > 0:
                candidates.append(
                    (degree * (line_size - 1) * comb(h, 2), line_size, degree)
                )
        collisions, line_size, degree = max(candidates)
        results.append((line_size, degree, collisions))
    if results != expected:
        raise AssertionError(results)
    return results


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
    members, identities, zeros = finite_fixture()
    official = official_bounds()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = mutation_controls(dag)
    print(
        "XR_RANK_FIVE_RATIO_MINOR_DICTIONARY_PASS "
        f"fixture={members}:{identities}:{zeros} "
        f"official={','.join(f'{r}:{d}:{z}' for r, d, z in official)} "
        f"mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
