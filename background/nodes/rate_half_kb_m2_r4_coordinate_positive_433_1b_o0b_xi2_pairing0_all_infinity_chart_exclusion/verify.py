#!/usr/bin/env python3
"""Verify the exact O0b all-infinity chart exclusion."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_chart_all_infinity_result.json"
PROGRAM = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_projective_chart_program.py"
LAUNCHER = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_chart_all_infinity_modal.py"
CHECKER = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_chart_all_infinity_check.py"
RESULT_SHA256 = "545a130914d9896d84a5215865fea7333a2af9f1f7f9d08bfc14d3587770bcaf"
PROGRAM_SHA256 = "277ad3a0d4489470eee9cef2c374b28d73aad333149ea415a3e55ea05549f4c5"
LAUNCHER_SHA256 = "1c9b81d9377c6e06edd5b1953e955c5ebffb0d3a9592485fe00d3c5c11dfbeb3"
CHECKER_SHA256 = "c8ce618837d678d19dced46b9ff250d0141d3ac7e61f579372192b4e1a9f9876"


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
    require(checked == {"status": "COMPLETE", "unit": True},
            "checked complete unit")
    payload = json.loads(RESULT.read_text())
    stdout = payload["row"]["stdout"]
    require("INITIAL_DIM=3,INITIAL_SIZE=54" in stdout, "initial ideal")
    require("SAT=4,DIM=3,SIZE=22" in stdout and
            "SAT=5,DIM=-1,SIZE=1" in stdout, "b+1 unit transition")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_XI2_PAIRING0_ALL_INFINITY_VERIFY_PASS "
          "initial=3/54 unit_at=b+1")


if __name__ == "__main__":
    main()
