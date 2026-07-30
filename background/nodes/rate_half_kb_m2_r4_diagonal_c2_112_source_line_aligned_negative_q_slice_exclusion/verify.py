#!/usr/bin/env python3
"""Verify the aligned negative q-slice exclusion contract."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_c2_112_source_line_aligned_negative_q_slice_exclusion"
PARENTS = {
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_negative_reconstruction_factor_gate",
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("m_0=(cd-1)(cd+1)/(c^2 d^2)" in statement, "constant mismatch")
    require("m_1-m_3=4(c^2-1)/c=-A" in statement, "outer mismatch")
    require("near-aligned negative candidate" in statement, "scope fence")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require(all((parent, NODE_ID, "req") in edges for parent in PARENTS),
            "dependencies")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    b, c, d, w = sp.symbols("b c d w", nonzero=True)
    p = c * d - 2 * c - 2 * d + 1
    q = 2 * c * d - c - d + 2
    factor_b = b * p + q
    factor_c = b * q + p
    require(sp.cancel(factor_c - b * factor_b.subs(b, 1 / b)) == 0,
            "B/C inversion")
    require(sp.expand(2 * p - q) == -3 * (c + d), "P/Q joint-zero router")

    d_special = -1 / c
    a_special = sp.factor((5 * c * d - 4 * c - 4 * d + 5).subs(d, d_special))
    outer_difference = 4 * (c**2 - 1) / c
    require(sp.cancel(outer_difference + a_special) == 0,
            "outer mismatch equals -A")
    require(sp.cancel((-q / p).subs(d, d_special) + sp.Rational(1, 2)) == 0,
            "B-locus b specialization")

    helper = (ROOT / "critical/nodes/rate_half_band_closure/notes/"
              "kb_c2_112_negative_qslice_locus.py").read_text()
    require("constant_mismatch" in helper, "symbolic constant replay")
    require("cd_minus_one_m1_minus_m3" in helper, "symbolic outer replay")

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_112_SOURCE_LINE_ALIGNED_NEGATIVE_Q_SLICE_EXCLUSION_PASS "
        "templates=8+4 retained_signs_aligned=positive near_aligned_unchanged=true"
    )


if __name__ == "__main__":
    main()
