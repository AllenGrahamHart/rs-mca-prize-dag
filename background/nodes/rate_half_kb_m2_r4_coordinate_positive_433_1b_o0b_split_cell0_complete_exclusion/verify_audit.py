#!/usr/bin/env python3
"""Run the independent outside transcript and guard audit."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
AUDIT = (ROOT / "experiments/prize_resolution" /
         "rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_audit.py")


def main():
    spec = importlib.util.spec_from_file_location("outside_audit", AUDIT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.main()


if __name__ == "__main__":
    main()
