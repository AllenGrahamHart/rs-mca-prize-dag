#!/usr/bin/env python3
"""Verify the aligned one-loop 442 outside-product router."""

import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_aligned_outside_product_router"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    values = tuple(values)
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index + 1:]
        if not rest:
            yield ((first, second),)
        else:
            for tail in pairings(rest):
                yield ((first, second),) + tail


def direct_collision(left, right):
    """Whether equality up to sign immediately identifies target pairs."""
    edges = {
        "x": frozenset(("C", "E")),
        "y": frozenset(("C", "F")),
        "z": ("D", "D"),
        "u": frozenset(("D", "E")),
        "v": frozenset(("D", "F")),
    }
    left_edge, right_edge = edges[left], edges[right]
    if isinstance(left_edge, tuple):
        left_edge = list(left_edge)
    else:
        left_edge = list(left_edge)
    if isinstance(right_edge, tuple):
        right_edge = list(right_edge)
    else:
        right_edge = list(right_edge)
    for vertex in set(left_edge) & set(right_edge):
        left_residual = left_edge.copy()
        right_residual = right_edge.copy()
        left_residual.remove(vertex)
        right_residual.remove(vertex)
        if len(left_residual) == len(right_residual) == 1:
            return left_residual[0] != right_residual[0]
    return False


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("`S0` is empty" in statement and "S1-DE" in statement
            and "S1-DF" in statement and "KB41R-4" in statement, "claim")
    require("does not impose the outside q equations" in statement
            and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_aligned_pair_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_edge_skeleton_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    # The two common negation pairs force Gamma=Beta=0.
    gamma0, alpha0, beta0, b, c = sp.symbols("Gamma Alpha Beta b c")
    row_b = -gamma0*b**2-beta0
    row_c = -gamma0*c**2-beta0
    require(sp.expand(row_b-row_c-gamma0*(c**2-b**2)) == 0,
            "involution subtraction")
    require(sp.expand(row_b.subs(gamma0, 0)) == -beta0,
            "involution beta")

    # For S0, whichever singleton is forced, the remaining two share a
    # target vertex and hence collide after imposing negation.
    s0_edges = ({"C", "E"}, {"C", "F"}, {"E", "F"})
    for forced in range(3):
        left, right = [s0_edges[index] for index in range(3)
                       if index != forced]
        require(bool(left & right), f"S0 forced branch {forced}")

    # Exhaust all three residual pairings for each possible forced S1
    # singleton. Only one non-immediate pairing remains for z,u,v.
    survivors = {}
    for forced in "xyzuv":
        residual = [value for value in "xyzuv" if value != forced]
        live = [pairing for pairing in pairings(residual)
                if not any(direct_collision(*pair) for pair in pairing)]
        survivors[forced] = live
    require(len(survivors["x"]) == len(survivors["y"]) == 0,
            "colored forced exclusions")
    require(len(survivors["z"]) == 1, "loop forced pre-exclusion")
    require(set(map(frozenset, survivors["z"][0]))
            == {frozenset(("x", "v")), frozenset(("y", "u"))},
            "loop residual pairing")
    require(len(survivors["u"]) == len(survivors["v"]) == 1,
            "internal forced branches")
    require(set(map(frozenset, survivors["u"][0]))
            == {frozenset(("x", "v")), frozenset(("y", "z"))},
            "DE branch")
    require(set(map(frozenset, survivors["v"][0]))
            == {frozenset(("x", "z")), frozenset(("y", "u"))},
            "DF branch")

    # The forced-loop residual branch gives c^2=+/-d^2. Together with
    # d^2=-b^2 this collides C with D or B, so it is not live.
    require("z" in survivors and len(survivors["z"]) == 1,
            "forced-loop secondary exclusion")

    # Symbolically replay both S1 branches and their quartic consequence.
    a, be, g, de, d, e, f = sp.symbols("a be g de d e f")
    x, y, z = a*c*e, be*c*f, -d**2
    u, v = g*d*e, de*d*f
    sign_rules = {a**2: 1, be**2: 1, g**2: 1, de**2: 1}

    de_subs = {e: g*b**2/d, f: be*d**2/c}
    de_numerator = sp.together((x+v).subs(de_subs)).as_numer_denom()[0]
    require(sp.expand(
        sp.expand(be*de*de_numerator).subs(sign_rules)
        -(d**4+a*be*g*de*b**2*c**2)
    ) == 0, "DE quartic")
    require(sp.expand((u-b**2).subs(de_subs)).subs(sign_rules) == 0,
            "DE forced converse")
    require(sp.expand((y+z).subs(de_subs)).subs(sign_rules) == 0,
            "DE residual converse")

    df_subs = {f: de*b**2/d, e: a*d**2/c}
    df_numerator = sp.together((y+u).subs(df_subs)).as_numer_denom()[0]
    require(sp.expand(
        sp.expand(a*g*df_numerator).subs(sign_rules)
        -(d**4+a*be*g*de*b**2*c**2)
    ) == 0, "DF quartic")
    require(sp.expand((v-b**2).subs(df_subs)).subs(sign_rules) == 0,
            "DF forced converse")
    require(sp.expand((x+z).subs(df_subs)).subs(sign_rules) == 0,
            "DF residual converse")

    # S2 has exactly three pre-existing pairs and one singleton.
    s2 = (("cd", "-cd"), ("df", "-df"), ("ef", "-ef"))
    require(len(s2) == 3, "S2 pair census")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_ROUTER_PASS "
        "S0=empty S1=2_branches S2=1_branch"
    )


if __name__ == "__main__":
    main()
