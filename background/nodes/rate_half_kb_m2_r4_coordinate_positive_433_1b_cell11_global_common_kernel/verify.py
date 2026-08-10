#!/usr/bin/env python3
"""Verify the positive 433-1b cell-11 global common kernel."""

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell11_compact_kernel_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
)
COMMON = EXPERIMENTS / "rate_half_kb_positive_433_1b_common_vieta_compiler.py"
PRODUCT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
)
STRUCTURE = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell11_complete_pivot_scout_result.json"
)
PINNED = {
    SCRIPT: "b2d334bfb7c0b883eccdaca3bb7bbe3e459ecd483d8dd86aeebe8e6567623a10",
    RESULT: "2ef59a5dd9e656f36fccc63f3c75aaee6889664312928ffe25d0d0816ed16236",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell11_quadratic_four_basis_common_locus",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
)
PRIME = 2130706433
t, r, c, b = sp.symbols("t r c b")
VARIABLES = (t, r, c, b)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def as_poly(text):
    return sp.Poly(sp.sympify(text), *VARIABLES, modulus=PRIME)


def common_rows():
    labels = (1, r**2, -r**2, t**2, -1)
    products = (-1, b, c, b*c, -b*c)
    product_rows = [
        (-product, -product*label, -product*label**2,
         1, label, label**2, 0, 0)
        for label, product in zip(labels, products)
    ]
    q_la = 0
    q_ab = r*(1+b)
    sum_la = (q_la, q_la, q_la, 0, 0, 0, 1, 1)
    x_ab = r**2
    sum_ab = (q_ab, q_ab*x_ab, q_ab*x_ab**2,
              0, 0, 0, x_ab, x_ab**2)
    return [*product_rows, sum_la, sum_ab]


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell11-compact-kernel-v1" and
            payload["field"] == PRIME and payload["cell"] == 11 and
            payload["pivot"] == 1 and
            payload["source_common_sha256"] == digest(COMMON) and
            payload["source_product_sha256"] == digest(PRODUCT) and
            payload["source_structure_sha256"] == digest(STRUCTURE),
            "kernel custody")
    structure = json.loads(STRUCTURE.read_text())
    structure_signatures = {}
    for row in structure["rows"]:
        signs = tuple(row["epsilon"])
        signature = tuple(item["sha256"] for item in row["lex_basis"])
        require(signs not in structure_signatures or
                structure_signatures[signs] == signature,
                "source chart mismatch")
        structure_signatures[signs] = signature

    expected = set(itertools.product((-1, 1), repeat=2))
    actual = set()
    kernel_signatures = set()
    shapes = ((14, 49), (14, 52), (12, 49), (15, 49),
              (15, 52), (13, 49), (14, 48), (14, 48))
    first_kernel = None
    for row in payload["rows"]:
        signs = tuple(row["epsilon"])
        require(signs not in actual, "duplicate kernel row")
        actual.add(signs)
        require(row["status"] == "COMPLETE" and row["all_rows_zero"] and
                row["remainders"] == ["0"] * 10 and
                row["common_dimension"] == 1 and
                row["common_basis_size"] == 40,
                "exact kernel reduction")
        require(row["identically_zero_rows"] ==
                [True] * 7 + [False] * 3,
                "formal identity ledger")
        require(tuple((item["degree"], item["terms"])
                      for item in row["kernel"]) == shapes,
                "kernel shapes")
        require(row["product_kernel_removed_gcd"]["expression"] == "1" and
                row["final_kernel_removed_gcd"]["expression"] ==
                "r**4 - r**2", "primitive gcd ledger")
        require(tuple(row["lex_signature"]) == structure_signatures[signs],
                "kernel/common chart custody")
        require(not row["stderr_tail"] and row["program_sha256"],
                "kernel transcript")
        signature = tuple(item["sha256"] for item in row["kernel"])
        kernel_signatures.add(signature)
        if first_kernel is None:
            first_kernel = [as_poly(item["expression"]) for item in row["kernel"]]
    require(actual == expected and len(kernel_signatures) == 1,
            "one sign-independent kernel")

    for index, row in enumerate(common_rows()):
        dot = sum(value * coordinate.as_expr()
                  for value, coordinate in zip(row, first_kernel))
        require(sp.Poly(dot, *VARIABLES, modulus=PRIME).is_zero,
                f"formal row identity {index}")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED",
            "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges,
                f"missing parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "DAG consumer")


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    verify_payload(json.loads(RESULT.read_text()))
    verify_dag()
    print("cell=11 kernels=1 sign_rows=4 exact_reductions=40 formal_rows=7")


if __name__ == "__main__":
    main()
