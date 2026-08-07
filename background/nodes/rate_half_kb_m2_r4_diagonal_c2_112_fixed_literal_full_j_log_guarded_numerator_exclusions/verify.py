#!/usr/bin/env python3
"""Verify the three completed literal guarded-numerator exclusions."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROUTER = HERE.parent / "rate_half_kb_m2_r4_diagonal_c2_112_full_j_log_derivative_branch_router"
BATCH = ROUTER / "modal_literal_guarded_numerator_intersections_output.json"
RETRY = ROUTER / "modal_f07_r02_guarded_numerator_retry_output.json"
BATCH_SHA256 = "5f1ea688ab3a8ca66cdcfa0343673588c4f60bf70925b24808bf8ed32a1bbcce"
RETRY_SHA256 = "d78864704fa48cfe08bcf69716b8c0d5c04d244737a820324da64edb949d0cdf"
EXPECTED = {
    ("F05", "R02"): {
        "numerator": (162322, "53840fd67dca97c6a4796d20e8b1ab429e691d3be612fb5b5db6b588bf8fcb1d"),
        "route": (37, "7f7321aba1adbfa60467c6a88cd1c1cc250906525099fa5a622b2691a5848ade"),
        "remainder": (39, [11, 38, 38], 1885, "06e3734ff7c689b6d4f6030d48016986a001bc67acbaf3cb4095abe0bc55524d"),
        "final": (36, "57014dbcdc560aeb4ce69e9d02668697b6b116455a090e95861398e8eda4e5c7"),
    },
    ("F07", "R02"): {
        "numerator": (162321, "d01eab14c3ee14cd64d080d31da94652aeca38ce29186c93bf45ff195394c6e7"),
        "route": (37, "f7c392dcc74ba6fc000b39bb0b18da96015f09c9726f2934d8ff2e3f41d75284"),
        "remainder": (39, [11, 38, 38], 1890, "bf0428a52b4bedaf6745d33bdc7784af3211f52d279455fdad0cfb71bccdaba1"),
        "final": (35, "5843a13583728958a013a0f3aeb838341cd30700983212f0835f7c9f53066566"),
    },
    ("F06", "R20"): {
        "numerator": (162321, "e199230fd30348f6a283c6ec83de3bbc031dd3db55651e79bd368d41cb5d2386"),
        "route": (46, "ecdbdbb6518d5f1c007ba72e8662b559dc14e5caca260d66621bd2370383fea8"),
        "remainder": (41, [7, 40, 40], 1945, "cab7da4a1137c1d2a5bbcce4785b5661f55e3f59cfcd79b67a908e04d00bb3dd"),
        "final": (44, "253f131c1db509ec5f46f624c27a90a91158b5b06e745e1abb59b618a7c17fbd"),
    },
}


def verify_row(row: dict[str, object]) -> None:
    key = (row["assignment"], row["target"])
    expected = EXPECTED[key]
    assert row["status"] == "PASS" and row["returncode"] == 0
    compiled = next(record for record in row["records"] if record["phase"] == "NUMERATOR_COMPILED")
    numerator = compiled["descended"]
    assert numerator["degree"] == 67 and numerator["degrees"] == [34, 24, 24, 15]
    assert (numerator["terms"], numerator["sha256"]) == expected["numerator"]
    route = next(record for record in row["records"] if record["phase"] == "BASE_GROEBNER_DONE")
    assert (route["basis_size"], route["basis_sha256"]) == expected["route"]
    assert route["dimension"] == 1
    horner = [record for record in row["records"] if record["phase"] == "HORNER_STEP"]
    assert [record["coefficient_index"] for record in horner] == list(range(14, -1, -1))
    reduced = next(record for record in row["records"] if record["phase"] == "NUMERATOR_REDUCED")
    remainder = reduced["remainder"]
    assert reduced["numerator_w_degree"] == 15
    assert (
        remainder["degree"],
        remainder["degrees"],
        remainder["terms"],
        remainder["sha256"],
    ) == expected["remainder"]
    done = next(record for record in row["records"] if record["phase"] == "DONE")
    assert done["cell"] == f"{key[0]}-{key[1]}"
    assert (done["basis_size"], done["basis_sha256"]) == expected["final"]
    assert done["dimension"] == 1 and not done["unit_ideal"]
    assert done["localizer_nilpotence_index"] == 1
    assert len(done["localizer_steps"]) == 15
    assert all(not step["zero"] for step in done["localizer_steps"][:-1])
    assert done["localizer_steps"][-1]["zero"]
    assert done["terminal"] == "FULL_J_LOG_GUARDED_NUMERATOR_INTERSECTION_EMPTY"


def main() -> None:
    assert hashlib.sha256(BATCH.read_bytes()).hexdigest() == BATCH_SHA256
    assert hashlib.sha256(RETRY.read_bytes()).hexdigest() == RETRY_SHA256
    batch = json.loads(BATCH.read_text())
    retry = json.loads(RETRY.read_text())
    assert batch["counts"] == {"FAIL": 0, "PASS": 2, "REMOTE_ERROR": 0, "TIMEOUT": 4}
    assert retry["counts"] == {"FAIL": 0, "PASS": 1, "REMOTE_ERROR": 0, "TIMEOUT": 0}
    batch_passes = [row for row in batch["results"] if row["status"] == "PASS"]
    batch_timeouts = [row for row in batch["results"] if row["status"] == "TIMEOUT"]
    assert {(row["assignment"], row["target"]) for row in batch_passes} == {
        ("F05", "R02"),
        ("F06", "R20"),
    }
    assert {(row["assignment"], row["target"]) for row in batch_timeouts} == {
        ("F05", "R20"),
        ("F06", "R02"),
        ("F07", "R02"),
        ("F07", "R20"),
    }
    rows = [*batch_passes, retry["results"][0]]
    assert {(row["assignment"], row["target"]) for row in rows} == set(EXPECTED)
    for row in rows:
        verify_row(row)
    print("KB_C2_112_FIXED_LITERAL_GUARDED_NUMERATOR_EXCLUSIONS_PASS cells=3")


if __name__ == "__main__":
    main()
