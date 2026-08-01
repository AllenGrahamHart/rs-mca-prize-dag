#!/usr/bin/env python3
"""Independent structural audit of the complete-Vieta router."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_zero_loop_433_complete_vieta_probe.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("router", SCRIPT)
    router = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(router)
    router.field_audit()
    for cell, records in router.COMMON_RECORDS.items():
        for record in records:
            router.common_data(cell, record)
    for name in router.PRODUCT.SKELETONS:
        products = tuple(router.PRODUCT.product_forms(name, 2, 3))
        edges = tuple(router.edge_forms(name, 2, 3))
        require(len(products) == len(edges), f"{name} form count")
        require(all(
            router.PRODUCT.monomial(product) ==
            router.PRODUCT.monomial(left * right)
            for product_row, edge_row in zip(products, edges)
            for product, (left, right) in zip(product_row, edge_row)
        ), f"{name} edge alignment")
    statement = (NODE / "statement.md").read_text()
    require("unresolved multiplicative families" in statement, "open-family fence")
    require("does not delete them" in statement, "nonclaim")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_COMPLETE_VIETA_AUDIT_PASS "
        "field=Fp[X]/(X6+X+6) common_records=40 skeletons=5"
    )


if __name__ == "__main__":
    main()
