#!/usr/bin/env python3
"""Registered local checker for the cell-0 outside pilot."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
CHECKER = (ROOT / "experiments/prize_resolution" /
           "rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_check.py")


def main():
    spec = importlib.util.spec_from_file_location("outside_pilot_check", CHECKER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.main()


if __name__ == "__main__":
    main()
