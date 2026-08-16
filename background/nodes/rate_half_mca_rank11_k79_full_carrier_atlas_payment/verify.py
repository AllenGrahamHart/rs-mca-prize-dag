#!/usr/bin/env python3
"""Verify the compact K'=79 carrier-atlas contract."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
EXPECTED_SHA256 = "29f26c362ce70c3f2f7bd5a8e911baa2d6f3a72fb30bcd066fbe60a1c16eb4cb"
API_PATH = ROOT / "experiments/prize_resolution/rate_half_mca_rank11_full_carrier_atlas_contract.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


API = load_module("full_carrier_atlas_contract_for_k79", API_PATH)


if __name__ == "__main__":
    API.guarded_main(lambda: API.run_primary(CONTRACT, EXPECTED_SHA256, ROOT))
