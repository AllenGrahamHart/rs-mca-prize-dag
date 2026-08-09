#!/usr/bin/env python3
"""Verify the complete cell-9 parallel-DE source census."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
NORM = EXP / "rate_half_kb_positive_433_1b_cell9_parallel_de_four_basis_norm_result.json"
REPLAY = EXP / "rate_half_kb_positive_433_1b_cell9_parallel_de_four_basis_replay_result.json"
NULL = EXP / "rate_half_kb_positive_433_1b_cell9_kernel_null_residual_result.json"
NORM_SHA = "0f1fabaca62173105aa9ea6256a705996fb70b1eff6735013966ad6b04afa34e"
REPLAY_SHA = "f0689375b5d904288bf0f79af077d028eacef4204850ddde47ed5e0f9ed65690"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    require(hashlib.sha256(NORM.read_bytes()).hexdigest() == NORM_SHA,
            "norm hash")
    require(hashlib.sha256(REPLAY.read_bytes()).hexdigest() == REPLAY_SHA,
            "replay hash")
    norm = json.loads(NORM.read_text())
    expected = set(itertools.product(
        (-1, 1), (-1, 1), (2, 3), (4, 5, 6), ("positive", "negative")
    ))
    rows = {
        (*row["epsilon"], row["b_row_index"], row["c_row_index"],
         row["cut_kind"]): row for row in norm["rows"]
    }
    require(set(rows) == expected and len(norm["rows"]) == 48,
            "norm chart keys")
    for row in rows.values():
        expected_roots = 11 if row["cut_kind"] == "positive" else 13
        expected_degree = 394 if row["cut_kind"] == "positive" else 406
        require(row["status"] == "COMPLETE"
                and row["source_root_count"] == expected_roots,
                "complete norm roots")
        require(row["source_norm"]["numerator"]["degree"] == expected_degree
                and row["source_norm"]["denominator"]["degree"] == 284,
                "norm degree")

    replay = json.loads(REPLAY.read_text())
    require(len(replay["rows"]) == 8, "replay row count")
    candidates = witnesses = missing_free = 0
    null_payload = json.loads(NULL.read_text())
    null_points = {
        tuple(row["point"][key] for key in ("r", "t", "b", "c"))
        for row in null_payload["rows"]
    }
    for row in replay["rows"]:
        expected_witnesses = 4 if row["cut_kind"] == "positive" else 2
        require(row["status"] == "COMPLETE" and not row["unresolved"],
                "complete direct replay")
        require(row["chart_source_root_sets_equal"], "chart root agreement")
        require(len(row["witnesses"]) == expected_witnesses
                and len(row["missing_free"]) == 2, "source census")
        for point in row["missing_free"]:
            require(tuple(point[key] for key in ("r", "t", "b", "c"))
                    in null_points, "base-point custody")
        candidates += row["candidate_root_count"]
        witnesses += len(row["witnesses"])
        missing_free += len(row["missing_free"])
    require((candidates, witnesses, missing_free) == (160, 24, 16),
            "aggregate census")
    print("PASS cell-9 parallel-DE source census: candidates=160 zeros=24 base=16")


if __name__ == "__main__":
    main()
