#!/usr/bin/env python3
"""Remote full-frontier audit for the K'=74 compact contract."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve()
ROOT = HERE.parents[3] if len(HERE.parents) > 3 else HERE.parent
CONTRACT = HERE.with_name("source_contract.json")
EXPECTED_SHA256 = "8162044ad85a08b7dbed81a06f707e799c4be5ae837fd855be8aaa3c2d285b4d"
AUDIT_NAME = "rate_half_mca_rank11_k74_full_carrier_atlas_audit.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


raw = CONTRACT.read_bytes()
assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
data = json.loads(raw)
repository_audit = ROOT / "experiments/prize_resolution" / AUDIT_NAME
audit_module = load_module(
    "k74_full_carrier_atlas_frontier_audit",
    repository_audit if repository_audit.exists() else HERE.with_name(AUDIT_NAME),
)
actual = audit_module.audit()
plain = actual["plain_frontier"]
expected_plain = data["plain_frontier"]
assert plain["evaluations"] == expected_plain["evaluations"]
assert (
    plain["unsafe_distinct_defect_tuples"]
    == expected_plain["unsafe_distinct_defect_tuples"]
)
assert plain["unsafe_tuple_sha256"] == expected_plain["unsafe_tuple_sha256"]
assert plain["safe_maximum"] == expected_plain["safe_maximum"]
assert plain["safe_maximum_label"] == expected_plain["safe_maximum_label"]

reroute = actual["reroute"]
expected_reroute = data["reroute"]
for key in ("cells", "evaluations", "all_safe", "maximum", "minimum_margin"):
    assert reroute[key] == expected_reroute[key]
assert reroute["active_defects"] in (
    (35, 34, 34, 33),
    (35, 34, 34, 34),
)

for key, value in actual["row"].items():
    assert value == data["row"][key]

print(json.dumps({
    "contract_sha256": EXPECTED_SHA256,
    "unsafe_tuple_sha256": plain["unsafe_tuple_sha256"],
    "rerouted_cells": reroute["cells"],
    "reroute_evaluations": reroute["evaluations"],
    "payment_gap": actual["row"]["gap"],
}, sort_keys=True))
