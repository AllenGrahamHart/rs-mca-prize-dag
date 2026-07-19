#!/usr/bin/env python3
"""Replay the H3 coupling-matrix odd-saturation theorem."""

from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_double_accident_coupling_matrix_odd_saturation"
DEPENDENCIES = {
    "f3_h3_double_accident_coupling_batch_odd_saturation",
    "f3_h3_shifted_product_sidon",
}
CONSUMER = "f3_h3_mobius_excess_half"


def load_helpers():
    sys.dont_write_bytecode = True
    path = ROOT / "background" / "nodes" / "f3_h3_double_accident_low_distance_joint_ideal_router" / "verify.py"
    spec = importlib.util.spec_from_file_location("joint_ideal_verify", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


H = load_helpers()
PI = [1, -1]
PI_SQUARED = H.multiply(PI, PI)


def normalized_shift(exponent: int) -> list[int]:
    return H.divide_exact(H.shifted(exponent), PI)


def coupling(product_pair: tuple[int, int], quotient: tuple[int, int]) -> list[int]:
    u, v = quotient
    return H.subtract(
        H.multiply(H.beta(product_pair), normalized_shift(u)), normalized_shift(v)
    )


def product_generator(
    baseline: tuple[int, int], other: tuple[int, int]
) -> list[int]:
    return H.divide_exact(H.subtract(H.beta(other), H.beta(baseline)), PI_SQUARED)


def theta(left: tuple[int, int], right: tuple[int, int]) -> list[int]:
    u0, v0 = left
    u1, v1 = right
    return H.subtract(
        H.multiply(normalized_shift(v1), normalized_shift(u0)),
        H.multiply(normalized_shift(v0), normalized_shift(u1)),
    )


def negate(poly: list[int]) -> list[int]:
    return [-coefficient for coefficient in poly]


def zero(poly: list[int], n: int) -> bool:
    return H.reduce_cyclotomic(poly, n) == [0]


def direction_identities() -> tuple[int, int]:
    n = 8
    products = tuple(itertools.combinations_with_replacement(range(1, n), 2))
    quotients = tuple((u, v) for u in range(1, n) for v in range(1, n) if u != v)

    product_checks = 0
    for baseline, other in itertools.combinations(products, 2):
        alpha = product_generator(baseline, other)
        for quotient in quotients:
            left = H.subtract(coupling(other, quotient), coupling(baseline, quotient))
            right = H.multiply(
                H.multiply(PI_SQUARED, normalized_shift(quotient[0])), alpha
            )
            assert zero(H.subtract(left, right), n)
            product_checks += 1

    quotient_checks = 0
    baseline = products[0]
    for left_q, right_q in itertools.combinations(quotients, 2):
        left = H.subtract(
            H.multiply(normalized_shift(left_q[0]), coupling(baseline, right_q)),
            H.multiply(normalized_shift(right_q[0]), coupling(baseline, left_q)),
        )
        assert zero(H.subtract(left, negate(theta(left_q, right_q))), n)
        quotient_checks += 1
    assert (product_checks, quotient_checks) == (15876, 861)
    return product_checks, quotient_checks


def zero_matching_check() -> tuple[int, int, int]:
    n = 8
    products = tuple(itertools.combinations_with_replacement(range(1, n), 2))
    quotients = tuple((u, v) for u in range(1, n) for v in range(1, n) if u != v)
    matrix = [[zero(coupling(product, quotient), n) for quotient in quotients] for product in products]
    row_max = max(sum(row) for row in matrix)
    column_max = max(sum(matrix[row][column] for row in range(len(products))) for column in range(len(quotients)))
    total = sum(sum(row) for row in matrix)
    assert (row_max, column_max, total) == (1, 1, 6)
    return row_max, column_max, total


def finite_fixture() -> tuple[int, int, int]:
    n, p, generator = 32, 1153, 194
    products = ((2, 25), (5, 10), (6, 8))
    quotients = ((9, 4), (23, 26))
    norms: list[list[int]] = []
    for product in products:
        row = []
        for quotient in quotients:
            value = coupling(product, quotient)
            assert H.evaluate(value, generator, p) == 0
            row.append(H.principal_norm(value, n))
        norms.append(row)
    assert norms == [[0, 2306], [73792, 1478146], [9224, 2306]]
    nonzero = [value for row in norms for value in row if value]
    assert len(nonzero) == 5
    common = 0
    for value in nonzero:
        common = gcd(common, value)
    assert common == 2 * p
    return len(nonzero), common, sum(value == 0 for row in norms for value in row)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "lambda_(i,j)-lambda_(0,j)=pi^2 c_(u_j)alpha_i",
        "I_joint O[1/2]=I_cross O[1/2]=I_rect O[1/2]",
        ">= mr-min(m,r)",
        "partial matching",
        "does not provide",
    ):
        assert marker in statement


def main() -> None:
    product_checks, quotient_checks = direction_identities()
    row_max, column_max, zeros = zero_matching_check()
    nonzero, common, fixture_zeros = finite_fixture()
    packet_check()
    print(
        "F3_H3_DOUBLE_ACCIDENT_COUPLING_MATRIX_ODD_SATURATION_PASS "
        f"identities={product_checks}/{quotient_checks} zero_matching={row_max}/{column_max}/{zeros} "
        f"fixture={nonzero}/{fixture_zeros}/{common}"
    )


if __name__ == "__main__":
    main()
