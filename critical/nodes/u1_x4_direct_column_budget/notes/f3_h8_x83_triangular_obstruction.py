#!/usr/bin/env python3
"""Triangular h=8 x83 low-obstruction compiler."""

from __future__ import annotations

from dataclasses import dataclass
import math

import sympy as sp


H = 8
LOCATOR = sp.symbols("c0:16")


@dataclass(frozen=True)
class KeyBound:
    name: str
    denominator: int
    terms: int
    total_degree: int
    conjugate_bound: int


def locator_coeff_bound(index: int) -> int:
    """Archimedean bound for the X^index coefficient of a 16-root locator."""

    return math.comb(2 * H, index)


def square_shift_root() -> list[sp.Expr]:
    """Forced monic degree-8 square root from the top locator coefficients."""

    locator = list(LOCATOR) + [sp.Integer(1)]
    root: list[sp.Expr] = [sp.Integer(0)] * (H + 1)
    root[H] = sp.Integer(1)
    for degree in range(2 * H - 1, H - 1, -1):
        unknown = degree - H
        known = sp.Integer(0)
        for i in range(max(0, degree - H), min(H, degree) + 1):
            j = degree - i
            if i == unknown or j == unknown:
                continue
            known += root[i] * root[j]
        root[unknown] = sp.factor((locator[degree] - known) / 2)
    return root


def square(poly: list[sp.Expr]) -> list[sp.Expr]:
    out = [sp.Integer(0)] * (2 * len(poly) - 1)
    for i, left in enumerate(poly):
        for j, right in enumerate(poly):
            out[i + j] = sp.expand(out[i + j] + left * right)
    return out


def low_obstructions() -> dict[int, sp.Expr]:
    locator = list(LOCATOR) + [sp.Integer(1)]
    root_square = square(square_shift_root())
    return {
        degree: sp.expand(root_square[degree] - locator[degree])
        for degree in range(1, H)
    }


def integer_denominator(expr: sp.Expr) -> int:
    poly = sp.Poly(expr, *LOCATOR, domain=sp.QQ)
    return int(sp.lcm([coefficient.q for coefficient in poly.coeffs()]))


def l1_conjugate_bound(poly: sp.Poly) -> int:
    total = 0
    coeff_bounds = [locator_coeff_bound(index) for index in range(2 * H)]
    for monom, coefficient in poly.terms():
        term = abs(int(coefficient))
        for index, power in enumerate(monom):
            term *= coeff_bounds[index] ** power
        total += term
    return total


def require_triangular(key_index: int, poly: sp.Poly, denominator: int) -> None:
    """Check D_j E_j = -D_j c_j + polynomial(c8,...,c15)."""

    coeff = poly.coeff_monomial(LOCATOR[key_index])
    if coeff != -denominator:
        raise AssertionError((key_index, coeff, -denominator))
    low_indices = set(range(1, H))
    for monom, term_coeff in poly.terms():
        used_low = [index for index in low_indices if monom[index]]
        if not used_low:
            continue
        if used_low != [key_index] or monom[key_index] != 1 or sum(monom) != 1:
            raise AssertionError((key_index, monom, term_coeff))
    if any(monom[0] for monom, _ in poly.terms()):
        raise AssertionError((key_index, "unexpected c0 term"))


def key_bounds() -> tuple[KeyBound, ...]:
    rows = []
    for key_index, expr in low_obstructions().items():
        denominator = integer_denominator(expr)
        cleared = sp.expand(expr * denominator)
        poly = sp.Poly(cleared, *LOCATOR, domain=sp.ZZ)
        require_triangular(key_index, poly, denominator)
        rows.append(
            KeyBound(
                name=f"E{key_index}",
                denominator=denominator,
                terms=len(poly.terms()),
                total_degree=poly.total_degree(),
                conjugate_bound=l1_conjugate_bound(poly),
            )
        )
    return tuple(rows)


def first_obstruction_formula() -> str:
    expr = low_obstructions()[7]
    denominator = integer_denominator(expr)
    return str(sp.factor(sp.expand(expr * denominator)))


def h8_triangular_summary() -> dict[str, int]:
    rows = key_bounds()
    return {
        "keys": len(rows),
        "max_denominator": max(row.denominator for row in rows),
        "max_terms": max(row.terms for row in rows),
        "max_total_degree": max(row.total_degree for row in rows),
        "max_conjugate_bound": max(row.conjugate_bound for row in rows),
        "first_key_denominator": next(row.denominator for row in rows if row.name == "E7"),
        "first_key_terms": next(row.terms for row in rows if row.name == "E7"),
        "first_key_total_degree": next(row.total_degree for row in rows if row.name == "E7"),
    }


def main() -> None:
    rows = key_bounds()
    expected = {
        "E1": (33_554_432, 141, 15, 4_241_183_626_964_720_815_177_728),
        "E2": (16_777_216, 116, 14, 179_012_679_426_302_933_991_424),
        "E3": (4_194_304, 90, 13, 3_474_426_376_778_600_677_376),
        "E4": (2_097_152, 71, 12, 133_190_716_344_152_096_768),
        "E5": (262_144, 53, 11, 1_336_383_684_118_315_008),
        "E6": (131_072, 41, 10, 58_575_957_453_176_832),
        "E7": (32_768, 30, 9, 1_316_617_259_581_440),
    }
    actual = {
        row.name: (
            row.denominator,
            row.terms,
            row.total_degree,
            row.conjugate_bound,
        )
        for row in rows
    }
    if actual != expected:
        raise AssertionError(actual)

    summary = h8_triangular_summary()
    if summary != {
        "keys": 7,
        "max_denominator": 33_554_432,
        "max_terms": 141,
        "max_total_degree": 15,
        "max_conjugate_bound": 4_241_183_626_964_720_815_177_728,
        "first_key_denominator": 32_768,
        "first_key_terms": 30,
        "first_key_total_degree": 9,
    }:
        raise AssertionError(summary)

    print("h=8 x83 triangular low-obstruction compiler")
    print("D_j E_j = -D_j c_j + P_j(c8,...,c15) for j=1..7")
    for row in rows:
        print(
            f"{row.name}: denominator={row.denominator} terms={row.terms} "
            f"total_degree={row.total_degree} "
            f"conjugate_bound={row.conjugate_bound}"
        )
    print("first obstruction E7 cleared formula:")
    print(first_obstruction_formula())
    print("H8_X83_TRIANGULAR_OBSTRUCTION_PASS")


if __name__ == "__main__":
    main()
