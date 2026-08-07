#!/usr/bin/env python3
"""Verify all literal logarithmic-denominator branch exclusions."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent / (
    "rate_half_kb_m2_r4_diagonal_c2_112_full_j_log_derivative_branch_router/"
    "modal_literal_denominator_intersections_output.json"
)
OUTPUT_SHA256 = "c488efd799114d95ee92561870d6cdad534d338a9e14604fe5679ec8e6cb5d35"
EXPECTED = {
    ("R02", 0): ([7, 7], 25, 1010, 17, 14),
    ("R02", 1): ([11, 11], 60, 12236, 36, 15),
    ("R20", 0): ([7, 7], 28, 1443, 22, 14),
    ("R20", 1): ([11, 11], 62, 12318, 45, 15),
}


def main() -> None:
    raw = OUTPUT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == OUTPUT_SHA256
    payload = json.loads(raw)
    assert payload["counts"] == {
        "FAIL": 0,
        "PASS": 12,
        "REMOTE_ERROR": 0,
        "TIMEOUT": 0,
    }
    assert {
        (row["assignment"], row["target"], row["pair_index"])
        for row in payload["results"]
    } == {
        (assignment, target, pair_index)
        for assignment in ("F05", "F06", "F07")
        for target in ("R02", "R20")
        for pair_index in (0, 1)
    }
    for row in payload["results"]:
        assert row["status"] == "PASS" and row["returncode"] == 0
        expected = EXPECTED[(row["target"], row["pair_index"])]
        compiled = next(
            record for record in row["records"] if record["phase"] == "BRANCH_COMPILED"
        )
        assert compiled["source_degrees"] == expected[0]
        assert compiled["essential_pair"]["degree"] == expected[1]
        assert compiled["essential_pair"]["terms"] == expected[2]
        done = next(record for record in row["records"] if record["phase"] == "DONE")
        assert done["cell"] == f"{row['assignment']}-{row['target']}"
        assert done["basis_size"] == expected[3]
        assert done["dimension"] == 1 and not done["unit_ideal"]
        assert done["localizer_nilpotence_index"] == 1
        assert done["terminal"] == "FULL_J_LOG_DENOMINATOR_UNION_EMPTY"
        assert len(done["localizer_steps"]) == expected[4]
        assert all(not step["zero"] for step in done["localizer_steps"][:-1])
        assert done["localizer_steps"][-1]["zero"]
    print("KB_C2_112_FIXED_LITERAL_LOG_DENOMINATOR_EXCLUSIONS_PASS cells=6 unions=12")


if __name__ == "__main__":
    main()
