#!/usr/bin/env python3
"""Verify the four F02 square-orbit named-open exclusions."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_f02_square_orbit_exclusions"
PARENT = "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_direct_residual_registry"
CONSUMER = "rate_half_kb_m2_r4_diagonal_c2_112_source_line_literal_assignment_coverage"
CLOSED = {"F02-A-RX", "F02-A-RL", "F02-OB-RX", "F02-OB-RL"}
OPEN = {"F02-A-RM", "F02-OB-RM"}
HASHES = {
    "direct_residual_cell_classify.sage":
        "529bc7fab889eddc860c8f9735480db89dc81f4f623d7e8fa175287172eb72f7",
    "direct_residual_cell_classify_modal.py":
        "c66954657be763f8c92512e6132e7f759ff9337506a437bf636dc87b5c4c8f3d",
    "direct_residual_f02_saturated_classification_output.json":
        "11c843e0eed4aa3b197a52d6136bd7db739ed7820307b9e5ad57004f80c9e77e",
    "direct_residual_cell_audit.sage":
        "7b838f649b87daf8877d9a79f2f9f361f1d9dd24356e485e249cdc62edf4a343",
    "direct_residual_cell_audit_modal.py":
        "1899419007d2c6073d2af1d7fb059b1d3b5159626136a1bde505536b37e9e521",
    "direct_residual_f02_square_audit_output.json":
        "de51965529c80cd71f4a6a32647f506cb8c37dc71e04680906485e16bd19c7ca",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    for filename, expected in HASHES.items():
        require(sha256(NODE / filename) == expected, f"SHA-256 drift: {filename}")

    primary = json.loads(
        (NODE / "direct_residual_f02_saturated_classification_output.json").read_text()
    )["results"]
    require(set(primary) == CLOSED | OPEN, "primary cell census")
    for cell, row in primary.items():
        payload = row["payload"]
        require(row["status"] == "PASS" and row["returncode"] == 0,
                f"primary status: {cell}")
        require(payload["localizer_count"] == 10, f"localizer count: {cell}")
        if cell in CLOSED:
            require(payload["terminal"] == "SATURATED_UNIT_IDEAL",
                    f"primary unit: {cell}")
            require(payload["unit_ideal"] is True, f"primary unit flag: {cell}")
        else:
            require(payload["terminal"] == "SATURATED_NONUNIT_IDEAL",
                    f"mixed scope: {cell}")
            require(payload["unit_ideal"] is False, f"mixed unit flag: {cell}")
            require(len(payload["saturation_progress"]) == 10,
                    f"complete mixed saturation: {cell}")

    audit = json.loads(
        (NODE / "direct_residual_f02_square_audit_output.json").read_text()
    )["results"]
    require(set(audit) == CLOSED, "audit cell census")
    for cell, row in audit.items():
        payload = row["payload"]
        require(row["status"] == "PASS" and row["returncode"] == 0,
                f"audit status: {cell}")
        require(payload["terminal"] == "RABINOWITSCH_UNIT_IDEAL",
                f"audit unit: {cell}")
        require(payload["unit_ideal"] is True and payload["localizer_count"] == 10,
                f"audit contract: {cell}")

    statement = (NODE / "statement.md").read_text(encoding="ascii")
    require("- **status:** PROVED" in statement, "statement status")
    for cell in sorted(CLOSED | OPEN):
        require(cell in statement, f"statement cell: {cell}")
    require("nonunit is not asserted" in statement, "mixed-cell scope fence")

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
        "KB_C2_112_NEAR_POSITIVE_F02_SQUARE_ORBIT_EXCLUSIONS_PASS "
        "closed=4 open_mixed=2 primary=sequential audit=rabinowitsch"
    )


if __name__ == "__main__":
    main()
