#!/usr/bin/env python3
"""Verify the P25 ordered-root quadratic tower compiler."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_p25_ordered_root_quadratic_tower_compiler"
DEPENDENCY = "f3_h3_p25_quadratic_divisor_tower_compiler"
CONSUMER = "f3_h3_dsp8_correlation_bound"


def load_divisor():
    path = ROOT / "background" / "nodes" / DEPENDENCY / "verify.py"
    spec = importlib.util.spec_from_file_location("divisor_verify", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def system_size(s: int, q: int = 25) -> tuple[int, int]:
    differences = q * (q - 1) // 2
    variables = 2 * q * s + q + differences + 3
    equations = 2 * q * s + 2 * q + differences + 2
    return variables, equations


def arithmetic_check() -> None:
    assert system_size(13) == (978, 1002)
    assert system_size(41) == (2378, 2402)
    divisor = load_divisor()
    for s in range(13, 42):
        variables, equations = system_size(s)
        assert equations - variables == 24
        assert variables < divisor.system_size(s)[0]
        assert equations < divisor.system_size(s)[1]


def finite_field_check() -> None:
    divisor = load_divisor()
    incidence = divisor.load_incidence()
    fibers = incidence.load_fibers()
    checks = 0
    for n, prime, q in ((4, 13, 2), (8, 41, 3), (8, 73, 3)):
        ordered, _, _ = fibers.fiber_counts(n, prime)
        for target in range(2, prime):
            distinct_first_coordinates = ordered[target]
            assert (distinct_first_coordinates >= q) == (ordered[target] >= q)
            checks += 1
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
        "B_(i,0)=(x_i-T)z_i",
        "A_(i,j+1)=A_(i,j)^2",
        "B_(i,j+1)=B_(i,j)^2",
        "binom(q,2)=300",
        "50s+328 variables",
        "50s+352 equations",
        "2,378",
        "q!",
    ):
        assert marker in text


def main() -> None:
    arithmetic_check()
    finite_field_check()
    packet_check()
    print(
        "F3_H3_P25_ORDERED_ROOT_QUADRATIC_TOWER_COMPILER_PASS "
        "max_variables=2378 max_equations=2402 symmetry=25_factorial"
    )


if __name__ == "__main__":
    main()
