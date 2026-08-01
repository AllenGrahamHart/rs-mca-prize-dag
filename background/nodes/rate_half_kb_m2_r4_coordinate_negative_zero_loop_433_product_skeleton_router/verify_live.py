#!/usr/bin/env python3
"""Audit guarded product-gate survivors in Z0, Z1, and Z4."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_zero_loop_433_cell2_product_probe.py"
)


def main():
    specification = importlib.util.spec_from_file_location("router", SCRIPT)
    router = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(router)
    expected = {
        "Z0": (420, 86, 216, 0, 48, 0),
        "Z1": (3360, 480, 1216, 0, 128, 0),
        "Z4": (1680, 240, 536, 0, 64, 0),
    }
    for packet in range(4):
        for name, counts in expected.items():
            checked, soluble, isolated, samples, guarded, families = (
                router.group_probe(packet, name, print_limit=0, verbose=False)
            )
            observed = (
                checked, soluble, isolated, samples,
                len(guarded), len(families),
            )
            if observed != counts:
                raise RuntimeError(f"{packet}/{name} census {observed}")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_PRODUCT_ROUTER_LIVE_PASS "
        "packets=4 Z0=48 Z1=128 Z4=64 guarded_certificates_per_packet"
    )


if __name__ == "__main__":
    main()
