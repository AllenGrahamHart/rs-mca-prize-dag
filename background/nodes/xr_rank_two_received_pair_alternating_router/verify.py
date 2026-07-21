#!/usr/bin/env python3
"""Verify the XR received-pair alternating router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_rank_two_received_pair_alternating_router"
PARENTS = {
    "xr_higher_rank_uniform_split_pencil_reduction",
    "xr_rank_two_three_anchor_grs3_factorization",
    "xr_rank_two_four_anchor_quadric_centroid_atlas",
}
CONSUMER = "xr_highcore_collision_count"
PRIME = 1009


def rank_mod(matrix: list[list[int]]) -> int:
    rows = [[entry % PRIME for entry in row] for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next(
            (i for i in range(rank, len(rows)) if rows[i][column]), None
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, PRIME)
        rows[rank] = [(entry * inverse) % PRIME for entry in rows[rank]]
        for i in range(len(rows)):
            if i == rank:
                continue
            factor = rows[i][column]
            if factor:
                rows[i] = [
                    (x - factor * y) % PRIME
                    for x, y in zip(rows[i], rows[rank])
                ]
        rank += 1
    return rank


def evaluate(poly: list[int], point: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % PRIME
    return value


def locator_derivative(domain: list[int], point: int) -> int:
    product = 1
    for other in domain:
        if other != point:
            product = product * (point - other) % PRIME
    return product


def pairing(poly: list[int], function: dict[int, int], domain: list[int]) -> int:
    return sum(
        evaluate(poly, point)
        * function[point]
        * pow(locator_derivative(domain, point), -1, PRIME)
        for point in domain
    ) % PRIME


def solve_two_by_two(
    a: int, b: int, c: int, d: int, first: int, second: int
) -> tuple[int, int]:
    determinant = (a * d - b * c) % PRIME
    assert determinant
    inverse = pow(determinant, -1, PRIME)
    x = (d * first - b * second) * inverse % PRIME
    y = (-c * first + a * second) * inverse % PRIME
    return x, y


def function_with_pairings(
    p: list[int],
    q: list[int],
    domain: list[int],
    target_p: int,
    target_q: int,
    seed: int | None = None,
) -> dict[int, int]:
    values = {point: 0 for point in domain}
    if seed is not None:
        values[seed] = 1
    residual_p = (target_p - pairing(p, values, domain)) % PRIME
    residual_q = (target_q - pairing(q, values, domain)) % PRIME
    candidates = [point for point in domain if point != seed]
    for index, x in enumerate(candidates):
        for y in candidates[index + 1 :]:
            p_x = evaluate(p, x) * pow(locator_derivative(domain, x), -1, PRIME) % PRIME
            p_y = evaluate(p, y) * pow(locator_derivative(domain, y), -1, PRIME) % PRIME
            q_x = evaluate(q, x) * pow(locator_derivative(domain, x), -1, PRIME) % PRIME
            q_y = evaluate(q, y) * pow(locator_derivative(domain, y), -1, PRIME) % PRIME
            if (p_x * q_y - p_y * q_x) % PRIME:
                values[x], values[y] = solve_two_by_two(
                    p_x, p_y, q_x, q_y, residual_p, residual_q
                )
                assert pairing(p, values, domain) == target_p % PRIME
                assert pairing(q, values, domain) == target_q % PRIME
                return values
    raise AssertionError("no independent evaluation pair")


def add_functions(
    left: dict[int, int], right: dict[int, int], scalar: int
) -> dict[int, int]:
    return {point: (left[point] + scalar * right[point]) % PRIME for point in left}


def add_polys(left: list[int], right: list[int], scalar: int) -> list[int]:
    size = max(len(left), len(right))
    return [
        ((left[i] if i < len(left) else 0) + scalar * (right[i] if i < len(right) else 0))
        % PRIME
        for i in range(size)
    ]


def barycentric_weights(points: list[int]) -> list[int]:
    result = []
    for i, point in enumerate(points):
        result.append(pow(locator_derivative(points, point), -1, PRIME))
    return result


def three_anchor_fixture(domain: list[int], p: list[int], q: list[int]) -> int:
    eta = 37
    b = function_with_pairings(p, q, domain, 0, -eta)
    received_q = function_with_pairings(p, q, domain, eta, 0)
    interaction = [
        pairing(p, b, domain),
        pairing(p, received_q, domain),
        pairing(q, b, domain),
        pairing(q, received_q, domain),
    ]
    assert interaction == [0, eta, PRIME - eta, 0]

    slopes = list(range(1, 7))
    scales = barycentric_weights(slopes)
    checked = 0
    for slope, scale in zip(slopes, scales):
        numerator = [scale * entry % PRIME for entry in add_polys(p, q, slope)]
        direction = add_functions(b, received_q, slope)
        assert pairing(numerator, direction, domain) == 0
        checked += 1
    broken = b.copy()
    broken[domain[-1]] = (broken[domain[-1]] + 1) % PRIME
    assert any(
        pairing(
            [scale * entry % PRIME for entry in add_polys(p, q, slope)],
            add_functions(broken, received_q, slope),
            domain,
        )
        for slope, scale in zip(slopes, scales)
    )
    return checked


def four_anchor_fixture(domain: list[int], f: list[int], g: list[int]) -> int:
    b = function_with_pairings(f, g, domain, 0, 0, seed=domain[4])
    received_q = function_with_pairings(f, g, domain, 0, 0, seed=domain[5])
    assert any(b.values()) and any(received_q.values())
    assert [
        pairing(f, b, domain),
        pairing(g, b, domain),
        pairing(f, received_q, domain),
        pairing(g, received_q, domain),
    ] == [0, 0, 0, 0]

    slopes = list(range(11, 18))
    scales = barycentric_weights(slopes)
    columns = [
        [scale, scale * slope * slope % PRIME, scale * slope % PRIME, scale * slope**3 % PRIME]
        for slope, scale in zip(slopes, scales)
    ]
    assert rank_mod([list(row) for row in zip(*columns)]) == 4
    assert [sum(column[row] for column in columns) % PRIME for row in range(4)] == [0, 0, 0, 0]

    checked = 0
    for slope, scale in zip(slopes, scales):
        parameter = slope * slope % PRIME
        numerator = [scale * entry % PRIME for entry in add_polys(f, g, parameter)]
        direction = add_functions(b, received_q, slope)
        assert pairing(numerator, direction, domain) == 0
        checked += 1
    broken = received_q.copy()
    broken[domain[-1]] = (broken[domain[-1]] + 1) % PRIME
    assert any(
        pairing(
            [scale * entry % PRIME for entry in add_polys(f, g, slope * slope % PRIME)],
            add_functions(b, broken, slope),
            domain,
        )
        for slope, scale in zip(slopes, scales)
    )
    return checked


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "<U,f>_X=sum_(xinX)U(x)f(x)/Lambda'_X(x)",
        "annihilateseverySegrecoefficientcolumn`v_i`",
        "<P,b>_X=0",
        "<P,q>_X+<Q,b>_X=0",
        "((0,eta),(-eta,0))",
        "perfect-pairingbranch",
        "<F,b>_X=<G,b>_X=<F,q>_X=<G,q>_X=0",
        "onlyfortheselectedtrade-rowparityconditions",
    ):
        assert marker in statement


def main() -> None:
    domain = list(range(20, 31))
    first = [3, 5, 7, 2]
    second = [11, 13, 17, 1]
    q3 = three_anchor_fixture(domain, first, second)
    q4 = four_anchor_fixture(domain, first, second)
    packet_check()
    print(
        "XR_RANK_TWO_RECEIVED_PAIR_ALTERNATING_ROUTER_PASS "
        f"q3_rows={q3} q4_rows={q4}"
    )


if __name__ == "__main__":
    main()
