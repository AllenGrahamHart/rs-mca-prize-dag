#!/usr/bin/env python3
"""Audit E22 selected-representative collision multiplicities.

Previous all-tail coverage probes found no omitted selected representatives,
but did find collisions: several listed codewords can share the same selected
support-scale representative.  This attacks the remaining premise needed by
the all-tail pricing route: the exact multiplicity convention must account for
these collisions, and the multiplicity should not hide a growing unpriced
factor.

The audit focuses on the row where collisions are most common in the existing
data, n=16,k=8,sigma=1, and sweeps many cyclic/shuffled presentations.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "experiments" / "falsification_pruning"))

from e22_tail_only_pricing_coverage import (  # noqa: E402
    full_agreement_support,
    listed_polys,
    parse_row,
    selected_representative,
    touched_support,
)

CORE = ROOT / "nodes" / "worst_word_challenger_pricing" / "notes"
sys.path.insert(0, str(CORE))

from e22_core import classify_pattern, pattern, sunflower_word  # noqa: E402


DEFAULT_ROWS = ((16, 8, 1),)
DEFAULT_SCALARS = ("linear", "geometric")


def default_layouts(shuffle_count: int) -> list[str]:
    cyclic = [f"cyclic_step_{step}" for step in range(1, 16, 2)]
    shuffles = [f"shuffle_{seed}" for seed in range(1, shuffle_count + 1)]
    return cyclic + shuffles


def record_key(selected: dict[str, Any]) -> tuple[Any, ...]:
    return (
        selected["M"],
        tuple(selected["tail"]),
        tuple(tuple(fib) for fib in selected["selected_fibers"]),
    )


def analyze_cell(n: int, k: int, sigma: int, layout: str, scalar_mode: str, max_examples: int) -> dict[str, Any]:
    word = sunflower_word(n, k, sigma, layout, scalar_mode)
    found = listed_polys(word)
    groups: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    support_groups: dict[tuple[int, ...], list[dict[str, Any]]] = defaultdict(list)
    class_counts = Counter()
    selected_missing = []
    structured = 0

    for poly, rec in found.items():
        cls = classify_pattern(rec, word["ell"])
        if cls not in {"mixed_petal", "full_petal"}:
            continue
        structured += 1
        class_counts[cls] += 1
        support = touched_support(poly, word)
        selected = selected_representative(n, sigma, set(support))
        record = {
            "poly": list(poly),
            "class": cls,
            "agreement": rec["agreement"],
            "petal_agreements": rec["petal_agreements"],
            "touched_support": list(support),
            "full_agreement_support": list(full_agreement_support(poly, word)),
        }
        if selected is None:
            if len(selected_missing) < max_examples:
                selected_missing.append(record)
            continue
        groups[record_key(selected)].append(record)
        support_groups[support].append(record)

    collisions = []
    multiplicities = Counter()
    full_support_multiplicities = Counter()
    tail_only_collision_groups = 0
    max_poly_count = 0
    max_full_support_count = 0
    for key, records in groups.items():
        multiplicities[len(records)] += 1
        full_support_count = len({tuple(r["full_agreement_support"]) for r in records})
        full_support_multiplicities[full_support_count] += 1
        max_poly_count = max(max_poly_count, len(records))
        max_full_support_count = max(max_full_support_count, full_support_count)
        if len(records) <= 1:
            continue
        if len(key[2]) == 0:
            tail_only_collision_groups += 1
        collisions.append(
            {
                "representative": repr(key),
                "poly_count": len(records),
                "unique_full_agreement_supports": full_support_count,
                "class_counts": dict(Counter(r["class"] for r in records)),
                "records": records[:max_examples],
            }
        )

    collisions.sort(
        key=lambda item: (
            item["poly_count"],
            item["unique_full_agreement_supports"],
            item["representative"],
        ),
        reverse=True,
    )
    support_collision_groups = sum(1 for records in support_groups.values() if len(records) > 1)
    support_collision_excess = sum(len(records) - 1 for records in support_groups.values() if len(records) > 1)
    return {
        "n": n,
        "k": k,
        "sigma": sigma,
        "layout": layout,
        "scalar_mode": scalar_mode,
        "list_size": len(found),
        "structured": structured,
        "class_counts": dict(class_counts),
        "selected_representatives": len(groups),
        "missing_selected_representative": len(selected_missing),
        "representative_collision_groups": len(collisions),
        "representative_collision_excess": sum(item["poly_count"] - 1 for item in collisions),
        "support_collision_groups": support_collision_groups,
        "support_collision_excess": support_collision_excess,
        "tail_only_collision_groups": tail_only_collision_groups,
        "max_poly_count_per_representative": max_poly_count,
        "max_unique_full_supports_per_representative": max_full_support_count,
        "multiplicity_histogram": {str(k): v for k, v in sorted(multiplicities.items())},
        "full_support_multiplicity_histogram": {
            str(k): v for k, v in sorted(full_support_multiplicities.items())
        },
        "collision_examples": collisions[:max_examples],
        "missing_examples": selected_missing,
    }


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    totals = Counter()
    mult_hist = Counter()
    full_hist = Counter()
    max_poly = 0
    max_full = 0
    cells_with_collisions = 0
    for row in rows:
        totals["cells"] += 1
        for key in (
            "structured",
            "selected_representatives",
            "missing_selected_representative",
            "representative_collision_groups",
            "representative_collision_excess",
            "support_collision_groups",
            "support_collision_excess",
            "tail_only_collision_groups",
        ):
            totals[key] += int(row[key])
        if row["representative_collision_groups"]:
            cells_with_collisions += 1
        max_poly = max(max_poly, int(row["max_poly_count_per_representative"]))
        max_full = max(max_full, int(row["max_unique_full_supports_per_representative"]))
        mult_hist.update({int(k): v for k, v in row["multiplicity_histogram"].items()})
        full_hist.update({int(k): v for k, v in row["full_support_multiplicity_histogram"].items()})
    return {
        "totals": dict(totals),
        "cells_with_collisions": cells_with_collisions,
        "max_poly_count_per_representative": max_poly,
        "max_unique_full_supports_per_representative": max_full,
        "multiplicity_histogram": {str(k): v for k, v in sorted(mult_hist.items())},
        "full_support_multiplicity_histogram": {str(k): v for k, v in sorted(full_hist.items())},
    }


def write_checkpoint(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    tmp.replace(path)


def run(args: argparse.Namespace) -> dict[str, Any]:
    started = time.time()
    deadline = started + args.seconds
    rows = args.row or list(DEFAULT_ROWS)
    layouts = args.layout or default_layouts(args.shuffle_count)
    scalar_modes = args.scalar_mode or list(DEFAULT_SCALARS)
    payload: dict[str, Any] = {
        "node": "e22_challenger_staircase_pricing",
        "downstream_premise_for": [
            "e22_cross_scale_pricing_multiplicity",
            "e22_minimal_scale_pricing_compatibility",
            "e22_staircase_injectivity",
        ],
        "obligation_attacked": (
            "whether all-tail selected support-scale representatives have "
            "small and explicitly countable codeword multiplicity"
        ),
        "parameters": {
            "rows": [list(row) for row in rows],
            "layouts": layouts,
            "scalar_modes": scalar_modes,
            "shuffle_count": args.shuffle_count,
            "seconds": args.seconds,
        },
        "rows": [],
        "summary": {},
        "verdict": "RUNNING",
    }
    write_checkpoint(args.output, payload)
    for layout in layouts:
        for scalar_mode in scalar_modes:
            for n, k, sigma in rows:
                if time.time() > deadline - 1:
                    payload["summary"] = summarize(payload["rows"])
                    payload["elapsed_seconds"] = time.time() - started
                    payload["verdict"] = "TIMEOUT_PARTIAL"
                    write_checkpoint(args.output, payload)
                    return payload
                payload["rows"].append(
                    analyze_cell(n, k, sigma, layout, scalar_mode, args.max_examples)
                )
                payload["summary"] = summarize(payload["rows"])
                write_checkpoint(args.output, payload)

    payload["summary"] = summarize(payload["rows"])
    summary = payload["summary"]
    if summary["totals"].get("missing_selected_representative", 0):
        payload["verdict"] = "SELECTED_REPRESENTATIVE_OMISSION_CANDIDATE"
    elif summary["max_poly_count_per_representative"] >= args.large_multiplicity_threshold:
        payload["verdict"] = "LARGE_MULTIPLICITY_COLLISION_CANDIDATE"
    elif summary["totals"].get("representative_collision_groups", 0):
        payload["verdict"] = "SMALL_BOUNDED_MULTIPLICITY_COLLISIONS_REPRODUCED"
    else:
        payload["verdict"] = "NO_REPRESENTATIVE_COLLISIONS_IN_SCOPE"
    payload["elapsed_seconds"] = time.time() - started
    write_checkpoint(args.output, payload)
    return payload


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=55.0)
    parser.add_argument("--row", action="append", type=parse_row)
    parser.add_argument("--layout", action="append")
    parser.add_argument("--scalar-mode", action="append")
    parser.add_argument("--shuffle-count", type=int, default=40)
    parser.add_argument("--large-multiplicity-threshold", type=int, default=5)
    parser.add_argument("--max-examples", type=int, default=6)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/falsification_pruning/results/e22_collision_multiplicity_audit.json"),
    )
    return parser


def main() -> None:
    print(json.dumps(run(make_parser().parse_args()), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
