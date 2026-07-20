#!/usr/bin/env python3
"""Verify the DSP8 nodal Stepanov constant barrier."""

from __future__ import annotations

import json
from fractions import Fraction
from math import isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_nodal_stepanov_constant_barrier"
DEPENDENCIES = (
    "f3_affine_coset_pair_cubic_preimage_stepanov",
    "f3_h3_dsp8_nodal_cube_preimage_envelope",
)
CONSUMER = "f3_h3_dsp8_correlation_bound"


def constants_check() -> None:
    assert 51**3 == 132651
    assert 32 * 16**3 == 131072
    assert 51**3 > 32 * 16**3
    assert Fraction(2176, 1) > Fraction(76599, 40)
    assert 87040 - 76599 == 10441
    # 3^(1/3)>4/3, hence 3^(4/3)>4.
    assert 3 * 3**3 > 4**3


def integer_parameter_check() -> int:
    checked = 0
    for m in range(2, 301):
        for b in range(1, m + 1):
            for a in range(1, m // b + 1):
                target = a * b * b
                d = max(0, (isqrt(a * a + 4 * target) - a) // 2)
                while d * (a + d) >= target:
                    d -= 1
                while (d + 1) * (a + d + 1) < target:
                    d += 1
                if d:
                    # The maximal feasible d is the hardest case.
                    assert (a + 2 * m * b) ** 3 > 32 * d**3 * m**2
                    checked += 1
    return checked


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
        "(A+2mB)/D > 2^(5/3)m^(2/3)",
        "17*32*3^(4/3)>2176>76599/40",
        "proof-method barrier",
        "not a lower bound on the actual nodal record",
    ):
        assert marker in text


def main() -> None:
    constants_check()
    checked = integer_parameter_check()
    packet_check()
    print(
        "F3_H3_DSP8_NODAL_STEPANOV_CONSTANT_BARRIER_PASS "
        f"integer_tuples={checked} allowance_slack=10441/40"
    )


if __name__ == "__main__":
    main()
