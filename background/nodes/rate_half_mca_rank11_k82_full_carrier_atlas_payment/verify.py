#!/usr/bin/env python3
"""Verify the compact K'=82 carrier-atlas contract."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
EXPECTED_SHA256 = "bef30d74e322c5ae37ad22c09fe8d7bf657b8a6f037cc1b6d9c2e14f5727c926"
API_PATH = ROOT / "experiments/prize_resolution/rate_half_mca_rank11_full_carrier_atlas_contract.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


API = load_module("full_carrier_atlas_contract_for_k82", API_PATH)


if __name__ == "__main__":
    API.guarded_main(lambda: API.run_primary(CONTRACT, EXPECTED_SHA256, ROOT))
