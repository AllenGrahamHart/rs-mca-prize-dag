#!/usr/bin/env python3
"""Apply cached upper-oriented raw-clipped pricing at K'=88."""

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
OLD = load_module(
    "k88_clipped_audit_base",
    DIRECTORY / "rate_half_mca_rank11_k87_clipped_domination_audit_cached.py",
)
CORE = load_module(
    "k88_clipped_audit_core",
    DIRECTORY / "rate_half_mca_rank11_k88_clipped_scan_core.py",
)
BASE = OLD.BASE
BASE.KPRIME, BASE.Q, BASE.M, BASE.N_CODE = 88, 78, 67_560, 1_048_664
BASE.LEADER = 41484929797626437211705768761745630928736846700
BASE.OLD_ROW = BASE.K71.LEDGER.row(BASE.KPRIME)
BASE.CEILING = (
    BASE.K71.LEDGER.RECORD_FLOOR * 55 * comb(BASE.M, 11)
    - 55 * comb(BASE.N_CODE, 11)
    - 55 * int(BASE.OLD_ROW["kernel"])
    - int(BASE.OLD_ROW["marks"])
    - 1
) // BASE.K71.LEDGER.RECORD_FLOOR
AUDIT = OLD.OLD.SINGLE.BEST.AUDIT
AUDIT.KPRIME, AUDIT.Q, AUDIT.M = BASE.KPRIME, BASE.Q, BASE.M
AUDIT.adjacent_pair.cache_clear()
OLD.clipped_bound.cache_clear()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("offset", type=int)
    args = parser.parse_args()
    row = CORE.scan(BASE, args.offset)
    row["implementation"] = "audit-cached"
    row["clipped_cache_entries"] = OLD.clipped_bound.cache_info().currsize
    print(json.dumps(row, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
