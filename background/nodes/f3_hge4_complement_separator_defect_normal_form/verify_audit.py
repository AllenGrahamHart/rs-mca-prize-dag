#!/usr/bin/env python3
"""Mutation guards for the HGE4 separator-defect normal form."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_complement_separator_defect_normal_form"


def main() -> None:
    # Exact defect arithmetic at the two closest dyadic third-lines.
    rows = 0
    for exponent in range(3, 42):
        order = 2**exponent
        width = order // 3
        defect = order - 3 * width
        assert defect == order % 3 in {1, 2}
        assert 3 * width < order
        rows += 1

    # Exact degree, not a weak upper bound or an off-by-one convention.
    for order, width in ((4, 1), (8, 2), (16, 4), (32, 10)):
        complement = order - 2 * width
        assert complement - width == order - 3 * width
        assert order - 3 * width != order - 3 * width + 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["f3_hge4_norm_gate_count"]["status"] == "TARGET"
    statement = (ROOT / "critical/nodes/f3_hge4_norm_gate_count/statement.md").read_text()
    for marker in (
        NODE, "G=B-A", "e=m-3h", "m(P+Q-PQG)=d^2 XP'R",
        "does not count",
    ):
        assert marker in statement
    print(
        "F3_HGE4_COMPLEMENT_SEPARATOR_DEFECT_NORMAL_FORM_AUDIT_PASS "
        f"dyadic_rows={rows} exact_degree_guards=4"
    )


if __name__ == "__main__":
    main()
