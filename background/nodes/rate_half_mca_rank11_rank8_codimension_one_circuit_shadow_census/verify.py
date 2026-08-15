#!/usr/bin/env python3
"""Verify the K'=11 rank-eight fixed-circuit shadow census."""

from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "c6e5d380725fb05eee4fe901c8884eaae9806545c70024ef1a58af18e56e3e7f"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    rows = [[value % prime for value in row] for row in matrix]
    if not rows or not rows[0]:
        return 0
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [(value * inverse) % prime for value in rows[rank]]
        for i, row in enumerate(rows):
            if i == rank:
                continue
            factor = row[column]
            if factor:
                rows[i] = [
                    (left - factor * right) % prime
                    for left, right in zip(row, rows[rank])
                ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def evaluate(coefficients: list[int], point: int, prime: int) -> int:
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * point + coefficient) % prime
    return value


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % prime
    return result


def locator(points: list[int], prime: int) -> list[int]:
    result = [1]
    for point in points:
        result = multiply(result, [(-point) % prime, 1], prime)
    return result


def restrict(matrix: list[list[int]], columns: tuple[int, ...] | list[int]) -> list[list[int]]:
    return [[row[column] for column in columns] for row in matrix]


def hyperplane_matrix(circuit_size: int, prime: int) -> tuple[list[list[int]], list[int]]:
    points = list(range(1, 12))
    circuit = points[:circuit_size]
    moments = [
        sum(pow(point, degree, prime) for point in circuit) % prime
        for degree in range(11)
    ]
    require(moments[0] == circuit_size, "nonzero constant moment")
    inverse = pow(moments[0], -1, prime)
    basis = []
    for degree in range(1, 11):
        polynomial = [0] * 11
        polynomial[degree] = 1
        polynomial[0] = (-moments[degree] * inverse) % prime
        basis.append(polynomial)
    matrix = [[evaluate(poly, point, prime) for point in points] for poly in basis]
    return matrix, points


def count_shadows(matrix: list[list[int]], prime: int) -> tuple[int, int, int]:
    rank8 = 0
    rank9 = 0
    for omitted in combinations(range(11), 2):
        columns = tuple(index for index in range(11) if index not in omitted)
        rank = rank_mod(restrict(matrix, columns), prime)
        require(rank in (8, 9), "nine-shadow rank")
        rank8 += rank == 8
        rank9 += rank == 9
    bases = 0
    for omitted in range(11):
        columns = tuple(index for index in range(11) if index != omitted)
        bases += rank_mod(restrict(matrix, columns), prime) == 10
    return rank8, rank9, bases


def eight_petal_matrix(prime: int) -> list[list[int]]:
    points = list(range(1, 12))
    b_points = points[:9]
    locator_b = locator(b_points, prime)
    basis = []
    for degree in range(8):
        polynomial = [0] * 11
        polynomial[degree] = 1
        basis.append(polynomial)
    basis.append(locator_b + [0] * (11 - len(locator_b)))
    shifted = [0] + locator_b
    basis.append(shifted + [0] * (11 - len(shifted)))
    return [[evaluate(poly, point, prime) for point in points] for poly in basis]


