#!/usr/bin/env python3
"""Check the common involution and signed product-form census."""

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
    expected = {"Z0": 4, "Z1": 32, "Z2": 16, "Z3": 32, "Z4": 16}
    for b, c in router.PACKETS:
        mate = router.involution_data(b, c)
        if mate != -c * c * pow(b, -1, router.P) % router.P:
            raise RuntimeError("mate")
        for name, count in expected.items():
            forms = tuple(router.product_forms(name, b, c))
            if len(forms) != count or any(len(form) != 7 for form in forms):
                raise RuntimeError(f"form census {name}")
    if len(router.MATCHINGS) != 15:
        raise RuntimeError("matching census")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_PRODUCT_ROUTER_CHECK_PASS "
        "common_rows=4 forms=100 matchings=15"
    )


if __name__ == "__main__":
    main()
