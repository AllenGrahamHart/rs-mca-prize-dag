#!/usr/bin/env python3
"""Verify the negative reconstruction determinant factors."""

import json
from fractions import Fraction as F
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_c2_112_source_line_negative_reconstruction_factor_gate"
PARENT = "rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def determinant(matrix):
    work = [[F(value) for value in row] for row in matrix]
    result = F(1)
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work))
                      if work[row][column]), None)
        if pivot is None:
            return F(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        value = work[column][column]
        result *= value
        work[column] = [entry / value for entry in work[column]]
        for row in range(column + 1, len(work)):
            value = work[row][column]
            if not value:
                continue
            work[row] = [left - value * right
                         for left, right in zip(work[row], work[column])]
    return result


def edge(left, right):
    return [left * right, -(left + right), F(1)]


def evaluation(point):
    return [
        [1, point, point * point, 0],
        [0, 0, 0, 1 - point * point],
        [-point * point, -point, -1, 0],
    ]


def augmented_determinant(template, b, c, d, w):
    a = F(2)
    q0, q1 = c * d, -(c + d)
    f = q0 + w
    g = -1 - w * q0
    m = q1 * (1 + w)
    numerator = f + m * a - g * a * a
    denominator = g - m * a - f * a * a
    require(denominator, "incidence denominator")
    z = -numerator / denominator
    vz = [f + g * z, m * (1 - z), -(g + f * z)]
    l1 = vz[2]
    l0 = vz[1] + a * l1
    require(vz[0] == -a * l0, "incidence division")

    if template == "fixed-moving":
        first, second = edge(a, 1 / a), edge(a, b)
        r, s = 1 / a, b
    else:
        first, second = edge(a, b), edge(a, 1 / b)
        r, s = b, 1 / b
    target = [
        ((l0 + s * l1) * first[index]
         + (l0 + r * l1) * second[index]) / (s - r)
        for index in range(3)
    ]

    at_w = evaluation(w)
    at_z = evaluation(z)
    rows = [
        [at_w[0][j] - q0 * at_w[2][j] for j in range(4)] + [0],
        [at_w[1][j] - q1 * at_w[2][j] for j in range(4)] + [0],
    ]
    rows.extend(row + [target[index]] for index, row in enumerate(at_z))
    return determinant(rows)


def printed_factor(template, b, c, d, w):
    incidence = c * d * w + 4 * c * d - 2 * c * w - 2 * c - 2 * d * w - 2 * d + 4 * w + 1
    factor_a = 5 * c * d - 4 * c - 4 * d + 5
    factor_b = b * c * d - 2 * b * c - 2 * b * d + b + 2 * c * d - c - d + 2
    factor_c = 2 * b * c * d - b * c - b * d + 2 * b + c * d - 2 * c - 2 * d + 1
    common = ((c - 2) * (2 * c - 1) * (d - 2) * (2 * d - 1)
              * (w - 1)**5 * (w + 1)**5 * (c * d - 1)**2)
    if template == "fixed-moving":
        return -6 * common * factor_a**2 * factor_b / ((2 * b - 1) * incidence**5)
    return 6 * common * factor_a * factor_b * factor_c / ((b - 1) * (b + 1) * incidence**5)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("F: A B=0" in statement and "M: A B C=0" in statement,
            "survivor loci")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require((PARENT, NODE_ID, "req") in edges, "dependency")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    fixtures = ((F(3), F(5), F(7), F(11)),
                (F(4), F(6), F(9), F(13)))
    checked = 0
    for template in ("fixed-moving", "moving-moving"):
        for fixture in fixtures:
            observed = augmented_determinant(template, *fixture)
            expected = printed_factor(template, *fixture)
            require(observed == expected, f"{template} factor identity")
            require(observed, f"{template} generic nonzero fixture")
            checked += 1

    # Each retained factor locus has a noncollision rational witness.
    a_locus = (F(5), F(3), F(7, 11), F(7))
    b_locus = (F(-17), F(3), F(7), F(5))
    c_locus = (F(-1, 17), F(3), F(7), F(5))
    require(augmented_determinant("fixed-moving", *a_locus) == 0,
            "A locus retained")
    require(augmented_determinant("fixed-moving", *b_locus) == 0,
            "B locus retained")
    require(augmented_determinant("moving-moving", *c_locus) == 0,
            "C locus retained")

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_112_SOURCE_LINE_NEGATIVE_RECONSTRUCTION_FACTOR_GATE_PASS "
        f"factor_fixtures={checked} templates=8+4 survivor_factors=AB/ABC"
    )


if __name__ == "__main__":
    main()
