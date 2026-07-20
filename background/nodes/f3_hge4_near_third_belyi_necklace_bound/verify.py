#!/usr/bin/env python3
"""Verify the HGE4 near-third recurrence, necklace counts, and debits."""

from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_near_third_belyi_necklace_bound"
NORMAL_FORM = "f3_hge4_complement_separator_defect_normal_form"
NECKLACE = "tame_central_star_belyi_necklace_bound"
CONSUMER = "f3_hge4_norm_gate_count"
DUAL_GAP = "f3_hge4_near_third_dual_gap_exclusion"
NECKLACE_VERIFY = ROOT / "background/nodes" / NECKLACE / "verify.py"


def load_necklace_verify():
    spec = importlib.util.spec_from_file_location("necklace_verify", NECKLACE_VERIFY)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def multiply(left: list[Fraction], right: list[Fraction], cutoff: int) -> list[Fraction]:
    output = [Fraction(0)] * cutoff
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            if i + j < cutoff:
                output[i + j] += first * second
    return output


def power(poly: list[Fraction], exponent: int, cutoff: int) -> list[Fraction]:
    output = [Fraction(1)] + [Fraction(0)] * (cutoff - 1)
    for _ in range(exponent):
        output = multiply(output, poly, cutoff)
    return output


def inverse_cube_root(z_poly: list[Fraction], cutoff: int) -> list[Fraction]:
    degree = len(z_poly) - 1
    output = [Fraction(1)] + [Fraction(0)] * (cutoff - 1)
    for index in range(1, cutoff):
        correction = Fraction(0)
        for shift in range(1, min(degree, index) + 1):
            correction += (3 * index - 2 * shift) * z_poly[shift] * output[index - shift]
        output[index] = -correction / (3 * index)
    return output


def reciprocal_ode_check(h_value: int, e_value: int) -> None:
    order = 3 * h_value + e_value
    cutoff = h_value + e_value
    z_poly = [Fraction(1)] + [Fraction(index + 1, index + 3) for index in range(e_value)]
    formal = inverse_cube_root(z_poly, cutoff)
    assert multiply(power(formal, 3, cutoff), z_poly, cutoff) == [Fraction(1)] + [
        Fraction(0)
    ] * (cutoff - 1)

    gamma = [
        -Fraction(3 * h_value + index, 3 * order) * z_poly[index]
        for index in range(e_value + 1)
    ]
    assert gamma[0] == -Fraction(h_value, order)
    fourth = power(formal, 4, cutoff)
    left = [(h_value - index) * formal[index] for index in range(cutoff)]
    right = multiply([-order * value for value in gamma], fourth, cutoff)
    assert left == right
    assert cutoff < 2 * h_value
    assert max(3 * h_value + index for index in range(cutoff)) < 4 * h_value + e_value


def debit_check() -> None:
    necklace = load_necklace_verify()
    expected = {
        (32, 9, 5): 286,
        (64, 20, 4): 892,
        (128, 41, 5): 59598,
        (256, 84, 4): 53020,
        (1024, 340, 4): 3333532,
    }
    for (order, width, defect), debit in expected.items():
        assert order == 3 * width + defect
        assert 0 < defect < width
        assert 2 * necklace.necklace_formula(width + defect, defect) == debit
        boundary = 2 if order % 3 == 1 else (order + 4) // 3
        assert 2 * (debit + boundary) < 21 * order * order

    for width in (5, 21, 85, 341):
        assert 2 * necklace.necklace_formula(width + 1, 1) == 2
    for width in (10, 42, 170, 682):
        order = 3 * width + 2
        assert 2 * necklace.necklace_formula(width + 2, 2) == width + 2
        assert width + 2 == (order + 4) // 3


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == nodes[NORMAL_FORM]["status"] == nodes[NECKLACE]["status"] == "PROVED"
    assert (NORMAL_FORM, NODE, "req") in edges
    assert (NECKLACE, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    assert (NODE, DUAL_GAP, "req") in edges
    base = ROOT / "background/nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join((base / name).read_text() for name in required if name.endswith(".md"))
    for marker in (
        "S=Z^(-1/3) mod y^c", "Phi=ZS^3", "Phi-1=y^cT",
        "E_h^prim(m,p)<=2N(h+e,e)", "(m+4)/3", "3333532",
        "not claimed to pay every",
    ):
        assert marker in text


def main() -> None:
    for h_value, e_value in ((9, 5), (20, 4), (41, 5), (84, 4)):
        reciprocal_ode_check(h_value, e_value)
    debit_check()
    packet_check()
    print(
        "F3_HGE4_NEAR_THIRD_BELYI_NECKLACE_BOUND_PASS "
        "recurrences=4 extra_paid_cells=5 boundaries=8"
    )


if __name__ == "__main__":
    main()
