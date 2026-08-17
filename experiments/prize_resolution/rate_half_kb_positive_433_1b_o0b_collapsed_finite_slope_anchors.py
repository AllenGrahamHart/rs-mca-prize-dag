#!/usr/bin/env python3
"""Verify the exact finite-slope anchors after the O0b FFI/FIF collapse."""

import sympy as sp


PRIME = 2130706433
ANCHOR_RECORD = "d*e"
FINITE_FIRST_RECORDS = {
    "q4": "b*e",
    "q5": "-d*e",
    "q6": "-d*f",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_generic_anchor():
    z0, z1, z3, z4, u, lam, y, anchor = sp.symbols(
        "z0 z1 z3 z4 u lam y anchor"
    )
    p0 = z3 - y * z0
    p1 = z4 - y * z1
    finite_equation = p0 + p1 * u
    identity_substitution = {z3: y * z0, z4: y * z1}
    require(sp.expand(finite_equation.subs(identity_substitution)) == 0,
            "zero slope and finite equation make the first polynomial zero")
    anchored_value = (z3 + z4 * lam) - anchor * (z0 + z1 * lam)
    expected = (y - anchor) * (z0 + z1 * lam)
    require(sp.expand(
        anchored_value.subs(identity_substitution) - expected
    ) == 0, "anchor evaluation identity")
    return expected


def verify_record_separations():
    b, d, e, f = sp.symbols("b d e f")
    anchor = d * e
    records = {
        "q4": b * e,
        "q5": -d * e,
        "q6": -d * f,
    }
    expected = {
        "q4": e * (b - d),
        "q5": -2 * d * e,
        "q6": -d * (e + f),
    }
    for label in records:
        require(sp.expand(records[label] - anchor - expected[label]) == 0,
                f"{label} record separation")
    require(PRIME % 2 == 1, "odd characteristic")
    return expected


def verify_scope():
    masks = {
        "FFI": ("q4", "q5"),
        "FIF": ("q4", "q6"),
    }
    require(set().union(*map(set, masks.values())) ==
            set(FINITE_FIRST_RECORDS), "finite-pair cover")
    return masks


if __name__ == "__main__":
    verify_generic_anchor()
    separations = verify_record_separations()
    masks = verify_scope()
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_COLLAPSED_FINITE_SLOPE_ANCHORS_PASS "
          f"masks={len(masks)} records={len(separations)} characteristic={PRIME}")
