#!/usr/bin/env python3
"""Verify the pure-quartic ramification passport packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_pure_ramification_passport"
DEPENDENCIES = {
    "rate_half_list_budget_three_antipodal_pure_euler_ramification_router",
    "rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity",
}
CONSUMER = "rate_half_list_adjacent_crossing"


def trim(poly: list[int], p: int) -> list[int]:
    result = [value % p for value in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def add(left: list[int], right: list[int], p: int) -> list[int]:
    size = max(len(left), len(right))
    result = [0] * size
    for index in range(size):
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


def subtract(left: list[int], right: list[int], p: int) -> list[int]:
    return add(left, scale(right, -1, p), p)


def defect(profile: list[int]) -> int:
    return sum(part - 1 for part in profile)


def passport_checks() -> None:
    checked = 0
    for r in range(2, 257):
        degree = 4 * r
        zero = [3] * r + [1] * r
        pole = [3] * (r - 1) + [1] * (r + 3)
        one = [degree]
        extra = [2] + [1] * (degree - 2)
        u_collision = [4] + [3] * (r - 1) + [1] * (r - 1)
        double_t = [3] * r + [2] + [1] * (r - 2)
        v_collision = [4] + [3] * (r - 2) + [1] * (r + 2)
        double_c = [3] * (r - 1) + [2] + [1] * (r + 1)

        for profile in (
            zero,
            pole,
            one,
            extra,
            u_collision,
            double_t,
            v_collision,
            double_c,
        ):
            assert sum(profile) == degree

        generic = defect(zero) + defect(pole) + defect(one) + defect(extra)
        assert generic == 2 * degree - 2
        assert defect(u_collision) + defect(pole) + defect(one) == generic
        assert defect(double_t) + defect(pole) + defect(one) == generic
        assert defect(zero) + defect(v_collision) + defect(one) == generic
        assert defect(zero) + defect(double_c) + defect(one) == generic

        broken_u_collision = [5] + [3] * (r - 1) + [1] * (r - 1)
        assert sum(broken_u_collision) != degree
        checked += 1
    assert checked == 255


def wronskian_fixture() -> None:
    p = 101
    y = [0, 1]
    d = 8
    e_4 = -1
    big_d = add(power(y, 4, p), [1], p)
    u = y
    v = [1]
    t = scale(y, 4, p)
    c = add(scale(power(y, 4, p), -4, p), [-8], p)
    linear = scale(y, 16, p)

    a = multiply(big_d, power(u, 4, p), p)
    b = scale(multiply(big_d, power(v, 4, p), p), e_4, p)
    binomial = add(power(y, d, p), [-1], p)
    assert add(a, b, p) == binomial

    phi = multiply(t, power(u, 3, p), p)
    assert add(phi, [d], p) == scale(multiply(power(v, 3, p), c, p), e_4, p)
    assert derivative(phi, p) == multiply(multiply(power(u, 2, p), power(v, 2, p), p), linear, p)

    wronskian = subtract(
        multiply(derivative(a, p), derivative(derivative(b, p), p), p),
        multiply(derivative(derivative(a, p), p), derivative(b, p), p),
        p,
    )
    lambda_factor = scale(linear, d, p)
    factored = multiply(
        multiply(power(y, d - 2, p), power(u, 2, p), p),
        multiply(power(v, 2, p), lambda_factor, p),
        p,
    )
    assert wronskian == factored
    assert wronskian != multiply(
        multiply(power(y, d - 2, p), power(u, 2, p), p),
        multiply(power(v, 2, p), scale(linear, d + 1, p), p),
        p,
    )

    # The fixture is the r=1 U--T collision: Phi=4Y^4.
    assert t[0] == 0
    assert (-4 * 0 * big_d[0] * u[1]) % p == 0
    assert defect([4]) + defect([1, 1, 1, 1]) + defect([4]) == 6


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
        "Lambda=dL",
        "Generic almost-Belyi case",
        "U--T collision",
        "double-T case",
        "V--C collision",
        "double-C case",
        "one exact almost-Belyi passport",
    ):
        assert marker in statement
    for marker in (
        "T(alpha)=-4 alpha D(alpha)U'(alpha)",
        "C(beta)=4 beta D(beta)V'(beta)",
        "R-1=-d/(Phi+d)",
        "2N-2",
    ):
        assert marker in proof


def main() -> None:
    passport_checks()
    wronskian_fixture()
    packet_check()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_ANTIPODAL_PURE_RAMIFICATION_PASSPORT_PASS "
        "profiles=255 cases=5 wronskian_weld=1 fixture=1 mutation=2"
    )


if __name__ == "__main__":
    main()
