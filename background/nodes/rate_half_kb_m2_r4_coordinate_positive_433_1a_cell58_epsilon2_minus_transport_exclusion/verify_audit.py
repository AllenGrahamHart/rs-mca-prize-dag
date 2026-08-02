#!/usr/bin/env python3
"""Hostile scope audit for the cell-5/8 sign transport."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CHECKER = ROOT / (
    "experiments/prize_resolution/"
    "check_rate_half_kb_positive_433_1a_cell58_epsilon2_minus_transport.py"
)
SPEC = importlib.util.spec_from_file_location("transport_checker", CHECKER)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def rejected(callback):
    try:
        callback()
    except RuntimeError:
        return True
    return False


def main():
    MODULE.check_duplicate_transport(-1, -1)
    for cell in (5, 8):
        for epsilon_1 in (-1, 1):
            MODULE.check_first_sign_transport(cell, epsilon_1, -1)
    MODULE.require(
        rejected(lambda: MODULE.check_first_sign_transport(5, -1, 1)),
        "epsilon2 mutation accepted",
    )
    MODULE.require(
        rejected(lambda: MODULE.check_first_sign_transport(6, -1, -1)),
        "cell mutation accepted",
    )
    print("positive 433-1a cell-5/8 transport audit verified mutations=2")


if __name__ == "__main__":
    main()
