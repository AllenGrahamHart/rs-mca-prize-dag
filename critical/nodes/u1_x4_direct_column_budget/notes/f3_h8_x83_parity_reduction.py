#!/usr/bin/env python3
"""Parity reduction for h=8 x83 full-zero supports."""

from __future__ import annotations

HIGH_ODD_DEGREES = (9, 11, 13, 15)
LOW_ODD_DEGREES = (1, 3, 5, 7)
ODD_ROOT_DEGREES = (1, 3, 5, 7)


def has_high_odd_locator_term(locator: list[int]) -> bool:
    return any(locator[degree] != 0 for degree in HIGH_ODD_DEGREES)


def parity_reduction_summary() -> dict[str, int]:
    import sympy as sp

    symbols = sp.symbols("c0:16")
    c = list(symbols) + [sp.Integer(1)]
    root = [sp.Integer(0)] * 9
    root[8] = sp.Integer(1)
    for degree in range(15, 7, -1):
        unknown = degree - 8
        known = sp.Integer(0)
        lo = max(0, degree - 8)
        hi = min(8, degree)
        for i in range(lo, hi + 1):
            j = degree - i
            if not (0 <= j <= 8):
                continue
            if i == unknown or j == unknown:
                continue
            known += root[i] * root[j]
        root[unknown] = sp.factor((c[degree] - known) / 2)

    high_odd_zero = {symbols[degree]: 0 for degree in HIGH_ODD_DEGREES}
    odd_root_zero = [
        sp.factor(root[degree].subs(high_odd_zero))
        for degree in ODD_ROOT_DEGREES
    ]
    if any(value != 0 for value in odd_root_zero):
        raise AssertionError(odd_root_zero)

    square = [sp.Integer(0)] * 17
    for i, x in enumerate(root):
        for j, y in enumerate(root):
            square[i + j] += x * y
    low_odd_square = [
        sp.factor(square[degree].subs(high_odd_zero))
        for degree in LOW_ODD_DEGREES
    ]
    if any(value != 0 for value in low_odd_square):
        raise AssertionError(low_odd_square)

    low_odd_obstructions = [
        sp.factor((square[degree] - symbols[degree]).subs(high_odd_zero))
        for degree in LOW_ODD_DEGREES
    ]
    expected = [-symbols[degree] for degree in LOW_ODD_DEGREES]
    if low_odd_obstructions != expected:
        raise AssertionError((low_odd_obstructions, expected))

    denominators = [
        coefficient.q
        for expression in root
        for coefficient in sp.Poly(expression, *symbols, domain=sp.QQ).coeffs()
    ]
    max_denominator_prime = 1
    for denominator in denominators:
        if denominator > 1:
            max_denominator_prime = max(
                max_denominator_prime, max(sp.factorint(denominator))
            )

    return {
        "high_odd_degrees": len(HIGH_ODD_DEGREES),
        "low_odd_degrees": len(LOW_ODD_DEGREES),
        "odd_root_degrees": len(ODD_ROOT_DEGREES),
        "max_denominator_prime": max_denominator_prime,
    }


def finite_control_summary() -> dict[str, int]:
    from f3_h8_n64_x83_obstruction_interface import (
        is_antipodal_support,
        locator_from_exponents,
        root_table,
    )

    p = 193
    vals = root_table(p, 64)
    antipodal_full_zero = (
        0,
        1,
        2,
        9,
        10,
        16,
        24,
        25,
        32,
        33,
        34,
        41,
        42,
        48,
        56,
        57,
    )
    nonantipodal_controls = (
        (0, 1, 3, 6, 8, 11, 14, 17, 20, 23, 27, 31, 36, 42, 49, 57),
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
    )
    antipodal_locator = locator_from_exponents(antipodal_full_zero, vals, p)
    if not is_antipodal_support(antipodal_full_zero):
        raise AssertionError(antipodal_full_zero)
    if has_high_odd_locator_term(antipodal_locator):
        raise AssertionError(antipodal_locator)

    high_odd_controls = 0
    for support in nonantipodal_controls:
        locator = locator_from_exponents(support, vals, p)
        if is_antipodal_support(support):
            raise AssertionError(support)
        if not has_high_odd_locator_term(locator):
            raise AssertionError((support, locator))
        high_odd_controls += 1
    return {
        "control_prime": p,
        "antipodal_controls": 1,
        "nonantipodal_high_odd_controls": high_odd_controls,
    }


def main() -> None:
    parity = parity_reduction_summary()
    controls = finite_control_summary()
    print("h=8 x83 parity reduction")
    print(
        "symbolic propagation: "
        f"high_odd_degrees={parity['high_odd_degrees']} "
        f"odd_root_degrees={parity['odd_root_degrees']} "
        f"low_odd_degrees={parity['low_odd_degrees']} "
        f"max_denominator_prime={parity['max_denominator_prime']}"
    )
    print(
        "finite controls: "
        f"p={controls['control_prime']} "
        f"antipodal={controls['antipodal_controls']} "
        f"nonantipodal_high_odd={controls['nonantipodal_high_odd_controls']}"
    )
    print("non-antipodal x83 full-zero supports must have a high odd locator coefficient")
    print("H8_X83_PARITY_REDUCTION_PASS")


if __name__ == "__main__":
    main()
