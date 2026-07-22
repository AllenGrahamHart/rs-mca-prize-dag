#!/usr/bin/env python3
"""Verify the P25 quadratic divisor-tower compiler contract."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_p25_quadratic_divisor_tower_compiler"
DEPENDENCIES = {
    "f3_h3_global_resultant_compression",
    "f3_h3_shifted_product_sidon",
}
CONSUMER = "f3_h3_dsp8_correlation_bound"
SUBRESULTANT_NODE = "f3_h3_nonidentity_p25_subresultant_scalar_compiler"


def load_incidence():
    path = ROOT / "background" / "nodes" / SUBRESULTANT_NODE / "verify.py"
    spec = importlib.util.spec_from_file_location("subresultant_verify", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def system_size(s: int, q: int = 25) -> tuple[int, int]:
    variables = (4 * s + 1) * q + 5 - 2 * s
    equations = (4 * s + 2) * q + 4 - 2 * s
    return variables, equations


def arithmetic_check() -> None:
    assert system_size(13) == (1304, 1328)
    assert system_size(41) == (4048, 4072)
    for s in range(13, 42):
        variables, equations = system_size(s)
        assert equations - variables == 24
        assert variables <= 4048
        assert equations <= 4072


def finite_field_check() -> None:
    incidence = load_incidence()
    fibers = incidence.load_fibers()
    # A degree-q common divisor exists exactly when the gcd degree is at least q.
    checks = 0
    for n, prime, q in ((4, 13, 2), (8, 41, 3), (8, 73, 3)):
        ordered, _, _ = fibers.fiber_counts(n, prime)
        for target in range(2, prime):
            f, g = incidence.incidence_polynomials(n, target, prime)
            degree = incidence.gcd_degree(f, g, prime)
            assert degree == ordered[target]
            assert (degree >= q) == (ordered[target] >= q)
            checks += 1
    assert checks > 100


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
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
        "XZ=1 mod Q",
        "T tau=1",
        "(T-1)eta=1",
        "A_(j+1)=A_j^2 mod Q",
        "B_(j+1)=B_j^2 mod Q",
        "98s+30 variables",
        "98s+54 equations",
        "4,048",
        "not a claim that Groebner",
    ):
        assert marker in text


def main() -> None:
    arithmetic_check()
    finite_field_check()
    packet_check()
    print(
        "F3_H3_P25_QUADRATIC_DIVISOR_TOWER_COMPILER_PASS "
        "max_variables=4048 max_equations=4072 degree=2"
    )


if __name__ == "__main__":
    main()
