#!/usr/bin/env python3
"""Audit representative guarded certificates in every retained type."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / (
    "experiments/prize_resolution/rate_half_kb_zero_loop_433_bc_product_probe.py"
)


def main():
    specification = importlib.util.spec_from_file_location("router", SCRIPT)
    router = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(router)
    retained = {
        12: ("Z2", "Z3", "Z4"),
        13: ("Z1", "Z2", "Z3"),
        14: ("Z1", "Z2", "Z3"),
    }
    counts = {}
    for cell, names in retained.items():
        for name in names:
            result = router.probe(cell, 0, name, verbose=False)
            if not result["guarded"]:
                raise RuntimeError(f"missing live certificate {cell}/{name}")
            counts[(cell, name)] = len(result["guarded"])
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_BC_PRODUCT_ROUTER_LIVE_PASS "
        "types=9 representative_guarded_counts="
        + ",".join(
            f"{cell}:{name}:{count}"
            for (cell, name), count in sorted(counts.items())
        )
    )


if __name__ == "__main__":
    main()
