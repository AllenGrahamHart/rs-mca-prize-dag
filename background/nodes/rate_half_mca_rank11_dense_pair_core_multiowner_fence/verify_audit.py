#!/usr/bin/env python3
"""Independent audit of the rank-11 dense-pair multi-owner fence."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "dee54ff8775ce74b055271d822937f7855f0ac51312009270c48697bc0d819bd"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def rank(rows: list[list[int]], p: int) -> int:
    matrix = [[value % p for value in row] for row in rows]
    if not matrix:
        return 0
    width = max(len(row) for row in matrix)
    for row in matrix:
        row.extend([0] * (width - len(row)))
    pivot_row = 0
    for column in range(width):
        pivot = next((i for i in range(pivot_row, len(matrix)) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], -1, p)
        matrix[pivot_row] = [(inverse * value) % p for value in matrix[pivot_row]]
        for i in range(pivot_row + 1, len(matrix)):
            factor = matrix[i][column]
            if factor:
                matrix[i] = [
                    (left - factor * right) % p
                    for left, right in zip(matrix[i], matrix[pivot_row])
                ]
        pivot_row += 1
    return pivot_row


def check(data: object) -> None:
    require(isinstance(data, dict), "object")
    row = data.get("official")
    toy = data.get("toy")
    require(isinstance(row, dict) and isinstance(toy, dict), "records")

    n, dimension, agreement, w, d, pair_types = (
        row.get(key)
        for key in ("n", "K", "m", "w", "polynomial_difference_rank", "pair_types")
    )
    require((n, dimension, agreement, w, d, pair_types) == (2097152, 1048576, 1116048, 67472, 9, 12), "official constants")
    shared = dimension - d
    petal = agreement - 1 - shared
    remainder = n - shared - pair_types * petal
    require(
        (shared, petal, remainder, pair_types * remainder)
        == (1048567, 67480, 238825, 2865900),
        "official partition",
    )
    require(
        tuple(
            row.get(key)
            for key in (
                "shared_core_size",
                "petal_size",
                "remainder_size",
                "total_slopes",
            )
        )
        == (shared, petal, remainder, pair_types * remainder),
        "stored official partition",
    )
    require(row.get("pair_core_size") == shared + petal == agreement - 1, "core")
    require(row.get("slopes_per_pair") == remainder > row.get("pr1168_forced_records"), "heavy terminal")
    require(row.get("core_deficiency") == 1 <= row.get("pr1168_forced_deficiency"), "deficiency")
    require(8 * 66 == row.get("bad_carrier_bound") <= shared, "root avoidance")
    require(
        pair_types**2 * (remainder - 1) == row.get("maximum_greedy_forbidden_values")
        < row.get("p") ** row.get("extension_degree"),
        "field avoidance",
    )
    require(agreement - w == dimension and n - w > agreement, "post-near root ledger")

    coefficients = row.get("q_coefficients_low_to_high")
    require(isinstance(coefficients, list) and len(coefficients) == 12, "q family")
    differences = [
        [(value - base) % row["p"] for value, base in zip(poly, coefficients[0])]
        for poly in coefficients[1:]
    ]
    require(rank(differences, row["p"]) == 9, "q rank")

    # Separate finite check of the translated slope blocks in the GF(29) toy.
    p = toy.get("field")
    require(p == 29, "toy field")
    shared_toy = toy.get("shared_core")
    remainder_toy = toy.get("remainder")
    translations = toy.get("translation_values")
    require((shared_toy, remainder_toy, translations) == ([28, 0, 1], [10, 11, 12], [0, 1, 4]), "toy data")

    def locator_value(x: int) -> int:
        value = 1
        for root in shared_toy:
            value = value * (x - root) % p
        return value

    def q_value(index: int, x: int) -> int:
        return (0, 1, x, x + 1)[index] % p

    slopes = []
    for x, translation in zip(remainder_toy, translations):
        block = [
            (translation - locator_value(x) * q_value(index, x)) % p
            for index in range(4)
        ]
        require(len(set(block)) == 4, "toy block")
        slopes.extend(block)
    require(len(set(slopes)) == 12 and sorted(slopes) == toy.get("expected_slopes"), "toy slope packing")
    require(toy.get("expected_explanation_affine_rank") == 3, "toy explanation rank")
    require(toy.get("expected_error_rank") == 4, "toy error rank")


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    check(data)
    controls = []
    for section, key, value in (
        ("official", "petal_size", 67479),
        ("official", "core_deficiency", 5),
        ("toy", "translation_values", [0, 1, 3]),
        ("toy", "expected_explanation_affine_rank", 2),
    ):
        altered = copy.deepcopy(data)
        altered[section][key] = value
        try:
            check(altered)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "audit controls")
    print(
        "RATE_HALF_MCA_RANK11_DENSE_PAIR_CORE_MULTIOWNER_FENCE_AUDIT_PASS "
        f"pairs=12 per_pair=238825 toy_slopes=12 controls={sum(controls)}/4"
    )


if __name__ == "__main__":
    main()
