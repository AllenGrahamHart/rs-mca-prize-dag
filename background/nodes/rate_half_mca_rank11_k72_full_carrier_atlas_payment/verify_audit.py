#!/usr/bin/env python3
"""Independent 36-cell reroute and final-payment audit for K'=72."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
EXPECTED_SHA256 = "3f3d1903b9ba5063f370ce8acad984d0d740a722b3c17ead912c6faa7c98a258"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


raw = CONTRACT.read_bytes()
assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
data = json.loads(raw)
probe = load_module(
    "k72_probe_for_independent_audit",
    ROOT / "experiments/prize_resolution/rate_half_mca_rank11_k72_two_step_probe.py",
)
K71 = probe.K71
kprime = 72
q = 62
m = 67544
baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(q, m)
exact45, _, _ = K71.exact45_rows(kprime, baseline)
_, high = K71.PARENT.high_group(kprime, baseline)

cell_maxima = []
evaluations = 0
for defects in data["unsafe_defect_tuples"]:
    s2, s3, s4, s5 = defects
    m2, m3, m4, m5 = (q - value for value in defects)
    left = K71.base23_vector(kprime, baseline, s2, s3)
    middle = next(vector for a, b, vector in exact45 if (a, b) == (s4, s5))
    local = K71.combine(left, middle)
    cases = probe.mixed_cases(m2, m3 - m2, m4, m5)
    charged = probe.charged_case_rows(kprime, local, cases)
    maximum = -1
    for (candidate, joint), _ in charged.items():
        for _, high_vector in high:
            caps = K71.combine(candidate, high_vector)
            value = K71.premium(caps)
            if joint is not None:
                old45 = sum(K71.LEDGER.DEFICITS[d] * caps[d - 2] for d in (4, 5))
                value -= old45 - min(old45, joint)
            maximum = max(maximum, value)
            evaluations += 1
    cell_maxima.append(maximum)

reroute = data["reroute"]
assert evaluations == reroute["evaluations"]
assert max(cell_maxima) == reroute["maximum"]
assert all(value < data["row"]["safe_premium_ceiling"] for value in cell_maxima)

row = data["row"]
full = (row["rank_nine_marks"] + row["record_floor"] * row["completion_premium"]) // 55
demand = row["record_floor"] * comb(67544, 11) - comb(1048648, 11)
assert full == row["full_rank_capacity"]
assert demand - (row["kernel_capacity"] + full) == row["gap"] > 0

print(json.dumps({
    "contract_sha256": EXPECTED_SHA256,
    "rerouted_cells": len(cell_maxima),
    "reroute_evaluations": evaluations,
    "payment_gap": row["gap"],
}, sort_keys=True))
