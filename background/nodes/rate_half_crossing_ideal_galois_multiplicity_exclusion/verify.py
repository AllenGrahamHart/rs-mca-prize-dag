#!/usr/bin/env python3
"""Replay the independent CS audit and verify the DAG contract."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_crossing_ideal_galois_multiplicity_exclusion"
CONSUMERS = ("rate_half_list_adjacent_crossing", "u2c_giant_tnull_dichotomy")
PILOT = ROOT / "notes/pilots_20260806/cs_transport"
CHECKER = PILOT / "cs_independent_audit.py"
RESULT = PILOT / "cs_independent_audit_rerun_result.json"


def load_checker():
    specification = importlib.util.spec_from_file_location("cs_audit", CHECKER)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for consumer in CONSUMERS:
        assert (NODE, consumer, "ev") in edges
        assert nodes[consumer]["status"] in {"TARGET", "CONDITIONAL"}


def main() -> None:
    persisted = json.loads(RESULT.read_text())
    assert persisted["status"] == "PASS"
    assert persisted["returncode"] == 0
    digest = hashlib.sha256(CHECKER.read_bytes()).hexdigest()
    assert digest == persisted["checker_sha256"]

    fresh = load_checker().run_audit()
    assert fresh == persisted["audit"]
    assert fresh["tamper_selftests"] == {
        "stronger_divisibility_rejected": True,
        "stronger_archimedean_ceiling_rejected": True,
        "floor_free_tower_shortcut_rejected": True,
    }
    boundary = fresh["threshold_and_tower"]
    assert boundary["last_unexcluded_256"] == 170_752_922_587
    assert boundary["first_excluded_256"] == 170_752_922_588
    assert boundary["last_unexcluded_64"] == 2**39
    check_dag()
    print(
        "RATE_HALF_CROSSING_IDEAL_GALOIS_MULTIPLICITY_EXCLUSION_PASS "
        f"norm_checks={fresh['archimedean']['checks']} "
        f"divisibility_checks={fresh['finite_fields']['divisibility_checks']} "
        f"first_excluded={boundary['first_excluded_256']} dag=2/2"
    )


if __name__ == "__main__":
    main()
