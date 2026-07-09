#!/usr/bin/env python3
"""Verify the structural reduction of the h=5 residual.

The reduction is only classificatory: it proves that h=5 has no unpaid
char-zero branch and that any finite-row h=5 survivor must be a p-specific
x83 norm-gate event.  It does not prove that the norm-gate branch is empty.
"""

from __future__ import annotations

import json
from pathlib import Path

from f3_h5_central_finite_scheme_payment import finite_scheme_payment_summary


ROOT = Path(__file__).resolve().parents[4]


REQUIRED_PROVED = (
    "x24_char0_dyadic_descent",
    "x83_uniform_square_shift_obstruction_gate",
    "a_universal_trade_variety",
)


def load_dag() -> dict:
    return json.loads((ROOT / "dag.json").read_text())


def node_by_id(dag: dict) -> dict[str, dict]:
    return {node["id"]: node for node in dag["nodes"]}


def require_proved(nodes: dict[str, dict], node_id: str) -> dict:
    node = nodes.get(node_id)
    if node is None:
        raise AssertionError(f"missing node {node_id}")
    if node.get("status") != "PROVED":
        raise AssertionError((node_id, node.get("status")))
    return node


def main() -> None:
    dag = load_dag()
    nodes = node_by_id(dag)
    loaded = {node_id: require_proved(nodes, node_id) for node_id in REQUIRED_PROVED}

    x24_statement = loaded["x24_char0_dyadic_descent"].get("statement", "")
    x83_statement = loaded["x83_uniform_square_shift_obstruction_gate"].get(
        "statement", ""
    )
    auniv_statement = loaded["a_universal_trade_variety"].get("statement", "")

    required_phrases = [
        (x24_statement, "h not a power of two: NO such trade exists"),
        (x24_statement, "h a power of two: P and Q are full mu_h fibers"),
        (x83_statement, "p-SPECIFIC NORM-GATE EVENT"),
        (x83_statement, "the row prime divides the cyclotomic norm"),
        (auniv_statement, "Trades at any row = points of W_h"),
    ]
    for text, phrase in required_phrases:
        if phrase not in text:
            raise AssertionError(f"missing phrase: {phrase}")

    h = 5
    if h & (h - 1) == 0:
        raise AssertionError("h=5 incorrectly classified as a power of two")

    finite_payment = finite_scheme_payment_summary()
    if finite_payment["degree_product"] != 19840464:
        raise AssertionError(finite_payment)

    print("proved inputs:")
    for node_id in REQUIRED_PROVED:
        print(f"  {node_id}: PROVED")
    print("h=5 is not a power of two: char-zero dyadic branch is empty")
    print("x83 leaves only p-specific norm-gate events at finite rows")
    print(
        "central finite-scheme payment route: "
        f"K={finite_payment['degree_product']} gives K*n<n^3 on official rows"
    )
    print("H5_STRUCTURAL_REDUCTION_PASS")


if __name__ == "__main__":
    main()
