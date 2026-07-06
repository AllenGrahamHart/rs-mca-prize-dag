#!/usr/bin/env python3
"""Bounded E22 shuffled-layout third-class search.

`e22_extended_local_census.py` stresses mostly cyclic petal layouts.  This
companion script keeps the same exact E15/E22 list classifier but randomizes
the domain order used to form the core, petals, and background.  A non-planted
word outside the mixed/full-petal challenger classes is a direct falsifier for
the two-column premise behind `worst_word_planted`.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
CORE = ROOT / "nodes" / "worst_word_challenger_pricing" / "notes"
OUT = ROOT / "experiments" / "amber_stress" / "e22_random_layout_census_results.json"

sys.path.insert(0, str(CORE))
from e22_core import exact_cell_census  # noqa: E402


def planned_cells() -> list[dict[str, Any]]:
    cells: list[dict[str, Any]] = []

    def add(
        n: int,
        k: int,
        sigma: int,
        layout: str,
        scalar: str,
        tier: str,
    ) -> None:
        cells.append(
            {
                "n": n,
                "k": k,
                "sigma": sigma,
                "layout": layout,
                "scalar_mode": scalar,
                "tier": tier,
                "agreement_sets": math.comb(n, k + sigma),
            }
        )

    # Positive controls: reproduce the known E15-style challenger cells.
    for k in (2, 4, 8):
        add(16, k, 1, "cyclic_step_1", "linear", "positive_control")

    # Shuffled analogues of the n=16 toy grid.
    for seed in range(12):
        for k in (2, 4, 8):
            for sigma in (1, 2):
                for scalar in ("linear", "geometric"):
                    add(16, k, sigma, f"shuffle_{seed}", scalar, "shuffle_toy")

    # Medium exact cells: randomized petal/background placements on n=24,32.
    for seed in range(8):
        for n in (24, 32):
            for k in (2, 3, 4):
                for sigma in (1, 2):
                    for scalar in ("linear", "geometric"):
                        add(n, k, sigma, f"shuffle_{100 + seed}", scalar, "shuffle_medium")

    # Larger-domain smoke cells kept low-k so exact enumeration stays bounded.
    for seed in range(8):
        for n in (48, 64):
            for sigma in (1, 2):
                add(n, 2, sigma, f"shuffle_{200 + seed}", "linear", "shuffle_large_low_k")

    # Try small exact cells first; larger cells remain available until the time
    # guard or combo cap stops the run.
    return sorted(cells, key=lambda item: (item["agreement_sets"], item["tier"], item["n"]))


def checkpoint(results: dict[str, Any]) -> None:
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")


def summarize(results: dict[str, Any]) -> None:
    checked = results["cells_checked"]
    skipped = results["cells_skipped"]
    failed = results["cells_failed"]
    total_sets = sum(cell.get("agreement_sets_checked", 0) for cell in checked)
    results["summary"] = {
        "status": "FAIL" if failed else "PASS",
        "cells_checked": len(checked),
        "cells_skipped": len(skipped),
        "cells_failed": len(failed),
        "agreement_sets_checked": total_sets,
        "structured_challenger_cells": sum(
            1 for cell in checked if cell.get("classified_challenger", 0) > 0
        ),
        "positive_control_cells": sum(1 for cell in checked if cell.get("tier") == "positive_control"),
        "positive_controls_detected": sum(
            1
            for cell in checked
            if cell.get("tier") == "positive_control" and cell.get("classified_challenger", 0) > 0
        ),
        "max_list_size": max((cell.get("list_size", 0) for cell in checked), default=0),
        "max_unclassified": max((cell.get("unclassified", 0) for cell in checked), default=0),
        "completed_all_planned_cells": results.get("completed_all_planned_cells", False),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=55.0)
    parser.add_argument("--combo-cap", type=int, default=220_000)
    parser.add_argument("--min-seconds-left", type=float, default=4.0)
    args = parser.parse_args()

    deadline = time.monotonic() + args.time_limit
    results: dict[str, Any] = {
        "started_at_unix": time.time(),
        "time_limit_seconds": args.time_limit,
        "combo_cap": args.combo_cap,
        "min_seconds_left": args.min_seconds_left,
        "cell_plan": planned_cells(),
        "cells_checked": [],
        "cells_skipped": [],
        "cells_failed": [],
        "completed_all_planned_cells": False,
    }
    checkpoint(results)

    for spec in results["cell_plan"]:
        seconds_left = deadline - time.monotonic()
        if seconds_left < args.min_seconds_left:
            results["cells_skipped"].append(
                {
                    **spec,
                    "skip_reason": "time_guard",
                    "seconds_left": round(seconds_left, 6),
                }
            )
            continue
        if spec["agreement_sets"] > args.combo_cap:
            results["cells_skipped"].append({**spec, "skip_reason": "combo_cap"})
            continue

        t0 = time.monotonic()
        cell = exact_cell_census(
            spec["n"],
            spec["k"],
            spec["sigma"],
            spec["layout"],
            spec["scalar_mode"],
            example_cap=6,
        )
        cell["tier"] = spec["tier"]
        cell["wall_seconds"] = round(time.monotonic() - t0, 6)
        results["cells_checked"].append(cell)
        if cell["unclassified"] > 0:
            results["cells_failed"].append(cell)
        summarize(results)
        checkpoint(results)

    results["completed_all_planned_cells"] = all(
        item["skip_reason"] == "combo_cap" for item in results["cells_skipped"]
    )
    results["finished_at_unix"] = time.time()
    summarize(results)
    checkpoint(results)
    print(json.dumps(results["summary"], indent=2, sort_keys=True))
    if results["cells_failed"]:
        print("THIRD_CLASS_ALARM: shuffled-layout unclassified challengers found")
        return 1
    print("PASS: shuffled-layout E22 census found no third challenger class")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
