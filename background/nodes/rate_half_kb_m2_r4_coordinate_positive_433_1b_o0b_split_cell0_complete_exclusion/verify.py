#!/usr/bin/env python3
"""Verify complete exclusion of O0b split-principal cell 0."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
FILES = {
    "launcher": EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_modal.py",
    "checker": EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_check.py",
    "audit": EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_audit.py",
    "core": EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_split_cell0_outside_core.py",
    "representatives": EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_split_cell0_component_representatives.json",
    "components": EXPERIMENTS / "rate_half_kb_positive_433_1b_cell0_principal_component_compiler_result.json",
    "result": EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_result.json",
}
HASHES = {
    "launcher": "04ae51440703ad0116e33ce6a4c7f3312eff748cd8c3fa1a1d326c4d465f5d48",
    "checker": "74770cfadbfa1275fe58fbee187b40e00cea8e8526ff3dc07347a8011c8046b5",
    "audit": "62ebf4c452cbff2a9f64af0c4643ca37009a9de972a42e368f11e1a05db85553",
    "core": "5cd86020b601b68e9a4295d55d057ec0e029dede334397e6bc51f9d840e5561f",
    "representatives": "658ae5f1f3c0667df2cece818e0c89a752ce9cdf7c4f6f421fc4a721134b8fa4",
    "components": "2fd2d65ebd033d8cd784f428d31d9b49eb66c4b6a059326ed7efcd60d53ed100",
    "result": "6aed35275a09c9ceaa55f2e47ad07409f7d3ed0ffd8f77010ce080ba862b95aa",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_split_cell0_common_component_classification",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_split_cell0_component_v4_quotient",
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    for name, path in FILES.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == HASHES[name],
                f"custody {name}")
    spec = importlib.util.spec_from_file_location("outside_check", FILES["checker"])
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    representatives = checker.preregistration()
    result = json.loads(FILES["result"].read_text())
    require(checker.validate_result(result, representatives) == {
        "scope": "all", "complete": True, "processed": 708,
        "expected": 708, "unit": 708, "nonunit": 0,
    }, "complete outside certificate")

    require(4 * 6 * 105 == 2520 and 39480 - 2520 == 36960,
            "raw closure census")
    require(11076 - 2 * 354 == 10368, "quotient closure census")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED" and
                (parent, NODE.name, "req") in edges, "parent")
    require((NODE.name, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELL0_COMPLETE_VERIFY_PASS "
          "closed=2520/708 owner=36960/10368 outside=708/708")


if __name__ == "__main__":
    main()
