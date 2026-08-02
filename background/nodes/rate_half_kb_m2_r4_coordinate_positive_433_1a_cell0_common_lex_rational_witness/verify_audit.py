#!/usr/bin/env python3
"""Mutation audit for the cell-0 common lex rational witness."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
RESULT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_cell0_common_triangle_result.json"
)
SPEC = importlib.util.spec_from_file_location("cell0_verify", NODE / "verify.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def rejected(payload):
    try:
        MODULE.verify_payload(payload)
    except RuntimeError:
        return True
    return False


def main():
    payload = json.loads(RESULT.read_text())
    MODULE.verify_payload(payload)

    changed = copy.deepcopy(payload)
    changed["result"]["rational_witnesses"][0]["equation_values"][0] = 1
    MODULE.require(rejected(changed), "reject nonzero minor")

    changed = copy.deepcopy(payload)
    changed["result"]["rational_witnesses"][1]["guard_values"][0] = 0
    MODULE.require(rejected(changed), "reject zero guard")

    changed = copy.deepcopy(payload)
    changed["result"]["stdout"] = changed["result"]["stdout"].replace(
        "33423356", "33423358", 1
    )
    MODULE.require(rejected(changed), "reject coefficient transcription")
    print("positive 433-1a cell-0 common lex witness audit verified")


if __name__ == "__main__":
    main()
