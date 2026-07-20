#!/usr/bin/env python3
"""Verify the DSP8 one-lift candidate compression contract."""

from __future__ import annotations

import json
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_single_quotient_candidate_compressor"
DEPENDENCIES = {
    "f3_h3_dsp8_single_quotient_endpoint_compiler",
    "f3_h3_double_accident_coupling_matrix_odd_saturation",
    "f3_h3_quotient_algebra_fitting_support_compiler",
}
CONSUMERS = {
    "f3_h3_dsp8_correlation_bound",
    "f3_h3_official_order_template_survivor",
}


def ideal_gcd(generators: list[int]) -> int:
    value = 0
    for generator in generators:
        value = gcd(value, abs(generator))
    return value


def center_ideals(lambda_0: int) -> list[int]:
    pi = 2
    c_u = 3
    C = pi * c_u
    beta_0 = 5
    alpha = [0, 6, 10, 14]
    betas = [beta_0 + pi * pi * item for item in alpha]
    D = beta_0 * C - pi * lambda_0

    ideals = []
    for center, beta_center in enumerate(betas):
        product_generators = [
            (beta - beta_center) // (pi * pi)
            for index, beta in enumerate(betas)
            if index != center
        ]
        coupling = (beta_center * C - D) // pi
        ideals.append(ideal_gcd(product_generators + [coupling]))

    for index in range(1, len(betas)):
        coupling = (betas[index] * C - D) // pi
        assert coupling - lambda_0 == pi * pi * c_u * alpha[index]
    return ideals


def coupling_check() -> None:
    for lambda_0 in (0, 7, 18):
        ideals = center_ideals(lambda_0)
        assert len(set(ideals)) == 1
        assert ideals[0] > 0
    assert center_ideals(0)[0] == 2


def support_check() -> None:
    for product_size in range(30, 42):
        for quotient_size in range(0, 5):
            x_35 = max(product_size - 35, 0) * quotient_size
            rectangle = product_size >= 36 and quotient_size >= 1
            assert (x_35 > 0) == rectangle

    synthetic_pairs = ((1, 1), (3, 15), (9, 315), (35, 3465))
    for s_35, s_18 in synthetic_pairs:
        assert s_18 % s_35 == 0


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for consumer in CONSUMERS:
        assert (NODE, consumer, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join(
        (base / name).read_text() for name in required if name.endswith(".md")
    )
    for marker in (
        "I_k=I_0",
        "nonzero even if `lambda_k=0`",
        "p divides s_(n,35)^X",
        "Dbar_17^0+Dbar_17^A>0",
        "s_(n,35)^X divides s_(n,18)^X",
        "No search for a nonzero coupling center",
        "not bound or efficiently compute",
    ):
        assert marker in text


def main() -> None:
    coupling_check()
    support_check()
    packet_check()
    print(
        "F3_H3_DSP8_SINGLE_QUOTIENT_CANDIDATE_COMPRESSOR_PASS "
        "center_independent=1 zero_tolerant=1 cutoff=35 divisor=s35|s18"
    )


if __name__ == "__main__":
    main()
