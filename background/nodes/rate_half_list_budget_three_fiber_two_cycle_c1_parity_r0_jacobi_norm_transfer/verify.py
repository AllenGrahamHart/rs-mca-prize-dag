#!/usr/bin/env python3
"""Verify the c=1 parity R0 Jacobi-norm transfer."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_fiber_two_cycle_c1_parity_r0_jacobi_norm_transfer"
DEPENDENCIES = {
    "rate_half_list_budget_three_fiber_two_cycle_c1_parity_r0_lift_free_compiler",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_torsion_cyclotomic_norm_decomposition",
}
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 97


def chebyshev_t(index: int, value: int) -> int:
    if index == 0:
        return 1
    if index == 1:
        return value % PRIME
    previous, current = 1, value % PRIME
    for _ in range(1, index):
        previous, current = current, (2 * value * current - previous) % PRIME
    return current


def chebyshev_u(index: int, value: int) -> int:
    if index == 0:
        return 1
    previous, current = 1, 2 * value % PRIME
    for _ in range(1, index):
        previous, current = current, (2 * value * current - previous) % PRIME
    return current


def legendre_p3(value: int) -> int:
    return (5 * value**3 - 3 * value) * pow(2, -1, PRIME) % PRIME


def h3(t_value: int) -> int:
    # [z^3]((1-z)(1-tz))^(-1/2).
    return (5 + 3 * t_value + 3 * t_value**2 + 5 * t_value**3) * pow(16, -1, PRIME) % PRIME


def algebra_check() -> None:
    # Toy M=1 instance in a field containing the 32nd roots of unity.
    generator = 5
    r_value = pow(generator, (PRIME - 1) // 32, PRIME)
    assert pow(r_value, 32, PRIME) == 1
    assert pow(r_value, 16, PRIME) == PRIME - 1

    u_value = r_value * r_value % PRIME
    t_value = u_value * u_value % PRIME
    a_value = (r_value + pow(r_value, -1, PRIME)) * pow(2, -1, PRIME) % PRIME
    x_value = (u_value + pow(u_value, -1, PRIME)) * pow(2, -1, PRIME) % PRIME
    assert x_value == (2 * a_value * a_value - 1) % PRIME

    epsilon = pow(r_value, 16, PRIME)
    p_value = legendre_p3(x_value)
    h_value = h3(t_value)
    assert h_value == pow(u_value, 3, PRIME) * p_value % PRIME
    assert t_value * h_value * h_value % PRIME == epsilon * p_value * p_value % PRIME

    original = (
        4 * t_value * (1 + t_value * h_value * h_value) ** 2
        + (t_value - 1) ** 2
    ) % PRIME
    transformed = (
        (1 + epsilon * p_value * p_value) ** 2 + x_value * x_value - 1
    ) % PRIME
    assert original == 4 * t_value * transformed % PRIME

    assert chebyshev_t(16, a_value) == epsilon
    assert chebyshev_t(4, x_value) == 0  # epsilon=-1 toy packet

    w_value = (2 * x_value * x_value - 1) % PRIME
    z_value = (w_value + 1) * pow(2, -1, PRIME) % PRIME
    q_value = (5 * w_value - 1) * pow(4, -1, PRIME) % PRIME
    assert p_value == x_value * q_value % PRIME
    even_scalar = (
        (1 + epsilon * z_value * q_value * q_value) ** 2 + z_value - 1
    ) % PRIME
    assert even_scalar == transformed
    assert chebyshev_t(4, x_value) == chebyshev_t(2, w_value)


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
        "E_epsilon(x):=(1+epsilon P(x)^2)^2+x^2-1=0",
        "F_epsilon(w)=(1+epsilon zQ(w)^2)^2+z-1",
        "degree less\nthan `M=2^36`",
        "exactly the already-defined CR-002 norm pair",
        "no separate large norm run",
        "does not evaluate the norms",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    wiring_check()
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_PARITY_R0_JACOBI_PASS "
        "sign_packets=2 jacobi_degree=2^36 shared_norms=2"
    )


if __name__ == "__main__":
    main()
