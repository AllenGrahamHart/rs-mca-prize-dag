#!/usr/bin/env python3
"""Modal dilution probe for the SOV Bohr-pricing crux.

The open SOV obligation is not whether small value-set cells are Bohr
detectable; that mechanism is already supported.  The pricing risk is that a
large-power-sum gate may include many cells whose h-sum value distribution is
already essentially uniform.

This probe builds cells by diluting the known interval/Bohr obstruction:

    Gamma = k points from I={1,...,m} plus m-k random points outside I.

It measures:

- directed/small-frequency additive power-sum ratios;
- sampled h-subset sum collision rates versus a uniform F_p baseline;
- naive combinatorial mass of the diluted family.

A broad threshold that accepts high-dilution families with near-uniform
collision rates is not false by itself, but it sharpens the pricing obligation:
the paid class must be near-pure or must include an internal Lane-1 fallback.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import statistics
import sys
import time
from pathlib import Path
from typing import Any

import modal


sys.dont_write_bytecode = True

APP_NAME = "rs-mca-sov-bohr-dilution-20260705"
app = modal.App(APP_NAME)


DEFAULT_BETAS = (1.0, 0.98, 0.95, 0.93, 0.90, 0.85, 0.80, 0.70, 0.50)
DEFAULT_THRESHOLDS = (0.85, 0.90, 0.93, 0.95, 0.98)


def parse_float_list(text: str) -> list[float]:
    return [float(x) for x in text.split(",") if x]


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    tmp.replace(path)


@app.function(image=modal.Image.debian_slim(), cpu=2, memory=2048, timeout=58)
def run_remote(
    p: int,
    m: int,
    h: int,
    betas: list[float],
    thresholds: list[float],
    cells_per_beta: int,
    sum_samples: int,
    max_frequency: int,
    seed: int,
    seconds: float,
) -> dict[str, Any]:
    started = time.time()
    deadline = started + seconds
    rng = random.Random(seed)
    interval = list(range(1, m + 1))
    outside = list(range(m + 1, p))

    def log2_comb(n: int, k: int) -> float:
        if k < 0 or k > n:
            return float("-inf")
        k = min(k, n - k)
        return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)) / math.log(2)

    def additive_ratio(gamma: list[int], freq: int) -> float:
        re = 0.0
        im = 0.0
        scale = 2.0 * math.pi * freq / p
        for x in gamma:
            angle = scale * x
            re += math.cos(angle)
            im += math.sin(angle)
        return math.hypot(re, im) / len(gamma)

    def sampled_sum_stats(gamma: list[int]) -> dict[str, Any]:
        seen: set[int] = set()
        collisions = 0
        for _ in range(sum_samples):
            total = sum(rng.sample(gamma, h)) % p
            if total in seen:
                collisions += 1
            else:
                seen.add(total)
        expected_uniform_collisions = sum_samples - p * (1.0 - ((p - 1.0) / p) ** sum_samples)
        ratio = collisions / expected_uniform_collisions if expected_uniform_collisions else None
        return {
            "samples": sum_samples,
            "distinct_sums": len(seen),
            "collisions": collisions,
            "expected_uniform_collisions": expected_uniform_collisions,
            "collision_ratio_vs_uniform": ratio,
        }

    def interval_exact_stats() -> dict[str, Any]:
        interval_value_size = h * (m - h) + 1
        denom = min(math.comb(m, h), p)
        return {
            "interval_h_sum_value_size_no_wrap": interval_value_size,
            "interval_value_fraction_no_wrap": min(interval_value_size, p) / denom,
            "interval_directed_ratio_freq_1": additive_ratio(interval, 1),
        }

    rows = []
    total_m_cell_log = log2_comb(p - 1, m)
    total_h_locator_log = log2_comb(p - 1, h)
    cell_locator_log = log2_comb(m, h)

    for beta in betas:
        if time.time() > deadline - 2:
            break
        k = max(0, min(m, round(beta * m)))
        cell_rows = []
        ratio_1 = []
        ratio_max_small = []
        collision_ratios = []
        collisions = []
        distincts = []
        for idx in range(cells_per_beta):
            if time.time() > deadline - 2:
                break
            if k == m:
                gamma = interval[:]
            else:
                gamma = sorted(rng.sample(interval, k) + rng.sample(outside, m - k))
            r1 = additive_ratio(gamma, 1)
            rmax = max(additive_ratio(gamma, freq) for freq in range(1, max_frequency + 1))
            ss = sampled_sum_stats(gamma)
            ratio_1.append(r1)
            ratio_max_small.append(rmax)
            if ss["collision_ratio_vs_uniform"] is not None:
                collision_ratios.append(ss["collision_ratio_vs_uniform"])
            collisions.append(ss["collisions"])
            distincts.append(ss["distinct_sums"])
            if idx < 3:
                cell_rows.append(
                    {
                        "directed_ratio_freq_1": r1,
                        "max_ratio_freq_1_to_max_frequency": rmax,
                        "sum_stats": ss,
                        "sample_prefix": gamma[:16],
                    }
                )

        family_log = log2_comb(m, k) + log2_comb((p - 1) - m, m - k)
        naive_locator_density_log = family_log + cell_locator_log - total_h_locator_log
        row = {
            "beta_requested": beta,
            "interval_points_kept": k,
            "random_points_added": m - k,
            "samples_completed": len(ratio_1),
            "log2_family_cell_count": family_log,
            "log2_family_cell_density_among_m_cells": family_log - total_m_cell_log,
            "log2_naive_cell_locator_mass_density": naive_locator_density_log,
            "directed_ratio_freq_1": {
                "min": min(ratio_1) if ratio_1 else None,
                "median": statistics.median(ratio_1) if ratio_1 else None,
                "max": max(ratio_1) if ratio_1 else None,
            },
            "max_ratio_freq_1_to_max_frequency": {
                "min": min(ratio_max_small) if ratio_max_small else None,
                "median": statistics.median(ratio_max_small) if ratio_max_small else None,
                "max": max(ratio_max_small) if ratio_max_small else None,
            },
            "sampled_h_sum_collisions": {
                "median_collision_ratio_vs_uniform": statistics.median(collision_ratios)
                if collision_ratios
                else None,
                "max_collision_ratio_vs_uniform": max(collision_ratios) if collision_ratios else None,
                "median_collisions": statistics.median(collisions) if collisions else None,
                "median_distinct_sums": statistics.median(distincts) if distincts else None,
            },
            "passes_thresholds_by_median_smallfreq": [
                f"{theta:.3f}"
                for theta in thresholds
                if ratio_max_small and statistics.median(ratio_max_small) >= theta
            ],
            "examples": cell_rows,
        }
        rows.append(row)

    risky = [
        row
        for row in rows
        if row["max_ratio_freq_1_to_max_frequency"]["median"] is not None
        and row["max_ratio_freq_1_to_max_frequency"]["median"] >= 0.90
        and row["sampled_h_sum_collisions"]["median_collision_ratio_vs_uniform"] is not None
        and row["sampled_h_sum_collisions"]["median_collision_ratio_vs_uniform"] <= 1.25
        and row["random_points_added"] > 0
    ]
    return {
        "node": "sov_gridsum_residual",
        "obligation_attacked": "Bohr/large_power_sum pricing threshold under diluted interval families",
        "scope": "constructed diluted-Bohr families; sampled h-sum collision evidence",
        "app_name": APP_NAME,
        "parameters": {
            "p": p,
            "m": m,
            "h": h,
            "cells_per_beta": cells_per_beta,
            "sum_samples": sum_samples,
            "max_frequency": max_frequency,
            "seed": seed,
            "seconds": seconds,
        },
        "interval_baseline": interval_exact_stats(),
        "thresholds": thresholds,
        "rows": rows,
        "elapsed_seconds": time.time() - started,
        "verdict": (
            "BROAD_BOHR_GATE_OVERINCLUSION_PRESSURE"
            if risky
            else "NO_DILUTED_OVERINCLUSION_AT_TESTED_THRESHOLDS"
        ),
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    betas = parse_float_list(args.betas)
    thresholds = parse_float_list(args.thresholds)
    initial = {
        "node": "sov_gridsum_residual",
        "obligation_attacked": "Bohr/large_power_sum pricing threshold under diluted interval families",
        "verdict": "RUNNING",
    }
    write_json(args.output, initial)
    with app.run():
        payload = run_remote.remote(
            args.p,
            args.m,
            args.h,
            betas,
            thresholds,
            args.cells_per_beta,
            args.sum_samples,
            args.max_frequency,
            args.seed,
            args.seconds,
        )
    write_json(args.output, payload)
    return payload


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--p", type=int, default=65537)
    parser.add_argument("--m", type=int, default=1024)
    parser.add_argument("--h", type=int, default=21)
    parser.add_argument("--betas", default=",".join(str(x) for x in DEFAULT_BETAS))
    parser.add_argument("--thresholds", default=",".join(str(x) for x in DEFAULT_THRESHOLDS))
    parser.add_argument("--cells-per-beta", type=int, default=16)
    parser.add_argument("--sum-samples", type=int, default=6000)
    parser.add_argument("--max-frequency", type=int, default=12)
    parser.add_argument("--seed", type=int, default=7205)
    parser.add_argument("--seconds", type=float, default=50.0)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/falsification_pruning/results/sov_modal_bohr_dilution_probe.json"),
    )
    return parser


def main() -> None:
    payload = run(make_parser().parse_args())
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
