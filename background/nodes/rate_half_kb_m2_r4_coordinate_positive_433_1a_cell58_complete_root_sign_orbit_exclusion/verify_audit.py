#!/usr/bin/env python3
"""Mutation audit for source-reciprocal cell-5/8 transport."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CHECKER = ROOT / (
    "experiments/prize_resolution/"
    "check_rate_half_kb_positive_433_1a_cell58_source_reciprocal_transport.py"
)
SPEC = importlib.util.spec_from_file_location("reciprocal_checker", CHECKER)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def rejected(callback):
    try:
        callback()
    except RuntimeError:
        return True
    return False


def main():
    MODULE.check_form_transport()
    MODULE.check_cell5_sign_map()
    MODULE.check_modal_audit()

    original = MODULE.SCOUT_SHA256
    MODULE.SCOUT_SHA256 = "0" * 64
    MODULE.require(rejected(MODULE.check_modal_audit), "packet mutation accepted")
    MODULE.SCOUT_SHA256 = original

    b, t = MODULE.sp.symbols("b t")
    MODULE.require(
        MODULE.parse_singular_bt("b4t4-1", b, t) == b**4 * t**4 - 1,
        "parser control",
    )
    print("positive 433-1a cell-5/8 reciprocal audit verified mutations=1")


if __name__ == "__main__":
    main()
