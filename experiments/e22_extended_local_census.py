#!/usr/bin/env python3
"""Bounded E22 third-class search.

This is an adversarial, checkpointed local sweep around the E15/E22 planted-word
model.  It does not try to prove the challenger-pricing predicate.  It tries to
falsify the two-column premise by looking for a non-planted list word outside
the known structured mixed/full-petal challenger classes.
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
OUT = ROOT / "experiments" / "amber_stress" / "e22_extended_local_census_results.json"

sys.path.insert(0, str(CORE))
from e22_core import exact_cell_census  # noqa: E402


def planned_cells() -> list[dict[str, Any]]:
    cells: list[dict[str, Any]] = []

    def add(n: int, k: int, sigma: int, layout: str, scalar: str, tier: str) -> None:
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

    # Full toy grid around the reproduced E15 counterexample.  These cells are
    # tiny but vary layout and scalar choices enough to catch obvious artifacts.
    for k in (1, 2, 4, 8):
        for sigma in (1, 2, 3):
            for layout in ("cyclic_step_1", "cyclic_step_5"):
                for scalar in ("linear", "geometric"):
                    add(16, k, sigma, layout, scalar, "toy_full")

    # Medium cells over a non-power-of-two subgroup size.  These are still exact
    # and deliberately include rate-like rows plus one larger k=6 stress cell.
    for k in (2, 3, 4):
        for sigma in (1, 2):
            for layout in ("cyclic_step_1", "cyclic_step_5"):
                add(24, k, sigma, layout, "linear", "medium")
    for sigma in (1, 2):
        add(24, 4, sigma, "cyclic_step_1", "geometric", "medium_scalar")
    add(24, 6, 1, "cyclic_step_1", "linear", "large_single")

    # Larger-n probes kept sparse so this remains laptop-safe.
    for sigma in (1, 2):
        for layout in ("cyclic_step_1", "cyclic_step_5"):
            for scalar in ("linear", "geometric"):
                add(32, 2, sigma, layout, scalar, "large_n_low_k")
    for scalar in ("linear", "geometric"):
        add(32, 4, 1, "cyclic_step_1", scalar, "large_n_mid_k")
    for n in (48, 64):
        for layout in ("cyclic_step_1", "cyclic_step_5"):
            add(n, 2, 1, layout, "linear", "larger_domain_smoke")

    # Cells we would like to know, but which are intentionally skipped by the
    # local cap.  Recording them makes the frontier explicit for Modal or proof.
    for spec in [
        (24, 8, 1, "cyclic_step_1", "linear"),
        (32, 4, 2, "cyclic_step_1", "linear"),
        (32, 8, 1, "cyclic_step_1", "linear"),
        (48, 4, 1, "cyclic_step_1", "linear"),
        (64, 2, 2, "cyclic_step_1", "linear"),
        (64, 4, 1, "cyclic_step_1", "linear"),
    ]:
        add(*spec, tier="frontier_skip")

    return cells


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
        "max_list_size": max((cell.get("list_size", 0) for cell in checked), default=0),
        "max_unclassified": max((cell.get("unclassified", 0) for cell in checked), default=0),
        "completed_all_planned_cells": results.get("completed_all_planned_cells", False),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=55.0)
    parser.add_argument("--combo-cap", type=int, default=360_000)
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
            results["cells_skipped"].append(
                {
                    **spec,
                    "skip_reason": "combo_cap",
                }
            )
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
        print("THIRD_CLASS_ALARM: unclassified non-planted list words found")
        return 1
    print("PASS: no third challenger class found in bounded exact cells")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
