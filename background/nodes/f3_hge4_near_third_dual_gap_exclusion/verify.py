#!/usr/bin/env python3
"""Verify the dual-gap algebra, recurrence, and HGE4 packet wiring."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_near_third_dual_gap_exclusion"
SOURCE = "f3_hge4_near_third_belyi_necklace_bound"
CONSUMER = "f3_hge4_norm_gate_count"


def multiply(left: list[Fraction], right: list[Fraction], cutoff: int) -> list[Fraction]:
    output = [Fraction(0)] * cutoff
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            if i + j < cutoff:
                output[i + j] += first * second
    return output


def rational_power(z_poly: list[Fraction], numerator: int, denominator: int, cutoff: int) -> list[Fraction]:
    """Solve denominator*Z*B'=numerator*Z'*B coefficientwise."""
    output = [Fraction(1)] + [Fraction(0)] * (cutoff - 1)
    degree = len(z_poly) - 1
    for index in range(1, cutoff):
        correction = Fraction(0)
        for shift in range(1, min(degree, index) + 1):
            correction += (
                denominator * (index - shift) - numerator * shift
            ) * z_poly[shift] * output[index - shift]
        output[index] = -correction / (denominator * index)
    return output


def inverse(poly: list[Fraction], cutoff: int) -> list[Fraction]:
    output = [Fraction(1)] + [Fraction(0)] * (cutoff - 1)
    for index in range(1, cutoff):
        output[index] = -sum(
            poly[shift] * output[index - shift]
            for shift in range(1, min(index, len(poly) - 1) + 1)
        )
    return output


def dual_gap_fixture(h_value: int, z_poly: list[Fraction]) -> None:
    e_value = len(z_poly) - 1
    center = h_value + e_value
    cutoff = 2 * h_value
    formal = rational_power(z_poly, -1, 3, cutoff)
    assert all(formal[index] == 0 for index in range(h_value + 1, center))
    centered = formal[: h_value + 1]
    centered += [Fraction(0)] * (cutoff - len(centered))
    centered_inverse = inverse(centered, cutoff)
    centered_inverse_square = multiply(centered_inverse, centered_inverse, cutoff)
    two_thirds = rational_power(z_poly, 2, 3, cutoff)
    for index in range(center + 1, cutoff):
        assert centered_inverse_square[index] == 3 * two_thirds[index]


def recurrence_check(e_value: int, h_value: int) -> None:
    center = h_value + e_value
    assert h_value >= 2 * e_value + 1
    zeros = set(range(center + 1, 2 * h_value))
    for root_index in range(center, -1, -1):
        if all(root_index + offset in zeros for offset in range(1, e_value + 1)):
            coefficient = 3 * root_index - 2 * e_value
            if coefficient:
                zeros.add(root_index)
            else:
                assert e_value % 3 == 0
                assert root_index == 2 * e_value // 3
                break
    if e_value % 3:
        assert 0 in zeros
    else:
        assert all(index in zeros for index in range(2 * e_value // 3 + 1, 2 * h_value))


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == nodes[SOURCE]["status"] == "PROVED"
    assert (SOURCE, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    base = ROOT / "background/nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join((base / name).read_text() for name in required if name.endswith(".md"))
    for marker in (
        "h>=2e+1", "E_h^prim(m,p)=0", "7h<=2m", "3ZB'=2Z'B",
        "3r-2e", "dyadic", "zero-cost",
    ):
        assert marker in text


def main() -> None:
    # e=1 has no endpoint-zero condition.
    dual_gap_fixture(5, [Fraction(1), Fraction(-1)])
    # For even h, Z=1+By^2 makes the sole e=2 endpoint coefficient odd and zero.
    dual_gap_fixture(10, [Fraction(1), Fraction(0), Fraction(2)])
    checked = 0
    for e_value in range(1, 10):
        if e_value % 3 == 0:
            continue
        recurrence_check(e_value, 2 * e_value + 1)
        recurrence_check(e_value, 3 * e_value + 4)
        checked += 2
    packet_check()
    print(
        "F3_HGE4_NEAR_THIRD_DUAL_GAP_EXCLUSION_PASS "
        f"formal_fixtures=2 recurrence_cells={checked}"
    )


if __name__ == "__main__":
    main()
