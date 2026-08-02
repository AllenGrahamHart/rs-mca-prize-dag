#!/usr/bin/env python3
"""Mutation audit for the cell-0 generic signed-pair exclusion."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
PAIR = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_cell0_generic_signed_pair_result.json"
)
KERNEL = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_cell0_kernel_reduction_result.json"
)
SPEC = importlib.util.spec_from_file_location("cell0_pair_verify", NODE / "verify.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def rejected(function, payload):
    try:
        function(payload)
    except RuntimeError:
        return True
    return False


def main():
    pair = json.loads(PAIR.read_text())
    kernel = json.loads(KERNEL.read_text())
    MODULE.verify_pair(pair)
    MODULE.verify_kernel(kernel)

    changed = copy.deepcopy(pair)
    changed["rows"][0]["unit"] = False
    MODULE.require(rejected(MODULE.verify_pair, changed), "reject nonunit pair")

    changed = copy.deepcopy(pair)
    changed["rows"][1]["c_gcd_degree"] = 1
    MODULE.require(rejected(MODULE.verify_pair, changed), "reject pole branch")

    changed = copy.deepcopy(kernel)
    changed["result"]["branch_rational_coefficients"][0][
        "normalized_coefficients"
    ]["b10"]["polynomial"] += "+1"
    MODULE.require(rejected(MODULE.verify_kernel, changed), "reject B1 mutation")
    print("positive 433-1a cell-0 signed-pair exclusion audit verified")


if __name__ == "__main__":
    main()
