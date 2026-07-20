#!/usr/bin/env python3
"""Verify the c=1 parity Frobenius router and result packet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_fiber_two_cycle_c1_parity_frobenius_router"
DEPENDENCIES = {
    "rate_half_list_budget_three_fiber_two_cycle_c1_parity_mobius_router",
    "rate_half_list_budget_three_fiber_two_cycle_c1_parity_nonharmonic_scalar_compiler",
}
CONSUMER = "rate_half_list_adjacent_crossing"
EXPERIMENT = ROOT / "experiments" / "prize_resolution"
RESULT = EXPERIMENT / "rate_half_list_fiber_two_cycle_c1_parity_antiinvariant_characteristic_result.json"
SOURCE = EXPERIMENT / "rate_half_list_fiber_two_cycle_c1_parity_antiinvariant_characteristic_modal.py"
PRIME = 1009


def inverse(value: int) -> int:
    return pow(value % PRIME, -1, PRIME)


IOTA = next(value for value in range(PRIME) if value * value % PRIME == PRIME - 1)


def tau(value: int) -> int:
    return (4 * (value + 1) ** 2 * inverse((value - 1) ** 2) - 2) % PRIME


def cross_ratios(role: str, r_value: int) -> list[int]:
    r_value %= PRIME
    if role == "R":
        return [
            (r_value - 1) * (r_value - IOTA)
            * inverse((r_value + 1) * (r_value + IOTA)) % PRIME,
            2 * (1 + IOTA) * r_value
            * inverse((r_value + 1) * (r_value + IOTA)) % PRIME,
            -2 * (1 + IOTA) * r_value
            * inverse((r_value - 1) * (r_value - IOTA)) % PRIME,
        ]
    return [
        IOTA * (r_value - IOTA) * inverse(r_value + IOTA) % PRIME,
        (1 - IOTA) * (r_value - 1) * inverse(r_value + IOTA) % PRIME,
        (1 + IOTA) * (r_value - 1) * inverse(r_value - IOTA) % PRIME,
    ]


def factorization_check() -> None:
    checked = 0
    for r_value in range(2, 122):
        if pow(r_value, 4, PRIME) == 1:
            continue
        r_negative = -r_value % PRIME
        y_r = [tau(value) for role in ("R", "P") for value in cross_ratios(role, r_value)]
        y_n = [tau(value) for role in ("R", "P") for value in cross_ratios(role, r_negative)]
        assert y_r[0] == y_n[0]

        denominator_r = (r_value * r_value - 1) ** 2 * (r_value * r_value + 1) ** 2
        common_r = (
            r_value * (r_value * r_value + IOTA)
            * (pow(r_value, 4, PRIME) + 8 * IOTA * r_value * r_value - 1)
        )
        assert (y_r[1] - y_n[1]) * denominator_r % PRIME == 64 * (1 + IOTA) * common_r % PRIME
        assert (y_r[2] - y_n[2]) * denominator_r % PRIME == -64 * (1 + IOTA) * common_r % PRIME

        denominator_p0 = (r_value * r_value - 1) ** 2
        assert (y_r[3] - y_n[3]) * denominator_p0 % PRIME == -32 * r_value * (r_value * r_value + 1) % PRIME

        denominator_p = (r_value * r_value + 1) ** 2
        p1_factor = r_value * (r_value * r_value - (3 + 4 * IOTA) * inverse(5))
        p2_factor = r_value * (r_value * r_value - (3 - 4 * IOTA) * inverse(5))
        assert (y_r[4] - y_n[4]) * denominator_p % PRIME == (-64 - 128 * IOTA) * p1_factor % PRIME
        assert (y_r[5] - y_n[5]) * denominator_p % PRIME == (-64 + 128 * IOTA) * p2_factor % PRIME
        checked += 1
    assert checked >= 100


def certificate_check() -> None:
    packet = json.loads(RESULT.read_text())
    assert packet["all_complete"] and packet["coverage_exact"]
    assert packet["hits"] == []
    assert packet["odd_candidates"] == packet["processed"] == 2_247_721
    assert packet["skipped_factor_five"] == 449_544
    assert len(packet["shards"]) == 16
    assert max(row[5] for row in packet["shards"]) < 3.0
    assert packet["source_sha256"] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()


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
        "R0` is the sole branch",
        "v+v^(-1)=-8",
        "u+u^(-1)=6/5",
        "2,247,721",
        "not exclude any Frobenius-invariant branch",
    ):
        assert marker in statement


def main() -> None:
    factorization_check()
    certificate_check()
    wiring_check()
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_PARITY_FROBENIUS_PASS "
        "factorizations=6 candidates=2247721 residual=R0"
    )


if __name__ == "__main__":
    main()
