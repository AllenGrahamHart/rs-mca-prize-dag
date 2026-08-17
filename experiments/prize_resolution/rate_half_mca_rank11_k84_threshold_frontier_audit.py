#!/usr/bin/env python3
"""Independent route-locating K'=84 replay through the pinned audit router."""

from __future__ import annotations

import argparse
import importlib.util
import json
import tarfile
from math import comb
from pathlib import Path


ARCHIVES = list(Path(".").glob("*.tar.gz"))
ROOT = Path("repo") if ARCHIVES else Path(__file__).resolve().parents[2]
if ARCHIVES:
    for archive_path in ARCHIVES:
        with tarfile.open(archive_path, "r:gz") as archive:
            archive.extractall(ROOT, filter="data")


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE = load_module(
    "k84_audit_from_pinned_k83_router",
    ROOT
    / "experiments/prize_resolution/"
    "rate_half_mca_rank11_k83_threshold_frontier_audit.py",
)
KPRIME = 84
BASE.KPRIME = KPRIME
BASE.Q = KPRIME - 10
BASE.M = 67472 + KPRIME
BASE.N_CODE = 1048576 + KPRIME
BASE.OLD_ROW = BASE.K71.LEDGER.row(KPRIME)
BASE.CEILING = (
    BASE.K71.LEDGER.RECORD_FLOOR * 55 * comb(BASE.M, 11)
    - 55 * comb(BASE.N_CODE, 11)
    - 55 * int(BASE.OLD_ROW["kernel"])
    - int(BASE.OLD_ROW["marks"])
    - 1
) // BASE.K71.LEDGER.RECORD_FLOOR
BASE.adjacent_pair.cache_clear()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("lane")
    args = parser.parse_args()
    allowed = {"ordinary"} | {
        f"offset{value}" for value in range(1, BASE.Q)
    }
    assert args.lane in allowed
    print(json.dumps({
        "event": "K84_AUDIT_START",
        "implementation": "audit",
        "kprime": KPRIME,
        "ceiling": BASE.CEILING,
        "lane": args.lane,
    }, sort_keys=True), flush=True)
    row = BASE.lane_audit(args.lane)
    print(json.dumps(row, sort_keys=True), flush=True)
    event = (
        "K84_AUDIT_PASS"
        if row["maximum"] <= BASE.CEILING
        else "K84_AUDIT_FAIL"
    )
    print(json.dumps({
        "event": event,
        "implementation": "audit",
        "lane": args.lane,
        "maximum": row["maximum"],
        "margin": BASE.CEILING - row["maximum"],
        "active_branch": row["active_branch"],
    }, sort_keys=True), flush=True)
    raise SystemExit(0 if event == "K84_AUDIT_PASS" else 1)


if __name__ == "__main__":
    main()
