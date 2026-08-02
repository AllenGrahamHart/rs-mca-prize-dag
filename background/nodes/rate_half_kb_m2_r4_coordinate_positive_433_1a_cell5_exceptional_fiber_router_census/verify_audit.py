#!/usr/bin/env python3
"""Scope and hostile-mutation audit for the finite router."""

import json
import subprocess
import sys
import tempfile
from pathlib import Path


HERE = Path(__file__).parent
ROOT = HERE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
statement = " ".join((HERE / "statement.md").read_text().split())
contract = " ".join((HERE / "claim_contract.md").read_text().split())
assert "exactly 69 deployed-field values" in statement
assert "does not exclude any of the 69" in statement
assert "No assertion that any of the 69" in contract


def rejected(command, payload):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
        json.dump(payload, handle)
        handle.flush()
        process = subprocess.run(
            [sys.executable, *command, handle.name],
            capture_output=True,
            text=True,
            timeout=30,
        )
    assert process.returncode != 0


guard_result = json.loads(
    (EXPERIMENTS / "rate_half_kb_positive_433_1a_cell5_pair_guard_norms_result.json").read_text()
)
guard_result[0]["records"][0]["numerator_roots"].append(2)
rejected(
    [
        str(EXPERIMENTS / "check_rate_half_kb_positive_433_1a_cell5_pair_guard_norms.py"),
        "--result",
    ],
    guard_result,
)

pole_result = json.loads(
    (EXPERIMENTS / "rate_half_kb_positive_433_1a_cell5_specialization_poles_result.json").read_text()
)
pole_result[0]["records"][0]["roots"].append(2)
rejected(
    [
        str(EXPERIMENTS / "check_rate_half_kb_positive_433_1a_cell5_specialization_poles.py"),
        "--base-result",
    ],
    pole_result,
)
print("positive 433-1a cell-5 exceptional-fiber router audit verified mutations=2")
