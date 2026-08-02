#!/usr/bin/env python3
"""Verify the deployed rational classifier for positive 433-1b rank drop."""

import hashlib
import itertools
import json
from pathlib import Path
import re

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_common_exception_classifier"
SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_rankdrop_fglm_profile_modal.py"
RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_rankdrop_fglm_profile_result.json"
SCRIPT_SHA256 = "448d074813f3331127327ceaf9c4e5a4b372a6cf9f5172b4dbb4bca6b7e04686"
RESULT_SHA256 = "1ef0469634892459a35ea9b7b2b72d112d0b10a099ddab2c6754cc9c8e184017"
PRIME = 2130706433
IOTA = 16711679
SURVIVOR_CELLS = {4, 5, 7, 8, 9, 10, 11, 12, 13, 14}
DEGREES = {
    4: (3, 3), 5: (2, 2, 4), 7: (3, 3), 8: (2, 2, 4),
    9: (1, 1, 2, 2, 4, 6), 10: (1, 1, 2, 2, 4, 6),
    11: (2, 2, 2, 2, 3, 3, 3, 3),
    12: (2, 2, 10), 13: (2, 2, 10), 14: (3, 3, 3, 3),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    values = tuple(values)
    first = values[0]
    for index in range(1, len(values)):
        rest = values[1:index] + values[index + 1:]
        yield ((first, values[index]), (rest[0], rest[1]))


def cells():
    return tuple(
        (singleton, matching)
        for singleton in range(5)
        for matching in pairings(tuple(i for i in range(5) if i != singleton))
    )


def rank_mod(rows):
    matrix = [[value % PRIME for value in row] for row in rows]
    pivot_row = 0
    for column in range(len(matrix[0])):
        pivot = next((row for row in range(pivot_row, len(matrix))
                      if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], -1, PRIME)
        matrix[pivot_row] = [value * inverse % PRIME
                             for value in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row:
                continue
            scale = matrix[row][column]
            if scale:
                matrix[row] = [(left - scale * right) % PRIME
                               for left, right in zip(matrix[row], matrix[pivot_row])]
        pivot_row += 1
    return pivot_row


def common_rows(cell, epsilon, point):
    singleton, matching = cells()[cell]
    roots = [None] * 5
    roots[matching[0][0]] = 1
    roots[matching[0][1]] = epsilon[0] * IOTA
    roots[matching[1][0]] = point["r"]
    roots[matching[1][1]] = epsilon[1] * IOTA * point["r"]
    roots[singleton] = point["t"]
    labels = [root * root % PRIME for root in roots]
    b, c = point["b"], point["c"]
    products = (-1, b, c, b*c, -b*c)
    sums = (0, 1+b, 1+c, b+c, b-c)
    product_rows = [
        [-product, -product*label, -product*label*label,
         1, label, label*label, 0, 0]
        for product, label in zip(products, labels)
    ]
    sum_rows = []
    for root, label, edge_sum in zip(roots, labels, sums):
        q_value = root * edge_sum
        sum_rows.append([
            q_value, q_value*label, q_value*label*label,
            0, 0, 0, label, label*label,
        ])
    return product_rows, product_rows + sum_rows


def parse_singular(expression):
    converted = re.sub(r"([a-zA-Z])(\d+)", r"\1**\2", expression)
    converted = re.sub(r"(?<=\d)(?=[a-zA-Z])", "*", converted)
    return sp.sympify(converted)


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-rankdrop-rational-classifier-v2",
            "schema")
    require(payload["field"] == PRIME, "field")
    require(payload["source_common_sha256"] ==
            "a956656cba6c884bae665a2439666964ed468dcf9d0466e80cb825e811a6f845",
            "common source")
    require(payload["source_product_sha256"] ==
            "ee4dcb25877e9101a544ee5896b9bf6890059d6398c78d7562127b0d1c53c293",
            "product source")
    expected = set(itertools.product(SURVIVOR_CELLS, (-1, 1), (-1, 1)))
    actual = set()
    total_points = 0
    b_symbol = sp.symbols("b")
    for row in payload["rows"]:
        case = (row["cell"], *row["epsilon"])
        require(row["status"] == "COMPLETE" and case not in actual,
                "complete unique case")
        actual.add(case)
        require("LEX_SIZE=5" in row["stdout"] and
                all(f"H[{index}]=" in row["stdout"] for index in range(1, 6)),
                "shape basis")
        require(tuple(factor["degree"] for factor in row["factors"]) ==
                DEGREES[row["cell"]], "factor degrees")
        require(all(factor["multiplicity"] == 1 for factor in row["factors"]),
                "square-free factors")
        eliminant = sp.Poly(parse_singular(row["eliminant"]), b_symbol,
                             modulus=PRIME).monic()
        product = sp.Poly(1, b_symbol, modulus=PRIME)
        for factor in row["factors"]:
            require(hashlib.sha256(factor["expression"].encode()).hexdigest() ==
                    factor["sha256"], "factor custody")
            product *= sp.Poly(factor["expression"], b_symbol,
                               modulus=PRIME) ** factor["multiplicity"]
        require(product.monic() == eliminant, "factor product")
        expected_points = 2 if row["cell"] in {9, 10} else 0
        require(row["linear_factor_count"] == expected_points and
                len(row["rational_points"]) == expected_points,
                "rational point count")
        basis = {
            int(index): parse_singular(expression)
            for index, expression in re.findall(r"H\[(\d+)\]=(.*)", row["stdout"])
        }
        for point in row["rational_points"]:
            require(point["guard_nonzero"], "guard marker")
            values = {sp.symbols(name): point[name]
                      for name in ("b", "c", "r", "t", "z")}
            require(all(int(expression.subs(values)) % PRIME == 0
                        for expression in basis.values()), "lex point replay")
            b, c, r, t, z = (point[name] for name in ("b", "c", "r", "t", "z"))
            guard_values = (
                r, t, b, c, b-1, b+1, c-1, c+1, b-c, b+c,
                r*r-1, r*r+1, t*t-1, t*t+1, t*t-r*r, t*t+r*r,
            )
            guard = 1
            for value in guard_values:
                guard = guard * value % PRIME
            require(guard and z*guard % PRIME == 1, "inverse guard replay")
            products, full = common_rows(row["cell"], row["epsilon"], point)
            require(rank_mod(products) == 4 and rank_mod(full) == 7,
                    "matrix rank replay")
            total_points += 1
    require(actual == expected and total_points == 16, "coverage")


def main():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "script custody")
    require(hashlib.sha256(RESULT.read_bytes()).hexdigest() == RESULT_SHA256,
            "result custody")
    verify_payload(json.loads(RESULT.read_text()))
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require((PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_RANKDROP_RATIONAL_VERIFY_PASS "
        "finite_rows=40 rationally_empty=32 retained_points=16"
    )


if __name__ == "__main__":
    main()
