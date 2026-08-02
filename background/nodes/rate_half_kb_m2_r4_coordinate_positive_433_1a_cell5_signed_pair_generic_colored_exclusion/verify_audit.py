#!/usr/bin/env python3
"""Scope and hostile-mutation audit for the generic colored exclusion."""

import json
import subprocess
import sys
import tempfile
from pathlib import Path


HERE = Path(__file__).parent
ROOT = HERE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
statement = (HERE / "statement.md").read_text()
contract = (HERE / "claim_contract.md").read_text()
assert "exceptional" in statement and "`t` fibers" in statement
assert "`DF+/DF-/CF`" in statement
assert "charts 3--5" in statement
assert "exceptional `t`" in contract


def rejected(checker, payload):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
        json.dump(payload, handle)
        handle.flush()
        process = subprocess.run(
            [sys.executable, str(checker), "--result", handle.name],
            capture_output=True,
            text=True,
            timeout=30,
        )
    assert process.returncode != 0


primary_path = EXPERIMENTS / (
    "rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd_result.json"
)
primary = json.loads(primary_path.read_text())
primary[0]["records"][0]["numerator"][0] ^= 1
rejected(
    EXPERIMENTS / "check_rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd.py",
    primary,
)

audit_path = EXPERIMENTS / (
    "rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd_audit_result.json"
)
audit = json.loads(audit_path.read_text())
audit[3]["program_sha256"] = "0" * 64
rejected(
    EXPERIMENTS / "audit_rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd.py",
    audit,
)
print("positive 433-1a cell-5 generic colored exclusion audit verified mutations=2")
