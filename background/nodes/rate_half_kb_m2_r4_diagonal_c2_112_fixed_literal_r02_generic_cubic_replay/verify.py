#!/usr/bin/env python3
"""Verify the literal F07-R02 generic cubic classification."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "modal_literal_r02_cubic_factor_replay_output.json"
OUTPUT_SHA256 = "73812373a485e16c5f5c46a0114e4f14a608a8e4a75367f00d29a0b6fa380cca"
EXPECTED = {
    0: {
        "factor_hash": "f0ada7de5b011ea3b4990e53ec1ba4aa62f7b10b1a21ec9ffbfad4052636cc46",
        "basis_size": 37,
        "basis_hash": "f7c392dcc74ba6fc000b39bb0b18da96015f09c9726f2934d8ff2e3f41d75284",
        "nilpotence": None,
        "terminal": "GENERIC_RESULTANT_FACTOR_SURVIVES",
    },
    1: {
        "factor_hash": "3cfefebb68ea5b83e036ccf4d80d84da335c883f743ddeb890d14a00ec5d026a",
        "basis_size": 36,
        "basis_hash": "ba6c62c222a580ff4a25ae3642db735ef45245c1d5036e8f88e9a8661cd9c287",
        "nilpotence": 1,
        "terminal": "GENERIC_RESULTANT_FACTOR_EMPTY_AFTER_LOCALIZATION",
    },
}


def main() -> None:
    raw = OUTPUT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == OUTPUT_SHA256
    payload = json.loads(raw)
    assert payload["counts"] == {"FAIL": 0, "PASS": 2, "REMOTE_ERROR": 0}
    assert {row["factor_index"] for row in payload["results"]} == {0, 1}
    for row in payload["results"]:
        assert row["status"] == "PASS" and row["returncode"] == 0
        expected = EXPECTED[row["factor_index"]]
        branch = next(record for record in row["records"] if record["phase"] == "BRANCH")
        assert branch["resultant_factor_count"] == 3
        assert branch["selected"]["degree"] == 3
        assert branch["selected"]["sha256"] == expected["factor_hash"]
        assert branch["transported_unit_factor_count"] == 24
        done = next(record for record in row["records"] if record["phase"] == "DONE")
        assert done["cell"] == "F07-R02"
        assert done["dimension"] == 1 and not done["unit_ideal"]
        assert done["basis_size"] == expected["basis_size"]
        assert done["basis_sha256"] == expected["basis_hash"]
        assert done["localizer_nilpotence_index"] == expected["nilpotence"]
        assert done["terminal"] == expected["terminal"]
    empty = next(row for row in payload["results"] if row["factor_index"] == 1)
    empty_done = next(record for record in empty["records"] if record["phase"] == "DONE")
    assert len(empty_done["localizer_steps"]) == 15
    assert all(not step["zero"] for step in empty_done["localizer_steps"][:-1])
    assert empty_done["localizer_steps"][-1]["zero"]
    print("KB_C2_112_FIXED_LITERAL_F07_R02_CUBIC_REPLAY_PASS empty=1 surviving=1")


if __name__ == "__main__":
    main()
