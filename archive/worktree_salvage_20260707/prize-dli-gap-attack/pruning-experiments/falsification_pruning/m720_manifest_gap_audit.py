#!/usr/bin/env python3
"""Audit M720 official norm-gate manifest coverage versus available evidence.

This is a premise stress test for the downstream amber M720 chain.  The amber
implications accept an actual complete official manifest; this script checks
which configured official-shape rows are complete certificates, which are
closed by the over-ceiling algebraic certificate, which have only slice
evidence, and which have not even been slice-probed in this worktree.
"""

from __future__ import annotations

import argparse
import json
from math import comb
from pathlib import Path
from typing import Any


COUNT_CEILING = 6_000_000
OFFICIAL_N = (16, 32, 64, 128, 256, 1024)
Q_EXPS = (2, 3)
H_RANGE = range(7, 21)
COMPLETE_UNDER = {
    (16, 7, 2),
    (16, 7, 3),
    (32, 7, 2),
    (32, 7, 3),
    (16, 8, 2),
    (16, 8, 3),
}
OVER_CEILING_COMPLETE = {
    (32, 16, 2),
    (32, 16, 3),
}


def chosen_window(n: int, h: int, count_ceiling: int = COUNT_CEILING) -> tuple[int, int]:
    best = 2 * h
    best_cost = comb(best - 1, h - 1) + comb(best, h)
    w = 2 * h
    while w <= n:
        cost = comb(w - 1, h - 1) + comb(w, h)
        if cost <= count_ceiling:
            best = w
            best_cost = cost
            w += 1
        else:
            break
    return best, best_cost


def load_slice_rows(paths: list[Path]) -> dict[tuple[int, int, int], list[dict[str, Any]]]:
    rows: dict[tuple[int, int, int], list[dict[str, Any]]] = {}
    for path in paths:
        if not path.exists():
            continue
        data = json.loads(path.read_text())
        for row in data.get("rows", []):
            if "n" not in row or "h" not in row or "q_exp" not in row:
                continue
            key = (int(row["n"]), int(row["h"]), int(row["q_exp"]))
            payload = dict(row)
            payload["source"] = str(path)
            rows.setdefault(key, []).append(payload)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--result",
        action="append",
        type=Path,
        default=[
            Path("experiments/falsification_pruning/results/m720_modal_slice_probe.json"),
            Path("experiments/falsification_pruning/results/m720_modal_slice_probe_h8_10.json"),
        ],
        help="M720 Modal slice result JSON to include in the audit.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/falsification_pruning/results/m720_manifest_gap_audit.json"),
    )
    args = parser.parse_args()

    slice_rows = load_slice_rows(args.result)
    official_rows: list[dict[str, Any]] = []
    counts = {
        "official_rows": 0,
        "complete_under_ceiling_certified": 0,
        "over_ceiling_algebraic_certified": 0,
        "slice_probed_no_nontoral": 0,
        "slice_probed_with_nontoral": 0,
        "not_slice_probed": 0,
    }
    nontoral_rows = []
    unprobed = []

    for h in H_RANGE:
        for n in OFFICIAL_N:
            if n < 2 * h:
                continue
            for q_exp in Q_EXPS:
                key = (n, h, q_exp)
                w, cost = chosen_window(n, h)
                records = slice_rows.get(key, [])
                status: str
                if key in COMPLETE_UNDER:
                    status = "complete_under_ceiling_certified"
                elif key in OVER_CEILING_COMPLETE:
                    status = "over_ceiling_algebraic_certified"
                elif records and any(int(r.get("anchored_nontoral", 0)) > 0 for r in records):
                    status = "slice_probed_with_nontoral"
                    nontoral_rows.append(key)
                elif records:
                    status = "slice_probed_no_nontoral"
                else:
                    status = "not_slice_probed"
                    unprobed.append(key)
                counts[status] += 1
                counts["official_rows"] += 1
                official_rows.append(
                    {
                        "n": n,
                        "h": h,
                        "q_exp": q_exp,
                        "modal_policy_W": w,
                        "modal_policy_cost": cost,
                        "complete_under_modal_policy": w == n,
                        "status": status,
                        "slice_records": [
                            {
                                "source": r.get("source"),
                                "W": r.get("W"),
                                "complete": r.get("complete"),
                                "aborted": r.get("aborted"),
                                "anchored_nontoral": r.get("anchored_nontoral"),
                                "anchored_toral": r.get("anchored_toral"),
                            }
                            for r in records
                        ],
                    }
                )

    suggested_next = [
        {"n": n, "h": h, "q_exp": q_exp}
        for n, h, q_exp in unprobed
        if n == 1024 and h in (7, 8, 9)
    ][:6]
    if len(suggested_next) < 6:
        suggested_next.extend(
            {"n": n, "h": h, "q_exp": q_exp}
            for n, h, q_exp in unprobed
            if n in (64, 128, 256) and h in (8, 9, 10, 11)
        )
        suggested_next = suggested_next[:6]

    verdict = (
        "MANIFEST_PREMISE_FALSIFIED_BY_NONTORAL_SLICE_WITNESS"
        if nontoral_rows
        else "OFFICIAL_MANIFEST_PREMISE_UNSATISFIED_IN_WORKTREE"
        if unprobed
        else "ALL_OFFICIAL_ROWS_HAVE_CERTIFICATE_OR_SLICE_EVIDENCE"
    )
    payload = {
        "node": "m720_official_norm_gate_case_manifest_payload",
        "downstream_amber_nodes": [
            "m720_official_h7_20_norm_gate_payload",
            "m720_official_h7_20_norm_gate_certificates",
            "m720_official_exclusion",
        ],
        "obligation_attacked": "actual complete official manifest premise, not the proved manifest-to-payload implication",
        "count_ceiling": COUNT_CEILING,
        "source_results": [str(path) for path in args.result if path.exists()],
        "counts": counts,
        "nontoral_rows": [list(row) for row in nontoral_rows],
        "suggested_next_slice_configs": suggested_next,
        "rows": official_rows,
        "verdict": verdict,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: payload[k] for k in ("verdict", "counts", "suggested_next_slice_configs")}, indent=2))


if __name__ == "__main__":
    main()
