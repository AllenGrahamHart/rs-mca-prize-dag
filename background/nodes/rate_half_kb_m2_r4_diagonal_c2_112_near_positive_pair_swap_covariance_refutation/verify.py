#!/usr/bin/env python3
"""Verify the reciprocal-pair-swap covariance route cut."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_pair_swap_covariance_refutation"
CONSUMER = "rate_half_kb_m2_r4_diagonal_c2_112_source_line_literal_assignment_coverage"
PARENTS = {
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction",
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate",
}
ASSIGNMENTS = {
    "F00", "F01", "F02", "F03", "F04", "F05",
    "F06", "F07", "M00", "M01", "M02", "M03",
}
HASHES = {
    "pair_swap_transport_probe.sage":
        "4426a63a1d416de82d5ab0e60e665595f2af7624c45a00ac45e01d55a8656d32",
    "pair_swap_transport_probe_modal.py":
        "45b137a9d98a86588e13f70f9b31e87def7005d428908ae844023dbe40f62373",
    "pair_swap_transport_core_shards_output.json":
        "385f06b7161391c6393c4a8ad8474e3e33b36301dcf137d4f34a914f446aad82",
    "pair_swap_transport_destination_search_output.json":
        "8445490be6926ad552a113f831f6ca93ab91e34099456ccbf9681033f3f19728",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def phi(value: Fraction, b: Fraction) -> Fraction:
    u = (2 * b - 1) / (b - 2)
    return (u * value + 1) / (value + u)


def main() -> None:
    for filename, expected in HASHES.items():
        require(sha256(NODE / filename) == expected, f"SHA-256 drift: {filename}")

    b = Fraction(3)
    b_prime = phi(Fraction(2), b)
    require(b_prime == Fraction(5 * b - 4, 4 * b - 5), "b-prime formula")
    require(phi(b, b) == 2 and phi(1 / b, b) == Fraction(1, 2),
            "moving-pair image")
    require(phi(Fraction(1, 2), b) == 1 / b_prime, "fixed-pair image")

    shards = json.loads((NODE / "pair_swap_transport_core_shards_output.json").read_text())
    require(shards["localizers"] is False, "core-only scope")
    require(set(shards["results"]) == ASSIGNMENTS, "assignment census")
    for assignment, row in shards["results"].items():
        payload = row["payload"]
        require(row["status"] == "PASS" and row["returncode"] == 0,
                f"shard status: {assignment}")
        require(payload["assignment_filter"] == assignment, "shard identity")
        require(payload["checks"] == 12, f"cell count: {assignment}")
        require(payload["target_failures"] == [], f"target map: {assignment}")
        require(payload["terminal"] == "PAIR_SWAP_CLASSIFIED", "shard terminal")
        failures = payload["residual_failures"]
        require(len(failures) == 2, f"residual failures: {assignment}")
        require({item["endpoint"] for item in failures} == {0, 1},
                f"endpoint census: {assignment}")

    search = json.loads(
        (NODE / "pair_swap_transport_destination_search_output.json").read_text()
    )["result"]
    payload = search["payload"]
    require(search["status"] == "PASS" and search["returncode"] == 0,
            "search status")
    require(payload["terminal"] == "PAIR_SWAP_DESTINATION_SEARCH_COMPLETE",
            "search terminal")
    require(set(payload["matches"]) == ASSIGNMENTS, "search source census")
    require(all(matches == [] for matches in payload["matches"].values()),
            "unexpected destination match")
    require(payload["samples"] == [["3", "5", "7"], ["5/2", "3", "7"],
                                    ["-2", "3", "5"]],
            "specialization set")

    statement = (NODE / "statement.md").read_text(encoding="ascii")
    require("- **status:** PROVED" in statement, "statement status")
    for fence in ("does not prove", "different, explicitly proved nonlinear transport",
                  "full quotient"):
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
        "KB_C2_112_NEAR_POSITIVE_PAIR_SWAP_COVARIANCE_REFUTATION_PASS "
        "assignments=12 residual_failures=24 target_failures=0 destinations=0"
    )


if __name__ == "__main__":
    main()
