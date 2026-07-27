#!/usr/bin/env python3
"""Stdlib exact certificates for the quadratic collision router."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_order_zero_quadratic_collision_router"
PARENT = "l1_mersenne_next_to_maximal_hypergeometric_normal_form"
CONSUMER = "l1_mixed_petal_amplification"
ZERO = [Fraction(0)]
ONE = [Fraction(1)]


def trim(a: list[Fraction]) -> list[Fraction]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return trim(out)


def neg(a: list[Fraction]) -> list[Fraction]:
    return [-value for value in a]


def sub(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    return add(a, neg(b))


def mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return trim(out)


def scale(a: list[Fraction], c: Fraction | int) -> list[Fraction]:
    return trim([Fraction(c) * value for value in a])


def rising(r: int) -> list[Fraction]:
    out = ONE
    for j in range(r):
        out = mul(out, [Fraction(j), Fraction(1)])
    return scale(out, Fraction(1, math.factorial(r)))


def wtrim(a: list[list[Fraction]]) -> list[list[Fraction]]:
    while len(a) > 1 and a[-1] == ZERO:
        a.pop()
    return a


def wadd(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    out = [ZERO[:] for _ in range(max(len(a), len(b)))]
    for i, value in enumerate(a):
        out[i] = add(out[i], value)
    for i, value in enumerate(b):
        out[i] = add(out[i], value)
    return wtrim(out)


def wsub(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return wadd(a, [neg(value) for value in b])


def wscale(a: list[list[Fraction]], c: list[Fraction]) -> list[list[Fraction]]:
    return wtrim([mul(value, c) for value in a])


def wshift(a: list[list[Fraction]], d: int) -> list[list[Fraction]]:
    return [ZERO[:] for _ in range(d)] + [value[:] for value in a]


def divide_monic(dividend: list[list[Fraction]], divisor: list[list[Fraction]]) -> list[list[Fraction]]:
    assert divisor[-1] == ONE
    rem = [value[:] for value in dividend]
    degree = len(divisor) - 1
    while len(rem) - 1 >= degree:
        shift = len(rem) - 1 - degree
        lead = rem[-1]
        rem = wsub(rem, wshift(wscale(divisor, lead), shift))
    rem += [ZERO[:] for _ in range(degree - len(rem))]
    return rem


def pseudo_remainder(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    rem = [value[:] for value in a]
    degree = len(b) - 1
    lead_b = b[-1]
    while len(rem) - 1 >= degree:
        shift = len(rem) - 1 - degree
        lead_r = rem[-1]
        rem = wsub(wscale(rem, lead_b), wshift(wscale(b, lead_r), shift))
    return rem


def p_s(h: int) -> list[list[Fraction]]:
    out = [ZERO[:] for _ in range(h + 1)]
    for r in range(h + 1):
        out[h - r] = rising(r)
    return out


def verify_weighted_derivative(h: int) -> None:
    locator = p_s(h)
    derivative = [scale(locator[i], i) for i in range(1, len(locator))]
    lhs = wsub(wshift(derivative, 2), wshift(derivative, 1))

    rhs = wadd(
        wshift(wscale(locator, [Fraction(h)]), 1),
        wscale(locator, [Fraction(-h), Fraction(-1)]),
    )
    rhs[0] = add(rhs[0], mul([Fraction(h), Fraction(1)], locator[0]))
    assert wtrim(lhs) == wtrim(rhs)


def reflection_remainder(m: int) -> list[list[Fraction]]:
    h = m - 1
    q = [ZERO[:] for _ in range(2 * m + 1)]
    q[0] = [Fraction(-1)]
    for j in range(m + 1):
        q[m + j] = [Fraction((-1) ** j * math.comb(m, j))]
    return divide_monic(q, p_s(h))


def linear_factor(j: int) -> list[Fraction]:
    return [Fraction(j), Fraction(1)]


def product_factors(factors: list[int], scalar: Fraction) -> list[Fraction]:
    out = [scalar]
    for j in factors:
        out = mul(out, linear_factor(j))
    return out


def expected_reflection(m: int) -> list[Fraction]:
    if m == 8:
        return product_factors(list(range(8)) + [3, 4], Fraction(1, 22400))
    if m == 16:
        return product_factors(list(range(16)) + [7, 8], Fraction(17, 188305108992000))
    raise AssertionError(m)


def antipodal_prem() -> list[list[Fraction]]:
    b = [rising(r) for r in range(8)]
    odd = [b[6], b[4], b[2], b[0]]
    even = [b[7], b[5], b[3], b[1]]
    s_poly = [Fraction(0), Fraction(1)]
    reduced = wsub(even, wscale(odd, s_poly))
    return pseudo_remainder(odd, reduced)


def expected_antipodal_y() -> list[Fraction]:
    factors = [0, 0, -3, -2, -1, -1, 1, 1, 2, 3]
    return product_factors(factors, Fraction(-1, 4725))


def main() -> None:
    for m in (8, 16):
        verify_weighted_derivative(m - 1)
        rem = reflection_remainder(m)
        assert rem[m - 2] == expected_reflection(m)

    prem = antipodal_prem()
    assert len(prem) <= 2
    assert prem[1] == expected_antipodal_y()

    atlas = ROOT / "background/nodes/l1_official_checkpoint_characteristic_atlas/checkpoint_atlas.tsv"
    rows = []
    for line in atlas.read_text().splitlines()[1:]:
        _, n, p, _, m, remainder = map(int, line.split("\t"))
        if m in (8, 16) and remainder == m:
            rows.append((n, p, m))
    assert len(rows) == 5
    for n, p, m in rows:
        assert n == m * (p + 1)
        denominators = (22400, 4725) if m == 8 else (188305108992000,)
        assert all(math.gcd(p, denominator) == 1 for denominator in denominators)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = Path(__file__).with_name("statement.md").read_text()
    proof = Path(__file__).with_name("proof.md").read_text()
    assert "at most one color is repeated" in statement
    assert "The theorem does not exclude a quadratic interpolant" in statement
    assert "(A,B)=(1,0)" in proof and "(A,B)=(-1,1)" in proof

    mutations = 0
    wrong = expected_reflection(8)
    wrong[0] += 1
    mutations += reflection_remainder(8)[6] != wrong
    wrong = expected_antipodal_y()
    wrong[-1] *= -1
    mutations += prem[1] != wrong
    assert mutations == 2

    print(
        "L1_MERSENNE_HNF_ORDER_ZERO_QUADRATIC_COLLISION_ROUTER_PASS "
        f"rows={len(rows)} reflection=2 antipodal=1 mutations={mutations}"
    )


if __name__ == "__main__":
    main()
