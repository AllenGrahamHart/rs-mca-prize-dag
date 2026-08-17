#!/usr/bin/env python3
"""Compute the exact K'=86 rank-nine component payment."""

from __future__ import annotations

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


KPRIME = 86
Q = KPRIME - 10
M = 67472 + KPRIME
N_CODE = 1048576 + KPRIME
PREMIUM = 41436891148468120556440841127823744176664445997
K71 = load_module(
    "k86_component_payment_ledger",
    ROOT
    / "background/nodes/"
    "rate_half_mca_rank11_k71_carrier_trichotomy_payment/verify.py",
)


def main() -> None:
    old = K71.LEDGER.row(KPRIME)
    floor = K71.LEDGER.RECORD_FLOOR
    marks, kernel = int(old["marks"]), int(old["kernel"])
    numerator = (
        floor * 55 * comb(M, 11)
        - 55 * comb(N_CODE, 11)
        - 55 * kernel
        - marks
        - 1
    )
    ceiling, ceiling_remainder = divmod(numerator, floor)
    full = (marks + floor * PREMIUM) // 55
    total = full + kernel
    required = floor * comb(M, 11) - comb(N_CODE, 11)
    gap = required - total
    assert ceiling - PREMIUM == 2429142732593969226237923721701123878841
    assert gap > 0
    print(json.dumps({
        "event": "K86_COMPONENT_PAYMENT",
        "kprime": KPRIME,
        "q": Q,
        "m": M,
        "n": N_CODE,
        "rank_nine_marks": marks,
        "kernel_capacity": kernel,
        "record_floor": floor,
        "premium": PREMIUM,
        "safe_premium_ceiling": ceiling,
        "premium_ceiling_margin": ceiling - PREMIUM,
        "ceiling_remainder": ceiling_remainder,
        "full_rank_capacity": full,
        "total_capacity": total,
        "required_component_incidence": required,
        "gap": gap,
        "status": "PASS",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
