#!/usr/bin/env python3
"""Route-locating K'=86 replay through the pinned K'=83 primary router."""

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
    "k86_primary_from_pinned_k83_router",
    ROOT
    / "experiments/prize_resolution/"
    "rate_half_mca_rank11_k83_threshold_frontier_replay.py",
)
KPRIME = 86
BASE.KPRIME = KPRIME
BASE.Q = KPRIME - 10
BASE.M = 67472 + KPRIME
BASE.N_CODE = 1048576 + KPRIME
old = BASE.K71.LEDGER.row(KPRIME)
BASE.CEILING = (
    BASE.K71.LEDGER.RECORD_FLOOR * 55 * comb(BASE.M, 11)
    - 55 * comb(BASE.N_CODE, 11)
    - 55 * int(old["kernel"])
    - int(old["marks"])
    - 1
) // BASE.K71.LEDGER.RECORD_FLOOR


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("lane")
    args = parser.parse_args()
    allowed = {"ordinary"} | {
        f"offset{value}" for value in range(1, BASE.Q)
    }
    assert args.lane in allowed
    print(json.dumps({
        "event": "K86_START",
        "implementation": "primary",
        "kprime": KPRIME,
        "ceiling": BASE.CEILING,
        "lane": args.lane,
    }, sort_keys=True), flush=True)
    row = BASE.replay_lane(args.lane)
    print(json.dumps(row, sort_keys=True), flush=True)
    print(json.dumps({
        "event": "K86_LANE",
        "implementation": "primary",
        "lane": args.lane,
        "safe": row["maximum"] <= BASE.CEILING,
        "maximum": row["maximum"],
        "margin": BASE.CEILING - row["maximum"],
        "active_branch": row["active_branch"],
    }, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
