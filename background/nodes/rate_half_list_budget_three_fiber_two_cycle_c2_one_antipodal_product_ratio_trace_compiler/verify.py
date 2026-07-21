#!/usr/bin/env python3
"""Checks for the c2 one-antipodal product/ratio trace compiler."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_product_ratio_trace_compiler"
DEPENDENCIES = {
    "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_primary_torsion_reducer",
    "rate_half_list_budget_three_fiber_two_cycle_c2_torsion_field_router",
}
CONSUMER = "rate_half_list_adjacent_crossing"


def tower(product: int, trace: int, levels: int, prime: int) -> tuple[int, int]:
    for _ in range(levels - 1):
        product = product * product % prime
        trace = (trace * trace - 2) % prime
    return product, trace


def subgroup_generator(prime: int, order: int) -> int:
    return next(
        value
        for value in range(2, prime)
        if pow(value, order, prime) == 1
        and pow(value, order // 2, prime) != 1
    )


def check_wiring() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    incoming = {
        edge["from"]
        for edge in dag["edges"]
        if edge["to"] == NODE_ID and edge.get("kind") == "req"
    }
    outgoing = {
        edge["to"]
        for edge in dag["edges"]
        if edge["from"] == NODE_ID and edge.get("kind") == "ev"
    }
    assert nodes[NODE_ID]["status"] == "PROVED"
    assert incoming == DEPENDENCIES
    assert CONSUMER in outgoing


def load_torsion_field_verify():
    path = (
        ROOT
        / "background/nodes/rate_half_list_budget_three_fiber_two_cycle_c2_torsion_field_router/verify.py"
    )
    spec = importlib.util.spec_from_file_location("c2_torsion_field_verify", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    check_wiring()

    prime = 97
    omega = subgroup_generator(prime, 16)
    c, d = omega, pow(omega, 3, prime)
    product = c * d % prime
    ratio = c * pow(d, -1, prime) % prime
    trace = (ratio + pow(ratio, -1, prime)) % prime
    square_total = (c + d) ** 2 % prime
    assert square_total == product * (trace + 2) % prime

    product_half, trace_half = tower(product, trace, 4, prime)
    assert product_half * product_half % prime == 1
    assert trace_half == 2 * product_half % prime
    assert (trace * trace - 4) % prime != 0
    assert (1 + product * product - product * trace) % prime != 0

    reconstructed = [
        value
        for value in range(1, prime)
        if pow(value, 16, prime) == 1
        and value * value % prime == product * ratio % prime
    ]
    assert set(reconstructed) == {c, -c % prime}

    # Reciprocal Frobenius fixes the ratio trace but may invert the product.
    field = load_torsion_field_verify()
    generator = field.primitive_element()
    omega_ext = field.power(generator, (field.PRIME**2 - 1) // 16)
    c_ext, d_ext = omega_ext, field.power(omega_ext, 3)
    product_ext = field.multiply(c_ext, d_ext)
    ratio_ext = field.multiply(c_ext, field.inverse(d_ext))
    trace_ext = field.add(ratio_ext, field.inverse(ratio_ext))
    assert field.power(trace_ext, field.PRIME) == trace_ext
    assert field.power(product_ext, field.PRIME) == field.inverse(product_ext)
    assert field.power(product_ext, field.PRIME) != product_ext

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_ONE_ANTIPODAL_PRODUCT_TRACE_PASS "
        "prime_order=16 half_levels=3 reconstructions=2 reciprocal_trace=1 wiring=3"
    )


if __name__ == "__main__":
    main()
