#!/usr/bin/env python3
"""Verify the exceptional-only reciprocal-resultant descent."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_reciprocal_resultant_descent"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_exceptional_only_unit_resultant_collapse"
CONSUMER = "rate_half_band_closure"


def trim(poly: list[int], p: int) -> list[int]:
    out = [coefficient % p for coefficient in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_divmod(left: list[int], right: list[int], p: int) -> tuple[list[int], list[int]]:
    remainder = trim(left, p)
    divisor = trim(right, p)
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, p)
    while len(remainder) >= len(divisor) and remainder != [0]:
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1] * inverse % p
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            remainder[index + shift] -= coefficient * value
        remainder = trim(remainder, p)
    return trim(quotient, p), remainder


def poly_gcd(left: list[int], right: list[int], p: int) -> list[int]:
    left, right = trim(left, p), trim(right, p)
    while right != [0]:
        _, remainder = poly_divmod(left, right, p)
        left, right = right, remainder
    inverse = pow(left[-1], -1, p)
    return trim([inverse * coefficient for coefficient in left], p)


def parity_and_scalar_check() -> None:
    p = 1013
    c_x, exceptional, q_bar = 17, 19, 23
    profiles = 0
    for e in range(3, 256):
        r = 2 * e + 1
        d_0 = 8 * e + 7
        assert r % 2 == d_0 % 2 == 1
        assert (-1) ** (r * d_0) == -1

        res_fg = -c_x * q_bar % p
        res_fc = pow(exceptional, r, p) * res_fg % p
        res_fy = -exceptional * q_bar % p
        res_fl = res_fc * pow(res_fy, -1, p) % p
        assert res_fl == c_x * pow(exceptional, r - 1, p) % p
        assert res_fl != c_x * pow(exceptional, r, p) % p
        profiles += 1
    assert profiles == 253


def coprimality_fixture() -> None:
    p = 1013
    exceptional = [-5, 1]
    other = [-2, 1]
    q_bar = [10, -7, 1]  # (t-5)(t-2), so E need not be coprime to q_bar.
    delta = [7, 1]
    assert poly_gcd(q_bar, delta, p) == [1]

    assert poly_gcd(q_bar, exceptional, p) == trim(exceptional, p)
    assert poly_gcd(q_bar, other, p) == trim(other, p)
    assert poly_gcd(q_bar, exceptional, p) != [1]
    assert poly_gcd(q_bar, other, p) != [1]


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
        "C(t,Y)=j_inf F(t,Y)+E G(t,Y)=Y L(t,Y)",
        "Res_Y(F,L)=c_X E^(r-1)",
        "gcd(q_bar,Delta_inf)=1",
        "not an exclusion",
    ):
        assert marker in statement
    for marker in (
        "(-1)^(rD_0)",
        "-E q_bar Res_Y(F,L)",
        "Delta_inf mod E",
        "exact degree `r-1`",
    ):
        assert marker in proof


def main() -> None:
    parity_and_scalar_check()
    coprimality_fixture()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_RECIPROCAL_DESCENT_PASS "
        "profiles=253 sign=checked scalar_mutation=1 gcd_fixture=1"
    )


if __name__ == "__main__":
    main()
