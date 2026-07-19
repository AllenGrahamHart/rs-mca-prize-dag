#!/usr/bin/env python3
"""Pin and replay the low-budget list certificate generator."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_low_budget_certificate_generator"
REQUIREMENTS = (
    "compiler",
    "rate_half_list_low_budget_exact_crossing",
    "rate_half_list_low_budget_all_arity_crossing",
)
EVIDENCE = ("descriptor",)
PINNED_HASHES = {
    "tools/prize_row_descriptor.py": "ee125103c9d31fc4ceed7b16e129b025aef9facd9437b61fc614a716f7ce7ce9",
    "tools/prize_certificate_compiler.py": "3339135a64ddad001d1fc54a6abce5e168c9a8c5895d5d5bef201c9b480fb51d",
    "tools/rate_half_list_low_budget_certificate.py": "759c3e588c483e0fa8bd93fc4aeaf8485c36267230e5df997d5891c112c24c50",
    "background/nodes/rate_half_list_low_budget_certificate_generator/verify_audit.py": "98e736ce8f14849ffd7d62c5b2b35e7c0710f178185fb00056f6674df7824b67",
}


def check_pins() -> None:
    for rel, expected in PINNED_HASHES.items():
        actual = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        if actual != expected:
            raise AssertionError((rel, actual, expected))


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for requirement in REQUIREMENTS:
        assert nodes[requirement]["status"] == "PROVED"
        assert (requirement, NODE, "req") in edges
    assert nodes["descriptor"]["status"] == "TARGET"
    assert ("descriptor", NODE, "ev") in edges
    assert (NODE, "list_grand", "ev") in edges


check_pins()
sys.path.insert(0, str(ROOT / "background" / "nodes" / NODE))

from verify_audit import main as audit_main  # noqa: E402


def main() -> None:
    check_pins()
    check_dag()
    audit_main()
    print(
        "RATE_HALF_LIST_LOW_BUDGET_CERTIFICATE_GENERATOR_PASS "
        f"dependencies={len(PINNED_HASHES)} "
        f"dag={len(REQUIREMENTS) + len(EVIDENCE) + 1}/"
        f"{len(REQUIREMENTS) + len(EVIDENCE) + 1}"
    )


if __name__ == "__main__":
    main()
