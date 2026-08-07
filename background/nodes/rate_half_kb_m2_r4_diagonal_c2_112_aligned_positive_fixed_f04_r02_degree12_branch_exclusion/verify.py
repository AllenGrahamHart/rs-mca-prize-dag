#!/usr/bin/env python3
"""Verify the logical composition of the F04-R02 degree-12 branch close."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
NODES = HERE.parent
REQUIRED = (
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_degree12_s_zero_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_degree12_degree6_leading_curve_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_degree12_b0_k8_nonzero_f_p6_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_degree12_k8_branch_cover",
)


def main() -> None:
    for node_id in REQUIRED:
        payload = json.loads((NODES / node_id / "node.json").read_text())
        assert payload["node"]["id"] == node_id
        assert payload["node"]["status"] == "PROVED"
    statement = (HERE / "statement.md").read_text()
    for label in ("s=0", "L6=0", "K8!=0", "K8=0, K10!=0", "K8=K10=0"):
        assert label in statement
    node = json.loads((HERE / "node.json").read_text())
    assert {edge["from"] for edge in node["requires"]} == set(REQUIRED)
    print("KB_C2_112_F04_R02_DEGREE12_BRANCH_EXCLUSION_PASS leaves=5 requirements=4")


if __name__ == "__main__":
    main()
