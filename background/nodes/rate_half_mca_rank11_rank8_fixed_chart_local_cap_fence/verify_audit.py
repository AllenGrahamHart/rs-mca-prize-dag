#!/usr/bin/env python3
"""Independent finite-field audit of the rank-eight eight-petal model."""

from __future__ import annotations

import hashlib
import json
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "553bbf5c9ba10d97f220480d50aea1dd7017407ddd833459f513992b97667093"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def poly_mul(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return out


def poly_eval(coefficients: list[int], x: int, prime: int) -> int:
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * x + coefficient) % prime
    return value


def matrix_rank(matrix: list[list[int]], prime: int) -> int:
    rows = [row[:] for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column] % prime), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [(value * inverse) % prime for value in rows[rank]]
        for i, row in enumerate(rows):
            if i == rank or not row[column] % prime:
                continue
            factor = row[column] % prime
            rows[i] = [(a - factor * b) % prime for a, b in zip(row, rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def toy_geometry() -> tuple[int, int, int, int]:
    prime = 1009
    domain = list(range(1, 20))
    selector = domain[:9]
    petals = [domain[9:12], domain[12:15]]
    remainder = domain[15:]
    owner_parameters = [0, 1]

    u0 = [1]
    for root in selector:
        u0 = poly_mul(u0, [(-root) % prime, 1], prime)
    u1 = [0] + u0
    monomials = [[0] * degree + [1] for degree in range(8)]
    basis = monomials + [u0, u1]

    def evaluation(points: list[int]) -> list[list[int]]:
        return [[poly_eval(poly, x, prime) for poly in basis] for x in points]

    require(matrix_rank(evaluation(selector), prime) == 8, "toy selector rank")
    extension_checks = 0
    for x, y in combinations(domain[9:], 2):
        require(matrix_rank(evaluation(selector + [x, y]), prime) == 10, "toy extension rank")
        extension_checks += 1

    a_values = {
        (owner, x): owner * poly_eval(u0, x, prime) % prime
        for owner in owner_parameters for x in domain
    }
    r0 = {x: 0 for x in selector}
    r1 = {x: 1 for x in selector}
    for owner, petal in enumerate(petals):
        for x in petal:
            r0[x] = a_values[(owner, x)]
            r1[x] = 1
    slopes: set[int] = set()
    records: list[tuple[int, int, int]] = []
    for x in remainder:
        chosen = None
        for received_value in range(prime):
            candidates = {
                (received_value - a_values[(owner, x)]) % prime
                for owner in owner_parameters
            }
            if len(candidates) == len(owner_parameters) and candidates.isdisjoint(slopes):
                chosen = received_value
                break
        require(chosen is not None, "toy greedy choice")
        r0[x], r1[x] = chosen, 0
        for owner in owner_parameters:
            slope = (chosen - a_values[(owner, x)]) % prime
            slopes.add(slope)
            records.append((owner, x, slope))

    require(len(slopes) == len(owner_parameters) * len(remainder), "toy slope count")
    error_vectors: list[list[int]] = []
    component_checks = 0
    for owner, singled, slope in records:
        support = []
        error = []
        for x in domain:
            explanation = (a_values[(owner, x)] + slope) % prime
            line_value = (r0[x] + slope * r1[x]) % prime
            error.append((line_value - explanation) % prime)
            if line_value == explanation:
                support.append(x)
        expected = selector + petals[owner] + [singled]
        require(support == expected, "toy exact support")
        error_vectors.append(error)

        for x, y in combinations(petals[owner], 2):
            tuple_points = selector + [x, y]
            require(matrix_rank(evaluation(tuple_points), prime) == 10, "toy component rank")
            require(all(
                r0[z] == a_values[(owner, z)] and r1[z] == 1
                for z in tuple_points
            ), "toy component owner")
            component_checks += 1

        eval_support = [
            [pow(x, degree, prime) for degree in range(11)]
            for x in support
        ]
        augmented = [row + [r1[x]] for row, x in zip(eval_support, support)]
        require(matrix_rank(eval_support, prime) == 11, "toy RS support rank")
        require(matrix_rank(augmented, prime) == 12, "toy pair noncontainment")

    anchor = error_vectors[0]
    differences = [
        [(a - b) % prime for a, b in zip(error, anchor)]
        for error in error_vectors[1:]
    ]
    require(matrix_rank(differences, prime) <= 2, "toy error affine rank")
    return len(records), len(slopes), component_checks, extension_checks


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    parameters = json.loads(CONTRACT.read_text())["parameters"]
    require(
        parameters["fixed_selector_size"] + 8 * parameters["petal_size"]
        + parameters["remainder_size"] == parameters["residual_n"],
        "independent partition",
    )
    require(
        parameters["rich_slope_count"]
        * parameters["component_extensions_per_record"]
        == parameters["marked_component_weight"],
        "independent marked count",
    )
    records, slopes, component_checks, extension_checks = toy_geometry()
    proof = (HERE / "proof.md").read_text()
    normalized_proof = " ".join(proof.split())
    require("u_0(x)u_0(y)(y-x) !=0" in proof, "determinant proof pin")
    require(
        "normalized deviations do not span the complete ten-space" in normalized_proof,
        "nonclaim proof pin",
    )
    print(
        "RATE_HALF_MCA_RANK11_RANK8_FIXED_CHART_LOCAL_CAP_FENCE_AUDIT_PASS "
        f"toy_records={records} toy_slopes={slopes} "
        f"components={component_checks} rank_checks={extension_checks}"
    )


if __name__ == "__main__":
    main()
