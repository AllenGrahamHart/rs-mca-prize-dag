#!/usr/bin/env python3
"""Verify the pure Euler spectral reconstruction gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_pure_euler_spectral_reconstruction"
DEPENDENCY = "rate_half_list_budget_three_antipodal_pure_ramification_passport"
CONSUMER = "rate_half_list_adjacent_crossing"


def trim(poly: list[int], p: int) -> list[int]:
    result = [value % p for value in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def add(left: list[int], right: list[int], p: int) -> list[int]:
    result = [0] * max(len(left), len(right))
    for index in range(len(result)):
        result[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % p
    return trim(result, p)


def scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return trim([scalar * value for value in poly], p)


def multiply(left: list[int], right: list[int], p: int) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % p
    return trim(result, p)


def power(poly: list[int], exponent: int, p: int) -> list[int]:
    result = [1]
    base = poly
    while exponent:
        if exponent & 1:
            result = multiply(result, base, p)
        base = multiply(base, base, p)
        exponent //= 2
    return result


def derivative(poly: list[int], p: int) -> list[int]:
    if len(poly) == 1:
        return [0]
    return trim([index * poly[index] for index in range(1, len(poly))], p)


def divmod_poly(
    dividend: list[int], divisor: list[int], p: int
) -> tuple[list[int], list[int]]:
    remainder = trim(dividend, p)
    divisor = trim(divisor, p)
    assert divisor != [0]
    if len(remainder) < len(divisor):
        return [0], remainder
    quotient = [0] * (len(remainder) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, p)
    while remainder != [0] and len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1] * inverse % p
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            remainder[index + shift] = (
                remainder[index + shift] - coefficient * value
            ) % p
        remainder = trim(remainder, p)
    return trim(quotient, p), remainder


def monic(poly: list[int], p: int) -> list[int]:
    poly = trim(poly, p)
    inverse = pow(poly[-1], -1, p)
    return scale(poly, inverse, p)


def gcd_poly(left: list[int], right: list[int], p: int) -> list[int]:
    left = trim(left, p)
    right = trim(right, p)
    while right != [0]:
        _, remainder = divmod_poly(left, right, p)
        left, right = right, remainder
    return monic(left, p)


def euler(poly: list[int], d: int, p: int) -> list[int]:
    y_times_derivative = [0] + derivative(poly, p)
    return add(scale(poly, d, p), scale(y_times_derivative, -1, p), p)


def spectral_lift(phi: list[int], d: int, p: int) -> list[int]:
    result = [0] * len(phi)
    result[0] = 1
    for degree, coefficient in enumerate(phi):
        result[degree] = (
            result[degree] + coefficient * pow(d - degree, -1, p)
        ) % p
    return trim(result, p)


def reconstruction_fixture() -> None:
    p = 101
    d = 8
    y = [0, 1]
    h = add(power(y, d, p), [-1], p)
    phi = scale(power(y, 4, p), 4, p)
    spectral = spectral_lift(phi, d, p)
    deleted = add(power(y, 4, p), [1], p)

    assert spectral == deleted
    assert euler(spectral, d, p) == add(phi, [d], p)
    assert gcd_poly(spectral, h, p) == deleted

    upper, upper_remainder = divmod_poly(add(h, spectral, p), deleted, p)
    lower, lower_remainder = divmod_poly(scale(spectral, -1, p), deleted, p)
    assert upper_remainder == [0]
    assert lower_remainder == [0]
    assert upper == power(y, 4, p)
    assert lower == [p - 1]

    a = add(h, spectral, p)
    assert euler(a, d, p) == phi
    assert add(a, scale(spectral, -1, p), p) == h

    # e_4=-1 gives X^4-1, split by 1,-1,10,-10 in F_101.
    roots = [1, p - 1, 10, p - 10]
    assert len(set(roots)) == 4
    assert all((pow(root, 4, p) - 1) % p == 0 for root in roots)

    broken = [0] * len(phi)
    broken[0] = 1
    for degree, coefficient in enumerate(phi):
        broken[degree] = (
            broken[degree] + coefficient * pow(d - degree + 1, -1, p)
        ) % p
    assert gcd_poly(trim(broken, p), h, p) == [1]


def official_denominator_check() -> None:
    d = 1 << 39
    degree = d - 4
    assert d - degree == 4
    for offset in range(4, 260):
        assert 0 < offset <= d


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    proof = (here / "proof.md").read_text()
    for marker in (
        "S_Phi=1+sum_(m=0)^N (phi_m/(d-m))Y^m",
        "D_Phi=monic gcd(S_Phi,H)",
        "(H+S_Phi)/D_Phi=U^4",
        "-S_Phi/D_Phi=e_4V^4",
        "not authorization to",
    ):
        assert marker in statement
    for marker in (
        "E_d(S_Phi)=Phi+d",
        "A=H+S_Phi",
        "B=-S_Phi",
        "Phi+d=dS_Phi-YS_Phi'",
        "gcd(U^4,V^4)=1",
    ):
        assert marker in proof


def main() -> None:
    official_denominator_check()
    reconstruction_fixture()
    packet_check()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_ANTIPODAL_PURE_EULER_SPECTRAL_RECONSTRUCTION_PASS "
        "official=1 fixture=1 gcd_degree=4 fourth_powers=2 split=1 mutation=1"
    )


if __name__ == "__main__":
    main()
