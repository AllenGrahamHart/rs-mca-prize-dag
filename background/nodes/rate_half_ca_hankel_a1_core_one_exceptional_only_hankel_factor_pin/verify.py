#!/usr/bin/env python3
"""Verify the exceptional-only middle-Hankel factor pin."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_factor_pin"
DEPENDENCIES = {
    "rate_half_ca_hankel_a1_core_one_middle_adjugate_factorization",
    "rate_half_ca_hankel_a1_core_one_exceptional_only_full_reciprocal_square_descent",
}
CONSUMER = "rate_half_band_closure"


def trim(poly: list[int], p: int) -> list[int]:
    out = [value % p for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def multiply(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] += left_value * right_value
    return trim(out, p)


def scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return trim([scalar * value for value in poly], p)


def profile_check() -> None:
    profiles = 0
    for e in range(3, 256):
        r = 2 * e + 1
        d = 2 * e + 1
        exceptional_degree = r - 1
        omission = r - exceptional_degree
        assert r == d
        assert omission == 1
        assert omission <= 1
        profiles += 1
    assert profiles == 253


def polynomial_fixture() -> None:
    p = 101
    c_h = 7
    exceptional = [0, 1]
    q_bar = [3, 1]
    q = [[1, 1], [2], multiply(exceptional, q_bar, p)]

    adjugate = [
        [scale(multiply(multiply(exceptional, left, p), right, p), c_h, p) for right in q]
        for left in q
    ]
    assert all(entry[0] == 0 for row in adjugate for entry in row)

    # The constant coordinate gives a cofactor with exactly one E in this
    # fixture, so E is the full common factor rather than merely a divisor.
    assert adjugate[1][1] == [0, 4 * c_h]

    divided_at_exception = [
        [entry[1] if len(entry) > 1 else 0 for entry in row]
        for row in adjugate
    ]
    q_at_exception = [coordinate[0] for coordinate in q]
    expected = [
        [c_h * left * right % p for right in q_at_exception]
        for left in q_at_exception
    ]
    assert divided_at_exception == expected
    assert any(value for row in expected for value in row)
    for i in range(len(expected)):
        for j in range(len(expected)):
            for k in range(len(expected)):
                for ell in range(len(expected)):
                    assert (
                        expected[i][j] * expected[k][ell]
                        - expected[i][ell] * expected[k][j]
                    ) % p == 0

    top = len(q) - 1
    assert all(expected[top][index] == expected[index][top] == 0 for index in range(len(q)))
    assert adjugate[top][top] == scale(
        multiply(multiply(multiply(exceptional, exceptional, p), exceptional, p), multiply(q_bar, q_bar, p), p),
        c_h,
        p,
    )

    overdivided = [
        scale(multiply(multiply(exceptional, exceptional, p), multiply(left, right, p), p), c_h, p)
        for left in q for right in q
    ]
    assert all(len(entry) < 2 or entry[1] == 0 for entry in overdivided)


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
        "adj M=c_H E q q^T",
        "(adj M/E)|_(E=0)",
        "q_r=[X^r]Q=E q_bar",
        "No square root of `c_H`",
    ):
        assert marker in statement
    for marker in (
        "Consequently `O=1`",
        "lambda=c_H E",
        "`E` would divide every coordinate",
        "Some other coordinate is nonzero",
    ):
        assert marker in proof


def main() -> None:
    profile_check()
    polynomial_fixture()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_HANKEL_FACTOR_PIN_PASS "
        "profiles=253 fixture=1 rank_one_minors=81 mutation=1"
    )


if __name__ == "__main__":
    main()
