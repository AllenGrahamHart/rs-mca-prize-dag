#!/usr/bin/env python3
"""Verify the compact K'=76 carrier-atlas contract."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
EXPECTED_SHA256 = "73e786205127e30c03437231c90b89c9192bcfa4820204a36ad97e465e5f1b1a"
API_PATH = ROOT / "experiments/prize_resolution/rate_half_mca_rank11_full_carrier_atlas_contract.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


API = load_module("full_carrier_atlas_contract_for_k76", API_PATH)


if __name__ == "__main__":
    API.guarded_main(lambda: API.run_primary(CONTRACT, EXPECTED_SHA256, ROOT))
