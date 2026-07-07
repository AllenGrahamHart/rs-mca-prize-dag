#!/usr/bin/env python3
"""Falsification probe for sov_gridsum_residual's Bohr pricing crux.

This attacks the current open obligation, not the settled mechanism:

    price/rule the paid_large_power_sum / additive-Bohr class.

Two lightweight probes are emitted to JSON:

1. Exact small-prime cell census.  Enumerate m-point residual root cells
   Gamma in F_p^*, compute their largest additive Fourier/power-sum ratio, and
   measure how much of the cell population lies above each Bohr threshold.
   This stress-tests whether a naive "large power sum" paid gate is too broad.

2. Interval/Bohr family frontier.  For Gamma={1,...,m}, compute the exact
   Fourier ratio and the locator-mass density C(m,h)/C(p-1,h).  This is the
   known adversarial family behind the T4B repair, now parameterized as a
   pricing stress curve.

The script is stdlib-only and checkpointed.  It is intentionally not a proof;
it records adversarial pressure on the pricing obligation.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import time
from collections import defaultdict
from pathlib import Path
from typing import Any


DEFAULT_THRESHOLDS = (0.50, 0.70, 0.85, 0.90, 0.93, 0.95, 0.98)
DEFAULT_ROWS = (
    # p, m, h.  Exact by default under --max-cells 150000.
    (17, 5, 3),
    (19, 6, 3),
    (23, 6, 4),
    # Sampled by default; included to expose the direction of travel.
    (29, 7, 4),
)


def parse_row(text: str) -> tuple[int, int, int]:
    parts = text.split(",")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("rows must have form p,m,h")
    p, m, h = map(int, parts)
    if p <= 2 or m <= 0 or h <= 0 or h > m or m >= p:
        raise argparse.ArgumentTypeError("need prime-like p>2 and 0<h<=m<p")
    return p, m, h


def parse_thresholds(text: str) -> list[float]:
    out = [float(x) for x in text.split(",") if x]
    if not out or any(x <= 0 or x >= 1 for x in out):
        raise argparse.ArgumentTypeError("thresholds must lie in (0,1)")
    return sorted(out)


def parse_interval(text: str) -> tuple[int, int]:
    parts = text.split(",")
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("interval rows must have form p,h")
    p, h = map(int, parts)
    if p <= 2 or h <= 0 or h >= p:
        raise argparse.ArgumentTypeError("need p>2 and 0<h<p")
    return p, h


def log2_comb(n: int, k: int) -> float:
    if k < 0 or k > n:
        return float("-inf")
    k = min(k, n - k)
    if k == 0:
        return 0.0
    return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)) / math.log(2)


def additive_tables(p: int) -> list[list[complex]]:
    return [
        [complex(math.cos(2 * math.pi * b * x / p), math.sin(2 * math.pi * b * x / p)) for x in range(p)]
        for b in range(1, p)
    ]


def max_additive_power_ratio(gamma: tuple[int, ...], tables: list[list[complex]]) -> float:
    m = len(gamma)
    best = 0.0
    for row in tables:
        s = 0j
        for x in gamma:
            s += row[x]
        ratio = abs(s) / m
        if ratio > best:
            best = ratio
    return best


def h_subset_value_fraction(gamma: tuple[int, ...], h: int, p: int) -> float:
    vals = set()
    for subset in itertools.combinations(gamma, h):
        vals.add(sum(subset) % p)
    denom = min(math.comb(len(gamma), h), p)
    return len(vals) / denom if denom else 0.0


def iter_cells(domain: list[int], m: int, max_cells: int, rng: random.Random):
    total = math.comb(len(domain), m)
    if total <= max_cells:
        for gamma in itertools.combinations(domain, m):
            yield gamma, "exact"
        return

    seen: set[tuple[int, ...]] = set()
    while len(seen) < max_cells:
        gamma = tuple(sorted(rng.sample(domain, m)))
        if gamma in seen:
            continue
        seen.add(gamma)
        yield gamma, "sample"


def exact_or_sample_row(
    p: int,
    m: int,
    h: int,
    thresholds: list[float],
    max_cells: int,
    rng: random.Random,
) -> dict[str, Any]:
    domain = list(range(1, p))
    tables = additive_tables(p)
    total_cells = math.comb(len(domain), m)
    counters = {
        f"{theta:.2f}": {
            "gate_cells": 0,
            "gate_cells_with_value_fraction_below_0_6": 0,
            "gate_cells_with_value_fraction_at_least_0_95": 0,
            "residual_collision_cells_if_threshold": 0,
        }
        for theta in thresholds
    }
    hist = defaultdict(int)
    best = {
        "max_power_ratio": -1.0,
        "gamma": None,
        "value_fraction": None,
    }
    worst_residual_by_threshold = {
        f"{theta:.2f}": {
            "min_value_fraction_below_threshold": 1.0,
            "gamma": None,
            "max_power_ratio": None,
        }
        for theta in thresholds
    }

    started = time.time()
    mode = "exact"
    visited = 0
    for gamma, mode in iter_cells(domain, m, max_cells, rng):
        visited += 1
        ratio = max_additive_power_ratio(gamma, tables)
        vf = h_subset_value_fraction(gamma, h, p)
        hist[f"{math.floor(ratio * 20) / 20:.2f}"] += 1
        if ratio > best["max_power_ratio"]:
            best = {
                "max_power_ratio": ratio,
                "gamma": list(gamma),
                "value_fraction": vf,
            }

        for theta in thresholds:
            key = f"{theta:.2f}"
            if ratio >= theta:
                counters[key]["gate_cells"] += 1
                if vf < 0.6:
                    counters[key]["gate_cells_with_value_fraction_below_0_6"] += 1
                if vf >= 0.95:
                    counters[key]["gate_cells_with_value_fraction_at_least_0_95"] += 1
            else:
                if vf < 0.6:
                    counters[key]["residual_collision_cells_if_threshold"] += 1
                if vf < worst_residual_by_threshold[key]["min_value_fraction_below_threshold"]:
                    worst_residual_by_threshold[key] = {
                        "min_value_fraction_below_threshold": vf,
                        "gamma": list(gamma),
                        "max_power_ratio": ratio,
                    }

    cell_mass = math.comb(m, h)
    for theta in thresholds:
        key = f"{theta:.2f}"
        c = counters[key]
        c["visited_fraction"] = c["gate_cells"] / visited if visited else 0.0
        c["naive_cell_locator_mass_sum"] = c["gate_cells"] * cell_mass
        c["log2_naive_cell_locator_mass_sum"] = (
            math.log2(c["naive_cell_locator_mass_sum"])
            if c["naive_cell_locator_mass_sum"]
            else None
        )

    return {
        "p": p,
        "m": m,
        "h": h,
        "domain_size": len(domain),
        "total_cells": total_cells,
        "visited_cells": visited,
        "mode": mode,
        "elapsed_seconds": time.time() - started,
        "max_observed": best,
        "ratio_histogram_floor_0_05": dict(sorted(hist.items())),
        "thresholds": counters,
        "worst_residual_by_threshold": worst_residual_by_threshold,
    }


def interval_fourier_ratio(p: int, m: int) -> float:
    # |sum_{x=1}^m exp(2 pi i x / p)| / m.
    numerator = abs(math.sin(math.pi * m / p))
    denominator = m * abs(math.sin(math.pi / p))
    return numerator / denominator


def interval_value_fraction_no_wrap(p: int, m: int, h: int) -> float:
    # Sums of h distinct values in [1,m] fill a full integer interval of this
    # length.  The expression is exact as a value-set size before mod wrap.
    interval_size = h * (m - h) + 1
    denom = min(math.comb(m, h), p)
    return min(interval_size, p) / denom


def interval_frontier(
    p: int,
    h: int,
    divisors: list[int],
    thresholds: list[float],
) -> dict[str, Any]:
    rows = []
    for R in divisors:
        m = (p - 1) // R
        if m < h:
            continue
        ratio = interval_fourier_ratio(p, m)
        row = {
            "R": R,
            "m": m,
            "alpha": m / (p - 1),
            "max_power_ratio_frequency_1": ratio,
            "log2_locator_density_C_m_h_over_C_pminus1_h": log2_comb(m, h) - log2_comb(p - 1, h),
            "value_fraction_no_wrap_model": interval_value_fraction_no_wrap(p, m, h),
            "passes_thresholds": [f"{theta:.2f}" for theta in thresholds if ratio >= theta],
        }
        rows.append(row)
    return {
        "p": p,
        "h": h,
        "family": "Gamma={1,...,(p-1)/R} in F_p^*",
        "rows": rows,
    }


def write_checkpoint(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def run(args: argparse.Namespace) -> dict[str, Any]:
    thresholds = parse_thresholds(args.thresholds)
    rng = random.Random(args.seed)
    started = time.time()
    deadline = started + args.seconds
    out: dict[str, Any] = {
        "node": "sov_gridsum_residual",
        "obligation_attacked": "price/rule the paid_large_power_sum/additive-Bohr class",
        "verdict": "RUNNING",
        "seed": args.seed,
        "thresholds": thresholds,
        "rows": [],
        "interval_frontiers": [],
        "notes": [
            "Exact rows enumerate residual root cells Gamma and measure Bohr-gate mass.",
            "Interval rows parameterize the known T4B adversarial family as a pricing stress curve.",
            "A residual_collision_cells_if_threshold count is a Lane-1 falsifier for that threshold.",
        ],
    }

    rows = args.row or list(DEFAULT_ROWS)
    for p, m, h in rows:
        if time.time() > deadline - 2:
            out["verdict"] = "TIMEOUT_PARTIAL"
            write_checkpoint(args.output, out)
            return out
        row = exact_or_sample_row(p, m, h, thresholds, args.max_cells, rng)
        out["rows"].append(row)
        write_checkpoint(args.output, out)

    for p, h in args.interval:
        if time.time() > deadline - 2:
            out["verdict"] = "TIMEOUT_PARTIAL"
            write_checkpoint(args.output, out)
            return out
        out["interval_frontiers"].append(interval_frontier(p, h, args.interval_R, thresholds))
        write_checkpoint(args.output, out)

    out["elapsed_seconds"] = time.time() - started
    out["verdict"] = "COMPLETE_NO_DELETION_SIGNAL"
    write_checkpoint(args.output, out)
    return out


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=55.0)
    parser.add_argument("--max-cells", type=int, default=150_000)
    parser.add_argument("--seed", type=int, default=20260705)
    parser.add_argument("--thresholds", default=",".join(str(x) for x in DEFAULT_THRESHOLDS))
    parser.add_argument("--row", action="append", type=parse_row, help="small census row p,m,h; repeatable")
    parser.add_argument(
        "--interval",
        action="append",
        type=parse_interval,
        default=[(65537, 21)],
        help="interval frontier row p,h; repeatable",
    )
    parser.add_argument(
        "--interval-R",
        type=int,
        nargs="+",
        default=[2, 3, 4, 5, 8, 12, 16, 24, 32, 48, 64, 96, 128],
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/falsification_pruning/results/sov_bohr_pricing_census.json"),
    )
    return parser


def main() -> None:
    args = make_parser().parse_args()
    payload = run(args)
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
