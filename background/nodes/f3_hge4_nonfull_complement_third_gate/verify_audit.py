#!/usr/bin/env python3
"""Mutation guards for the HGE4 complement-third gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_nonfull_complement_third_gate"


def main() -> None:
    # Full-fiber mutation: the conclusion fails when c=0.
    prime = 17
    p_poly = [(-1) % prime, 0, 0, 0, 1]
    q_poly = [1, 0, 0, 0, 1]
    product = [0] * 9
    for i, first in enumerate(p_poly):
        for j, second in enumerate(q_poly):
            product[i + j] = (product[i + j] + first * second) % prime
    assert product == [(-1) % prime] + [0] * 7 + [1]
    assert 4 > 0 and (q_poly[0] - p_poly[0]) % prime == 2

    # Nondyadic equality mutation: m=3,h=1 leaves c=1.
    roots = {pow(2, exponent, 7) for exponent in range(3)}
    assert roots == {1, 2, 4}
    assert 3 * 1 == 3 and len(roots - {1, 2}) == 1

    # Dyadic arithmetic turns the generic weak inequality into strictness.
    rows = 0
    for exponent in range(3, 42):
        order = 2**exponent
        assert order % 3 != 0
        assert 3 * (order // 3) < order
        assert 3 * (order // 3 + 1) > order
        rows += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["f3_hge4_norm_gate_count"]["status"] == "TARGET"
    statement = (ROOT / "critical/nodes/f3_hge4_norm_gate_count/statement.md").read_text()
    for marker in (
        "f3_hge4_nonfull_complement_third_gate",
        "E_h^prim(m,p)=0",
        "floor((m-1)/3)",
        "No exact-ratio level estimate `(ERT4)`",
    ):
        assert marker in statement
    print(
        "F3_HGE4_NONFULL_COMPLEMENT_THIRD_GATE_AUDIT_PASS "
        f"full_fiber_guard=1 nondyadic_equality_guard=1 dyadic_rows={rows}"
    )


if __name__ == "__main__":
    main()
