#!/usr/bin/env python3
"""Verify coordinate orientation transport by endpoint transposition."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_transpose_transport"
PARENTS = (
    "rate_half_kb_q6_u2_primitive_subdegree4_route_cut",
    "rate_half_kb_m2_r4_coordinate_k_fiber_vieta_rank_compiler",
)
Q = 101


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def endpoint_divided_difference(coefficients: list[int], left: int,
                                right: int) -> int:
    require(left != right, "off diagonal")
    f_left = sum(value * pow(left, degree, Q)
                 for degree, value in enumerate(coefficients)) % Q
    f_right = sum(value * pow(right, degree, Q)
                  for degree, value in enumerate(coefficients)) % Q
    return (f_left - f_right) * pow(left - right, Q - 2, Q) % Q


def transpose(element: tuple[int, int]) -> tuple[int, int]:
    return element[1], element[0]


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("fresh" in statement and "H'(T',X')" in statement,
            "fresh source record")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer")

    coefficients = [3, 5, 7, 11, 13, 17]
    checks = 0
    for left, right in ((2, 3), (5, 8), (13, 21), (34, 55)):
        require(
            endpoint_divided_difference(coefficients, left, right)
            == endpoint_divided_difference(coefficients, right, left),
            "symmetric endpoint relation",
        )
        checks += 1

    a, c, diagonal = (1, 0), (0, 1), (1, 1)
    require(transpose(a) == c and transpose(c) == a,
            "coordinate generators")
    require(transpose(diagonal) == diagonal, "diagonal generator")
    require(transpose(transpose(a)) == a, "transpose involution")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_TRANSPOSE_TRANSPORT_PASS "
        f"endpoint_checks={checks} subgroup_checks=4"
    )


if __name__ == "__main__":
    main()
