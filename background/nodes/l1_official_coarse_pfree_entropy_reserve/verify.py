#!/usr/bin/env python3
"""Verify the official coarse p-free entropy reserve."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_official_coarse_pfree_entropy_reserve"


def main() -> None:
    checks = 0

    rates = (Fraction(1, 2), Fraction(1, 4), Fraction(1, 8), Fraction(1, 16))
    step_caps = tuple((1 - rate) / rate for rate in rates)
    assert step_caps == (1, 3, 7, 15)
    checks += 1

    gap = 3175
    checkpoint_cap = 23
    reserve_bits = 9 * gap - 13 * checkpoint_cap
    assert reserve_bits == 28276
    assert reserve_bits - 128 == 28148
    checks += 2

    p = 3583
    d0 = 408
    d = p
    checkpoint_count = 1
    delta = d - d0
    exponent_15 = -18 * delta + 22 * checkpoint_count + 15 * (d - checkpoint_count)
    exponent_16 = -18 * delta + 22 * checkpoint_count + 16 * (d - checkpoint_count)
    assert delta == 3175
    assert exponent_15 == -3398
    assert exponent_15 < -3393 < -106
    assert exponent_16 == 184
    assert Fraction(-(21 * p - 595), 22) < -3393
    checks += 5

    # Exact consecutive-binomial ratios obey the advertised four-rate cap.
    n = 1 << 13
    for rate, cap in zip(rates, step_caps, strict=True):
        k = n * rate.numerator // rate.denominator
        ratio = Fraction(1, 1)
        for offset in range(32):
            ratio *= Fraction(n - k - offset, k + offset + 1)
            assert ratio < cap ** (offset + 1)
            checks += 1

    # The finite inflation exponent is exactly the average reserve minus 128.
    assert 28148 - 28276 == -128
    checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_official_reserve_tame_refinement_router",
        "l1_official_newton_cofactor_window_router",
        "l1_official_frobenius_checkpoint_q_router",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    assert (NODE, "l1_mixed_petal_amplification", "ev") in edges
    checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "Delta>=3175",
        "r<=23",
        "mu_free(d)<2^(-28276)",
        "K_d<=q 2^28148",
        "max_s Exc_d(s)<=2^(15(d-r)) mu_free(d)",
        "max_s Exc_d(s)<2^-3393<1",
        "arithmetically sufficient",
        "does not prove `(CER6)`",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_OFFICIAL_COARSE_PFREE_ENTROPY_RESERVE_PASS checks={checks}")


if __name__ == "__main__":
    main()
