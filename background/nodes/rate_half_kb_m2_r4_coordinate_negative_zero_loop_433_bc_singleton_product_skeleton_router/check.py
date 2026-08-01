#!/usr/bin/env python3
"""Check the three common involutions and signed-form census."""

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
    expected = {12: 8, 13: 4, 14: 4}
    for cell, count in expected.items():
        if len(router.PACKETS[cell]) != count:
            raise RuntimeError(f"packet rows {cell}")
        for b, c in router.PACKETS[cell]:
            router.involution(cell, b, c)
    if len(router.PRODUCT.MATCHINGS) != 15:
        raise RuntimeError("matching census")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_BC_PRODUCT_ROUTER_CHECK_PASS "
        "product_rows=16 involutions=negation,reciprocal-positive,reciprocal-negative"
    )


if __name__ == "__main__":
    main()
