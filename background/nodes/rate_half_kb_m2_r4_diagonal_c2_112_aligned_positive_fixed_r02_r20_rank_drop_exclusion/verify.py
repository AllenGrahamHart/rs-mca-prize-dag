#!/usr/bin/env python3
"""Fail-closed verifier for all remaining fixed rank-drop branches."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
LEDGER = (
    HERE.parent
    / "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_balanced_quadratic_branch_reduction"
    / "modal_rank_drop_remaining_all_output.json"
)
EXPECTED_SHA256 = "08942c31836a0e7ae9da7a1c2644bceeb2f144b59b70febf0f47837d643b3835"
CELLS = tuple(
    f"{assignment}-{target}"
    for assignment in ("F04", "F05", "F06", "F07")
    for target in ("R02", "R20")
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def done(row: dict[str, object]) -> dict[str, object]:
    records = [record for record in row["records"] if record.get("phase") == "DONE"]
    require(len(records) == 1, "one DONE record")
    return records[0]


def check(data: dict[str, object]) -> None:
    require(data["upstream_commit"] == "55ac3e07477bd7a768190a3e755f22b0d44354b0", "commit")
    require(data["counts"] == {"FAIL": 0, "PASS": 16, "REMOTE_ERROR": 0, "TIMEOUT": 0}, "counts")
    require({(row["cell"], row["factor_index"]) for row in data["results"]} == {(cell, index) for cell in CELLS for index in (0, 1)}, "case census")
    for row in data["results"]:
        require(row["status"] == "PASS" and row["prime"] == 2130706433, "status")
        branch = next(record for record in row["records"] if record.get("phase") == "BRANCH")
        terminal = done(row)
        expected_degree = 2 if row["factor_index"] == 0 else (11 if row["cell"].endswith("R02") else 14)
        require(branch["nonnamed_v_factor_count"] == 2, "factor count")
        require(branch["selected"]["degree"] == expected_degree, "factor degree")
        require(terminal["dimension"] == 2, "dimension")
        require(terminal["localizer_nilpotence_index"] == 2, "nilpotence")
        require(terminal["terminal"] == "RANK_DROP_FACTOR_EMPTY_AFTER_NAMED_LOCALIZATION", "terminal")


def main() -> None:
    require(hashlib.sha256(LEDGER.read_bytes()).hexdigest() == EXPECTED_SHA256, "ledger hash")
    data = json.loads(LEDGER.read_text())
    check(data)
    hostile = copy.deepcopy(data)
    done(hostile["results"][0])["localizer_nilpotence_index"] = None
    try:
        check(hostile)
    except AssertionError:
        pass
    else:
        raise AssertionError("nilpotence mutation accepted")
    print("KB_C2_112_FIXED_R02_R20_RANK_DROP_PASS cells=8 branches=16 mutations=1/1")


if __name__ == "__main__":
    main()
