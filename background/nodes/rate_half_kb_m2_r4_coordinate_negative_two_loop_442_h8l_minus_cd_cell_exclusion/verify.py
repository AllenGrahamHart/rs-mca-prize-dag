#!/usr/bin/env python3
"""Verify the H8-L-minus colored-xi cell exclusion."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h8l_minus_cd_cell_exclusion"
DEPLOYED_PRIME = 2130706433
REPRESENTATIVES = (3, 4, 5, 9, 10, 11)
EXPECTED_SUPPORT = {
    (-1, 3): {2, 7, 23, 103},
    (-1, 4): {2, 7, 31, 97},
    (-1, 5): {2, 7, 103, 1223},
    (-1, 9): {2, 7, 23, 24137},
    (-1, 10): {2, 3, 7, 9479},
    (-1, 11): {2, 7, 2377},
    (1, 3): {2, 3, 7},
    (1, 4): {2, 7},
    (1, 5): {2, 7},
    (1, 9): {2, 7, 239},
    (1, 10): {2, 7, 743},
    (1, 11): {2, 7, 137},
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
        second = items[index]
        for tail in matchings(items[1:index]+items[index+1:]):
            yield ((first, second),)+tail


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("36 to 34 cells" in statement and "468 to 444" in statement, "claim")
    require("does not delete" in statement and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_outside_product_involution_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_product_invariance_router",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_signed_pair_matching_template_exclusion",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    l, b, a, x = sp.symbols("l b a x")
    relation = l**4+1
    b_gate = b**2-b*l**3+b*l-b+1
    p4 = b**4-2*b**3+b**2-2*b+1
    require(sp.factor(sp.resultant(relation, b_gate, l)) == p4**2, "univariate descent")

    c_original = (b-2)*(l**3-l+1)
    numerator = b*(2*b*l**2+2*b-l**2+2*l-1)
    denominator = b*l**2-2*b*l+b-2*l**2-2
    ideal = sp.groebner((relation, b_gate), b, l, order="lex")
    require(ideal.reduce(sp.expand(numerator-denominator))[1] == 0, "forced product one")

    c = (b-2)*(b**2+1)/b
    gamma = b+c
    alpha = -b*c*(b-1)
    beta = b**2*c*gamma
    require(sp.rem(sp.together(beta+gamma).as_numer_denom()[0], p4, domain=sp.QQ) == 0,
            "beta equals minus gamma")

    all_matchings = tuple(matchings(tuple(range(6))))
    flip = {0: 0, 1: 1, 2: 3, 3: 2, 4: 5, 5: 4}
    partner = {}
    for index, pairs in enumerate(all_matchings):
        image = tuple(sorted(tuple(sorted((flip[u], flip[v]))) for u, v in pairs))
        partner[index] = next(
            other for other, candidate in enumerate(all_matchings)
            if tuple(sorted(candidate)) == image
        )
    require({partner[index] for index in REPRESENTATIVES} == {6, 8, 7, 13, 12, 14},
            "F-sign matching partners")

    observed_support = {}
    for sigma in (-1, 1):
        values = (a, sigma*a/c**2, x, -x, a*x, -a*x)
        for index in REPRESENTATIVES:
            equations = []
            for left, right in all_matchings[index]:
                y, z = values[left], values[right]
                equation = gamma*(y*z+1)-alpha*(y+z)
                equations.append(sp.together(equation).as_numer_denom()[0])
            r12 = sp.resultant(equations[0], equations[1], x)
            r13 = sp.resultant(equations[0], equations[2], x)
            obstruction = sp.factor(sp.resultant(r12, r13, a))
            factors = sp.factor_list(obstruction)[1]
            support = set()
            for factor, _multiplicity in factors:
                norm = sp.resultant(p4, factor, b)
                require(norm != 0, f"nonzero factor norm {sigma}/{index}")
                if norm.is_Integer:
                    support.update(sp.factorint(abs(int(norm))))
            observed_support[(sigma, index)] = support
    require(observed_support == EXPECTED_SUPPORT, "factor-norm support table")
    require(all(DEPLOYED_PRIME % prime for values in EXPECTED_SUPPORT.values() for prime in values),
            "deployed characteristic")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_H8L_MINUS_CD_PASS "
        "cells_deleted=2 matching_representatives=12 frontier_cells=34 matching_cap=444"
    )


if __name__ == "__main__":
    main()
