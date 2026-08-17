#!/usr/bin/env python3
"""Compare the branch-free incidence baseline with exact row ceilings."""

from __future__ import annotations

import argparse
import importlib.util
import json
import tarfile
from math import comb
from pathlib import Path


ARCHIVES = list(Path(".").glob("*.tar.gz"))
ROOT = Path("repo") if ARCHIVES else Path(__file__).resolve().parents[2]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if ARCHIVES:
    with tarfile.open(ARCHIVES[0], "r:gz") as archive:
        archive.extractall(ROOT, filter="data")


K71 = load_module(
    "k71_for_interval_baseline",
    ROOT
    / "background/nodes/rate_half_mca_rank11_k71_carrier_trichotomy_payment/verify.py",
)


def row(kprime: int) -> dict[str, int]:
    q = kprime - 10
    m = 67472 + kprime
    n = 1048576 + kprime
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(q, m)
    premium = sum(
        K71.LEDGER.DEFICITS[support] * baseline[support]
        for support in K71.SUPPORTS
    )
    old = K71.LEDGER.row(kprime)
    marks = int(old["marks"])
    kernel = int(old["kernel"])
    record_floor = K71.LEDGER.RECORD_FLOOR
    ceiling = (
        record_floor * 55 * comb(m, 11)
        - 55 * comb(n, 11)
        - 55 * kernel
        - marks
        - 1
    ) // record_floor
    return {
        "kprime": kprime,
        "baseline_premium": premium,
        "safe_premium_ceiling": ceiling,
        "margin": ceiling - premium,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("kprimes", help="comma-separated K' checkpoints")
    args = parser.parse_args()
    points = [int(item) for item in args.kprimes.split(",")]
    print(json.dumps([row(kprime) for kprime in points], indent=2))


if __name__ == "__main__":
    main()
