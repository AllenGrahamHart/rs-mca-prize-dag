#!/usr/bin/env python3
"""Mutation audit for the seven-orbit common curve profile."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
RESULT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_remaining_common_saturation_result.json"
)
SPEC = importlib.util.spec_from_file_location("profile_verify", NODE / "verify.py")
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
    changed["rows"][0]["full_unit"] = True
    MODULE.require(rejected(changed), "reject unit mutation")

    changed = copy.deepcopy(payload)
    changed["rows"][3]["stdout"] = changed["rows"][3]["stdout"].replace(
        "\n1\n23\n", "\n2\n23\n", 1
    )
    MODULE.require(rejected(changed), "reject dimension mutation")

    changed = copy.deepcopy(payload)
    changed["rows"].pop()
    MODULE.require(rejected(changed), "reject missing orbit")
    print("positive 433-1a remaining common curve profile audit verified")


if __name__ == "__main__":
    main()
