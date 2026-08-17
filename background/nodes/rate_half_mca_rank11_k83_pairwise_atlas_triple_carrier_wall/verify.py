#!/usr/bin/env python3
"""Verify the exact K'=83 pairwise-atlas route cut."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
EXPECTED_CONTRACT_SHA256 = "06a01a521241157263a72b3d90539bfbbc74c9a367603136efb173165c363187"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(data: dict, actual: dict) -> None:
    require(
        data["scope"] == "single exact cell; not a complete K'=83 frontier maximum",
        "scope",
    )
    for relative, digest in data["replay_sources"].items():
        require(
            hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == digest,
            f"source hash: {relative}",
        )
    cell = data["active_cell"]
    require(actual["kprime"] == data["parameters"]["kprime"] == 83, "row")
    require(list(actual["defects"]) == cell["defects"], "defects")
    require(actual["completion_maxima"] == cell["completion_maxima"], "maxima")
    require(
        [list(charge) for charge in actual["pairwise_charges"]]
        == cell["pairwise_charges"],
        "charges",
    )
    require(actual["pairwise_maximum"] == cell["pairwise_maximum"], "premium")
    require(actual["pairwise_margin"] == cell["pairwise_margin"] < 0, "margin")
    require(len(actual["rows"]) == len(data["forced_intersection_rows"]) == 4, "rows")
    for got, expected in zip(actual["rows"], data["forced_intersection_rows"]):
        for key, value in expected.items():
            require(got[key] == value, f"intersection {key}")
        require(got["safe_premium_ceiling"] == cell["safe_premium_ceiling"], "ceiling")


def main() -> int:
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == EXPECTED_CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    source = load_module(
        "k83_triple_carrier_wall_source",
        ROOT / "experiments/prize_resolution/rate_half_mca_rank11_k83_triple_carrier_intersection_probe.py",
    )
    actual = source.audit()
    validate(data, actual)
    baseline = load_module(
        "k83_branch_free_baseline_source",
        ROOT / "experiments/prize_resolution/rate_half_mca_rank11_carrier_interval_baseline_probe.py",
    )
    for expected in data["branch_free_baseline"]:
        require(baseline.row(expected["kprime"]) == expected, "baseline row")
    trial = copy.deepcopy(data)
    trial["active_cell"]["pairwise_margin"] = 1
    rejected = False
    try:
        validate(trial, actual)
    except Reject:
        rejected = True
    require(rejected, "tamper rejection")
    print(json.dumps({
        "contract_sha256": EXPECTED_CONTRACT_SHA256,
        "kprime": 83,
        "pairwise_deficit": -actual["pairwise_margin"],
        "intersection_rows": len(actual["rows"]),
        "tamper_rejected": 1,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
