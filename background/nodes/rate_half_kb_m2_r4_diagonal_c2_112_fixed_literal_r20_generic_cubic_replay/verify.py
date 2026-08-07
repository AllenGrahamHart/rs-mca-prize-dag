#!/usr/bin/env python3
"""Verify the literal F06-R20 generic cubic classification."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent / (
    "rate_half_kb_m2_r4_diagonal_c2_112_fixed_literal_r02_generic_cubic_replay/"
    "modal_literal_f06_r20_cubic_factor_replay_output.json"
)
OUTPUT_SHA256 = "f74085f14f9d29e3cd2a4b48b26bff8e93932cf3010c02ebb83fec548f7d6731"
EXPECTED = {
    0: {
        "factor_hash": "9dee8f7040029003d057202727fd2e747735521d8e246ca21691d4e45eb423be",
        "basis_size": 45,
        "basis_hash": "b718cf1ce737487960ad970f9c64bd0fc05fc7dcf6b666cd1e63fcdfb62e84d2",
        "nilpotence": 1,
        "terminal": "GENERIC_RESULTANT_FACTOR_EMPTY_AFTER_LOCALIZATION",
    },
    1: {
        "factor_hash": "a8fe7e86764442a43197e17bbf88450309657adb9840f94878719b0a82fd5554",
        "basis_size": 46,
        "basis_hash": "ecdbdbb6518d5f1c007ba72e8662b559dc14e5caca260d66621bd2370383fea8",
        "nilpotence": None,
        "terminal": "GENERIC_RESULTANT_FACTOR_SURVIVES"
    }
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
        assert done["cell"] == "F06-R20"
        assert done["dimension"] == 1 and not done["unit_ideal"]
        assert done["basis_size"] == expected["basis_size"]
        assert done["basis_sha256"] == expected["basis_hash"]
        assert done["localizer_nilpotence_index"] == expected["nilpotence"]
        assert done["terminal"] == expected["terminal"]
    empty = next(row for row in payload["results"] if row["factor_index"] == 0)
    empty_done = next(record for record in empty["records"] if record["phase"] == "DONE")
    assert len(empty_done["localizer_steps"]) == 15
    assert all(not step["zero"] for step in empty_done["localizer_steps"][:-1])
    assert empty_done["localizer_steps"][-1]["zero"]
    print("KB_C2_112_FIXED_LITERAL_F06_R20_CUBIC_REPLAY_PASS empty=1 surviving=1")


if __name__ == "__main__":
    main()
