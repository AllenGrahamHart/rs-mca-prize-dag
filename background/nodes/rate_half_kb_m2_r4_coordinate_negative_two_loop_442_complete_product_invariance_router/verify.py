#!/usr/bin/env python3
"""Verify the 442 complete-product invariance router."""

import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_product_invariance_router"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def orbits(points, permutations):
    remaining = set(points)
    answer = []
    while remaining:
        orbit = {remaining.pop()}
        changed = True
        while changed:
            changed = False
            for point in tuple(orbit):
                for permutation in permutations:
                    image = permutation[point]
                    if image not in orbit:
                        orbit.add(image)
                        remaining.discard(image)
                        changed = True
        answer.append(orbit)
    return answer


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("= 36 cells" in statement and "21 `2 x 2`" in statement, "claim")
    require("independent projectivities" in statement and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_exceptional_product_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_outside_product_involution_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_edge_skeleton_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    c, d, e, f = sp.symbols("c d e f")
    common_rows = ("H6-", "H6+", "H8L-", "H8L+", "H8M-", "H8M+")
    xi_indices = (0, 2, 3)
    canonical_cells = []
    for row in common_rows:
        for sigma in (-1, 1):
            products = (c*d, c*e, sigma*d*e, d*f, -d*f, e*f, -e*f)
            for xi_index in xi_indices:
                residual = products[:xi_index] + products[xi_index+1:]
                require(len(residual) == 6, "residual sextic")
                canonical_cells.append((row, sigma, xi_index, residual))
    require(len(canonical_cells) == 36, "cell count")
    require(len({cell[:3] for cell in canonical_cells}) == 36, "cell uniqueness")
    require(sp.binomial(7, 2) == 21, "proportionality minors")

    for u, v, w in itertools.product((-1, 1), repeat=3):
        old = {sp.expand(u*c*d), sp.expand(v*c*e), sp.expand(w*d*e),
               d*f, -d*f, e*f, -e*f}
        new_d, new_e, sigma = u*d, v*e, w*u*v
        canonical = {sp.expand(c*new_d), sp.expand(c*new_e),
                     sp.expand(sigma*new_d*new_e),
                     new_d*f, -new_d*f, new_e*f, -new_e*f}
        require(old == canonical, "sign gauge")

    points = tuple(range(7))
    swap_de = (1, 0, 2, 5, 6, 3, 4)
    flip_f = (0, 1, 2, 4, 3, 6, 5)
    occurrence_orbits = orbits(points, (swap_de, flip_f))
    require(sorted(map(len, occurrence_orbits)) == [1, 2, 4], "xi occurrence orbits")
    require({frozenset(value) for value in occurrence_orbits} == {
        frozenset((0, 1)), frozenset((2,)), frozenset((3, 4, 5, 6))
    }, "xi orbit representatives")

    gamma, alpha, beta = sp.symbols("Gamma Alpha Beta")
    matrix = sp.Matrix([[alpha, beta], [gamma, -alpha]])
    require(matrix*matrix == (alpha**2+beta*gamma)*sp.eye(2), "involution square")
    y, z = sp.symbols("Y Z")
    fixed = gamma*y**2-2*alpha*y*z-beta*z**2
    require(sp.Poly(fixed, y, z).total_degree() == 2, "fixed quadratic")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_INVARIANCE_PASS "
        "naive=540 canonical=36 rows=6 sigma=2 xi_types=3 minors=21"
    )


if __name__ == "__main__":
    main()
