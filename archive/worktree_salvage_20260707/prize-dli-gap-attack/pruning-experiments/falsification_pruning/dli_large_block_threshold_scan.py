#!/usr/bin/env python3
"""Threshold scan for the DLI weighted large-block premise.

The downstream DLI conductor-mass implication consumes the premise that the
actual U-weighted central measure puts negligible mass on small/exceptional
support.  This script probes the entropy side of that premise.

For inactive-or-ternary profiles on N = alpha * L seen coordinates, the
U-weighted contribution of profiles with active support <= beta * L is bounded
by

    q^L * sum_{k <= beta L} binom(N,k) / 4^N.

The prize-shaped seen-coordinate lever is alpha = 256.  Positive exponents are
a falsification warning for the premise; negative exponents mean this specific
low-support route is exponentially suppressed in the U-weighted object.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Iterable


def log2_choose(n: int, k: int) -> float:
    if k < 0 or k > n:
        return float("-inf")
    return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)) / math.log(2.0)


def log2_sum(values: Iterable[float]) -> float:
    vals = [v for v in values if math.isfinite(v)]
    if not vals:
        return float("-inf")
    m = max(vals)
    return m + math.log2(sum(2.0 ** (v - m) for v in vals))


def row(q_bits: int, alpha: int, L: int, beta: int) -> dict[str, float | int]:
    N = alpha * L
    cutoff = min(N, beta * L)
    log2_low_sum = log2_sum(log2_choose(N, k) for k in range(cutoff + 1))
    log2_contribution = q_bits * L + log2_low_sum - 2 * N
    return {
        "q_bits": q_bits,
        "alpha": alpha,
        "L": L,
        "beta": beta,
        "N": N,
        "support_cutoff": cutoff,
        "log2_low_support_count_sum": log2_low_sum,
        "log_q_zero_skew_low_mass_contribution": log2_contribution / q_bits,
        "log_q_per_L": log2_contribution / (q_bits * L),
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    rows = [
        row(args.q_bits, alpha, L, beta)
        for beta in args.beta
        for L in args.L
        for alpha in args.alpha
    ]
    thresholds = []
    for beta in args.beta:
        for L in args.L:
            candidates = [r for r in rows if r["beta"] == beta and r["L"] == L]
            negative = [r for r in candidates if float(r["log_q_per_L"]) < 0]
            thresholds.append(
                {
                    "beta": beta,
                    "L": L,
                    "first_alpha_with_negative_exponent": (
                        min(int(r["alpha"]) for r in negative) if negative else None
                    ),
                    "prize_alpha_256_log_q_per_L": next(
                        float(r["log_q_per_L"]) for r in candidates if r["alpha"] == 256
                    ),
                }
            )
    verdict = (
        "PRIZE_ALPHA_SUPPRESSES_TESTED_LOW_SUPPORT_MASS"
        if all(float(r["log_q_per_L"]) < 0 for r in rows if r["alpha"] == 256)
        else "LOW_SUPPORT_MASS_PRESSURE_AT_PRIZE_ALPHA"
    )
    payload = {
        "node": "dli_prime_weighted_large_block_support",
        "downstream_amber_node": "dli_prime_block_conductor_mass",
        "obligation_attacked": "U-weighted small/exceptional support suppression premise consumed by conductor-mass implication",
        "formula": "q^L * sum_{k <= beta L} binom(alpha L,k) / 4^(alpha L)",
        "rows": rows,
        "thresholds": thresholds,
        "verdict": verdict,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return payload


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--q-bits", type=int, default=256)
    parser.add_argument("--alpha", type=int, nargs="+", default=[64, 96, 128, 160, 192, 224, 240, 256, 288, 320])
    parser.add_argument("--L", type=int, nargs="+", default=[1, 2, 4, 8, 16, 32])
    parser.add_argument("--beta", type=int, nargs="+", default=[1, 2, 4])
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/falsification_pruning/results/dli_large_block_threshold_scan.json"),
    )
    return parser


def main() -> None:
    print(json.dumps(run(make_parser().parse_args()), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
