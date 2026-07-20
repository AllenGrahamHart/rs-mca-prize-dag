#!/usr/bin/env python3
"""Verify the c=1 parity R0 lift-free compiler."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_fiber_two_cycle_c1_parity_r0_lift_free_compiler"
DEPENDENCIES = {
    "rate_half_list_budget_three_fiber_two_cycle_c1_parity_frobenius_router",
    "rate_half_list_budget_three_fiber_two_cycle_c1_parity_nonharmonic_scalar_compiler",
}
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 1009
IOTA = next(value for value in range(PRIME) if value * value % PRIME == PRIME - 1)


def inverse(value: int) -> int:
    return pow(value % PRIME, -1, PRIME)


def k_value(t_value: int, y_value: int) -> int:
    return (
        t_value * (y_value - 2) ** 2 + 4 * (t_value - 1) ** 2
    ) % PRIME


def trace_pair(t_value: int, u_value: int) -> tuple[int, int]:
    delta = 2 * IOTA * (u_value - inverse(u_value))
    return ((2 - delta) % PRIME, (2 + delta) % PRIME)


def algebra_check() -> None:
    checked = 0
    for u_value in range(2, 122):
        t_value = u_value * u_value % PRIME
        if t_value == 1:
            continue
        first, second = trace_pair(t_value, u_value)
        assert k_value(t_value, first) == 0
        assert k_value(t_value, second) == 0
        assert first != second

        # Build an exact scalar model for each root and check the eliminated
        # polynomial identity. T is a scalar here; the identity is formal in x.
        for y_value in (first, second):
            t_poly_value = 7
            s_squared = (y_value + 2) * t_poly_value % PRIME
            eliminated = (
                t_value * (s_squared - 4 * t_poly_value) ** 2
                + 4 * (t_value - 1) ** 2 * t_poly_value * t_poly_value
            ) % PRIME
            assert eliminated == 0
        checked += 1
    assert checked >= 100

    # Find an exact constant-gate model and verify the lift-free specialization.
    found = False
    for u_value in range(2, PRIME):
        t_value = u_value * u_value % PRIME
        if t_value == 1:
            continue
        for y_value in trace_pair(t_value, u_value):
            h_squared = -(y_value + 2) * inverse(4 * t_value) % PRIME
            roots = [h for h in range(PRIME) if h * h % PRIME == h_squared]
            if not roots:
                continue
            h_value = roots[0]
            assert (4 * t_value * h_value * h_value + y_value + 2) % PRIME == 0
            assert (
                4 * t_value * (1 + t_value * h_value * h_value) ** 2
                + (t_value - 1) ** 2
            ) % PRIME == 0
            found = True
            break
        if found:
            break
    assert found


def wiring_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "K_t(Y)=t(Y-2)^2+4(t-1)^2",
        "deg gcd(K_t,C_39-2)>=1",
        "t(S^2-4T)^2+4(t-1)^2T^2=0",
        "same trace",
        "4t(1+tH^2)^2+(t-1)^2=0",
        "does not discharge",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    wiring_check()
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_PARITY_R0_LIFT_FREE_PASS "
        "trace_degree=2 trace_depth=39 scalar_resultant=1 constant_gate=1"
    )


if __name__ == "__main__":
    main()

