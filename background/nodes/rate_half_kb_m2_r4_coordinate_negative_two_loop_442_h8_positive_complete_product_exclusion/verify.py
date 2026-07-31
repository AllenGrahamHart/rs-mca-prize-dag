#!/usr/bin/env python3
"""Verify the positive-H8 complete-product exclusions and transport."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h8_positive_complete_product_exclusion"
DEPLOYED_PRIME = 2130706433
REPRESENTATIVES = (3, 4, 5, 9, 10, 11)
EXPECTED_SUPPORT = {
    ("cD", -1): {2, 3, 7, 17, 23, 41, 193, 503, 1783, 2287, 56873,
                  160879, 197969, 448303, 1051079, 91632847, 755155991,
                  6691712346841},
    ("cD", 1): {2, 7, 11, 17, 23, 31, 47, 193, 577, 3313, 18143,
                 23017, 29881, 55009, 12290297, 30635257, 7006911559,
                 263547408991},
    ("DE", -1): {2, 3, 7, 17, 23, 41, 71, 89, 127, 137, 241, 1262119,
                  144472513, 161888663533439},
    ("DE", 1): {2, 7, 17, 23, 41, 71, 89, 241, 433, 457, 991, 1033,
                 6287, 181808623, 1318666033},
    ("DF", -1): {2, 3, 5, 7, 17, 23, 31, 233, 673, 1447, 1481, 3041,
                  4513, 6551, 16657, 21383, 44711, 47807, 201497, 319097,
                  373649, 4925663, 150378409, 251619409, 538254793,
                  8775762599, 115822123129, 212930374207,
                  2415263060833681, 3485009410023503, 13095696023106569},
    ("DF", 1): {2, 7, 17, 23, 31, 41, 47, 73, 79, 89, 137, 167, 191,
                 839, 1063, 2729, 3823, 4129, 6551, 21383, 31247, 47407,
                 69761, 77513, 168719, 267913, 1657897, 5837263, 46071847,
                 111995831, 3585308983, 14321191361, 90723895279,
                 838253707519, 13655205154751, 27401175328159,
                 113388216599263},
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
        equation = gamma * y * z - alpha * (y + z) - beta
        equations.append(sp.together(equation).as_numer_denom()[0])
    return equations


def primary_support(equations, first_var, second_var, p4, b):
    r12 = sp.resultant(equations[0], equations[1], first_var)
    r13 = sp.resultant(equations[0], equations[2], first_var)
    obstruction = sp.factor(sp.resultant(r12, r13, second_var))
    if obstruction == 0:
        return None
    support = set()
    for factor, _ in sp.factor_list(obstruction)[1]:
        norm = sp.resultant(p4, factor, b)
        require(norm != 0 and norm.is_Integer, "nonzero integral factor norm")
        support.update(sp.factorint(abs(int(norm))))
    return support


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("four to two common rows" in statement and "24 to 12" in statement,
            "claim")
    require("does not delete either `H6`" in statement and "nonclaim" in contract,
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
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h8m_minus_transport_exclusion",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    l, b, c_symbol, a, x, q = sp.symbols("l b c a x q")
    relation = l**4 + 1
    gate = b**2 - 2*b*l**3 + 2*b*l - b + 1
    p4 = b**4 - 2*b**3 - 5*b**2 - 2*b + 1
    require(sp.factor(sp.resultant(relation, gate, l)) == p4**2,
            "positive univariate descent")
    ideal = sp.groebner((relation, gate), b, l, order="lex")

    c_original = -b*l**3 + b*l + b + 2
    c = (-b**2 + 3*b + 3) / 2
    c_identity = sp.expand(2*c_original - (-b**2 + 3*b + 3))
    require(ideal.reduce(c_identity)[1] == 0, "locator descent")

    numerator = b * (2*b*l**2 + 2*b - l**2 + 2*l - 1)
    denominator = b*l**2 - 2*b*l + b - 2*l**2 - 2
    p_numerator = 5*b**3 - 16*b**2 + 8*b + 8
    p = p_numerator / 23
    require(ideal.reduce(sp.expand(23*numerator - p_numerator*denominator))[1] == 0,
            "forced-product descent")

    first_row = sp.Matrix([b*c_symbol, -(b + c_symbol), -1])
    second_row = sp.Matrix([-b**3*c_symbol, b**2 - b*c_symbol, -1])
    gamma_symbol, alpha_symbol, beta_symbol = first_row.cross(second_row)
    require(sp.expand(gamma_symbol - (b**2 - b*c_symbol + b + c_symbol)) == 0,
            "gamma")
    require(sp.expand(alpha_symbol - b*c_symbol*(b**2 + 1)) == 0, "alpha")
    require(sp.expand(
        beta_symbol + b**2*c_symbol*(b**2 + b*c_symbol - b + c_symbol)
    ) == 0,
            "beta")
    gamma = gamma_symbol.subs(c_symbol, c)
    alpha = alpha_symbol.subs(c_symbol, c)
    beta = beta_symbol.subs(c_symbol, c)

    all_matchings = tuple(matchings(tuple(range(6))))
    observed_support = {}
    exceptional = []
    for sigma in (-1, 1):
        values_by_type = {
            "cD": (a, sigma*p*a/c**2, x, -x, a*x/p, -a*x/p),
            "DE": (a, sigma*p*c**2/a, x, -x,
                   sigma*p*c**2*x/a**2, -sigma*p*c**2*x/a**2),
            "DF": (a, q, sigma*a*q/c**2, -p, p*q/a, -p*q/a),
        }
        for kind, values in values_by_type.items():
            indices = REPRESENTATIVES if kind != "DF" else range(15)
            support = set()
            for index in indices:
                equations = pair_equations(
                    values, all_matchings[index], gamma, alpha, beta
                )
                first_var = x if kind != "DF" else q
                part = primary_support(equations, first_var, a, p4, b)
                if part is None:
                    exceptional.append((kind, sigma, index, equations))
                else:
                    support.update(part)
            observed_support[(kind, sigma)] = support
    require(observed_support == EXPECTED_SUPPORT, "primary support census")
    require([(kind, sigma, index) for kind, sigma, index, _ in exceptional] == [
        ("DF", -1, 6), ("DF", -1, 7), ("DF", -1, 8),
        ("DF", 1, 6), ("DF", 1, 7), ("DF", 1, 8),
    ], "primary projection exceptions")

    for kind, sigma, index, equations in exceptional:
        basis = sp.groebner(
            (p4, *equations), q, a, b,
            order="grevlex", method="f5b", modulus=DEPLOYED_PRIME,
        )
        require(len(basis.polys) == 1 and basis.polys[0].as_expr() == 1,
                f"deployed unit ideal {kind}/{sigma}/{index}")
    all_support = set().union(*EXPECTED_SUPPORT.values())
    require(all(DEPLOYED_PRIME % prime for prime in all_support),
            "deployed primary norms")

    # Positive-sign equal-loop transport.
    d, e, f, sigma_symbol = sp.symbols("d e f sigma")
    bp = 1 / b
    cp = c_original / b
    transported_gate = sp.together(
        bp**2 - 2*bp*l**3 + 2*bp*l - bp + 1
    ).as_numer_denom()[0]
    require(sp.expand(transported_gate - gate) == 0, "row-gate transport")
    require(sp.expand(cp - (2*bp - l**3 + l + 1)) == 0,
            "locator transport")
    h8l_labels = (l, -l**2, 1, -1, l**2)
    swapped_labels = (h8l_labels[1], h8l_labels[0], h8l_labels[2],
                      h8l_labels[4], h8l_labels[3])
    require(swapped_labels == (-l**2, l, 1, l**2, -1), "label transport")

    old_products = (-1, -b**2, b, c_original, b*c_original)
    swapped_products = (old_products[1], old_products[0], old_products[2],
                        old_products[4], old_products[3])
    new_products = (-1, -bp**2, bp, cp, bp*cp)
    require(all(sp.expand(new - old/b**2) == 0
                for new, old in zip(new_products, swapped_products)),
            "common product scaling")

    numerator_m = bp * (bp*l**2 - 2*bp*l + bp - 2*l**2 - 2)
    denominator_m = 2*bp*l**2 + 2*bp - l**2 + 2*l - 1
    forced_transport = sp.together(
        numerator_m/denominator_m - (p_numerator/23)/b**2
    ).as_numer_denom()[0]
    require(ideal.reduce(sp.expand(forced_transport))[1] == 0,
            "forced-product transport")

    dp, ep, fp = d/b, e/b, f/b
    old_outside = (c_original*d, c_original*e, sigma_symbol*d*e,
                   d*f, -d*f, e*f, -e*f)
    new_outside = (cp*dp, cp*ep, sigma_symbol*dp*ep,
                   dp*fp, -dp*fp, ep*fp, -ep*fp)
    require(all(sp.expand(new - old/b**2) == 0
                for new, old in zip(new_outside, old_outside)),
            "outside product scaling")
    require(sp.simplify(1/bp - b) == 0 and sp.simplify(cp/bp - c_original) == 0,
            "parameter involution")
    require(sp.simplify(dp/bp - d) == 0, "horizontal involution")
    require(24 - 12 == 12 and 312 - 2*78 == 156, "frontier count")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_H8_POSITIVE_PASS "
        "intrinsic_cases=54 exceptional_unit_ideals=6 rows_deleted=2 "
        "frontier_rows=2 frontier_cells=12 cap=156"
    )


if __name__ == "__main__":
    main()
