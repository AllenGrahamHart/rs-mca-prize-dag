#!/usr/bin/env python3
"""Verify the HGE4 non-full complement-third gate."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_nonfull_complement_third_gate"
DEPENDENCIES = {
    "f3_hge4_exact_ratio_tower_orbit_compiler",
    "f3_hge4_primitive_shift_pair_near_square_union_router",
}
CONSUMER = "f3_hge4_norm_gate_count"


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    size = max(len(left), len(right))
    out = [0] * size
    for index in range(size):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    return trim(out)


def sub(left: list[int], right: list[int], prime: int) -> list[int]:
    return add(left, [(-value) % prime for value in right], prime)


def scale(poly: list[int], scalar: int, prime: int) -> list[int]:
    return trim([(scalar * value) % prime for value in poly])


def mul(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            out[i + j] = (out[i + j] + first * second) % prime
    return trim(out)


def derivative(poly: list[int], prime: int) -> list[int]:
    return trim([(index * poly[index]) % prime for index in range(1, len(poly))])


def div_exact(numerator: list[int], denominator: list[int], prime: int) -> list[int]:
    remainder = numerator[:]
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    inverse = pow(denominator[-1], -1, prime)
    while len(remainder) >= len(denominator) and remainder != [0]:
        offset = len(remainder) - len(denominator)
        coefficient = remainder[-1] * inverse % prime
        quotient[offset] = coefficient
        for index, value in enumerate(denominator):
            remainder[index + offset] = (
                remainder[index + offset] - coefficient * value
            ) % prime
        trim(remainder)
    assert remainder == [0]
    return trim(quotient)


def locator(roots: tuple[int, ...], prime: int) -> list[int]:
    output = [1]
    for root in roots:
        output = mul(output, [(-root) % prime, 1], prime)
    return output


def subgroup(prime: int, order: int) -> list[int]:
    for generator in range(2, prime):
        if len({pow(generator, exponent, prime) for exponent in range(1, prime)}) == prime - 1:
            omega = pow(generator, (prime - 1) // order, prime)
            return [pow(omega, exponent, prime) for exponent in range(order)]
    raise AssertionError("primitive root not found")


def shift_pairs(order: int, prime: int, width: int) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    points = subgroup(prime, order)
    buckets: dict[tuple[int, ...], list[tuple[tuple[int, ...], frozenset[int]]]] = {}
    for indices in combinations(range(order), width):
        roots = tuple(points[index] for index in indices)
        polynomial = locator(roots, prime)
        buckets.setdefault(tuple(polynomial[1:]), []).append((roots, frozenset(indices)))
    output = []
    for bucket in buckets.values():
        for first, second in combinations(bucket, 2):
            if first[1].isdisjoint(second[1]):
                output.append((first[0], second[0]))
    return output


def algebra_fixture() -> tuple[int, int]:
    prime, order, width = 17, 16, 4
    pairs = shift_pairs(order, prime, width)
    assert pairs
    left, right = pairs[0]
    p_poly = locator(left, prime)
    q_poly = locator(right, prime)
    difference = sub(q_poly, p_poly, prime)
    assert len(difference) == 1 and difference[0] != 0
    d_value = difference[0]

    x_power_minus_one = [(-1) % prime] + [0] * (order - 1) + [1]
    r_poly = div_exact(x_power_minus_one, mul(p_poly, q_poly, prime), prime)
    complement = len(r_poly) - 1
    assert complement == order - 2 * width == 8 and width <= complement

    h_poly = scale(
        mul([0, 1], mul(derivative(p_poly, prime), r_poly, prime), prime),
        d_value * pow(order, -1, prime),
        prime,
    )
    a_poly = div_exact(sub(h_poly, [1], prime), p_poly, prime)
    b_poly = div_exact(add(h_poly, [1], prime), q_poly, prime)
    assert len(a_poly) - 1 == len(b_poly) - 1 == complement
    assert a_poly[-1] == b_poly[-1] == d_value * width * pow(order, -1, prime) % prime
    identity = add(
        mul(p_poly, sub(b_poly, a_poly, prime), prime),
        scale(b_poly, d_value, prime),
        prime,
    )
    assert identity == [2]
    return len(pairs), complement


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
        "H=(d/m) X P' R", "h<=c", "3h<m", "E_h^prim(m,p)=0",
        "floor((m-1)/3)", "Non-fullness is load-bearing",
    ):
        assert marker in text


def main() -> None:
    pair_count, complement = algebra_fixture()
    empty_widths = []
    for width in (6, 7):
        assert 3 * width >= 16
        assert not shift_pairs(16, 17, width)
        empty_widths.append(width)
    packet_check()
    print(
        "F3_HGE4_NONFULL_COMPLEMENT_THIRD_GATE_PASS "
        f"boundary_pairs={pair_count} complement={complement} empty_widths={empty_widths}"
    )


if __name__ == "__main__":
    main()
