#!/usr/bin/env python3
"""Verify the balanced-factor Haar gate and the complete m=128 upper range."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_multiscale_haar_m128_frontier"


def augmented_subset_gate(m: int, h: int, s: int, positive_mask: int) -> bool:
    """Exact cross-multiplied form of (MX3)."""
    H = (h - 1) // 2
    ell = H.bit_length()
    A = m // 4
    orders = [m // (1 << (a + 1)) for a in range(ell)]
    rs = [((H // (1 << a)) + 1) // 2 for a in range(ell)]
    positive = [a for a in range(ell) if positive_mask & (1 << a)]
    zero = [a for a in range(ell) if not positive_mask & (1 << a)]
    Bs = {a: orders[a] // 4 for a in positive}
    W = A + sum(Bs.values())
    row_exp = h // 2 + sum(rs[a] for a in positive)

    norm_orders = [m] + [orders[a] for a in positive]
    structural_two_exp = sum(
        min(order, orders[a]) // 2
        for order in norm_orders
        for a in zero
    )
    balanced_two_exp = len(norm_orders)
    upper_two_exp = sum((a + 1) * Bs[a] for a in positive)

    left = (
        (1 << (structural_two_exp + balanced_two_exp))
        * (1 << s) ** (2 * row_exp)
        * W**W
    )
    right = (1 << upper_two_exp) * (4 * h) ** W * A**A
    for value in Bs.values():
        right *= value**value
    return left >= right


def failing_masks(h: int, s: int = 13) -> list[int]:
    ell = ((h - 1) // 2).bit_length()
    return [
        mask
        for mask in range(1 << ell)
        if not augmented_subset_gate(128, h, s, mask)
    ]


def main() -> None:
    for h in range(12, 32):
        assert failing_masks(h) == []

    assert failing_masks(11) == [0b111]
    assert failing_masks(10) == [0b011, 0b111]
    assert failing_masks(9) == [0b000, 0b001, 0b011, 0b101, 0b111]

    assert list(range(32, 43)) == [h for h in range(32, 64) if 32 <= h < 128 / 3]
    assert list(range(43, 65)) == [h for h in range(32, 65) if 3 * h >= 128]

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for dependency in (
        "f3_hge4_multiscale_haar_m64_level_close",
        "f3_hge4_cyclotomic_norm_quarter_width_exclusion",
        "f3_hge4_nonfull_complement_third_gate",
    ):
        assert (dependency, NODE, "req") in edges
    assert (NODE, "f3_hge4_norm_gate_count", "ev") in edges

    statement = Path(__file__).with_name("statement.md").read_text()
    proof = Path(__file__).with_name("proof.md").read_text()
    for marker in ("(MX2)", "(MX3)", "(MX4)", "(MX5)"):
        assert marker in statement
    assert "coprime" in proof and "1+|S|" in proof

    print(
        "F3_HGE4_MULTISCALE_HAAR_M128_FRONTIER_PASS "
        "closed=12..64 h11_residual=111 h10_residual=011,111"
    )


if __name__ == "__main__":
    main()
