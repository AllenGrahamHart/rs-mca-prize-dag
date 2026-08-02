#!/usr/bin/env python3
"""Scope and hostile-mutation audit for the first finite batch."""

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
assert "This leaves 46 values" in statement
assert "other 46 router values" in contract


def rejected(payload):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
        json.dump(payload, handle)
        handle.flush()
        process = subprocess.run(
            [
                sys.executable,
                str(EXPERIMENTS / "check_rate_half_kb_positive_433_1a_cell5_finite_candidate_batch.py"),
                "--result",
                handle.name,
            ],
            capture_output=True,
            text=True,
            timeout=30,
        )
    assert process.returncode != 0


result_path = EXPERIMENTS / "rate_half_kb_positive_433_1a_cell5_finite_candidate_batch_result.json"
payload = json.loads(result_path.read_text())
payload["records"][0]["rows"][0]["closure_reason"] = "target_collision"
rejected(payload)

payload = json.loads(result_path.read_text())
row = next(
    row
    for record in payload["records"]
    for row in record["rows"]
    if row["closure_reason"] == "target_collision"
)
row["coordinates"]["b"][0] ^= 1
rejected(payload)
print("positive 433-1a cell-5 finite candidate first-batch audit verified mutations=2")
