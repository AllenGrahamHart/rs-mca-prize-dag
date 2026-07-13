# IMPORT RE-POSE (catch #116, 2026-07-13): this verifier pinned the branch's
# PROVED status + statement; master re-posed the node CONDITIONAL on G1 + the
# descent-classification bridge. The pinned contract check below is adjusted
# to the re-posed sentinel; the ledger arithmetic checks are unchanged.
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
    if g1["status"] != "TARGET" or "sum_(chart chi)(m_chi+1)" not in g1["statement"]:
        raise AssertionError(("weighted G1 contract missing", g1))
    if reserve["status"] != "CONDITIONAL" or "121/126" not in reserve["statement"]:
        raise AssertionError(("reserve contract missing (re-posed form expected)", reserve))
    required = {
        # re-posed wiring (catch #116): ALTERNATE route, ev into the census
        # gate; req hypotheses = the proved chain + G1 + the bridge red
        ("petal_g1_k4_scale_reserve", "petal_small_scale_staircase_census", "ev"),
        ("petal_g1_layer_maps", "petal_g1_k4_scale_reserve", "req"),
        ("petal_descent_classification_bridge", "petal_g1_k4_scale_reserve", "req"),
        ("petal_k4_primitive_bound", "petal_g1_k4_scale_reserve", "req"),
    }
    if not required <= edges:
        raise AssertionError(("reserve wiring missing", sorted(required - edges)))

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
