#!/usr/bin/env python3
"""Verify the two guarded logarithmic-numerator exclusions."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent / (
    "rate_half_kb_m2_r4_diagonal_c2_112_full_j_log_derivative_branch_router/"
    "modal_guarded_numerator_intersections_output.json"
)
OUTPUT_SHA256 = "583bc9272c8ea28fe1ffc3d32c93b38ba9b18f0e100e506307187b25b0165865"
NUMERATOR = {
    "degree": 67,
    "degrees": [34, 24, 24, 15],
    "sha256": "57f0d18de937af8c9bebb7e59b079861571ecd9cdf156f3fa4d0ab574331437e",
    "terms": 162322,
}
EXPECTED = {
    "R02": {
        "route_size": 36,
        "route_hash": "1e92618798e4de21c02240c1fa130bb444cfabfc9faa13ce1e04097289b88268",
        "remainder": {
            "degree": 39,
            "degrees": [10, 37, 37],
            "sha256": "065c9dfea5c30ca176bd38d67016e0b5521cfad7f8d0d7ce89d039306bef9504",
            "terms": 1788,
        },
        "final_size": 35,
        "final_hash": "834050982576bf5911b0b0e617062457daedad1bc7929dfe790fb70cc4aec0cf",
    },
    "R20": {
        "route_size": 46,
        "route_hash": "5eac3b6c1b26d29ebe7763534d3a39473409b2552dac175500508f3d0b1e887c",
        "remainder": {
            "degree": 41,
            "degrees": [7, 40, 40],
            "sha256": "c9b9b33ff33d97b09e8f28174c23fd97cee1eef2de3a63ae9e621c5f646c3f5d",
            "terms": 1945,
        },
        "final_size": 44,
        "final_hash": "15ed43f6af501c70ce289631c7dfed477fd2372cd87e1400a8e8e473d09f61b2",
    },
}


def main() -> None:
    raw = OUTPUT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == OUTPUT_SHA256
    payload = json.loads(raw)
    assert payload["counts"] == {
        "FAIL": 0,
        "PASS": 2,
        "REMOTE_ERROR": 0,
        "TIMEOUT": 0,
    }
    assert {row["target"] for row in payload["results"]} == set(EXPECTED)
    for row in payload["results"]:
        assert row["status"] == "PASS" and row["returncode"] == 0
        expected = EXPECTED[row["target"]]
        compiled = next(
            record for record in row["records"] if record["phase"] == "NUMERATOR_COMPILED"
        )
        assert compiled["descended"] == NUMERATOR
        route = next(
            record for record in row["records"] if record["phase"] == "BASE_GROEBNER_DONE"
        )
        assert route["basis_size"] == expected["route_size"]
        assert route["basis_sha256"] == expected["route_hash"]
        assert route["dimension"] == 1
        horner = [record for record in row["records"] if record["phase"] == "HORNER_STEP"]
        assert [record["coefficient_index"] for record in horner] == list(range(14, -1, -1))
        reduced = next(
            record for record in row["records"] if record["phase"] == "NUMERATOR_REDUCED"
        )
        assert reduced["numerator_w_degree"] == 15
        assert reduced["remainder"] == expected["remainder"]
        done = next(record for record in row["records"] if record["phase"] == "DONE")
        assert done["cell"] == f"F04-{row['target']}"
        assert done["numerator_remainder"] == expected["remainder"]
        assert done["basis_size"] == expected["final_size"]
        assert done["basis_sha256"] == expected["final_hash"]
        assert done["dimension"] == 1 and not done["unit_ideal"]
        assert len(done["localizer_steps"]) == 15
        assert all(not step["zero"] for step in done["localizer_steps"][:-1])
        assert done["localizer_steps"][-1]["zero"]
        assert done["localizer_nilpotence_index"] == 1
        assert done["terminal"] == "FULL_J_LOG_GUARDED_NUMERATOR_INTERSECTION_EMPTY"
    print("KB_C2_112_FULL_J_LOG_GUARDED_NUMERATOR_EXCLUSIONS_PASS targets=R02,R20")


if __name__ == "__main__":
    main()
