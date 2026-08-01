#!/usr/bin/env python3
"""Run the independent factor audit for the BC mixed-pair exclusion."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
AUDIT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_433_cell9_factor_audit.py"
)


def main():
    specification = importlib.util.spec_from_file_location("audit", AUDIT)
    audit = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(audit)
    audit.main()


if __name__ == "__main__":
    main()
