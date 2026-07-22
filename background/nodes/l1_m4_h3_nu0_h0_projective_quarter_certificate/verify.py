#!/usr/bin/env python3
"""Verify the h=0 projective quarter certificate and DAG wiring."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_nu0_h0_projective_quarter_certificate"
SUPPLIER = "l1_m4_h3_nu0_h0_projective_branch_exclusion"
CONSUMER = "l1_mixed_petal_amplification"
SCRIPT = ROOT / "experiments" / "prize_resolution" / \
    "l1_m4_h3_nu0_h0_projective_quarter_check.py"


def load_script():
    spec = importlib.util.spec_from_file_location("nu0_h0_projective_quarter", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_script()
    expected = {
        8191: {(6, 20)},
        131071: {(6, 20)},
        524287: {(6, 20)},
        2147483647: {(6, 20), (844833809, 2002167159)},
    }
    assert module.census() == expected
    checks = 64 + 4

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[SUPPLIER]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (SUPPLIER, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    checks += 5

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in ("(PQC2)", "(PQC3)", "(PQC4)", "(PQC5)",
                   "844833809", "does not prove"):
        assert anchor in statement
        checks += 1

    print(f"L1_M4_H3_NU0_H0_PROJECTIVE_QUARTER_CERTIFICATE_PASS checks={checks}")


if __name__ == "__main__":
    main()
