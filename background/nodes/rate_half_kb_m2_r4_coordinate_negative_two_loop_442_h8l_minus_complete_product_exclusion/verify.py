#!/usr/bin/env python3
"""Verify the complete H8-L-minus product-row exclusion."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h8l_minus_complete_product_exclusion"
DEPLOYED_PRIME = 2130706433
DE_REPRESENTATIVES = (3, 4, 5, 9, 10, 11)
DE_SUPPORT = {
    -1: {2, 5, 7, 17, 31, 47, 89, 223, 463, 1249, 14057},
    1: {2, 3, 7, 17, 79, 103, 401, 457},
}
DF_SUPPORT = {
    -1: {2, 7, 11, 23, 31, 103, 14057},
    1: {2, 3, 7, 17, 79, 103},
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def matchings(items):
    if not items:
        yield ()
        return
    first = items[0]
    for index in range(1, len(items)):
        for tail in matchings(items[1:index]+items[index+1:]):
            yield ((first, items[index]),)+tail


def pair_equations(values, pairs, gamma, alpha):
    equations = []
    for left, right in pairs:
        y, z = values[left], values[right]
        equations.append(sp.together(gamma*(y*z+1)-alpha*(y+z)).as_numer_denom()[0])
    return equations


def obstruction_support(equations, eliminate_first, eliminate_second, p4, b):
    r12 = sp.resultant(equations[0], equations[1], eliminate_first)
    r13 = sp.resultant(equations[0], equations[2], eliminate_first)
    obstruction = sp.factor(sp.resultant(r12, r13, eliminate_second))
    if obstruction == 0:
        return None
    support = set()
    for factor, _ in sp.factor_list(obstruction)[1]:
        norm = sp.resultant(p4, factor, b)
        require(norm != 0, "nonzero primary factor norm")
        if norm.is_Integer:
            support.update(sp.factorint(abs(int(norm))))
    return support


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("34 to 30 cells" in statement and "six to five common rows" in statement, "claim")
    require("does not delete another" in statement and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_product_invariance_router",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_signed_pair_matching_template_exclusion",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h8l_minus_cd_cell_exclusion",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    b, a, x, q = sp.symbols("b a x q")
    p4 = b**4-2*b**3+b**2-2*b+1
    c = (b-2)*(b**2+1)/b
    gamma = b+c
    alpha = -b*c*(b-1)
    all_matchings = tuple(matchings(tuple(range(6))))

    observed_de = {}
    for sigma in (-1, 1):
        kappa = sigma*c**2
        values = (a, kappa/a, x, -x, kappa*x/a**2, -kappa*x/a**2)
        support = set()
        for index in DE_REPRESENTATIVES:
            equations = pair_equations(values, all_matchings[index], gamma, alpha)
            support.update(obstruction_support(equations, x, a, p4, b))
        observed_de[sigma] = support
    require(observed_de == DE_SUPPORT, "DE support table")

    observed_df = {-1: set(), 1: set()}
    exceptional = []
    for sigma in (-1, 1):
        values = (a, q, sigma*a*q/c**2, -1, q/a, -q/a)
        for index, pairs in enumerate(all_matchings):
            equations = pair_equations(values, pairs, gamma, alpha)
            support = obstruction_support(equations, q, a, p4, b)
            if support is None:
                exceptional.append((sigma, index, equations))
            else:
                observed_df[sigma].update(support)
    require([(sigma, index) for sigma, index, _ in exceptional] ==
            [(-1, 6), (-1, 7), (-1, 8), (1, 6), (1, 7), (1, 8)],
            "DF projection exceptions")
    require(observed_df == DF_SUPPORT, "DF support table")

    for sigma, index, equations in exceptional:
        basis = sp.groebner(
            (p4, *equations), q, a, b,
            order="grevlex", method="f5b", modulus=DEPLOYED_PRIME,
        )
        require(len(basis.polys) == 1 and basis.polys[0].as_expr() == 1,
                f"deployed unit ideal {sigma}/{index}")

    all_support = set().union(*DE_SUPPORT.values(), *DF_SUPPORT.values())
    require(all(DEPLOYED_PRIME % prime for prime in all_support), "deployed norms")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_H8L_MINUS_COMPLETE_PASS "
        "remaining_cells_deleted=4 common_rows_deleted=1 frontier_rows=5 frontier_cells=30 cap=390"
    )


if __name__ == "__main__":
    main()
