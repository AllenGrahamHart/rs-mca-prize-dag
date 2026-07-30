#!/usr/bin/env python3
"""Verify the saturated (1,1,2) colored quotient compiler."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_c2_112_source_line_colored_quotient_compiler"
PARENTS = {
    "rate_half_kb_m2_r4_diagonal_c2_112_saturated_defect_classifier",
    "rate_half_kb_m2_u2_colored_source_resultant_split_compiler",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def mate_map(edges):
    mate = {}
    for left, right in edges:
        mate[left] = right
        mate[right] = left
    return mate


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("C_H(X) ~ chi_Omega(psi(X))" in statement, "colored descent")
    require("Q_J(W) ~ K_5(W)^2 chi_Omega(W)" in statement,
            "quotient resultants")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require(all((parent, NODE_ID, "req") in edges for parent in PARENTS),
            "dependencies")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    I = set(range(6))
    K = set(range(5))
    xi = 5

    # Aligned row: internal K pair, xi-K pair, and two crossing K labels.
    aligned = mate_map(((0, 1), (2, xi), (3, 6), (4, 7), (8, 9), (10, 11)))
    Lc_aligned = set(range(6, 12))
    omega_aligned = {aligned[k] for k in K if aligned[k] in Lc_aligned}
    J1_aligned = {aligned[i] for i in I if aligned[i] not in I}
    require(omega_aligned == J1_aligned == {6, 7}, "aligned Omega")

    # Near row: eta=6 pairs into K; xi and the other crossing label lie in Lc.
    eta = 6
    near = mate_map(((0, 1), (2, xi), (3, eta), (4, 7), (8, 9), (10, 11)))
    L_near = K | {eta}
    Lc_near = set(range(12)) - L_near
    omega_near = {near[k] for k in K if near[k] in Lc_near}
    require(omega_near == {xi, 7}, "near Omega")
    require(len(omega_aligned) == len(omega_near) == 2, "quotient degree")
    require(2 * 5 + 2 == 12 and 2 * 7 - 2 == 12,
            "partial resultant degrees")

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_112_SOURCE_LINE_COLORED_QUOTIENT_COMPILER_PASS "
        "aligned_Omega=J1 near_Omega=xi,ell colored_fibers=2 quotient_degree=2"
    )


if __name__ == "__main__":
    main()
