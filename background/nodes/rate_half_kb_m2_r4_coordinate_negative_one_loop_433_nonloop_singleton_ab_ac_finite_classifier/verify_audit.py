#!/usr/bin/env python3
"""Run the import-independent one-loop 433 packet replay."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
AUDIT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_433_cell36_packet_audit.py"
)


def main():
    specification = importlib.util.spec_from_file_location("packet_audit", AUDIT)
    packet_audit = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(packet_audit)
    packet_audit.main()


if __name__ == "__main__":
    main()
