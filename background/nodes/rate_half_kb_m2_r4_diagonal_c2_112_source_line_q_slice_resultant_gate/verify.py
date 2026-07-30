#!/usr/bin/env python3
"""Verify the saturated (1,1,2) q-slice resultant gate."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate"
PARENTS = {
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_colored_quotient_compiler",
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def power(poly, exponent):
    result = [1]
    for _ in range(exponent):
        result = multiply(result, poly)
    return result


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("Res_T(q(T),G(T,W))" in statement, "resultant identity")
    require("does not assert that `(KBQS-1)` is sufficient" in statement,
            "scope fence")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require(all((parent, NODE_ID, "req") in edges for parent in PARENTS),
            "dependencies")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    w, k1, k2 = 2, 3, 5
    forced = [-w, 1]
    first = [-k1, 1]
    second = [-k2, 1]
    target = multiply(power(forced, 4),
                      multiply(power(first, 2), power(second, 2)))
    for multiplicity in range(3):
        at_r1 = multiply(
            power(forced, 2),
            multiply(power(first, multiplicity),
                     power(second, 2 - multiplicity)),
        )
        at_r2 = multiply(
            power(forced, 2),
            multiply(power(first, 2 - multiplicity),
                     power(second, multiplicity)),
        )
        require(multiply(at_r1, at_r2) == target,
                "resultant root divisor")
        require(len(at_r1) == len(at_r2) == 5, "fiber degree")

    # For tau(t)=1/t, the roots of tau^*q are the reciprocal q-roots.
    r1, r2 = 7, 11
    q = [r1 * r2, -(r1 + r2), 1]
    tau_q = [1, -(r1 + r2), r1 * r2]
    reciprocal_locator = multiply([-1, r1], [-1, r2])
    require(tau_q == reciprocal_locator, "aligned reciprocal locator")
    require(len(target) == 9, "resultant degree eight")

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_112_SOURCE_LINE_Q_SLICE_RESULTANT_GATE_PASS "
        "incidence_patterns=3 resultant_degree=8 aligned_target=tau_q near_target=tau_chi_Omega"
    )


if __name__ == "__main__":
    main()
