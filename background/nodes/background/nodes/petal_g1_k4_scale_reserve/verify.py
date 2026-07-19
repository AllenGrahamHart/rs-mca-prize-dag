# IMPORT RE-POSE (catch #116, 2026-07-13): this verifier pinned the branch's
# PROVED status + statement; master re-posed the node CONDITIONAL on G1 + the
# descent-classification bridge. The pinned contract check below is adjusted
# to the re-posed sentinel; the ledger arithmetic checks are unchanged.
#
# RETIREMENT RE-POSE (2026-07-13 evening, first caught by the 121-script
# Modal replay): the node was RETIRED at the bsr surgery (catch #150 — it
# hypothesizes exactly the falsified weighted form + the 64/63 rider, whose
# ledger hypothesis is g1a-unsatisfiable per #148; superseded by Lemma COL +
# clause (D)), and G1 itself is now PROVED (clause-(P) banking). Pins below
# re-posed to the banked retired truth: G1 PROVED with the weighted-form
# history retained in its custody-merged statement; reserve REFUTED with the
# RETIRED block; req in-edges REMOVED (refuted nodes carry none), the ev
# ALTERNATE edge to the census gate retained as history. The ledger
# arithmetic checks remain unchanged (historically exact).
#!/usr/bin/env python3
"""Exact contract and coefficient replay for the G1/K4 scale reserve."""

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


ROWS = (
    (1 << 41, 1 << 40, 8_592_912_739),
    (1 << 42, 1 << 40, 2 * 7_014_660_390),
    (1 << 43, 1 << 40, 4 * 4_722_556_392),
    (1 << 44, 1 << 40, 8 * 2_943_177_800),
)


def main() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind")) for edge in dag["edges"]}
    g1 = nodes["petal_g1_layer_maps"]
    reserve = nodes["petal_g1_k4_scale_reserve"]
    if g1["status"] != "PROVED" or "sum_(chart chi)(m_chi+1)" not in g1["statement"]:
        raise AssertionError(("G1 contract drift (expected PROVED with the "
                              "weighted-form history retained)", g1["status"]))
    if "CLAUSE (P) PROVED" not in g1["statement"]:
        raise AssertionError("G1 clause-(P) resolution block missing")
    if reserve["status"] != "REFUTED" or "121/126" not in reserve["statement"]:
        raise AssertionError(("reserve contract drift (expected REFUTED with "
                              "the historical 121/126 constant)",
                              reserve["status"]))
    if "RETIRED (2026-07-13, catch #150)" not in reserve["statement"]:
        raise AssertionError("reserve RETIRED block missing")
    # retirement wiring: the ev ALTERNATE edge remains as history; the req
    # in-edges were removed with the retirement and must stay gone
    if ("petal_g1_k4_scale_reserve", "petal_small_scale_staircase_census",
            "ev") not in edges:
        raise AssertionError("historical ev ALTERNATE edge missing")
    stale_req = {(f, "petal_g1_k4_scale_reserve", "req")
                 for f in ("petal_g1_layer_maps",
                           "petal_descent_classification_bridge",
                           "petal_k4_primitive_bound")} & edges
    if stale_req:
        raise AssertionError(("req in-edges must not return on a REFUTED "
                              "node", sorted(stale_req)))

    quotient_rows = 0
    for n, k, slack in ROWS:
        if not slack < n // 128:
            raise AssertionError((n, slack, n // 128))
        scale = 1
        while 2 * scale <= slack:
            scale *= 2
        quotient_n = n // scale
        if quotient_n < 256 or quotient_n & (quotient_n - 1):
            raise AssertionError((n, slack, scale, quotient_n))
        quotient_rows += 1

    worst = Fraction(15, 16) + Fraction(2, 256)
    if worst != Fraction(121, 128) or not worst < Fraction(63, 64):
        raise AssertionError(worst)
    combined = Fraction(64, 63) * worst
    if combined != Fraction(121, 126) or not combined < 1:
        raise AssertionError(combined)

    for denominator in (2, 4, 8, 16):
        for quotient_n in (256, 512, 1024, 1 << 20):
            coefficient = Fraction(denominator - 1, denominator) + Fraction(2, quotient_n)
            if coefficient > worst:
                raise AssertionError((denominator, quotient_n, coefficient))

    # At n'=32 the desired 63/64 reserve can fail, so the quotient floor is
    # load-bearing rather than cosmetic.
    if Fraction(15, 16) + Fraction(2, 32) <= Fraction(63, 64):
        raise AssertionError("short-quotient mutation was accepted")

    print(
        "PETAL_G1_K4_SCALE_RESERVE_PASS "
        f"official_rows={quotient_rows} C={worst} combined={combined} "
        f"margin={1-combined} premise=weighted"
    )


if __name__ == "__main__":
    main()
