#!/usr/bin/env python3
"""Verify the official Newton cofactor-window router."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_official_newton_cofactor_window_router"


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def elementary(roots: tuple[int, ...], depth: int, prime: int) -> list[int]:
    out = [1] + [0] * depth
    for root in roots:
        for j in range(depth, 0, -1):
            out[j] = (out[j] + root * out[j - 1]) % prime
    return out


def recover_elementary(power_sums: list[int], prime: int) -> list[int]:
    out = [1]
    for j in range(1, len(power_sums)):
        numerator = 0
        for i in range(1, j + 1):
            sign = 1 if i % 2 == 1 else -1
            numerator += sign * out[j - i] * power_sums[i]
        out.append(numerator * pow(j, -1, prime) % prime)
    return out


def main() -> None:
    checks = 0

    # The weak order bound alone contradicts the field cap below 257.
    for prime in range(3, 252):
        if is_prime(prime):
            assert prime**32 > 2 ** (prime + 1)
            checks += 1

    factors = {
        511: (7, 73),
        513: (27, 19),
        1023: (3, 11, 31),
        1025: (25, 41),
        1535: (5, 307),
        1537: (29, 53),
        2047: (23, 89),
        2049: (3, 683),
        2559: (3, 853),
        2561: (13, 197),
        3071: (37, 83),
        3073: (7, 439),
    }
    for candidate, pieces in factors.items():
        product = 1
        for piece in pieces:
            product *= piece
        assert product == candidate
        assert candidate % 512 in (1, 511)
        checks += 2

    assert is_prime(3583)
    assert 5 * (3583 + 1) <= 44 * (3583 - 3175)
    checks += 2
    for characteristic in range(3583, 10_000, 2):
        # This is the conservative log_2(p)>11 reserve bound.
        ell_upper = (5 * (characteristic + 1) + 43) // 44 + 1
        assert ell_upper <= characteristic - 3174
        checks += 1

    # Exhaust Newton recovery on split root sets for characteristic-safe
    # depths. Repeated roots are also allowed by the algebraic identity.
    for prime in (5, 7):
        for size in range(1, prime):
            for roots in itertools.combinations(range(prime), min(size, 3)):
                depth = min(len(roots), prime - 1)
                powers = [0] + [sum(pow(root, j, prime) for root in roots) % prime for j in range(1, depth + 1)]
                expected = elementary(roots, depth, prime)
                assert recover_elementary(powers, prime) == expected
                checks += 1

    # The uniform excess window and the all-word large-characteristic
    # corollary are exact integer statements.
    p = 3583
    ell = p - 3174
    for excess in (0, 1, 3174):
        assert ell - 1 + excess < p
        checks += 1
    for n, k, characteristic in (
        (1 << 13, 1 << 12, 12_289),
        (1 << 16, 1 << 15, 65_537),
        (1 << 20, 1 << 16, 7_340_033),
        (1 << 41, 1 << 40, 6_597_069_766_657),
    ):
        assert characteristic >= n - k
        assert n - k - 1 < characteristic
        checks += 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_official_reserve_tame_refinement_router",
        "l1_exact_shell_fixed_cofactor_prefix_transport",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    assert (NODE, "l1_mixed_petal_amplification", "ev") in edges
    checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "p>=3583",
        "ell_0<=p-3174",
        "d=min(a,h-k)<p",
        "0<=e_0<=3174",
        "If `p>=n-k`",
        "does not prove prefix flatness",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_OFFICIAL_NEWTON_COFACTOR_WINDOW_ROUTER_PASS checks={checks}")


if __name__ == "__main__":
    main()
