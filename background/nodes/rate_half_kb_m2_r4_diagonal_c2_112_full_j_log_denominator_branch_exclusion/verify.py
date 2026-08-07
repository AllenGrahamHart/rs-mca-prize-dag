#!/usr/bin/env python3
"""Verify the four logarithmic-denominator branch exclusions."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent / (
    "rate_half_kb_m2_r4_diagonal_c2_112_full_j_log_derivative_branch_router/"
    "modal_denominator_intersections_output.json"
)
OUTPUT_SHA256 = "758e8481ee1875e7ae7b62b6385839e1c899b253885bdc72c091dda88a2e89c6"
EXPECTED = {
    ("R02", 0): ("F04-R02", [7, 7], 25, 1010, 17, 14),
    ("R02", 1): ("F04-R02", [11, 11], 60, 12236, 36, 15),
    ("R20", 0): ("F04-R20", [7, 7], 28, 1443, 22, 14),
    ("R20", 1): ("F04-R20", [11, 11], 62, 12318, 45, 15),
}


def main() -> None:
    raw = OUTPUT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == OUTPUT_SHA256
    payload = json.loads(raw)
    assert payload["counts"] == {
        "FAIL": 0,
        "PASS": 4,
        "REMOTE_ERROR": 0,
        "TIMEOUT": 0,
    }
    assert {(row["target"], row["pair_index"]) for row in payload["results"]} == set(EXPECTED)
    for row in payload["results"]:
        assert row["status"] == "PASS"
        expected = EXPECTED[(row["target"], row["pair_index"])]
        compiled = next(
            record for record in row["records"] if record["phase"] == "BRANCH_COMPILED"
        )
        assert compiled["source_degrees"] == expected[1]
        assert (
            compiled["essential_pair"]["degree"],
            compiled["essential_pair"]["terms"],
        ) == expected[2:4]
        done = next(record for record in row["records"] if record["phase"] == "DONE")
        assert done["cell"] == expected[0]
        assert done["source_degrees"] == expected[1]
        assert done["basis_size"] == expected[4]
        assert done["dimension"] == 1
        assert not done["unit_ideal"]
        assert done["localizer_nilpotence_index"] == 1
        assert done["terminal"] == "FULL_J_LOG_DENOMINATOR_UNION_EMPTY"
        steps = done["localizer_steps"]
        assert len(steps) == expected[5]
        assert all(not step["zero"] for step in steps[:-1])
        assert steps[-1]["zero"]
    print(
        "KB_C2_112_FULL_J_LOG_DENOMINATOR_EXCLUSIONS_PASS "
        "targets=2 unions=4 remaining=guarded_degree67"
    )


if __name__ == "__main__":
    main()
