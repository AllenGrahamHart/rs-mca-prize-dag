#!/usr/bin/env python3
"""Verify dense-root factorization and high-span saturation."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "9847a084251f60c01dabceda6a29f64b11df92cdb06352e922a19fa4ba1e79a6"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def rank_mod(vectors: list[list[int]], field: int) -> int:
    rows = [[entry % field for entry in vector] for vector in vectors]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, field)
        rows[rank] = [(inverse * value) % field for value in rows[rank]]
        for i in range(len(rows)):
            if i == rank or not rows[i][column]:
                continue
            scale = rows[i][column]
            rows[i] = [(a - scale * b) % field for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def multiply(left: list[int], right: list[list[int]], field: int) -> list[list[int]]:
    dimension = len(right[0])
    product = [[0] * dimension for _ in range(len(left) + len(right) - 1)]
    for i, scalar in enumerate(left):
        for j, vector in enumerate(right):
            for coordinate, value in enumerate(vector):
                product[i + j][coordinate] = (
                    product[i + j][coordinate] + scalar * value
                ) % field
    return product


def evaluate(coefficients: list[list[int]], slope: int, field: int) -> list[int]:
    value = [0] * len(coefficients[0])
    for coefficient in reversed(coefficients):
        value = [
            (slope * entry + addend) % field
            for entry, addend in zip(value, coefficient)
        ]
    return value


def locator(roots: list[int], field: int) -> list[int]:
    coefficients = [1]
    for root in roots:
        next_coefficients = [0] * (len(coefficients) + 1)
        for i, value in enumerate(coefficients):
            next_coefficients[i] = (next_coefficients[i] - root * value) % field
            next_coefficients[i + 1] = (next_coefficients[i + 1] + value) % field
        coefficients = next_coefficients
    return coefficients


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank11-dense-root-highspan-saturation-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == [
            "rate_half_mca_rank11_global_core_rankdrop_highcomplexity_router",
            "rate_half_mca_rank11_relative_correction_tenflat_collapse",
        ],
        "dependencies",
    )
    parameters = data.get("parameters")
    require(
        parameters
        == {
            "dense_root_count": 18,
            "slope_degree_maximum": 31,
            "quotient_degree_maximum": 13,
            "deviation_dimension": 10,
            "high_coefficient_start": 2,
            "triangular_coefficient_start": 18,
            "surviving_correction_dimension": 10,
        },
        "parameter pins",
    )
    require(18 + 13 == 31, "degree split")
    require(18 >= parameters["high_coefficient_start"], "high range")
    require(len(data.get("logical_pins", [])) == 5, "logical pins")

    toy = data.get("toy")
    require(isinstance(toy, dict), "toy")
    field = toy.get("field")
    roots = toy.get("dense_roots")
    dimension = toy.get("quotient_vector_dimension")
    count = toy.get("quotient_coefficient_count")
    slopes = toy.get("basis_evaluation_slopes")
    require(field == 101, "field")
    require(roots == list(range(18)), "roots")
    require((dimension, count) == (10, 14), "quotient dimensions")
    require(slopes == list(range(18, 28)), "basis slopes")

    quotient = []
    for index in range(count):
        vector = [0] * dimension
        if index < dimension:
            vector[index] = 1
        else:
            vector = [pow(index + 1, coordinate, field) for coordinate in range(dimension)]
        quotient.append(vector)
    q = locator(roots, field)
    require(len(q) == 19 and q[-1] == 1, "monic locator")
    deviation = multiply(q, quotient, field)
    require(len(deviation) == 32, "degree")
    require(all(evaluate(deviation, root, field) == [0] * dimension for root in roots), "roots vanish")
    high = deviation[18:32]
    require(rank_mod(quotient, field) == dimension, "quotient span")
    require(rank_mod(high, field) == dimension, "triangular high span")
    values = [evaluate(deviation, slope, field) for slope in slopes]
    require(rank_mod(values, field) == dimension, "basis value span")
    require("aggregate mass" in str(data.get("nonclaim")), "nonclaim")
    return {"roots": len(roots), "rank": rank_mod(high, field)}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("dense_root_count", 17),
        lambda item: item["parameters"].__setitem__("quotient_degree_maximum", 14),
        lambda item: item["parameters"].__setitem__("surviving_correction_dimension", 9),
        lambda item: item["logical_pins"].pop(),
        lambda item: item["toy"]["dense_roots"].pop(),
        lambda item: item["toy"]["basis_evaluation_slopes"].__setitem__(0, 0),
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
        "RATE_HALF_MCA_RANK11_DENSE_ROOT_HIGHSPAN_SATURATION_PASS "
        f"roots={result['roots']} rank={result['rank']} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
