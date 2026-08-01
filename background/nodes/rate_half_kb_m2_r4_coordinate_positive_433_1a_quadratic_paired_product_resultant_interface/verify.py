#!/usr/bin/env python3
"""Verify the positive 433-1a quadratic paired-product interface."""

from fractions import Fraction
import itertools
import json
from pathlib import Path


NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "quadratic_paired_product_resultant_interface"
)
PARENTS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_kernel_uniqueness",
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_o0b_signed_edge_atlas",
    "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def determinant(matrix):
    total = 0
    for permutation in itertools.permutations(range(len(matrix))):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(len(matrix))
            for j in range(i + 1, len(matrix))
        )
        term = (-1) ** inversions
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def resultant_formula(p, q):
    p0, p1, p2 = p
    q0, q1, q2 = q
    return ((p2 * q0 - p0 * q2) ** 2
            - (p2 * q1 - p1 * q2) * (p1 * q0 - p0 * q1))


def perfect_matchings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        rest = values[1:index] + values[index + 1:]
        for tail in perfect_matchings(rest):
            yield ((first, values[index]), *tail)


def evaluate(coefficients, value):
    return sum(coefficient * value**degree
               for degree, coefficient in enumerate(coefficients))


def main():
    root = Path(__file__).resolve().parents[3]
    dag = json.loads((root / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "node status")
    incoming = {
        edge["from"] for edge in dag["edges"]
        if edge["to"] == NODE_ID and edge["kind"] == "req"
    }
    require(incoming == PARENTS, "dependency set")

    for p, q in (
        ((1, 2, 3), (4, 5, 6)),
        ((7, -3, 2), (5, 0, -4)),
        ((2, 9, 0), (-1, 3, 5)),
    ):
        p0, p1, p2 = p
        q0, q1, q2 = q
        sylvester = (
            (p2, p1, p0, 0),
            (0, p2, p1, p0),
            (q2, q1, q0, 0),
            (0, q2, q1, q0),
        )
        require(determinant(sylvester) == resultant_formula(p, q),
                "quadratic resultant formula")

    a2 = (Fraction(2), Fraction(1), Fraction(3))
    a0 = (Fraction(5), Fraction(-2), Fraction(4))
    for w in map(Fraction, (1, 2, -3, 5)):
        require(evaluate(a2, w) and evaluate(a2, -w), "test support")
        y = evaluate(a0, w) / evaluate(a2, w)
        z = evaluate(a0, -w) / evaluate(a2, -w)
        p = tuple(a0[i] - y * a2[i] for i in range(3))
        q = tuple(((-1) ** i) * (a0[i] - z * a2[i])
                  for i in range(3))
        require(resultant_formula(p, q) == 0, "forced deck-pair cut")

    for source_root in map(Fraction, (1, 2, 3, 4)):
        xi = source_root**2
        target_sum = Fraction(7)
        denominator = evaluate(a2, xi)
        q_value = source_root * target_sum
        b1_value = -(q_value * denominator) / xi
        require(xi * b1_value**2 == target_sum**2 * denominator**2,
                "squared sum identity")

    matchings = tuple(perfect_matchings(range(6)))
    require(len(matchings) == 15 and len(set(matchings)) == 15,
            "six-record matching census")
    require(5 * 7 * len(matchings) == 525, "case ledger")

    result = (root / "experiments/prize_resolution/"
              "rate_half_kb_positive_433_1a_outside_product_probe_result.md")
    text = result.read_text()
    for marker in ("13", "17", "29", "xi=eta", "160", "timed out"):
        require(marker in text, f"result marker {marker}")
    print("positive 433-1a quadratic paired-product interface verified")


if __name__ == "__main__":
    main()
