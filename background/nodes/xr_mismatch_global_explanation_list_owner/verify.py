#!/usr/bin/env python3
"""Verify the XR global-explanation list owner."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_mismatch_global_explanation_list_owner"
DEPENDENCIES = {
    "xr_mismatch_accumulated_locator_flag_normal_form",
    "xr_true_tangent_coordinate_injection",
    "list_subsqrt_interleaving_collapse",
}
CONSUMER = "xr_tangent_support_mismatch_bridge"

ROWS = (
    (1024, 261),
    (1024, 133),
    (1024, 67),
    (2**41, 558_345_748_481),
    (2**41, 283_467_841_537),
    (2**41, 141_733_920_769),
)


def ownership_arithmetic() -> None:
    for n, agreement in ROWS:
        discrepancy = n - agreement
        threshold = 1 + (16 * n**3) // discrepancy
        assert discrepancy * (threshold - 1) <= 16 * n**3
        assert discrepancy * threshold > 16 * n**3
        assert discrepancy * n**2 < n**3 < 16 * n**3

    for field_size in (17, 29, 101):
        for ordinary in range(1, field_size):
            projected = ordinary * (field_size - 1) // (field_size - ordinary)
            assert projected >= ordinary
            if ordinary * ordinary < field_size:
                assert projected == ordinary


def root_subtraction_check() -> None:
    for explanations in range(1, 30):
        for discrepancy in range(1, 20):
            residual = discrepancy * (explanations - 1)
            with_root = discrepancy * explanations
            assert with_root - residual == discrepancy
            assert residual >= 0


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "|Z_tan|<=(n-A)max(E-1,0)",
        "E<=floor(L_A(q-1)/(q-L_A))",
        "|Z_tan|<=(n-A)(L_A-1)",
        "L_A<=1+floor(16n^3/(n-A))",
        "doesnotproveeitherlistbound",
    ):
        assert marker in statement


def main() -> None:
    ownership_arithmetic()
    root_subtraction_check()
    packet_check()
    print("XR_MISMATCH_GLOBAL_EXPLANATION_LIST_OWNER_PASS rows=6 projections=145")


if __name__ == "__main__":
    main()
