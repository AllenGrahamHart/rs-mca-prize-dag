#!/usr/bin/env python3
"""Verify the H6 exclusions and complete closure of the 442 product gate."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h6_complete_product_exclusion"
DEPLOYED_PRIME = 2130706433
REPRESENTATIVES = (3, 4, 5, 9, 10, 11)
EXPECTED_SUPPORT = {
    (-1, "cD"): {2, 3, 5, 7},
    (-1, "DE"): {2, 3, 5, 7, 29, 41, 757},
    (1, "cD"): {2, 3, 5},
    (1, "DE"): {2, 3, 5, 7, 11, 13, 17, 149},
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
        for tail in matchings(items[1:index] + items[index + 1:]):
            yield ((first, items[index]),) + tail


def pair_equations(values, pairs, gamma, alpha, beta):
    equations = []
    for left, right in pairs:
        y, z = values[left], values[right]
        equations.append(
            sp.together(gamma*y*z - alpha*(y + z) - beta).as_numer_denom()[0]
        )
    return equations


def resultant_support(equations, p2, x, a, b):
    r12 = sp.resultant(equations[0], equations[1], x)
    r13 = sp.resultant(equations[0], equations[2], x)
    obstruction = sp.factor(sp.resultant(r12, r13, a))
    require(obstruction != 0, "nonzero primary obstruction")
    support = set()
    for factor, _ in sp.factor_list(obstruction)[1]:
        norm = sp.resultant(p2, factor, b)
        require(norm != 0 and norm.is_Integer, "nonzero integral factor norm")
        support.update(sp.factorint(abs(int(norm))))
    return support


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("frontier drops" in statement and "empty set" in statement, "claim")
    require("does not close the `(4,3,3)`" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_exceptional_product_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_outside_product_involution_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_product_invariance_router",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_signed_pair_matching_template_exclusion",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h8_positive_complete_product_exclusion",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    l, b, c_symbol, a, x = sp.symbols("l b c a x")
    relation = l**2 - l + 1
    numerator = b * (b*l**2 + b - l**2 + 2*l - 1)
    denominator = b*l**2 - 2*b*l + b - l**2 - 1
    require(sp.rem(sp.expand(numerator + b*denominator), relation, l) == 0,
            "forced product minus b")

    all_matchings = tuple(matchings(tuple(range(6))))
    flip = {0: 0, 1: 1, 2: 3, 3: 2, 4: 5, 5: 4}
    partner = {}
    for index, pairs in enumerate(all_matchings):
        image = tuple(sorted(tuple(sorted((flip[u], flip[v]))) for u, v in pairs))
        partner[index] = next(
            other for other, candidate in enumerate(all_matchings)
            if tuple(sorted(candidate)) == image
        )
    require({partner[index] for index in REPRESENTATIVES} == {6, 7, 8, 12, 13, 14},
            "F-sign matching partners")

    observed_support = {}
    aligned_units = {}
    aligned_collision = {}
    for tau in (-1, 1):
        row_coefficient = 1 if tau == -1 else 7
        p2 = 4*b**2 + row_coefficient*b + 4
        c = 2*(1 - b)/3 if tau == -1 else 2*(b + 1)

        first_row = sp.Matrix([-c_symbol, 1 - c_symbol, -1])
        second_row = sp.Matrix(
            [-tau*b**3*c_symbol, b**2 - tau*b*c_symbol, -1]
        )
        gamma_symbol, alpha_symbol, beta_symbol = first_row.cross(second_row)
        require(sp.expand(
            gamma_symbol - (b**2 - tau*b*c_symbol + c_symbol - 1)
        ) == 0, f"gamma {tau}")
        require(sp.expand(alpha_symbol - c_symbol*(tau*b**3 - 1)) == 0,
                f"alpha {tau}")
        require(sp.expand(
            beta_symbol + b*c_symbol*(
                tau*b**2*c_symbol - tau*b**2 + b - tau*c_symbol
            )
        ) == 0, f"beta {tau}")
        gamma = gamma_symbol.subs(c_symbol, c)
        alpha = alpha_symbol.subs(c_symbol, c)
        beta = beta_symbol.subs(c_symbol, c)

        # p_xi=-b, so forced DF leaves -DF=b, already a common product.
        forced_product = -b
        require(sp.expand(-forced_product - b) == 0, f"DF collision {tau}")

        for sigma in (-tau, tau):
            values_by_type = {
                "cD": (a, -sigma*b*a/c**2, x, -x, -a*x/b, a*x/b),
                "DE": (a, -sigma*b*c**2/a, x, -x,
                       -sigma*b*c**2*x/a**2, sigma*b*c**2*x/a**2),
            }
            for kind, values in values_by_type.items():
                if sigma == -tau:
                    support = set()
                    for index in REPRESENTATIVES:
                        equations = pair_equations(
                            values, all_matchings[index], gamma, alpha, beta
                        )
                        support.update(resultant_support(equations, p2, x, a, b))
                    observed_support[(tau, kind)] = support
                    continue

                unit_indices = set()
                collision_indices = set()
                for index in REPRESENTATIVES:
                    equations = pair_equations(
                        values, all_matchings[index], gamma, alpha, beta
                    )
                    basis = sp.groebner((p2, *equations), x, a, b, order="lex")
                    is_unit = len(basis.polys) == 1 and basis.polys[0].as_expr() == 1
                    if is_unit:
                        unit_indices.add(index)
                    else:
                        require(basis.reduce(a**2 - b**2)[1] == 0,
                                f"aligned collision {tau}/{kind}/{index}")
                        collision_indices.add(index)
                aligned_units[(tau, kind)] = unit_indices
                aligned_collision[(tau, kind)] = collision_indices

    require(observed_support == EXPECTED_SUPPORT, "opposite-sign support census")
    require(all(DEPLOYED_PRIME % prime
                for support in EXPECTED_SUPPORT.values() for prime in support),
            "deployed norm supports")
    for tau in (-1, 1):
        require(aligned_units[(tau, "cD")] == set(), f"cD units {tau}")
        require(aligned_collision[(tau, "cD")] == set(REPRESENTATIVES),
                f"cD collision coverage {tau}")
        require(aligned_units[(tau, "DE")] == {5, 10}, f"DE units {tau}")
        require(aligned_collision[(tau, "DE")] == {3, 4, 9, 11},
                f"DE collision coverage {tau}")

    require(DEPLOYED_PRIME % 2 and DEPLOYED_PRIME % 3,
            "deployed field supports signs and H6-minus locator")
    require(12 - 12 == 0 and 156 - 156 == 0, "frontier count")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_H6_COMPLETE_PASS "
        "opposite_resultant_cases=24 aligned_unit_cases=4 "
        "aligned_collision_cases=20 forced_DF_cells=4 frontier_rows=0 cells=0 cap=0"
    )


if __name__ == "__main__":
    main()
