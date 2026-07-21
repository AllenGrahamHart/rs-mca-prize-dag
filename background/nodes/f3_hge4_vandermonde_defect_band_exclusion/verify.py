#!/usr/bin/env python3
"""Verify the HGE4 Vandermonde-defect band exclusion packet."""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_vandermonde_defect_band_exclusion"
DEPENDENCIES = {
    "f3_hge4_cyclotomic_haar_near_quarter_swap_router",
    "f3_hge4_swap_norm_haar_band_exclusion",
}
CONSUMER = "f3_hge4_norm_gate_count"
EXPECTED_CAPS = {
    9: 2, 10: 4, 11: 9, 12: 17, 13: 33, 14: 61, 15: 115,
    16: 215, 17: 404, 18: 761, 19: 1437, 20: 2720, 21: 5164,
    22: 9827, 23: 18742, 24: 35824, 25: 68606, 26: 131623,
    27: 252943, 28: 486832, 29: 938320, 30: 1810906,
    31: 3499241, 32: 6769391, 33: 13109649, 34: 25413774,
    35: 49312552, 36: 95770531, 37: 186153140, 38: 362120147,
    39: 704953197, 40: 1373333614, 41: 2677220820,
}

getcontext().prec = 90
LOG_TWO = Decimal(2).ln()


def admitted(exponent: int, defect: int) -> bool:
    order = 1 << exponent
    width = order // 4 - defect
    if defect < 1 or width < 4:
        return False
    order_decimal = Decimal(order)
    radius = Decimal(defect + 1)
    logarithm = exponent * LOG_TWO
    x_value = 4 * radius * logarithm / order_decimal
    if x_value > 1:
        return False
    ceiling = (
        4 * (radius * logarithm - defect)
        - 8 * radius**2 * logarithm**2 / order_decimal
        + Decimal(32) * radius**3 * logarithm**3 / (3 * order_decimal**2)
    )
    rank_floor = (width - 1) // 2 + 2
    return ceiling <= rank_floor


def band_cap(exponent: int) -> int:
    order = 1 << exponent
    low, high = 0, order // 4 - 4
    while low < high:
        middle = (low + high + 1) // 2
        if admitted(exponent, middle):
            low = middle
        else:
            high = middle - 1
    return low


def endpoint_check() -> tuple[int, dict[int, int]]:
    caps: dict[int, int] = {}
    for exponent in range(4, 42):
        cap = band_cap(exponent)
        if cap:
            caps[exponent] = cap
            assert admitted(exponent, cap)
            assert not admitted(exponent, cap + 1)
            order = 1 << exponent
            assert exponent * (cap + 1) <= order // 2
    assert caps == EXPECTED_CAPS
    assert sum(caps.values()) == 5_501_420_621
    return sum(caps.values()), caps


def primitive_root(prime: int) -> int:
    factors: set[int] = set()
    value = prime - 1
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.add(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.add(value)
    for candidate in range(2, prime):
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError("primitive root not found")


def moment_and_vandermonde_check() -> int:
    prime, order = 97, 16
    omega = pow(primitive_root(prime), (prime - 1) // order, prime)
    eta = omega * omega % prime
    values = [1, 0, -1, 0, 1, -1, 0, 0, -1, 0, 0, 1, 0, 1, -1, 0]
    half = order // 2
    defect = [values[index] + values[index + half] for index in range(half)]
    for moment in range(half):
        full = sum(
            value * pow(omega, 2 * moment * index, prime)
            for index, value in enumerate(values)
        ) % prime
        collapsed = sum(
            value * pow(eta, moment * index, prime)
            for index, value in enumerate(defect)
        ) % prime
        assert full == collapsed

    determinants = 0
    points = [pow(eta, index, prime) for index in range(half)]
    for size in range(1, 6):
        for support in combinations(points, size):
            determinant = 1
            for left, right in combinations(support, 2):
                determinant = determinant * (right - left) % prime
            assert determinant
            determinants += 1
    return determinants


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join((base / name).read_text() for name in required if name.endswith(".md"))
    for marker in (
        "Y_3=4((d+1)R-d)",
        "x<=1",
        "v_h=floor((h-1)/2)+2",
        "square Vandermonde matrix",
        "E_h^prim(m,p)=0",
        "2,677,220,820",
        "not a payment",
    ):
        assert marker in text


def main() -> None:
    cells, caps = endpoint_check()
    determinants = moment_and_vandermonde_check()
    packet_check()
    print(
        "F3_HGE4_VANDERMONDE_DEFECT_BAND_EXCLUSION_PASS "
        f"cells={cells} first_level={min(caps)} top_defect={caps[41]} "
        f"vandermonde_determinants={determinants}"
    )


if __name__ == "__main__":
    main()
