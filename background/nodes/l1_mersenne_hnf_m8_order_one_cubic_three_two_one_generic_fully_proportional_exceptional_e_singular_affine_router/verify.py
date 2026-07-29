#!/usr/bin/env python3
"""Check the exceptional-E singular-affine polynomial compiler."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_singular_affine_router"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_quadratic_router"
CONSUMER = "l1_mixed_petal_amplification"
PRIMES = (8191, 131071, 524287, 2147483647)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return trim(out)


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value for value in poly])


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] += left_value * right_value
    return trim(out)


def evaluate(poly: list[int], value: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def polynomial_check() -> None:
    b = [0, 1]
    z = multiply(b, b)
    z_plus_27 = add(z, [27])
    a = add([1575], scale(z, -247))
    c = add(add(scale(multiply(z, z), -800), scale(z, 8929)), [-11025])
    n = add(add(scale(multiply(z, z), 40), scale(z, 51)), [-2835])
    q_coefficient = add(
        add(scale(multiply(z, z), -52800), scale(z, 710097)),
        [-1497825],
    )
    e0 = add(scale(multiply(a, b), 42), multiply(z_plus_27, c))
    e1 = add(
        scale(multiply(a, add(scale(z, 8), [-21])), 15),
        multiply(b, q_coefficient),
    )
    r = add(scale(multiply(b, z_plus_27), 163), scale(n, -1))
    left = add(multiply(z_plus_27, e1), scale(multiply(b, e0), -66))
    right = scale(multiply(a, r), -3)
    assert left == right

    z = [0, 1]
    z_plus_27 = add(z, [27])
    a = add([1575], scale(z, -247))
    c = add(add(scale(multiply(z, z), -800), scale(z, 8929)), [-11025])
    n = add(add(scale(multiply(z, z), 40), scale(z, 51)), [-2835])
    h = add(
        multiply(n, n),
        scale(multiply(z, multiply(z_plus_27, z_plus_27)), -(163**2)),
    )
    k = add(
        scale(multiply(a, n), 42),
        scale(multiply(multiply(z_plus_27, z_plus_27), c), 163),
    )
    assert len(h) - 1 == len(k) - 1 == 4
    assert h[-1] == 1600 and k[-1] == -130400
    assert evaluate(n, -27) == 24948
    assert tuple(24948 % prime for prime in PRIMES) == (375, 24948, 24948, 24948)
    assert all(163 % prime and 126 % prime and 360 % prime for prime in PRIMES)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    base = ROOT / "background" / "nodes" / NODE
    refs = set(nodes[NODE]["refs"])
    for name in (
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "lineage.md",
        "upstream_crosswalk.md",
        "verify.py",
        "verify_audit.py",
    ):
        assert str((base / name).relative_to(ROOT)) in refs
    packet = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in ("(FSA4)", "N(z)=40z^2+51z-2835", "H(z)=N(z)^2", "degree four"):
        assert marker in packet


def main() -> None:
    polynomial_check()
    packet_check()
    print(
        "L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_321_EXCEPTIONAL_E_SINGULAR_AFFINE_ROUTER_PASS "
        "quartics=2 degree=4"
    )


if __name__ == "__main__":
    main()
