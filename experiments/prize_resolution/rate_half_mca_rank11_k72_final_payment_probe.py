#!/usr/bin/env python3
"""Compute the exact K'=72 payment from the certified atlas premium."""

from __future__ import annotations

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


PROBE = load_module(
    "k72_two_step_for_final_payment",
    Path("rate_half_mca_rank11_k72_two_step_probe.py"),
)
K71 = PROBE.K71
KPRIME = 72
PREMIUM = 41089877204729279662874647920595743958596178333
old = K71.LEDGER.row(KPRIME)
n = 1048576 + KPRIME
m = 67472 + KPRIME
marks = int(old["marks"])
kernel = int(old["kernel"])
record_floor = K71.LEDGER.RECORD_FLOOR
full_rank = (marks + record_floor * PREMIUM) // 55
total = kernel + full_rank
demand = record_floor * comb(m, 11) - comb(n, 11)
ceiling = (
    record_floor * 55 * comb(m, 11)
    - 55 * comb(n, 11)
    - 55 * kernel
    - marks
    - 1
) // record_floor
coefficient = 55 * comb(m, 11) - PREMIUM
raw = (
    record_floor * coefficient
    - 55 * comb(n, 11)
    - 55 * kernel
    - marks
)

print(json.dumps({
    "kprime": KPRIME,
    "n": n,
    "m": m,
    "rank_nine_marks": marks,
    "kernel_capacity": kernel,
    "record_floor": record_floor,
    "completion_premium": PREMIUM,
    "safe_premium_ceiling": ceiling,
    "premium_ceiling_margin": ceiling - PREMIUM,
    "full_rank_capacity": full_rank,
    "total_capacity": total,
    "required_component_incidence": demand,
    "gap": demand - total,
    "record_coefficient_cross": coefficient,
    "floor_record_raw_cross": raw,
}, indent=2))
