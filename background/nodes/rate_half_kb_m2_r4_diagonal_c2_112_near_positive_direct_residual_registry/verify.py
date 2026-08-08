#!/usr/bin/env python3
"""Verify the exact 30-cell direct residual registry."""

from __future__ import annotations

import hashlib
import json
from itertools import product
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_direct_residual_registry"
PARENT = "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_literal_inversion_transport"
CONSUMER = "rate_half_kb_m2_r4_diagonal_c2_112_source_line_literal_assignment_coverage"
HASHES = {
    "direct_residual_registry_compile.sage":
        "093524b689c11de6b44dedc3d06b950947711914a585371041b5552570a2cb28",
    "direct_residual_registry_compile_modal.py":
        "fe4ad9c6fb2c089a11479a63111ca0cdb94ee0a6b1f767008917f8bc115143e4",
    "direct_residual_registry_output.json":
        "a1ba64f5ed1afef30012bfd5587cc0dcc9ad69373d00aa56f484615b870e623a",
}
REGISTRY_SHA256 = "2607f88572c63091b06a1c35dd55c80a3e4f10daff2fb3423f5bb8c03f0f116e"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    for filename, expected in HASHES.items():
        require(sha256(NODE / filename) == expected, f"SHA-256 drift: {filename}")

    result = json.loads((NODE / "direct_residual_registry_output.json").read_text())["result"]
    payload = result["payload"]
    require(result["status"] == "PASS" and result["returncode"] == 0,
            "Modal status")
    require(payload["terminal"] == "DIRECT_RESIDUAL_REGISTRY_COMPILED",
            "terminal")
    require(payload["registry_sha256"] == REGISTRY_SHA256, "registry digest")
    require(payload["cell_count"] == 30 and payload["equation_count"] == 120,
            "registry census")
    require(payload["max_terms"] == 1098 and payload["max_total_degree"] == 30,
            "complexity maxima")

    expected_cells = {
        f"{assignment}-{root}-{allocation}"
        for assignment, root, allocation in product(
            ("F02", "F04", "F06", "M01", "M03"),
            ("A", "OB"),
            ("RX", "RL", "RM"),
        )
    }
    cells = payload["cells"]
    require({cell["cell"] for cell in cells} == expected_cells, "cell keys")
    require(all(len(cell["equations"]) == 4 for cell in cells), "equation arity")
    require(all(
        cell["common_gcd"]["total_degree"] == 0
        and cell["common_gcd"]["terms"] == 1
        for cell in cells
    ), "common gcd")
    localizer_counts = {
        assignment: {
            len(cell["radical_localizer_factors"])
            for cell in cells if cell["assignment"] == assignment
        }
        for assignment in ("F02", "F04", "F06", "M01", "M03")
    }
    require(localizer_counts == {
        "F02": {10}, "F04": {12}, "F06": {12}, "M01": {11}, "M03": {11}
    }, "localizer counts")

    statement = (NODE / "statement.md").read_text(encoding="ascii")
    require("- **status:** PROVED" in statement, "statement status")
    require("only an exact compiler" in statement, "scope fence")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require((PARENT, NODE_ID, "req") in edges, "DAG dependency")
    require((NODE_ID, CONSUMER, "ev") in edges, "DAG consumer")

    print(
        "KB_C2_112_NEAR_POSITIVE_DIRECT_RESIDUAL_REGISTRY_PASS "
        "cells=30 equations=120 max_degree=30 max_terms=1098"
    )


if __name__ == "__main__":
    main()
