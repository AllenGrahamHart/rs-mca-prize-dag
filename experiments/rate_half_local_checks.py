#!/usr/bin/env python3
"""Local 60s-safe equivalent of the rate-half Modal arithmetic checks."""

from __future__ import annotations

import json
import time
from math import lgamma, log
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "experiments" / "amber_stress" / "rate_half_results.json"
LOG2 = log(2.0)
N = 2**41
K = 2**40
SIGMA_STAR = 8_592_912_738


def log2c(n: int, m: int) -> float:
    if m < 0 or m > n:
        return float("-inf")
    return (lgamma(n + 1) - lgamma(m + 1) - lgamma(n - m + 1)) / LOG2


def max_depth(log2q: float) -> tuple[int, list[dict]]:
    trig = log2q - 40.0
    rows: list[dict] = []
    best = 0
    for e in range(12, 40):
        c = 2**e
        if K % c:
            continue
        n_q = N // c
        base = K // c
        lo, hi, dmax = 1, n_q - base, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if log2c(n_q, base + mid) - log2q * (mid - 1) > trig:
                dmax, lo = mid, mid + 1
            else:
                hi = mid - 1
        if dmax:
            depth = dmax * c
            best = max(best, depth)
            rows.append(
                {
                    "e": e,
                    "c": c,
                    "N": n_q,
                    "dmax": dmax,
                    "depth": depth,
                    "margin_bits": round(log2c(n_q, base + dmax) - log2q * (dmax - 1) - trig, 3),
                    "next_margin_bits": round(log2c(n_q, base + dmax + 1) - log2q * dmax - trig, 3),
                }
            )
    return best, rows


def q_threshold() -> dict:
    lo, hi = 128.0, 256.0
    for _ in range(60):
        mid = (lo + hi) / 2
        depth, _ = max_depth(mid)
        if depth >= SIGMA_STAR:
            lo = mid
        else:
            hi = mid
    d_lo, _ = max_depth(lo)
    d_hi, _ = max_depth(hi)
    d_256, _ = max_depth(256.0)
    return {
        "threshold_log2q": round(lo, 6),
        "depth_at_threshold": d_lo,
        "depth_just_above": d_hi,
        "sigma_star": SIGMA_STAR,
        "open_band_slice_bits": round(256 - lo, 6),
        "sanity_256": d_256,
    }


def main() -> int:
    start = time.monotonic()
    depth_256, rows_256 = max_depth(256.0)
    results = {
        "status": "PASS",
        "wall_seconds": None,
        "floor_depth_256": {
            "rows": rows_256,
            "max_depth": depth_256,
            "sigma_star": SIGMA_STAR,
            "gap": SIGMA_STAR - depth_256,
            "banked_band": 2_978_147,
        },
        "q_threshold": q_threshold(),
    }
    if depth_256 != 2**33:
        results["status"] = "FAIL"
        results["error"] = f"expected max_depth at 256 to be 2^33, got {depth_256}"
    if results["q_threshold"]["sanity_256"] != depth_256:
        results["status"] = "FAIL"
        results["error"] = "threshold sanity_256 mismatch"
    results["wall_seconds"] = round(time.monotonic() - start, 6)
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0 if results["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
