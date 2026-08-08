#!/usr/bin/env python3
"""Verify the exact near-positive literal inversion transport certificate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_literal_inversion_transport"
CONSUMER = "rate_half_kb_m2_r4_diagonal_c2_112_source_line_literal_assignment_coverage"
PARENTS = {
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction",
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate",
}
FILES = {
    "near_literal_assignment_transport_probe_modal.py":
        "f9d502b5c6e48b3ce2989c1b0846bf82e73a7c188f083a9b97bbc7e6b9843086",
    "near_literal_assignment_transport_audit.sage":
        "2ebf44346600507f6d0db3f9f502fdd0c4e45e5350ff34a03b80d9a212f1754f",
    "near_literal_assignment_transport_probe_output.json":
        "bc82dbe4721afd5d7d626268e97b8060ea2f9b3398c972d44fcd44a483828292",
}
UPSTREAM_COMMIT = "9e1d96cbf997c30efa448bbce9a7f48c2bea9643"
UPSTREAM_SOURCE_SHA256 = "c382adee5be3b72dcb675b4932a681f65ae958f58e24c3f5fdb8163d4d1508b7"
B_MAP = {
    "F00": "F01", "F01": "F00", "F02": "F03", "F03": "F02",
    "F04": "F05", "F05": "F04", "F06": "F07", "F07": "F06",
    "M00": "M00", "M01": "M02", "M02": "M01", "M03": "M03",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def semantic_orbits():
    allocations = ("RX", "RL", "RM")
    cells = {
        (assignment, target, allocation)
        for assignment in B_MAP
        for target in ("A", "TA", "O")
        for allocation in allocations
    }
    unseen = set(cells)
    orbits = []
    while unseen:
        seed = unseen.pop()
        orbit = {seed}
        queue = [seed]
        while queue:
            assignment, target, allocation = queue.pop()
            images = (
                (B_MAP[assignment], target, allocation),
                (
                    B_MAP[assignment],
                    {"A": "TA", "TA": "A", "O": "O"}[target],
                    allocation,
                ),
            )
            for image in images:
                if image not in orbit:
                    orbit.add(image)
                    unseen.discard(image)
                    queue.append(image)
        orbits.append(frozenset(orbit))
    return cells, orbits


def main() -> None:
    for filename, expected in FILES.items():
        require(sha256(NODE / filename) == expected, f"SHA-256 drift: {filename}")

    row = json.loads((NODE / "near_literal_assignment_transport_probe_output.json").read_text())
    require(row["upstream_commit"] == UPSTREAM_COMMIT, "upstream commit")
    require(row["source_sha256"] == UPSTREAM_SOURCE_SHA256, "upstream source hash")

    primary = row["result"]
    payload = primary["payload"]
    require(primary["status"] == "PASS" and primary["returncode"] == 0,
            "primary status")
    require(payload["terminal"] == "B_TRANSPORT_PASS_TW_AUDITED",
            "primary terminal")
    require(payload["checks"] == 288, "primary check count")
    require(payload["failed"] == payload["b_failed"] == [], "primary failures")
    require(payload["tw_failed_count"] == 0, "TW failures")
    require(payload["b_assignment_map"] == B_MAP, "B assignment map")
    require(payload["tw_residual_assignment_map"] == B_MAP, "TW assignment map")
    require(all(
        matches == [{"assignment": B_MAP[source], "variant": "same-root-order"}]
        for source, matches in payload["tw_all_assignment_search"].items()
    ), "exhaustive TW destination search")
    require(payload["raw_cells"] == 144, "oriented cell count")
    require(payload["semantic_cells_after_other_orientation_quotient"] == 108,
            "semantic cell count")
    require(payload["affine_semantic_orbits_under_transports"] == 42,
            "primary orbit count")
    require(payload["canonical_orbits_already_covered"] == 12,
            "primary represented count")
    require(payload["residual_affine_orbits"] == 30, "primary residual count")

    audit = row["independent_audit"]
    audit_payload = audit["payload"]
    require(audit["status"] == "PASS" and audit["returncode"] == 0,
            "independent status")
    require(audit_payload["terminal"] == "INDEPENDENT_TRANSPORT_AUDIT_PASS",
            "independent terminal")
    require(audit_payload["solver"] == "generic_5x5_solve_right",
            "independent solver")
    require(audit_payload["imports_pr1140_compiler"] is False,
            "independent import fence")
    require(audit_payload["checks"] == 288, "independent check count")
    require((audit_payload["affine_semantic_orbits"],
             audit_payload["canonical_orbits_covered"],
             audit_payload["residual_affine_orbits"]) == (42, 12, 30),
            "independent census")

    cells, orbits = semantic_orbits()
    represented = [
        orbit for orbit in orbits
        if any(cell[0] in {"F00", "M00"} for cell in orbit)
    ]
    require(len(cells) == 108 and len(orbits) == 42, "recomputed orbit census")
    require(len(represented) == 12 and len(orbits) - len(represented) == 30,
            "recomputed frontier census")

    statement = (NODE / "statement.md").read_text(encoding="ascii")
    require("- **status:** PROVED" in statement, "statement status")
    for fence in ("full colored quotient", "w=0", "near-negative", "30 residual"):
        require(fence in statement, f"scope fence: {fence}")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require(all((parent, NODE_ID, "req") in edges for parent in PARENTS),
            "DAG dependencies")
    require((NODE_ID, CONSUMER, "ev") in edges, "DAG consumer")

    print(
        "KB_C2_112_NEAR_POSITIVE_LITERAL_INVERSION_TRANSPORT_PASS "
        "checks=288 semantic_cells=108 orbits=42 represented=12 residual=30"
    )


if __name__ == "__main__":
    main()
