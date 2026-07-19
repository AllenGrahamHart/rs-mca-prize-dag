#!/usr/bin/env python3
"""Verify the full exceptional-only reciprocal square descent."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_full_reciprocal_square_descent"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_exceptional_only_full_reciprocal_complement"
CONSUMER = "rate_half_band_closure"


def trim(poly: list[int], p: int) -> list[int]:
    out = [value % p for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(left: list[int], right: list[int], p: int) -> list[int]:
    size = max(len(left), len(right))
    out = [0] * size
    for index in range(size):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % p
    return trim(out, p)


def scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return trim([scalar * value for value in poly], p)


def multiply(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] += left_value * right_value
    return trim(out, p)


def subtract(left: list[int], right: list[int], p: int) -> list[int]:
    return add(left, scale(right, -1, p), p)


def degree_check() -> None:
    profiles = 0
    for e in range(3, 256):
        r = 2 * e + 1
        d_0 = 8 * e + 7
        n_x = d_0 - 1
        exponent = n_x + r - 1
        assert exponent == 10 * e + 6
        assert (r - 1) + d_0 == r + n_x
        assert r + (n_x - 1) == exponent
        profiles += 1
    assert profiles == 253


def polynomial_fixture() -> None:
    p = 101
    exceptional, p_cl, j_inf = 3, 5, 7
    exponent = 3

    f = [6, 2, 1]
    g = [87, 4, 3, 1]
    ell = [26, 16, 3]
    u = [29]
    r_x = [1, 37, 44]
    w_vee = [85, 4]
    k_vee = [71, 91, 3]
    s_form = [99, 9]
    v_vee = [70, 41]

    assert add(scale(f, j_inf, p), scale(g, exceptional, p), p) == [0] + ell
    assert add(multiply(f, u, p), scale(ell, p_cl, p), p) == r_x

    unit_rhs = [0] * (exponent + 1) + [1]
    assert subtract(multiply(w_vee, g, p), multiply(f, k_vee, p), p) == unit_rhs
    assert add(scale(w_vee, j_inf, p), scale(k_vee, exceptional, p), p) == [0] + s_form

    reduced_rhs = [0] * exponent + [exceptional]
    assert subtract(multiply(ell, w_vee, p), multiply(f, s_form, p), p) == reduced_rhs
    assert add(add(v_vee, multiply(u, w_vee, p), p), scale(s_form, p_cl, p), p) == [0]

    first_rhs = [0] * exponent + [p_cl * exceptional]
    assert add(multiply(f, v_vee, p), multiply(r_x, w_vee, p), p) == first_rhs

    mutated = w_vee[:]
    mutated[0] += 1
    assert subtract(multiply(ell, mutated, p), multiply(f, s_form, p), p) != reduced_rhs


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
        "L W_vee-F S=E Y^N",
        "V_vee+U W_vee+P_cl S=0",
        "K_vee=(YS-j_infW_vee)/E",
        "allocate only `F,U,W_vee,S`",
    ):
        assert marker in statement
    for marker in (
        "W_vee G-FK_vee=Y^(r+n_X)",
        "cancel `Y`",
        "R_X=FU+P_clL",
        "The polynomial ring is a domain",
    ):
        assert marker in proof


def main() -> None:
    degree_check()
    polynomial_fixture()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_FULL_RECIPROCAL_SQUARE_PASS "
        "profiles=253 fixture=1 identities=6 mutation=1"
    )


if __name__ == "__main__":
    main()
