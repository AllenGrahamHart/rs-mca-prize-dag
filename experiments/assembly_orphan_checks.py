#!/usr/bin/env python3
"""Logical surface checks for root/packaging and orphan amber nodes."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "experiments" / "amber_stress" / "assembly_orphan_results.json"


def req_successors(dag: dict) -> dict[str, set[str]]:
    succ = {node["id"]: set() for node in dag["nodes"]}
    for edge in dag["edges"]:
        if edge.get("kind") == "req":
            succ[edge["from"]].add(edge["to"])
    return succ


def reaches_by_req(start: str, target: str, succ: dict[str, set[str]]) -> bool:
    seen = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node == target:
            return True
        if node in seen:
            continue
        seen.add(node)
        stack.extend(sorted(succ.get(node, ())))
    return False


def main() -> int:
    dag = json.loads((ROOT / "dag.json").read_text())
    by = {node["id"]: node for node in dag["nodes"]}
    reqs = {node["id"]: set() for node in dag["nodes"]}
    for edge in dag["edges"]:
        if edge.get("kind") == "req":
            reqs[edge["to"]].add(edge["from"])

    checks = []
    expected_req_packages = {
        "prize": {"mca_grand", "list_grand", "packaging"},
        "packaging": {"compiler", "harness", "dossier_partial", "bridge_ledger"},
    }
    for node, expected in expected_req_packages.items():
        actual = reqs[node]
        checks.append(
            {
                "node": node,
                "kind": "req_package_exact",
                "expected": sorted(expected),
                "actual": sorted(actual),
                "ok": actual == expected,
            }
        )

    for node, expected_status in [
        ("compiler", "TARGET"),
        ("harness", "TARGET"),
        ("dossier_partial", "TARGET"),
        ("bridge_ledger", "PROVED"),
    ]:
        actual_status = by[node]["status"]
        checks.append(
            {
                "node": node,
                "kind": "status",
                "expected": expected_status,
                "actual": actual_status,
                "ok": actual_status == expected_status,
            }
        )

    succ = req_successors(dag)
    for node in ["a_regular_collapse", "free_pool_ladder", "m_le3_route"]:
        req_reaches_prize = reaches_by_req(node, "prize", succ)
        checks.append(
            {
                "node": node,
                "kind": "not_on_required_prize_path",
                "req_reaches_prize": req_reaches_prize,
                "evidence_consumers": sorted(
                    edge["to"]
                    for edge in dag["edges"]
                    if edge["from"] == node and edge.get("kind") == "ev"
                ),
                "ok": not req_reaches_prize,
            }
        )

    results = {
        "node": "prize / packaging / orphan amber surface",
        "checks": checks,
        "status": "PASS" if all(check["ok"] for check in checks) else "FAIL",
    }
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0 if results["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
