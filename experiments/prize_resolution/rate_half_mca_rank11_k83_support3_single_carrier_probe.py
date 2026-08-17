#!/usr/bin/env python3
"""Price the exact K'=83 M2=0 support-three carrier wall cell."""

from __future__ import annotations

import importlib.util
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ROUTER = load_module(
    "k83_single_carrier_router",
    ROOT
    / "experiments/prize_resolution/rate_half_mca_rank11_k83_stratified56_lane_probe.py",
)
PROBE, K71 = ROUTER.PROBE, ROUTER.K71
KPRIME, Q, M, N_CODE = 83, 73, 67555, 1048659


def main() -> None:
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(Q, M)
    left = K71.base23_vector(KPRIME, baseline, 73, 37)
    exact45, _, _ = K71.exact45_rows(KPRIME, baseline)
    middle = next(
        vector for s4, s5, vector in exact45 if (s4, s5) == (37, 37)
    )
    _, high = K71.PARENT.high_group(KPRIME, baseline)
    high_vector = next(
        vector
        for name, vector in high
        if name == "c6d3/c7d2/c8d1/c9d0"
    )
    raw_caps = K71.combine(left, middle, high_vector)
    union, dimension = 38, 8
    charged_caps = K71.combine(
        raw_caps, PROBE.fixed_union_cap(KPRIME, union, dimension)
    )
    joint45 = PROBE.joint45_weighted_cap(KPRIME, union, dimension)
    joint56 = ROUTER.stratified56_weighted_cap(
        KPRIME, union, dimension
    )
    charged = ROUTER.priced(
        KPRIME, charged_caps, joint45, (joint56,)
    )
    old = K71.LEDGER.row(KPRIME)
    ceiling = (
        K71.LEDGER.RECORD_FLOOR * 55 * comb(M, 11)
        - 55 * comb(N_CODE, 11)
        - 55 * int(old["kernel"])
        - int(old["marks"])
        - 1
    ) // K71.LEDGER.RECORD_FLOOR
    print(json.dumps({
        "kprime": KPRIME,
        "defects": [73, 37, 37, 37],
        "completion_maxima": [0, 36, 36, 36],
        "high_branch": "c6d3/c7d2/c8d1/c9d0",
        "charge": [union, dimension],
        "raw_premium": K71.premium(raw_caps),
        "charged_premium": charged,
        "safe_premium_ceiling": ceiling,
        "margin": ceiling - charged,
        "joint45": joint45,
        "joint56": joint56,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
