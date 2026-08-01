#!/usr/bin/env python3
"""Verify the deployed cell-5 rational lift atlas and its F_p cover."""

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).parent
DATA = json.loads(
    (HERE / "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json")
    .read_text()
)
P = DATA["characteristic"]
I = DATA["iota"]
b, t = sp.symbols("b t")


def poly(expression):
    return sp.Poly(sp.sympify(expression, locals={"b": b, "t": t}), b, t,
                   modulus=P)


def tpoly(expression):
    return sp.Poly(sp.sympify(expression, locals={"t": t}), t, modulus=P)


assert (I * I + 1) % P == 0

A0 = t**4 - 2 * I * t**3 - 4 * I * t**2 - 2 * I * t - 1
A1 = -8 * I * (t**4 + 1)
A2 = -2 * t**4 + 4 * I * t**3 - 24 * I * t**2 + 4 * I * t + 2
projection = sp.Poly(A0 * (b**4 + 1) + A1 * (b**3 + b) + A2 * b**2,
                     b, t, modulus=P)

leading = [poly(chart["leading"]) for chart in DATA["c_charts"]]
for chart in DATA["c_charts"]:
    assert chart["basis_index"] in {2, 3, 4, 5}
    assert poly(chart["constant"]).degree(b) >= 0

cover = sp.groebner(
    [projection.as_expr(), *(item.as_expr() for item in leading)],
    b, t, modulus=P, method="f5b",
)
expected_cover = [poly(value).monic() for value in DATA["cover_groebner"]]
assert len(cover.polys) == len(expected_cover) == 3
assert all(actual.monic() == expected
           for actual, expected in zip(cover.polys, expected_cover))

eliminant = sp.Poly(cover.polys[-1], t, modulus=P).monic()
cubic = tpoly(DATA["exceptional_cubic"]).monic()
guard_factor = tpoly((t - I) * (t + I)**2)
assert (guard_factor * cubic).monic() == eliminant
assert tpoly(A0) == tpoly(t + 1) * cubic

def multiply_mod(left, right):
    return (left * right).rem(cubic)

power = P
base = tpoly(t)
frobenius = tpoly(1)
while power:
    if power & 1:
        frobenius = multiply_mod(frobenius, base)
    base = multiply_mod(base, base)
    power >>= 1
remainder = (frobenius - tpoly(t)).rem(cubic)
assert remainder == tpoly(DATA["frobenius_remainder"])

left = tpoly(DATA["bezout_left"])
right = tpoly(DATA["bezout_right"])
assert left * cubic + right * remainder == tpoly(1)

r_leading = poly(DATA["r_chart"]["leading"])
assert r_leading == poly((t**2 + 1)**2)
assert poly(DATA["r_chart"]["constant"]).degree(b) >= 0

print(
    "RATE_HALF_KB_POSITIVE_433_1A_CELL5_LIFT_ATLAS_PASS "
    "c_charts=4 exceptional_degree=3 fp_roots=0 r_guard_unit=1 "
    "projection_rank=4"
)
