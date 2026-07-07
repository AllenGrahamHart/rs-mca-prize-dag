#!/usr/bin/env python3
"""Local guardrail replay for rate_half_band_closure.

This does not pretend to find the missing mechanism.  It attacks the arithmetic
escape hatches around the rate-1/2 residual band:

* quotient-remainder floor depth at Q=256;
* log2(q) threshold below which the floor already closes the band;
* AQB c=2 finite deficit constants.

All computations are light and checkpointed to JSON.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import time
from typing import Dict, List, Tuple


RESULT_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "results",
    "rate_half_guardrail_replay.json",
)

N_BIG = 2**41
K_BIG = 2**40
SIGMA_STAR = 8_592_912_738
Q_MAX = 256.0
LOG2 = math.log(2.0)


def log2C(n: int, m: int) -> float:
    if m < 0 or m > n:
        return float("-inf")
    return (math.lgamma(n + 1) - math.lgamma(m + 1) - math.lgamma(n - m + 1)) / LOG2


def max_floor_depth(log2q: float) -> Tuple[int, List[Dict[str, object]]]:
    trig = log2q - 40.0
    rows: List[Dict[str, object]] = []
    best = 0
    for e in range(12, 40):
        c = 2**e
        if K_BIG % c:
            continue
        N = N_BIG // c
        base = K_BIG // c
        if base + 1 > N:
            continue
        lo, hi, dmax = 1, N - base, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            score = log2C(N, base + mid) - log2q * (mid - 1)
            if score > trig:
                dmax, lo = mid, mid + 1
            else:
                hi = mid - 1
        if dmax == 0:
            continue
        margin = log2C(N, base + dmax) - log2q * (dmax - 1) - trig
        margin_next = log2C(N, base + dmax + 1) - log2q * dmax - trig
        depth = dmax * c
        best = max(best, depth)
        rows.append(
            {
                "e": e,
                "c": c,
                "N": N,
                "base": base,
                "dmax": dmax,
                "depth": depth,
                "margin_bits": margin,
                "next_margin_bits": margin_next,
            }
        )
    return best, rows


def q_threshold() -> Dict[str, object]:
    lo, hi = 128.0, 256.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if max_floor_depth(mid)[0] >= SIGMA_STAR:
            lo = mid
        else:
            hi = mid
    return {
        "threshold_log2q": lo,
        "depth_at_threshold": max_floor_depth(lo)[0],
        "depth_just_above": max_floor_depth(hi)[0],
        "sigma_star": SIGMA_STAR,
        "open_band_slice_bits": 256.0 - lo,
        "depth_at_256": max_floor_depth(256.0)[0],
    }


def aqb_deficit_constants() -> Dict[str, object]:
    import mpmath as mp

    mp.mp.dps = 80
    N = 2**40
    base = 2**39
    d = 4_296_456_369
    m = base + d

    def log_factorial_bounds(n: int):
        x = mp.mpf(n)
        core = (x + mp.mpf("0.5")) * mp.log(x) - x + mp.mpf("0.5") * mp.log(2 * mp.pi)
        return core + 1 / (12 * x + 1), core + 1 / (12 * x)

    n_lo, n_hi = log_factorial_bounds(N)
    m_lo, m_hi = log_factorial_bounds(m)
    r_lo, r_hi = log_factorial_bounds(N - m)
    log2mp = mp.log(2)
    log_c_lo = n_lo - m_hi - r_hi
    log_c_hi = n_hi - m_lo - r_lo
    deficit_lo = mp.mpf(d) * Q_MAX - 40 - log_c_hi / log2mp
    deficit_hi = mp.mpf(d) * Q_MAX - 40 - log_c_lo / log2mp
    qcrit_lo = (log_c_lo / log2mp + 40) / d
    qcrit_hi = (log_c_hi / log2mp + 40) / d
    claimed_bits = mp.mpf(429_645_547)
    return {
        "N": N,
        "d": d,
        "m": m,
        "deficit_bits_lo": str(deficit_lo),
        "deficit_bits_hi": str(deficit_hi),
        "claimed_bits": str(claimed_bits),
        "certified_margin_bits": str(claimed_bits - deficit_hi),
        "per_fiber_bits": str(claimed_bits / N),
        "qcrit_lo": str(qcrit_lo),
        "qcrit_hi": str(qcrit_hi),
        "convexity_interpretation": (
            "These constants only measure the required AQB gain. The Pro "
            "convex-combination lemma says an averaged quotient-box family "
            "cannot realize this as box-charge amortization without a separate "
            "heavy-fiber theorem."
        ),
    }


def write_result(payload: Dict[str, object]) -> None:
    os.makedirs(os.path.dirname(RESULT_PATH), exist_ok=True)
    tmp = RESULT_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    os.replace(tmp, RESULT_PATH)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seconds", type=float, default=55.0)
    args = ap.parse_args()

    started = time.time()
    payload: Dict[str, object] = {
        "script": os.path.relpath(__file__),
        "started_unix": started,
        "actual_obligation": (
            "rate_half_band_closure has no surviving concrete lemma; this "
            "replays the arithmetic guardrails for the known routes and "
            "quantifies the remaining new-mechanism/bracket-grade crux"
        ),
        "completed": False,
    }
    write_result(payload)

    depth, rows = max_floor_depth(Q_MAX)
    payload["floor_depth_Q256"] = {
        "max_depth": depth,
        "sigma_star": SIGMA_STAR,
        "gap": SIGMA_STAR - depth,
        "banked_band": 2_978_147,
        "best_rows": [r for r in rows if r["depth"] == depth],
    }
    write_result(payload)

    if time.time() - started <= args.seconds:
        payload["q_threshold"] = q_threshold()
        write_result(payload)

    if time.time() - started <= args.seconds:
        payload["aqb_deficit_constants"] = aqb_deficit_constants()
        write_result(payload)

    payload["completed"] = True
    payload["elapsed_seconds"] = time.time() - started
    write_result(payload)


if __name__ == "__main__":
    main()
