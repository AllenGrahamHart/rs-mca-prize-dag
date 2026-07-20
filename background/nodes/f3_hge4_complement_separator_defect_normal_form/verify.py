#!/usr/bin/env python3
"""Verify the HGE4 complement-separator defect normal form."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_complement_separator_defect_normal_form"
DEPENDENCY = "f3_hge4_nonfull_complement_third_gate"
CONSUMER = "f3_hge4_norm_gate_count"
BASE_PATH = ROOT / "background/nodes" / DEPENDENCY / "verify.py"


def load_base():
    spec = importlib.util.spec_from_file_location("hge4_complement_base", BASE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fixture(order: int, prime: int, width: int) -> tuple[int, int]:
    base = load_base()
    pairs = base.shift_pairs(order, prime, width)
    assert pairs
    left, right = pairs[0]
    p_poly = base.locator(left, prime)
    q_poly = base.locator(right, prime)
    difference = base.sub(q_poly, p_poly, prime)
    assert len(difference) == 1 and difference[0] != 0
    d_value = difference[0]

    x_power_minus_one = [(-1) % prime] + [0] * (order - 1) + [1]
    r_poly = base.div_exact(
        x_power_minus_one, base.mul(p_poly, q_poly, prime), prime
    )
    complement = len(r_poly) - 1
    defect = order - 3 * width
    h_poly = base.scale(
        base.mul(
            [0, 1],
            base.mul(base.derivative(p_poly, prime), r_poly, prime),
            prime,
        ),
        d_value * pow(order, -1, prime),
        prime,
    )
    a_poly = base.div_exact(base.sub(h_poly, [1], prime), p_poly, prime)
    b_poly = base.div_exact(base.add(h_poly, [1], prime), q_poly, prime)
    g_poly = base.sub(b_poly, a_poly, prime)

    assert complement == order - 2 * width
    assert len(g_poly) - 1 == defect == complement - width
    expected_lead = -d_value * d_value * width * pow(order, -1, prime)
    assert g_poly[-1] == expected_lead % prime

    rebuilt_a = base.scale(
        base.sub([2], base.mul(q_poly, g_poly, prime), prime),
        pow(d_value, -1, prime),
        prime,
    )
    rebuilt_b = base.scale(
        base.sub([2], base.mul(p_poly, g_poly, prime), prime),
        pow(d_value, -1, prime),
        prime,
    )
    assert rebuilt_a == a_poly and rebuilt_b == b_poly

    left_side = base.scale(
        base.sub(
            base.add(p_poly, q_poly, prime),
            base.mul(base.mul(p_poly, q_poly, prime), g_poly, prime),
            prime,
        ),
        order,
        prime,
    )
    right_side = base.scale(
        base.mul(
            [0, 1],
            base.mul(base.derivative(p_poly, prime), r_poly, prime),
            prime,
        ),
        d_value * d_value,
        prime,
    )
    assert left_side == right_side
    return defect, len(pairs)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    base = ROOT / "background/nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join((base / name).read_text() for name in required if name.endswith(".md"))
    for marker in (
        "e=c-h=m-3h", "deg G=e", "lc(G)=-d^2 h/m",
        "m(P+Q-PQG)=d^2 XP'R", "necessary, not sufficient",
    ):
        assert marker in text


def main() -> None:
    linear_defect, linear_pairs = fixture(4, 5, 1)
    quartic_defect, quartic_pairs = fixture(16, 17, 4)
    assert linear_defect == 1 and quartic_defect == 4
    packet_check()
    print(
        "F3_HGE4_COMPLEMENT_SEPARATOR_DEFECT_NORMAL_FORM_PASS "
        f"e1_pairs={linear_pairs} e4_pairs={quartic_pairs}"
    )


if __name__ == "__main__":
    main()
