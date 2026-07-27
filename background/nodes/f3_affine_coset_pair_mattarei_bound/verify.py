#!/usr/bin/env python3
"""Deterministic statement, source-pin, DAG, and arithmetic checks for MAC1."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_affine_coset_pair_mattarei_bound"
CONSUMERS = {
    "f3_h3_dsp8_nodal_cube_preimage_envelope",
    "f3_h3_dsp8_antipodal_quotient_mass_payment",
    "f3_h3_dsp8_global_overlap_cover_payment",
}


def main() -> None:
    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "source_pin.json",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}

    text = "\n".join(
        (base / name).read_text()
        for name in required
        if name.endswith(".md")
    ).replace(" ", "")
    for marker in (
        "C_M=3*2^(-2/3)",
        "d^3>=4m",
        "alpha,betainF_p^*",
        "arbitrarycoefficientsin`(4)`",
        "prime-fieldonly",
        "bypasses,butdoesnotrefute",
    ):
        assert marker in text, marker

    pin = json.loads((base / "source_pin.json").read_text())
    assert pin["doi"] == "10.1016/j.ffa.2006.03.005"
    assert pin["arxiv_id"] == "math/0511339"
    assert pin["arxiv_version"] == "v1"
    assert pin["source_archive_sha256"] == (
        "69a757ee03e108c794105efd8e86ec549dec222ee6c1f8772e1f6521bdd490fd"
    )
    assert pin["source_member"] == "GV.tex"

    # (3*2^(-2/3))^3 = 27/4, and 1.89 is a strict rational upper bound.
    assert 4 * 189**3 > 27 * 100**3

    n_min = 1 << 13
    assert n_min * n_min >= 768
    # d>n/4 and m<=3n imply d^3>n^3/64>=12n>=4m.
    assert n_min**3 >= 64 * 12 * n_min
    assert n_min // 4 >= 4

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for consumer in CONSUMERS:
        assert (NODE, consumer, "req") in edges

    print(
        "F3_AFFINE_COSET_PAIR_MATTAREI_BOUND_PASS "
        "constant_cube=27/4 consumers=3 official_m=n,3n"
    )


if __name__ == "__main__":
    main()
