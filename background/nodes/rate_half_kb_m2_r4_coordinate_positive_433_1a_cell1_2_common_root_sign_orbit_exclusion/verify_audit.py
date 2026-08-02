#!/usr/bin/env python3
"""Mutation audit for the deployed cells-1/2 common exclusion payload."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
VERIFY = NODE / "verify.py"
RESULT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_cell12_common_saturation_result.json"
)
SPEC = importlib.util.spec_from_file_location("cell12_verify", VERIFY)
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
    changed["rows"][0]["full_unit"] = False
    MODULE.require(rejected(changed), "reject nonunit full ideal")

    changed = copy.deepcopy(payload)
    changed["rows"][1]["program_sha256"] = "0" * 64
    MODULE.require(rejected(changed), "reject altered program")

    changed = copy.deepcopy(payload)
    changed["rows"][1]["epsilon"] = [-1, -1]
    MODULE.require(rejected(changed), "reject missing sign class")
    print("positive 433-1a cells 1/2 common exclusion audit verified")


if __name__ == "__main__":
    main()
