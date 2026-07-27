#!/usr/bin/env python3
"""Verify the H3 norm-one torus affine quotient cap."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_norm_one_torus_affine_quotient_cap"
DEPENDENCY = "f3_h3_pgl2_pair_identity"
CONSUMERS = {"f3_h3_mobius_excess_half", "f3_h3_dsp8_correlation_bound"}


def add(x: tuple[int, int], y: tuple[int, int], p: int) -> tuple[int, int]:
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)


def mul(
    x: tuple[int, int], y: tuple[int, int], p: int, nonsquare: int
) -> tuple[int, int]:
    return (
        (x[0] * y[0] + nonsquare * x[1] * y[1]) % p,
        (x[0] * y[1] + x[1] * y[0]) % p,
    )


def power(
    x: tuple[int, int], exponent: int, p: int, nonsquare: int
) -> tuple[int, int]:
    answer = (1, 0)
    while exponent:
        if exponent & 1:
            answer = mul(answer, x, p, nonsquare)
        x = mul(x, x, p, nonsquare)
        exponent //= 2
    return answer


def norm(x: tuple[int, int], p: int, nonsquare: int) -> int:
    return (x[0] * x[0] - nonsquare * x[1] * x[1]) % p


def finite_check() -> tuple[int, int, int]:
    p = 31
    squares = {x * x % p for x in range(p)}
    nonsquare = next(x for x in range(2, p) if x not in squares)
    field = [(a, b) for a in range(p) for b in range(p)]
    torus = {x for x in field if norm(x, p, nonsquare) == 1}
    assert len(torus) == p + 1
    subgroup = {x for x in torus if power(x, 16, p, nonsquare) == (1, 0)}
    assert len(subgroup) == 16

    one = (1, 0)
    maximum = 0
    sharp = 0
    for t in field:
        if t in {(0, 0), one}:
            continue
        count = 0
        for z in subgroup:
            w = add(one, mul(t, add(z, (-1, 0), p), p, nonsquare), p)
            count += w in subgroup
        assert count <= 2
        assert one in subgroup
        maximum = max(maximum, count)
        sharp += count == 2
    assert maximum == 2 and sharp > 0
    return len(subgroup), maximum, sharp


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    for consumer in CONSUMERS:
        assert (NODE, consumer, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    compact = "".join(statement.split())
    for marker in (
        "I_(a,b)<=2",
        "R(t)=I_aff(t)-1<=1",
        "n=2^21",
        "17X_18<17n^2<300n^2",
        "notthedeployedMersenne-31Chebyshevlineround",
    ):
        assert marker in compact

    p_m = 2**31 - 1
    n = 2**21
    assert p_m + 1 == 2**31
    assert (p_m + 1) % n == 0
    assert (p_m**2 - 1) % n == 0
    assert (p_m - 1) % n != 0
    assert 17 * (n - 1) ** 2 < 17 * n**2 < 300 * n**2


def main() -> None:
    order, maximum, sharp = finite_check()
    packet_check()
    print(
        "F3_H3_NORM_ONE_TORUS_AFFINE_QUOTIENT_CAP_PASS "
        f"toy_order={order} max_affine={maximum} sharp_targets={sharp}"
    )


if __name__ == "__main__":
    main()
