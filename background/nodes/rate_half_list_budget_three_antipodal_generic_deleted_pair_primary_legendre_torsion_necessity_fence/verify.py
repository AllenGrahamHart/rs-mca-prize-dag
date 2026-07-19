#!/usr/bin/env python3
"""Verify exact non-torsion primary/Legendre route-fence rows."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_primary_legendre_torsion_necessity_fence"
PARITY = "rate_half_list_budget_three_antipodal_generic_deleted_pair_parity_reduction"
LEGENDRE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_legendre_collapse"
CONSUMER = "rate_half_list_adjacent_crossing"

ROWS = (
    (0, 384690601, 362094250, 334403939, 90326885, 15359535),
    (1, 114830041, 53151121, 43471449, 59896164, 36780295),
    (
        2,
        96186353595534244333511041,
        24643621616413434900523946,
        91117748793720439379754436,
        48473322157903157538287266,
        16136690780167816062921118,
    ),
)

# Complete n-1 factorizations for the nontrivial Pocklington certificate tree.
FACTORS = {
    384690601: {2: 3, 3: 3, 5: 2, 7: 1, 10177: 1},
    10177: {2: 6, 3: 1, 53: 1},
    114830041: {2: 3, 3: 1, 5: 1, 13: 1, 73609: 1},
    73609: {2: 3, 3: 1, 3067: 1},
    3067: {2: 1, 3: 1, 7: 1, 73: 1},
    96186353595534244333511041: {
        2: 7,
        3: 1,
        5: 1,
        209441: 1,
        239194136603342957: 1,
    },
    209441: {2: 5, 5: 1, 7: 1, 11: 1, 17: 1},
    239194136603342957: {2: 2, 7: 1, 73: 1, 117022571723749: 1},
    117022571723749: {2: 2, 3: 1, 31: 1, 241: 1, 569: 1, 2294021: 1},
    2294021: {2: 2, 5: 1, 23: 1, 4987: 1},
    4987: {2: 1, 3: 2, 277: 1},
}


def small_prime(value: int) -> bool:
    return value >= 2 and all(value % divisor for divisor in range(2, math.isqrt(value) + 1))


def certify_prime(value: int, proved: set[int]) -> None:
    if value in proved:
        return
    if value < 1000:
        assert small_prime(value)
        proved.add(value)
        return
    factors = FACTORS[value]
    assert math.prod(prime**exponent for prime, exponent in factors.items()) == value - 1
    for prime in factors:
        certify_prime(prime, proved)
        assert prime in proved
        witness = next(
            base
            for base in range(2, 1000)
            if pow(base, value - 1, value) == 1
            and math.gcd(pow(base, (value - 1) // prime, value) - 1, value) == 1
        )
        assert witness < 1000
    # Complete factorization gives F=value-1>sqrt(value) in Pocklington.
    proved.add(value)


def coefficient_check() -> None:
    proved: set[int] = set()
    for branch, prime, r_value, t_expected, f3_expected, torsion_expected in ROWS:
        certify_prime(prime, proved)
        assert prime > 16
        inverse = lambda value: pow(value % prime, -1, prime)
        t_value = pow(r_value, 4, prime)
        assert t_value == t_expected and t_value != 1

        f_values = [1]
        for degree in range(1, 4):
            previous_two = f_values[degree - 2] if degree >= 2 else 0
            f_values.append(
                (
                    (4 * degree - 3) * (1 + t_value) * f_values[degree - 1]
                    - (4 * degree - 6) * t_value * previous_two
                )
                * inverse(4 * degree)
                % prime
            )
        assert f_values[2] == 0
        assert f_values[3] == f3_expected != 0

        h3 = (
            5 * pow(t_value, 3, prime)
            + 3 * pow(t_value, 2, prime)
            + 3 * t_value
            + 5
        ) * inverse(16) % prime
        chi = (r_value + inverse(r_value)) % prime
        gates = (
            t_value * h3**2 + (chi - 1) ** 2,
            t_value * (chi - 2) ** 2 * h3**2 + (chi + 2) ** 2,
            t_value * chi**2 * h3**2 + (chi - 4) ** 2,
        )
        assert gates[branch] % prime == 0

        k3 = pow(4, 3, prime) * h3 % prime
        scale = pow(4, 6, prime)
        cleared = (
            r_value**6 * k3**2 + scale * (r_value**2 - r_value + 1) ** 2,
            r_value**4 * (r_value - 1) ** 4 * k3**2 + scale * (r_value + 1) ** 4,
            r_value**4 * (r_value**2 + 1) ** 2 * k3**2
            + scale * (r_value**2 - 4 * r_value + 1) ** 2,
        )
        assert cleared[branch] % prime == 0
        assert pow(r_value, 32, prime) == torsion_expected != 1


def wiring_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PARITY]["status"] == "PROVED"
    assert nodes[LEGENDRE]["status"] == "PROVED"
    assert (PARITY, NODE, "req") in edges
    assert (LEGENDRE, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "F_2(t)=(5t^2+2t+5)/32",
        "H_3(t)=(5t^3+3t^2+3t+5)/16",
        "96186353595534244333511041",
        "F_3(t)!=0",
        "r^32=1",
        "not deleted-pair survivors",
        "makes no assertion",
    ):
        assert marker in statement


def main() -> None:
    coefficient_check()
    wiring_check()
    print(
        "RATE_HALF_DELETED_PAIR_TORSION_NECESSITY_FENCE_PASS "
        "branches=3 primary_gap_rows=3 torsion_rows=0"
    )


if __name__ == "__main__":
    main()
