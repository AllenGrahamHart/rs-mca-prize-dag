#!/usr/bin/env python3
"""Verify the diagonal branch coefficient compiler."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_branch_coefficient_compiler"
PARENT = "rate_half_kb_m2_r4_diagonal_source_subfield_dichotomy"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def orbit_dimensions(rows: int, columns: int) -> tuple[int, int]:
    positions = {(i, j) for i in range(rows) for j in range(columns)}
    fixed = sum(
        (i, j) == (rows - 1 - i, columns - 1 - j)
        for i, j in positions
    )
    return ((len(positions) + fixed) // 2, (len(positions) - fixed) // 2)


def poly_mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def poly_eval(poly: list[int], value: int) -> int:
    return sum(coefficient * value**degree for degree, coefficient in enumerate(poly))


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("U(T,W)^2-W V(T,W)^2" in statement, "norm identity")
    require("cubic resolvent" in statement, "resolvent branch")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    require((PARENT, NODE_ID, "req") in edges, "dependency")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    require(orbit_dimensions(3, 3) == (5, 4), "U reciprocal dimensions")
    require(orbit_dimensions(3, 2) == (3, 3), "V reciprocal dimensions")

    for roots in ((1, 2, 4, 8), (-3, 2, 5, 11), (2, 7, 13, 19)):
        quartic = [1]
        for root in roots:
            quartic = poly_mul(quartic, [-root, 1])
        d, c, b, a, leading = quartic
        require(leading == 1, "monic quartic")
        resolvent = [4 * b * d - a * a * d - c * c, a * c - 4 * d, -b, 1]
        pair_roots = (
            roots[0] * roots[1] + roots[2] * roots[3],
            roots[0] * roots[2] + roots[1] * roots[3],
            roots[0] * roots[3] + roots[1] * roots[2],
        )
        require(len(set(pair_roots)) == 3, "separable resolvent roots")
        require(all(poly_eval(resolvent, root) == 0 for root in pair_roots),
                "resolvent convention")

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_BRANCH_COEFFICIENT_COMPILER_PASS "
        "source_dims=8,7 resolvent_rows=3"
    )


if __name__ == "__main__":
    main()
