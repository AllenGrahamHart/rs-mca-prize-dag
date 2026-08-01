#!/usr/bin/env python3
"""Reverse-order audit of the cells 3/6 complete-product exclusion."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_433_cell36_complete_product_exclusion.py"
)


def main():
    specification = importlib.util.spec_from_file_location("certificate", SCRIPT)
    certificate = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(certificate)
    counts = certificate.verify(
        (certificate.F, certificate.E, certificate.D), controls=True
    )
    if sum(counts.values()) != 11760:
        raise RuntimeError("audit count")
    print(
        "RATE_HALF_KB_ONE_LOOP_433_CELL36_PRODUCT_AUDIT_PASS "
        "order=FED controls=2 total=11760"
    )


if __name__ == "__main__":
    main()
