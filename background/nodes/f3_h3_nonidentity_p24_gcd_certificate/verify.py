#!/usr/bin/env python3
"""Verify the nonidentity P24 gcd-certificate contract."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_nonidentity_p24_gcd_certificate"
DEPENDENCY = "f3_h3_unordered_product_cutoff12_candidate_compiler"
CONSUMER = "f3_h3_dsp8_correlation_bound"


def load_dependency():
    path = ROOT / "background" / "nodes" / DEPENDENCY / "verify.py"
    spec = importlib.util.spec_from_file_location("unordered_verify", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def profile_verdict(unordered: int, diagonal: int) -> tuple[int, int, bool]:
    ordered = 2 * unordered - diagonal
    g12_valuation = max(unordered - 12, 0)
    diagonal_valuation = max(diagonal - 1, 0)
    divides = g12_valuation <= diagonal_valuation
    return ordered, g12_valuation, divides


def synthetic_check() -> None:
    expected = {
        (12, 0): (24, 0, True),
        (13, 2): (24, 1, True),
        (13, 1): (25, 1, False),
        (13, 0): (26, 1, False),
        (14, 2): (26, 2, False),
    }
    for profile, result in expected.items():
        assert profile_verdict(*profile) == result


def row_check() -> None:
    dependency = load_dependency()
    checks = 0
    for n, primes in ((4, (5, 13, 17, 29)), (8, (17, 41, 73, 89))):
        for prime in primes:
            ordered, diagonal, unordered = dependency.fiber_counts(n, prime)
            targets = (set(ordered) | set(diagonal) | set(unordered)) - {1}
            direct = max((ordered[target] for target in targets), default=0) <= 24
            divisibility = all(
                max(unordered[target] - 12, 0)
                <= max(diagonal[target] - 1, 0)
                for target in targets
            )
            assert direct == divisibility
            checks += len(targets)
    assert checks > 100


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

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
        "G_12^neq divides H_D",
        "max_(t!=1) P(t)<=24",
        "ord_t(G_12)=max(U(t)-12,0)",
        "ord_t(H_D)=max(D(t)-1,0)",
        "U(t)=13,       D(t)=2,       P(t)=24",
        "not construct",
    ):
        assert marker in text


def main() -> None:
    synthetic_check()
    row_check()
    packet_check()
    print(
        "F3_H3_NONIDENTITY_P24_GCD_CERTIFICATE_PASS "
        "criterion=G12neq_divides_HD boundary=U13_D2_P24"
    )


if __name__ == "__main__":
    main()
