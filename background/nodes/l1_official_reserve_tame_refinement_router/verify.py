#!/usr/bin/env python3
"""Verify the official-reserve tame-refinement router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_official_reserve_tame_refinement_router"


def v2(value: int) -> int:
    out = 0
    while value % 2 == 0:
        value //= 2
        out += 1
    return out


def order_mod_power_two(value: int, exponent: int) -> int:
    modulus = 1 << exponent
    value %= modulus
    if value == 1:
        return 1
    if value % 4 == 1:
        order = 1 << max(0, exponent - v2(value - 1))
    else:
        b = v2(value + 1)
        order = 2 if exponent <= b else 1 << (exponent - b)
    assert pow(value, order, modulus) == 1
    if order > 1:
        assert pow(value, order // 2, modulus) != 1
    return order


def ceil_ratio(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def main() -> None:
    checks = 0

    # Exhaust the exact 2-adic order formula over a broad finite frame.
    for exponent in range(3, 17):
        n = 1 << exponent
        for value in range(3, 512, 2):
            order = order_mod_power_two(value, exponent)
            assert order * (value + 1) >= n
            checks += 3

    # Characteristics 3 and 5 violate the official field cap already at the
    # smallest scoped domain.
    n_min = 1 << 13
    for characteristic in (3, 5):
        order = order_mod_power_two(characteristic, 13)
        assert order == n_min // 4
        assert characteristic**order >= 1 << 256
        checks += 2

    # Exact integer form of 5(p+1)/(4 log_2 p) <= p-2 at the boundary and
    # nearby odd characteristics. The proof supplies monotonicity thereafter.
    for characteristic in range(7, 128, 2):
        assert characteristic ** (4 * (characteristic - 2)) >= 2 ** (
            5 * (characteristic + 1)
        )
        checks += 1

    # Representative prime and extension-field rows. floor(log_2 p) gives a
    # conservative upper bound on ell_0, so this check uses integer arithmetic.
    rows = (
        (1 << 13, 12_289, 2),
        (1 << 16, 65_537, 1),
        (1 << 20, 7_340_033, 1),
        (1 << 41, 6_597_069_766_657, 1),
    )
    for n, characteristic, degree in rows:
        q = characteristic**degree
        assert (q - 1) % n == 0
        assert q < 1 << 256
        assert degree * (characteristic + 1) >= n
        log_floor = characteristic.bit_length() - 1
        ell_upper = ceil_ratio(5 * (characteristic + 1), 4 * log_floor) + 1
        assert ell_upper < characteristic
        checks += 5

    # The reserve trial lies below n-k uniformly on the official rate box.
    for exponent in range(13, 42):
        n = 1 << exponent
        trial_upper = ceil_ratio(5 * n, 4 * exponent)
        assert n // 2 + trial_upper <= n
        checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "field_cap_check",
        "l1_exact_shell_prefix_hankel_bridge",
        "l1_tame_fixed_petal_refinement_census",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    assert (NODE, "l1_mixed_petal_amplification", "ev") in edges
    checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "n | p^f-1",
        "p^f<2^256",
        "eta=min(epsilon,1/4)",
        "ell_0<p",
        "ImgFib_U(k+sigma) subset ImgFib_U(k+sigma_0)",
        "wild fixed-petal decomposition is not an official L1 escape",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_OFFICIAL_RESERVE_TAME_REFINEMENT_ROUTER_PASS checks={checks}")


if __name__ == "__main__":
    main()
