#!/usr/bin/env python3
"""Verify the complete cell-5 parallel-DE source census."""

import collections
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
NORM = EXP / "rate_half_kb_positive_433_1b_cell5_parallel_de_four_basis_norm_result.json"
REPLAY = EXP / "rate_half_kb_positive_433_1b_cell5_parallel_de_four_basis_replay_result.json"
NORM_SHA = "9242ebeebf28e09fdb66475983864433462896d416c5463ea081a2c75a9bdf98"
REPLAY_SHA = "010dd87bb6d253e0ad6a33aafe4b4e387538d68720f316918faafa418bc42e14"


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
        (-1, 1), (-1, 1), ("opposite", "equal_negative")
    ))
    rows = {(*row["epsilon"], row["cut_kind"]): row for row in norm["rows"]}
    require(set(rows) == expected and len(norm["rows"]) == 8,
            "norm row keys")
    for row in rows.values():
        opposite = row["cut_kind"] == "opposite"
        require(row["status"] == "COMPLETE"
                and len(row["candidate_roots"]) == (13 if opposite else 15),
                "complete norm roots")
        require(row["target_norm"]["numerator"]["degree"]
                == (272 if opposite else 284)
                and row["target_norm"]["denominator"]["degree"]
                == (144 if opposite else 148), "norm degree")

    replay = json.loads(REPLAY.read_text())
    require(len(replay["rows"]) == 8, "replay row count")
    candidates = finite = boundaries = no_lift = witnesses = 0
    finite_status = collections.Counter()
    for row in replay["rows"]:
        opposite = row["cut_kind"] == "opposite"
        require(row["status"] == "COMPLETE" and not row["unresolved"],
                "complete direct replay")
        require(row["candidate_root_count"] == (13 if opposite else 15)
                and len(row["witnesses"]) == (0 if opposite else 2),
                "source census")
        require(all(point["cut"] == 0 and point["missing"] != 0
                    for point in row["witnesses"]), "ordinary zeros")
        candidates += row["candidate_root_count"]
        finite += len(row["finite_rows"])
        boundaries += len(row["route_boundary"])
        no_lift += len(row["no_lift"])
        witnesses += len(row["witnesses"])
        finite_status.update(point["status"] for point in row["finite_rows"])
    require((candidates, finite, boundaries, no_lift, witnesses)
            == (112, 112, 72, 56, 8), "aggregate census")
    require(finite_status == collections.Counter({
        "NONZERO": 88, "MISSING_IMPOSSIBLE": 16, "ZERO": 8,
    }), "finite classification")
    print("PASS cell-5 parallel-DE source census: candidates=112 zeros=8 unresolved=0")


if __name__ == "__main__":
    main()