def validate(data: object) -> dict[str, object]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-rank8-codimension-one-circuit-shadow-census-v1",
        "schema",
    )
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_shortened_partial_relative_router",
        "rate_half_mca_rank11_dense_root_highspan_saturation",
        "rate_half_mca_rank11_component_ninesubset_target_router",
        "rate_half_mca_rank11_rank8_minimal_shortening_exclusion",
        "rate_half_mca_rank11_rank8_fixed_chart_local_cap_fence",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["residual_dimension"] == p["ambient_rs_dimension"] == 11, "ambient row")
    require(p["correction_space_dimension"] == 10, "hyperplane dimension")
    require(
        p["selector_size"] == 9
        and p["selector_rank"] == 8
        and p["selector_kernel_dimension"] == 2,
        "selector dimensions",
    )
    require(p["empty_global_common_support"] is True, "empty common support")
    require(p["fixed_chart_record_floor"] == 2578110, "fixed-chart floor")
    require(p["minimum_distinct_slopes_for_loop_exclusion"] == 2, "two-root exclusion")
    circuit_sizes = list(range(2, 10))
    rank8_counts = [comb(11 - c, 2) for c in circuit_sizes]
    rank9_counts = [55 - value for value in rank8_counts]
    require(p["circuit_size_minimum"] == 2, "circuit minimum")
    require(p["circuit_size_maximum"] == 9, "circuit maximum")
    require(p["total_nine_shadows"] == comb(11, 2) == 55, "shadow total")
    require(p["circuit_sizes"] == circuit_sizes, "circuit sizes")
    require(p["rank8_shadow_counts"] == rank8_counts, "rank-eight counts")
    require(p["rank9_shadow_counts"] == rank9_counts, "rank-nine counts")
    require(p["rank10_basis_counts"] == circuit_sizes, "basis counts")
    require(p["locator_ideal_dimensions"] == [11 - c for c in circuit_sizes], "ideal dimensions")
    require(p["sharp_circuit_sizes"] == circuit_sizes, "sharp sizes")
    require(p["eight_petal_circuit_size"] == 9, "eight-petal endpoint")

    prime = 101
    replay = []
    for c, expected8, expected9 in zip(circuit_sizes, rank8_counts, rank9_counts):
        matrix, points = hyperplane_matrix(c, prime)
        require(rank_mod(matrix, prime) == 10, f"hyperplane rank c={c}")
        require(rank_mod(restrict(matrix, tuple(range(9))), prime) == 8, f"B rank c={c}")
        require(all(any(row[column] for row in matrix) for column in range(11)), f"loopless c={c}")
        relation = [sum(matrix[row][column] for column in range(c)) % prime for row in range(10)]
        require(relation == [0] * 10, f"circuit relation c={c}")
        ideal_c = locator(points[:c], prime)
        for shift in range(11 - c):
            polynomial = [0] * shift + ideal_c
            require(
                sum(evaluate(polynomial, point, prime) for point in points[:c]) % prime == 0,
                f"locator ideal c={c} shift={shift}",
            )
        observed8, observed9, bases = count_shadows(matrix, prime)
        require((observed8, observed9, bases) == (expected8, expected9, c), f"census c={c}")
        replay.append([c, observed8, observed9, bases])

    petal = eight_petal_matrix(prime)
    require(rank_mod(restrict(petal, tuple(range(9))), prime) == 8, "petal B rank")
    require(count_shadows(petal, prime) == (1, 54, 9), "petal census")
    return {"prime": prime, "rows": replay, "petal": [1, 54, 9]}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("residual_dimension", 12),
        lambda item: item["parameters"].__setitem__("selector_rank", 9),
        lambda item: item["parameters"].__setitem__("empty_global_common_support", False),
        lambda item: item["parameters"].__setitem__("circuit_size_minimum", 1),
        lambda item: item["parameters"]["rank8_shadow_counts"].__setitem__(0, 35),
        lambda item: item["parameters"]["rank9_shadow_counts"].__setitem__(7, 53),
        lambda item: item["parameters"]["locator_ideal_dimensions"].__setitem__(0, 8),
        lambda item: item["parameters"].__setitem__("eight_petal_circuit_size", 8),
    )
    caught = 0
    for mutation in mutations:
        changed = copy.deepcopy(data)
        mutation(changed)
        try:
            validate(changed)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "hostile mutations")
    print(
        "RATE_HALF_MCA_RANK11_RANK8_CODIMENSION_ONE_CIRCUIT_SHADOW_CENSUS_PASS "
        f"toy=GF({result['prime']}) rows={len(result['rows'])} "
        f"petal={'/'.join(map(str, result['petal']))} controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
