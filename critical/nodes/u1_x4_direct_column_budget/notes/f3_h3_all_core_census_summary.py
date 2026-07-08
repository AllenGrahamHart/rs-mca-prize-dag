#!/usr/bin/env python3
"""Aggregate the complete n=96 h=3 core-orbit census slices."""

from __future__ import annotations

import json
import runpy
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
SUMMARY_PATH = HERE / "f3_h3_all_core_census_summary.json"
N = 96
SHAPES_PER_CORE = 129766
EXPECTED_CORES = {(0, 1, k) for k in range(2, 93)}
CONSECUTIVE_CORE = (0, 1, 2)


def pct(num: int, den: int) -> str:
    return f"{100 * num / den:.4f}%"


def load_consecutive_core() -> tuple[dict, list[dict]]:
    ns = runpy.run_path(str(HERE / "f3_h3_consecutive_core_structure.py"))
    exceptions = ns["EXCEPTIONS"]
    activation_exceptions = [
        {
            "shape": [0, 1, 2, *list(b)],
            "activation_primes": [p],
        }
        for b, p in exceptions
    ]
    summary = {
        "core": list(CONSECUTIVE_CORE),
        "source": "F3_H3_CONSECUTIVE_CORE_CENSUS.md",
        "total_shapes": SHAPES_PER_CORE,
        "norm_exception_count": 1122,
        "activation_exception_count": len(activation_exceptions),
    }
    if summary["activation_exception_count"] != 44:
        raise AssertionError(summary)
    return summary, activation_exceptions


def load_generic_cores() -> tuple[list[dict], list[dict]]:
    core_summaries = []
    activation_exceptions = []
    seen: set[tuple[int, int, int]] = set()
    for path in sorted(HERE.glob("f3_h3_core_*_census_results.json")):
        data = json.loads(path.read_text())
        core = tuple(data["core"])
        if core in seen:
            raise AssertionError(f"duplicate core {core}")
        seen.add(core)
        if core == CONSECUTIVE_CORE:
            raise AssertionError(f"unexpected generic consecutive core file {path}")
        if core not in EXPECTED_CORES:
            raise AssertionError(f"unexpected core {core} in {path}")
        if data["total_shapes"] != SHAPES_PER_CORE:
            raise AssertionError((path, data["total_shapes"]))
        if data["activation_exception_count"] != len(data["activation_exceptions"]):
            raise AssertionError(path)
        core_summaries.append(
            {
                "core": list(core),
                "source": path.name,
                "total_shapes": data["total_shapes"],
                "norm_exception_count": data["norm_exception_count"],
                "activation_exception_count": data["activation_exception_count"],
            }
        )
        activation_exceptions.extend(data["activation_exceptions"])

    missing = sorted(EXPECTED_CORES - seen - {CONSECUTIVE_CORE})
    if missing:
        raise AssertionError(f"missing generic cores: {missing}")
    if len(seen) != 90:
        raise AssertionError(len(seen))
    return core_summaries, activation_exceptions


def main() -> None:
    consecutive_summary, consecutive_activations = load_consecutive_core()
    generic_summaries, generic_activations = load_generic_cores()
    core_summaries = [consecutive_summary] + sorted(
        generic_summaries, key=lambda rec: tuple(rec["core"])
    )
    activation_exceptions = consecutive_activations + sorted(
        generic_activations, key=lambda rec: tuple(rec["shape"])
    )

    cores = {tuple(rec["core"]) for rec in core_summaries}
    if cores != EXPECTED_CORES:
        raise AssertionError(sorted(EXPECTED_CORES - cores))

    total_shapes = sum(rec["total_shapes"] for rec in core_summaries)
    norm_total = sum(rec["norm_exception_count"] for rec in core_summaries)
    activation_total = sum(rec["activation_exception_count"] for rec in core_summaries)
    if activation_total != len(activation_exceptions):
        raise AssertionError((activation_total, len(activation_exceptions)))
    if total_shapes != 91 * SHAPES_PER_CORE:
        raise AssertionError(total_shapes)
    if (norm_total, activation_total) != (106250, 720):
        raise AssertionError((norm_total, activation_total))

    prime_counts = Counter(
        p for rec in activation_exceptions for p in rec["activation_primes"]
    )
    top_cores = sorted(
        core_summaries,
        key=lambda rec: (-rec["activation_exception_count"], tuple(rec["core"])),
    )[:12]
    summary = {
        "n": N,
        "scope": (
            "one complete oriented B-slice for each of the 91 affine/Galois "
            "orbits of the first h=3 core"
        ),
        "core_type_count": len(core_summaries),
        "shapes_per_core": SHAPES_PER_CORE,
        "total_oriented_shapes": total_shapes,
        "norm_exception_count": norm_total,
        "activation_exception_count": activation_total,
        "rates": {
            "rational_norm_exception": {
                "numerator": norm_total,
                "denominator": total_shapes,
                "percent": pct(norm_total, total_shapes),
            },
            "actual_common_root_activation": {
                "numerator": activation_total,
                "denominator": total_shapes,
                "percent": pct(activation_total, total_shapes),
            },
        },
        "core_summaries": core_summaries,
        "top_activation_cores": top_cores,
        "activation_prime_counts": dict(sorted(prime_counts.items())),
        "activation_exceptions": activation_exceptions,
    }
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n")
    print(
        "TOTAL "
        f"core_types={summary['core_type_count']} "
        f"oriented_shapes={total_shapes} "
        f"norm_exceptions={norm_total} "
        f"activation_exceptions={activation_total}"
    )
    print(
        "RATES "
        f"norm={summary['rates']['rational_norm_exception']['percent']} "
        f"activation={summary['rates']['actual_common_root_activation']['percent']}"
    )
    print("TOP_ACTIVATION_CORES")
    for rec in top_cores[:6]:
        print(
            f"  {tuple(rec['core'])}: "
            f"{rec['activation_exception_count']}/{rec['total_shapes']}"
        )
    print("H3_ALL_CORE_CENSUS_SUMMARY_DONE")


if __name__ == "__main__":
    main()
