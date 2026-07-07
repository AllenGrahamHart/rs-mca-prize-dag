#!/usr/bin/env python3
"""Sweep E22 all-tail pricing coverage over sunflower presentations.

The existing all-tail probe checks whether vacuous common-tail certificates are
still selected by the dyadic minimal-scale pricing machinery.  This wrapper
attacks the premise more adversarially by changing the sunflower layout and
petal scalars.  The implication "selected representatives price the class" is
not the main target here; the premise being tested is whether all-tail
challengers remain covered, injective enough, and non-omitted under alternate
presentations of the same local E22 construction.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Any


sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "experiments" / "falsification_pruning"))

from e22_tail_only_pricing_coverage import (  # noqa: E402
    DEFAULT_ROWS,
    analyze_cell,
    parse_row,
)


DEFAULT_LAYOUTS = ("cyclic_step_1", "cyclic_step_3", "cyclic_step_5", "shuffle_17")
DEFAULT_SCALARS = ("linear", "geometric")


def write_checkpoint(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    tmp.replace(path)


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    totals = Counter()
    by_mode: dict[str, Counter] = {}
    for row in rows:
        key = f"{row['layout']}|{row['scalar_mode']}"
        by_mode.setdefault(key, Counter())
        for counter in (totals, by_mode[key]):
            counter["cells"] += 1
            counter["structured"] += row["structured"]
            counter["missing_selected_representative"] += row["missing_selected_representative"]
            counter["representative_collision_count"] += row["representative_collision_count"]
            counter["representative_collision_polynomial_excess"] += row[
                "representative_collision_polynomial_excess"
            ]
            counter["support_collision_count"] += row["support_collision_count"]
            counter["support_collision_polynomial_excess"] += row[
                "support_collision_polynomial_excess"
            ]
            counter["tail_only_representatives"] += row["tail_only_representatives"]
            counter["with_full_fiber_representatives"] += row["with_full_fiber_representatives"]
    return {
        "totals": dict(totals),
        "by_mode": {key: dict(counter) for key, counter in sorted(by_mode.items())},
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    started = time.time()
    deadline = started + args.seconds
    rows = args.row or list(DEFAULT_ROWS)
    layouts = args.layout or list(DEFAULT_LAYOUTS)
    scalar_modes = args.scalar_mode or list(DEFAULT_SCALARS)
    payload: dict[str, Any] = {
        "node": "e22_challenger_staircase_pricing",
        "downstream_premise_for": [
            "e22_common_tail_invariance_payload",
            "e22_cofactor_common_tail_kernel_invariance",
        ],
        "obligation_attacked": (
            "whether vacuous all-tail common-tail certificates remain covered "
            "by dyadic minimal-scale pricing under alternate sunflower layouts "
            "and petal scalar choices"
        ),
        "parameters": {
            "rows": [list(row) for row in rows],
            "layouts": layouts,
            "scalar_modes": scalar_modes,
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
                if time.time() > deadline - 2:
                    payload["summary"] = summarize(payload["rows"])
                    payload["elapsed_seconds"] = time.time() - started
                    payload["verdict"] = "TIMEOUT_PARTIAL"
                    write_checkpoint(args.output, payload)
                    return payload
                cell = analyze_cell(n, k, sigma, layout, scalar_mode, args.max_examples)
                payload["rows"].append(cell)
                payload["summary"] = summarize(payload["rows"])
                write_checkpoint(args.output, payload)

    payload["summary"] = summarize(payload["rows"])
    totals = payload["summary"]["totals"]
    if totals.get("missing_selected_representative", 0):
        payload["verdict"] = "ALL_TAIL_PRICING_OMISSION_CANDIDATE"
    elif totals.get("representative_collision_count", 0):
        payload["verdict"] = "SELECTED_REPRESENTATIVE_COLLISION_CANDIDATE"
    elif totals.get("structured", 0) and not totals.get("with_full_fiber_representatives", 0):
        payload["verdict"] = "ALL_STRUCTURED_CHALLENGERS_TAIL_ONLY_BUT_SELECTED"
    elif totals.get("structured", 0):
        payload["verdict"] = "STRUCTURED_CHALLENGERS_SELECTED_ACROSS_MODES"
    else:
        payload["verdict"] = "NO_STRUCTURED_CHALLENGERS_IN_SCOPE"
    payload["elapsed_seconds"] = time.time() - started
    write_checkpoint(args.output, payload)
    return payload


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=55.0)
    parser.add_argument("--row", action="append", type=parse_row)
    parser.add_argument("--layout", action="append")
    parser.add_argument("--scalar-mode", action="append")
    parser.add_argument("--max-examples", type=int, default=4)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/falsification_pruning/results/e22_all_tail_mode_sweep.json"),
    )
    return parser


def main() -> None:
    print(json.dumps(run(make_parser().parse_args()), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
