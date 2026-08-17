#!/usr/bin/env python3
"""Verify the three O0b one-finite projective-chart exclusions."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_chart_remaining_pilot_result.json"
PROGRAM = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_projective_chart_program.py"
LAUNCHER = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_chart_remaining_pilot_modal.py"
CHECKER = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_chart_remaining_pilot_check.py"
RESULT_SHA256 = "09d854294bb4b0f3d33fc45f140f12ca86eebbb568c1f845a061b4143c50dba0"
PROGRAM_SHA256 = "277ad3a0d4489470eee9cef2c374b28d73aad333149ea415a3e55ea05549f4c5"
LAUNCHER_SHA256 = "99eaffabe8f10e1b303421fdec25f7d958f33f1dcc4e0dc05eac78da04333777"
CHECKER_SHA256 = "902c15e5dd3316957efab6342d3feec4df881e9ddb7d7ec1315762f4e007d5fb"
UNIT_MASKS = {
    ("finite", "infinity", "infinity"): (57, 22),
    ("infinity", "finite", "infinity"): (74, 43),
    ("infinity", "infinity", "finite"): (62, 28),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_checker():
    require(hashlib.sha256(RESULT.read_bytes()).hexdigest() == RESULT_SHA256,
            "result custody")
    require(hashlib.sha256(PROGRAM.read_bytes()).hexdigest() == PROGRAM_SHA256,
            "program-core custody")
    require(hashlib.sha256(LAUNCHER.read_bytes()).hexdigest() == LAUNCHER_SHA256,
            "launcher custody")
    require(hashlib.sha256(CHECKER.read_bytes()).hexdigest() == CHECKER_SHA256,
            "checker custody")
    spec = importlib.util.spec_from_file_location("chart_checker", CHECKER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    checker = load_checker()
    checked = checker.verify()
    require(checked == {"rows": 7, "unit": 3, "nonunit": 0, "timeout": 4},
            "checked row census")
    payload = json.loads(RESULT.read_text())
    unit_rows = [row for row in payload["rows"] if row.get("unit")]
    require({tuple(row["chart_mask"]) for row in unit_rows} == set(UNIT_MASKS),
            "one-finite unit masks")
    for row in unit_rows:
        initial_size, guard4_size = UNIT_MASKS[tuple(row["chart_mask"])]
        stdout = row["stdout"]
        require(f"INITIAL_DIM=4,INITIAL_SIZE={initial_size}" in stdout,
                "initial basis ledger")
        require(f"SAT=4,DIM=4,SIZE={guard4_size}" in stdout and
                "SAT=5,DIM=-1,SIZE=1" in stdout, "b+1 unit transition")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_XI2_PAIRING0_ONE_FINITE_VERIFY_PASS "
          "charts=3 unit_at=b+1")


if __name__ == "__main__":
    main()
