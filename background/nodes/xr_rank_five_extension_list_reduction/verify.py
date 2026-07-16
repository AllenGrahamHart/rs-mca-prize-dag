#!/usr/bin/env python3
"""Replay the rank-five extension-list reduction and RowC residuals."""

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
NODE = "xr_rank_five_extension_list_reduction"
DEPENDENCY = "xr_rs_flat_nullity_basis_charge"
CONSUMERS = {"xr_highcore_collision_count", "xr_lowcore_spread_heart"}


def poly_mul(left: list[int], right: list[int], prime: int) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % prime
    return result


def poly_eval(poly: list[int], value: int, prime: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % prime
    return result


def matrix_rank(rows: list[list[int]], prime: int) -> int:
    matrix = [row[:] for row in rows]
    rank = 0
    width = len(matrix[0]) if matrix else 0
    for column in range(width):
        pivot = next(
            (index for index in range(rank, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], -1, prime)
        matrix[rank] = [(entry * inverse) % prime for entry in matrix[rank]]
        for index, row in enumerate(matrix):
            if index == rank or not row[column]:
                continue
            factor = row[column]
            matrix[index] = [
                (entry - factor * pivot_entry) % prime
                for entry, pivot_entry in zip(row, matrix[rank])
            ]
        rank += 1
    return rank


def extension_list_fixture() -> tuple[int, int, int]:
    """A finite GRS4-extension list with exact five-point agreements."""
    prime = 101
    domain = tuple(range(1, 9))
    received = [pow(point, 5, prime) for point in domain]
    by_quotient: dict[int, tuple[tuple[int, ...], list[int]]] = {}

    for support in itertools.combinations(domain, 5):
        locator = [1]
        for point in support:
            locator = poly_mul(locator, [(-point) % prime, 1], prime)
        code_poly = [(-coefficient) % prime for coefficient in locator]
        code_poly[5] = (code_poly[5] + 1) % prime
        if code_poly[5] != 0:
            raise AssertionError("degree-five term did not cancel")
        code_poly = code_poly[:5]
        quotient = code_poly[4]
        by_quotient.setdefault(quotient, (support, code_poly))

    rows = []
    agreement_sets = []
    for quotient, (support, code_poly) in sorted(by_quotient.items()):
        values = [poly_eval(code_poly, point, prime) for point in domain]
        agreements = {
            point
            for point, left, right in zip(domain, values, received)
            if left == right
        }
        if agreements != set(support) or len(agreements) != 5:
            raise AssertionError((quotient, support, agreements))
        if code_poly[4] != quotient:
            raise AssertionError("quotient coordinate")
        rows.append(values)
        agreement_sets.append(agreements)

    for left, right in itertools.combinations(agreement_sets, 2):
        if len(left & right) > 4:
            raise AssertionError("P-A pair cap")

    affine_rows = [
        [(entry - base) % prime for entry, base in zip(row, rows[0])]
        for row in rows[1:]
    ]
    affine_rank = matrix_rank(affine_rows, prime)
    if affine_rank != 5:
        raise AssertionError(("affine rank", affine_rank))
    return len(rows), affine_rank, max(
        len(left & right)
        for left, right in itertools.combinations(agreement_sets, 2)
    )


def flat_bounds(n: int, k: int, h: int, core: int, u: int, v: int) -> int:
    a = 4
    r = n - k
    g = k - a - u
    p = g - v
    pencil = (n - core) // (k + h - core)
    chart = r + a + u
    m0 = a + h + u + v
    mstar = a + h + u
    weight0 = m0 * comb(m0 - u - 1, a - 1)
    weightstar = mstar * comb(mstar - u - 1, a - 1)
    numerator = a * pencil * comb(chart, a) + v * (weight0 - weightstar)
    basis = max(v, numerator // weight0)
    threshold = core - p + 1
    packing = comb(n - p, threshold) // comb(k + h - p, threshold)
    return min(basis, packing)


def residual_table() -> tuple[tuple[int, ...], tuple[int, ...]]:
    n = 1024
    budget = 8 * n**3
    expected = (
        (256, 5, (14, 8, 10, 7, 1, 1)),
        (128, 5, (70, 49, 38, 29, 3, 2)),
        (64, 3, (323, 274, 60, 60, 7, 6)),
    )
    counts = []
    maxima = []
    for k, h, target in expected:
        row_counts = []
        row_maxima = []
        for core in (k, k - 1):
            residual = []
            for u in range(k - 3):
                for v in range(k - 3 - u):
                    if flat_bounds(n, k, h, core, u, v) > budget:
                        residual.append((u, v))
                        p = k - 4 - u - v
                        length = n - p
                        agreement = k + h - p
                        cap = core - p
                        if (length, agreement, cap) != (
                            n - k + 4 + u + v,
                            4 + h + u + v,
                            core - k + 4 + u + v,
                        ):
                            raise AssertionError("normalized parameters")
            row_counts.append(len(residual))
            row_maxima.extend((max(u for u, _ in residual), max(v for _, v in residual)))
        observed = (
            row_counts[0], row_counts[1],
            row_maxima[0], row_maxima[2],
            row_maxima[1], row_maxima[3],
        )
        if observed != target:
            raise AssertionError((k, h, observed, target))
        counts.extend(row_counts)
        maxima.extend(row_maxima)

    if (1024 - (256 - 4), 4 + 5, 4) != (772, 9, 4):
        raise AssertionError("u=v=0 base case")
    return tuple(counts), tuple(maxima)


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
    fixture_count, affine_rank, pair_cap = extension_list_fixture()
    counts, maxima = residual_table()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = mutation_controls(dag)
    print(
        "XR_RANK_FIVE_EXTENSION_LIST_REDUCTION_PASS "
        f"fixture={fixture_count} rank={affine_rank} cap={pair_cap} "
        f"residual={','.join(map(str, counts))} "
        f"maxima={','.join(map(str, maxima))} "
        f"mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
