#!/usr/bin/env python3
"""Independently price the K'=86 best-single residual traversal."""

from __future__ import annotations

import argparse
import importlib.util
import json
from math import comb
from pathlib import Path


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


DIRECTORY = Path(__file__).resolve().parent
BEST = load_module(
    "k86_best_single_audit_formulas",
    DIRECTORY / "rate_half_mca_rank11_k85_best_single_domination_audit.py",
)
CORE = load_module(
    "k86_best_single_audit_core",
    DIRECTORY / "rate_half_mca_rank11_k86_best_single_scan_core.py",
)
BASE = BEST.BASE
BASE.KPRIME, BASE.Q, BASE.M, BASE.N_CODE = 86, 76, 67558, 1048662
BASE.LEADER = 41436891148468120556440841127823744176664445997
BASE.OLD_ROW = BASE.K71.LEDGER.row(BASE.KPRIME)
BASE.CEILING = (
    BASE.K71.LEDGER.RECORD_FLOOR * 55 * comb(BASE.M, 11)
    - 55 * comb(BASE.N_CODE, 11)
    - 55 * int(BASE.OLD_ROW["kernel"])
    - int(BASE.OLD_ROW["marks"])
    - 1
) // BASE.K71.LEDGER.RECORD_FLOOR
BEST.AUDIT.KPRIME, BEST.AUDIT.Q, BEST.AUDIT.M = (
    BASE.KPRIME,
    BASE.Q,
    BASE.M,
)
BEST.AUDIT.adjacent_pair.cache_clear()
BASE.geometry_profiles = BEST.geometry_profiles
BASE.edge4_price = BEST.best_single_price


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("offset", type=int)
    args = parser.parse_args()
    row = CORE.scan(BASE, args.offset)
    row["implementation"] = "audit"
    print(json.dumps(row, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
