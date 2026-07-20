#!/usr/bin/env python3
"""Verify the pure Euler ramification router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_pure_euler_ramification_router"
DEPENDENCIES = {
    "rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity",
    "rate_half_list_budget_three_antipodal_reverse_residual_stratification",
}
CONSUMER = "rate_half_list_adjacent_crossing"


def trim(poly: list[int], p: int) -> list[int]:
    result = [value % p for value in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def add(left: list[int], right: list[int], p: int) -> list[int]:
    size = max(len(left), len(right))
    return trim(
        [
            (left[i] if i < len(left) else 0)
            + (right[i] if i < len(right) else 0)
            for i in range(size)
        ],
        p,
    )


def scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return trim([scalar * value for value in poly], p)


def multiply(left: list[int], right: list[int], p: int) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % p
    return trim(result, p)


def derivative(poly: list[int], p: int) -> list[int]:
    if len(poly) == 1:
        return [0]
    return trim([i * poly[i] for i in range(1, len(poly))], p)


def shift(poly: list[int], amount: int, p: int) -> list[int]:
    return trim([0] * amount + poly, p)


def divide_exact(numerator: list[int], denominator: list[int], p: int) -> list[int]:
    work = trim(numerator, p)
    divisor = trim(denominator, p)
    quotient = [0] * max(1, len(work) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, p)
    while len(work) >= len(divisor) and work != [0]:
        degree = len(work) - len(divisor)
        factor = work[-1] * inverse % p
        quotient[degree] = factor
        for index, value in enumerate(divisor):
            work[index + degree] = (work[index + degree] - factor * value) % p
        work = trim(work, p)
    assert work == [0]
    return trim(quotient, p)


def gcd_poly(left: list[int], right: list[int], p: int) -> list[int]:
    a, b = trim(left, p), trim(right, p)
    while b != [0]:
        work = a[:]
        inverse = pow(b[-1], -1, p)
        while len(work) >= len(b) and work != [0]:
            degree = len(work) - len(b)
            factor = work[-1] * inverse % p
            for index, value in enumerate(b):
                work[index + degree] = (work[index + degree] - factor * value) % p
            work = trim(work, p)
        a, b = b, work
    inverse = pow(a[-1], -1, p)
    return scale(a, inverse, p)


def profile_check() -> None:
    r = (1 << 37) - 1
    d = 4 * r + 4
    v = r - 1
    assert d == 1 << 39
    assert 4 * r == d - 4
    assert r + 3 == (1 << 37) + 2
    assert 2 * r - 1 == 2 * v + 1


def finite_fixture() -> None:
    p = 101
    d = 8
    e_4 = -1
    # (Y^4+1)(Y^4-1)=Y^8-1.
    d_poly = [1, 0, 0, 0, 1]
    u = [0, 1]
    v = [1]

    t = add(
        scale(multiply(d_poly, u, p), d, p),
        scale(shift(add(multiply(derivative(d_poly, p), u, p), scale(multiply(d_poly, derivative(u, p), p), 4, p), p), 1, p), -1, p),
        p,
    )
    c = add(
        scale(shift(multiply(d_poly, derivative(v, p), p), 1, p), 4, p),
        multiply(v, add(shift(derivative(d_poly, p), 1, p), scale(d_poly, -d, p), p), p),
        p,
    )
    assert t == [0, 4]
    assert c == [p - 8, 0, 0, 0, p - 4]

    left = add(multiply(t, multiply(multiply(u, u, p), u, p), p), [d], p)
    right = scale(multiply(multiply(multiply(v, v, p), v, p), c, p), e_4, p)
    assert left == right == [8, 0, 0, 0, 4]
    assert gcd_poly(multiply(t, u, p), multiply(v, c, p), p) == [1]

    w = add(multiply(derivative(t, p), u, p), scale(multiply(t, derivative(u, p), p), 3, p), p)
    v_square = multiply(v, v, p)
    linear = divide_exact(w, v_square, p)
    assert linear == [0, 16]

    z = add(scale(multiply(derivative(v, p), c, p), 3, p), multiply(v, derivative(c, p), p), p)
    assert scale(z, e_4, p) == multiply(multiply(u, u, p), linear, p)
    phi_prime = derivative(multiply(t, multiply(multiply(u, u, p), u, p), p), p)
    assert phi_prime == multiply(multiply(multiply(u, u, p), v_square, p), linear, p)

    broken_c = c[:]
    broken_c[0] += 1
    broken = scale(multiply(multiply(multiply(v, v, p), v, p), broken_c, p), e_4, p)
    assert broken != left


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    proof = (here / "proof.md").read_text()
    for marker in (
        "T U^3+d=e_4 V^3 C",
        "(TU^3)'=U^2V^2L",
        "at most three finite critical values",
        "does not classify",
    ):
        assert marker in statement
    for marker in (
        "The converse is also exact",
        "(4r-d)v_0=-4v_0",
        "defects are confined to one point",
    ):
        assert marker in proof


def main() -> None:
    profile_check()
    finite_fixture()
    packet_check()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_ANTIPODAL_PURE_EULER_RAMIFICATION_ROUTER_PASS "
        "official=1 fixture=1 converse=1 critical_linear=1 mutation=1"
    )


if __name__ == "__main__":
    main()
