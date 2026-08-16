#!/usr/bin/env python3
"""Remote full-frontier audit for the compact K'=79 contract."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve()
ROOT = HERE.parents[3] if len(HERE.parents) > 3 else HERE.parent
CONTRACT = HERE.with_name("source_contract.json")
EXPECTED_SHA256 = "29f26c362ce70c3f2f7bd5a8e911baa2d6f3a72fb30bcd066fbe60a1c16eb4cb"
API_NAME = "rate_half_mca_rank11_full_carrier_atlas_contract.py"
AUDIT_NAME = "rate_half_mca_rank11_k74_full_carrier_atlas_audit.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def locate(name: str) -> Path:
    repository_path = ROOT / "experiments/prize_resolution" / name
    return repository_path if repository_path.exists() else HERE.with_name(name)


API = load_module("full_carrier_atlas_contract_audit_for_k79", locate(API_NAME))


def main() -> int:
    raw = CONTRACT.read_bytes()
    API.require(hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256, "contract hash")
    data = json.loads(raw)
    audit_module = load_module("full_carrier_atlas_frontier_for_k79", locate(AUDIT_NAME))
    result = API.compare_full_audit(data, audit_module.audit(79))
    result["contract_sha256"] = EXPECTED_SHA256
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    API.guarded_main(main)
