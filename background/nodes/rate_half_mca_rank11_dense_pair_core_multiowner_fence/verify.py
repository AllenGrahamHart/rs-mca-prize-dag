#!/usr/bin/env python3
"""Verify the deployed rank-11 dense-pair multi-owner construction."""

from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "dee54ff8775ce74b055271d822937f7855f0ac51312009270c48697bc0d819bd"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def trim(poly: list[int], p: int) -> list[int]:
    out = [value % p for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def degree(poly: list[int], p: int) -> int:
    value = trim(poly, p)
    return -1 if value == [0] else len(value) - 1


def add(left: list[int], right: list[int], p: int) -> list[int]:
    size = max(len(left), len(right))
    return trim(
        [
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
            for index in range(size)
        ],
        p,
    )


def subtract(left: list[int], right: list[int], p: int) -> list[int]:
    return add(left, [(-value) % p for value in right], p)


def scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return trim([scalar * value for value in poly], p)


def multiply(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return trim(out, p)


def evaluate(poly: list[int], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def locator(points: tuple[int, ...], p: int) -> list[int]:
    out = [1]
    for point in points:
        out = multiply(out, [(-point) % p, 1], p)
    return out


def interpolate(points: tuple[int, ...], values: tuple[int, ...], p: int) -> list[int]:
    out = [0]
    for i, (x_i, y_i) in enumerate(zip(points, values)):
        basis = [1]
        denominator = 1
        for j, x_j in enumerate(points):
            if i == j:
                continue
            basis = multiply(basis, [(-x_j) % p, 1], p)
            denominator = denominator * (x_i - x_j) % p
        out = add(out, scale(basis, y_i * pow(denominator, -1, p), p), p)
    return trim(out, p)


def matrix_rank(rows: list[list[int]], p: int) -> int:
    if not rows:
        return 0
    matrix = [[value % p for value in row] for row in rows]
    columns = max(len(row) for row in matrix)
    for row in matrix:
        row.extend([0] * (columns - len(row)))
    rank = 0
    for column in range(columns):
        pivot = next(
            (index for index in range(rank, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], -1, p)
        matrix[rank] = [(inverse * value) % p for value in matrix[rank]]
        for index, row in enumerate(matrix):
            if index == rank or not row[column]:
                continue
            factor = row[column]
            matrix[index] = [
                (left - factor * right) % p
                for left, right in zip(row, matrix[rank])
            ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def validate_official(row: object) -> dict[str, int]:
    require(isinstance(row, dict), "official record")
    fixed = (
        2130706433,
        6,
        2097152,
        1048576,
        1116048,
        67472,
        10,
        11,
        9,
        12,
    )
    require(
        tuple(
            row.get(key)
            for key in (
                "p",
                "extension_degree",
                "n",
                "K",
                "m",
                "w",
                "explanation_affine_rank",
                "error_rank",
                "polynomial_difference_rank",
                "pair_types",
            )
        )
        == fixed,
        "official constants",
    )
    p, extension_degree, n, dimension, agreement, w, _, _, d, pair_types = fixed
    require(p - 1 == 127 * 2**24, "base-field factorization")
    for prime, witness in ((2, 3), (127, 2)):
        require(pow(witness, p - 1, p) == 1, "Pocklington power")
        require(
            math.gcd(pow(witness, (p - 1) // prime, p) - 1, p) == 1,
            "Pocklington gcd",
        )
    shared = dimension - d
    petal = agreement - 1 - shared
    remainder = n - shared - pair_types * petal
    bad_bound = 8 * pair_types * (pair_types - 1) // 2
    forbidden = pair_types**2 * (remainder - 1)
    require(
        tuple(
            row.get(key)
            for key in (
                "shared_core_size",
                "petal_size",
                "pair_core_size",
                "core_deficiency",
                "remainder_size",
                "slopes_per_pair",
                "total_slopes",
                "bad_carrier_bound",
                "maximum_greedy_forbidden_values",
            )
        )
        == (
            shared,
            petal,
            agreement - 1,
            1,
            remainder,
            remainder,
            pair_types * remainder,
            bad_bound,
            forbidden,
        ),
        "official cardinality ledger",
    )
    require(bad_bound <= shared, "bad carriers fit shared core")
    require(forbidden < p**extension_degree, "extension-field avoidance")
    require(row.get("pr1168_forced_records") == 200632 < remainder, "record terminal")
    require(row.get("pr1168_forced_deficiency") == 4 and row.get("core_deficiency") == 1, "deficiency terminal")

    coefficients = row.get("q_coefficients_low_to_high")
    require(isinstance(coefficients, list) and len(coefficients) == pair_types, "q family")
    require(all(isinstance(poly, list) and len(poly) == d for poly in coefficients), "q width")
    differences = [subtract(poly, coefficients[0], p) for poly in coefficients[1:]]
    require(matrix_rank(differences, p) == d, "q affine span")
    for left in range(pair_types):
        for right in range(left):
            difference = subtract(coefficients[left], coefficients[right], p)
            require(degree(difference, p) in range(d), "nonzero bounded q difference")
    require(shared > 0 and agreement - 1 >= dimension, "uniqueness core")
    require(n - w > agreement and agreement - w == dimension, "post-near intersection")
    return {
        "pair_types": pair_types,
        "remainder": remainder,
        "total": pair_types * remainder,
        "forbidden": forbidden,
    }


def validate_toy(toy: object) -> dict[str, int]:
    require(isinstance(toy, dict), "toy record")
    p = toy.get("field")
    domain = toy.get("domain")
    dimension = toy.get("K")
    agreement = toy.get("m")
    w = toy.get("w")
    d = toy.get("polynomial_difference_rank")
    pair_types = toy.get("pair_types")
    shared = toy.get("shared_core")
    petals = toy.get("petals")
    remainder = toy.get("remainder")
    translations = toy.get("translation_values")
    require(
        (p, dimension, agreement, w, d, pair_types) == (29, 5, 6, 1, 2, 4),
        "toy constants",
    )
    require(
        domain == [28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        and shared == [28, 0, 1]
        and petals == [[2, 3], [4, 5], [6, 7], [8, 9]]
        and remainder == [10, 11, 12]
        and translations == [0, 1, 4],
        "toy partition",
    )
    pieces = [set(shared), *(set(petal) for petal in petals), set(remainder)]
    require(set().union(*pieces) == set(domain), "toy partition union")
    require(sum(len(piece) for piece in pieces) == len(domain), "toy partition disjoint")

    q_polys = ([0], [1], [0, 1], [1, 1])
    shared_locator = locator(tuple(shared), p)
    a_polys = [multiply(shared_locator, list(poly), p) for poly in q_polys]
    require(all(degree(poly, p) < dimension for poly in a_polys), "toy code degrees")
    require(
        all(
            len({evaluate(poly, x, p) for poly in a_polys}) == pair_types
            for x in set(domain) - set(shared)
        ),
        "toy pair separation",
    )

    r0: dict[int, int] = {x: 0 for x in shared}
    r1: dict[int, int] = {x: 1 for x in shared}
    for index, petal in enumerate(petals):
        for x in petal:
            r0[x] = evaluate(a_polys[index], x, p)
            r1[x] = 1
    for x, translation in zip(remainder, translations):
        r0[x] = translation
        r1[x] = 0

    slopes: set[int] = set()
    errors: list[list[int]] = []
    explanations: list[list[int]] = []
    loads = [0] * pair_types
    for index in range(pair_types):
        core = set(shared) | set(petals[index])
        require(len(core) == agreement - 1, "toy core size")
        for x in remainder:
            gamma = (r0[x] - evaluate(a_polys[index], x, p)) % p
            require(gamma not in slopes, "toy global slope collision")
            slopes.add(gamma)
            explanation = add(a_polys[index], [gamma], p)
            slope_values = [(r0[y] + gamma * r1[y]) % p for y in domain]
            explanation_values = [evaluate(explanation, y, p) for y in domain]
            agreement_set = {
                y for y, left, right in zip(domain, slope_values, explanation_values) if left == right
            }
            support = core | {x}
            require(agreement_set == support and len(support) == agreement, "toy exact support")

            points = tuple(y for y in domain if y in support)
            r0_interpolant = interpolate(points, tuple(r0[y] for y in points), p)
            r1_interpolant = interpolate(points, tuple(r1[y] for y in points), p)
            require(
                degree(r0_interpolant, p) >= dimension
                or degree(r1_interpolant, p) >= dimension,
                "toy pair noncontainment",
            )
            require(degree(r1_interpolant, p) >= dimension, "toy theta lower bound")
            require(sum(r1[y] != 1 for y in support) == 1, "toy theta upper bound")
            require(len(agreement_set) - w == dimension, "toy post-near intersection")
            error = [(left - right) % p for left, right in zip(slope_values, explanation_values)]
            errors.append(error)
            explanations.append(explanation_values)
            loads[index] += 1

    require(sorted(slopes) == toy.get("expected_slopes"), "toy slope set")
    require(loads == [len(remainder)] * pair_types, "toy pair loads")
    explanation_differences = [
        [(left - right) % p for left, right in zip(row, explanations[0])]
        for row in explanations[1:]
    ]
    explanation_rank = matrix_rank(explanation_differences, p)
    error_rank = matrix_rank(errors, p)
    require(explanation_rank == toy.get("expected_explanation_affine_rank") == 3, "toy explanation rank")
    require(error_rank == toy.get("expected_error_rank") == 4, "toy error rank")
    return {"records": len(errors), "explanation_rank": explanation_rank, "error_rank": error_rank}


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract object")
    require(data.get("schema") == "rate-half-mca-rank11-dense-pair-core-multiowner-fence-v1", "schema")
    upstream = data.get("upstream")
    require(
        upstream == {
            "pr1168_head": "6a5dcdae1591fc7f044eda6a942bfe178521a48c",
            "import_node": "rate_half_mca_rank11_pair_core_route_cut_import",
        },
        "upstream pins",
    )
    official = validate_official(data.get("official"))
    toy = validate_toy(data.get("toy"))
    return {**official, **{f"toy_{key}": value for key, value in toy.items()}}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["official"].__setitem__("remainder_size", 238824),
        lambda item: item["official"].__setitem__("pair_types", 11),
        lambda item: item["official"]["q_coefficients_low_to_high"].__setitem__(11, [0] * 9),
        lambda item: item["official"].__setitem__("extension_degree", 1),
        lambda item: item["official"].__setitem__("pr1168_forced_records", 238826),
        lambda item: item["toy"].__setitem__("translation_values", [0, 1, 3]),
        lambda item: item["toy"].__setitem__("expected_error_rank", 3),
        lambda item: item["upstream"].__setitem__("pr1168_head", "0" * 40),
    )
    controls = []
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_DENSE_PAIR_CORE_MULTIOWNER_FENCE_PASS "
        f"pairs={result['pair_types']} per_pair={result['remainder']} total={result['total']} "
        f"toy={result['toy_records']} ranks={result['toy_explanation_rank']}/{result['toy_error_rank']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
