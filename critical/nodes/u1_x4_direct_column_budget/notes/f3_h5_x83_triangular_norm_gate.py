#!/usr/bin/env python3
"""Compile the h=5 x83 triangular obstruction and norm-divisor bounds.

The compiler is symbolic and local.  It derives the h=5 square-shift
obstruction equations from the same recurrence used by the x83 certifier.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

import sympy as sp


H = 5
X = sp.Symbol("X")
LOCATOR = sp.symbols("l0:10")


@dataclass(frozen=True)
class KeyBound:
    name: str
    denominator: int
    terms: int
    conjugate_bound: int
    log2_bound: float


def locator_coeff_bound(index: int) -> int:
    """Archimedean bound for the X^index coefficient of a 10-root locator."""
    return math.comb(2 * H, index)


def square_shift_root() -> list[sp.Expr]:
    """Forced monic degree-5 square root from the top locator coefficients."""
    locator = list(LOCATOR) + [sp.Integer(1)]
    s: list[sp.Expr] = [sp.Integer(0)] * (H + 1)
    s[H] = sp.Integer(1)
    for degree in range(2 * H - 1, H - 1, -1):
        unknown = degree - H
        known = sp.Integer(0)
        for i in range(max(0, degree - H), min(H, degree) + 1):
            j = degree - i
            if i == unknown or j == unknown:
                continue
            known += s[i] * s[j]
        s[unknown] = sp.expand((locator[degree] - known) / 2)
    return s


def square(poly: list[sp.Expr]) -> list[sp.Expr]:
    out = [sp.Integer(0)] * (2 * len(poly) - 1)
    for i, a in enumerate(poly):
        for j, b in enumerate(poly):
            out[i + j] = sp.expand(out[i + j] + a * b)
    return out


def low_obstructions() -> dict[int, sp.Expr]:
    locator = list(LOCATOR) + [sp.Integer(1)]
    s2 = square(square_shift_root())
    return {j: sp.expand(s2[j] - locator[j]) for j in range(1, H)}


def integer_denominator(expr: sp.Expr) -> int:
    poly = sp.Poly(expr, *LOCATOR, domain=sp.QQ)
    return int(sp.lcm([coeff.q for coeff in poly.coeffs()]))


def l1_conjugate_bound(poly: sp.Poly) -> int:
    total = 0
    coeff_bounds = [locator_coeff_bound(i) for i in range(2 * H)]
    for monom, coeff in poly.terms():
        term = abs(int(coeff))
        for index, power in enumerate(monom):
            term *= coeff_bounds[index] ** power
        total += term
    return total


def require_triangular(key_index: int, poly: sp.Poly, denominator: int) -> None:
    """Check D_j E_j = -D_j l_j + polynomial(l5,...,l9)."""
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


def key_bounds() -> tuple[KeyBound, ...]:
    rows = []
    for key_index, expr in low_obstructions().items():
        denominator = integer_denominator(expr)
        cleared = sp.expand(expr * denominator)
        poly = sp.Poly(cleared, *LOCATOR, domain=sp.ZZ)
        require_triangular(key_index, poly, denominator)
        bound = l1_conjugate_bound(poly)
        rows.append(
            KeyBound(
                name=f"E{key_index}",
                denominator=denominator,
                terms=len(poly.terms()),
                conjugate_bound=bound,
                log2_bound=math.log2(bound),
            )
        )
    return tuple(rows)


def activation_bound(s: int, bound: int) -> int:
    """Prime-divisor count bound for one nonzero key at n=2^s, p >= n^2."""
    n = 1 << s
    phi_n = n // 2
    return math.floor(phi_n * math.log(bound) / (2 * math.log(n)))


def first_obstruction_formula() -> str:
    expr = low_obstructions()[4]
    denominator = integer_denominator(expr)
    return str(sp.factor(sp.expand(expr * denominator)))


def main() -> None:
    rows = key_bounds()
    expected = {
        "E1": (16384, 23, 1104676577280),
        "E2": (16384, 19, 195853455360),
        "E3": (256, 14, 546954240),
        "E4": (512, 11, 187415040),
    }
    actual = {
        row.name: (row.denominator, row.terms, row.conjugate_bound)
        for row in rows
    }
    if actual != expected:
        raise AssertionError(actual)

    max_low_bound = max(row.conjugate_bound for row in rows)
    official_samples = {s: activation_bound(s, max_low_bound) for s in (13, 16, 20, 24, 32, 41)}
    expected_samples = {
        13: 6302,
        16: 40966,
        20: 524376,
        24: 6991688,
        32: 1342404147,
        41: 536437794038,
    }
    if official_samples != expected_samples:
        raise AssertionError(official_samples)

    print("h=5 x83 triangular norm-gate compiler")
    print("D_j E_j = -D_j l_j + P_j(l5,l6,l7,l8,l9) for j=1..4")
    for row in rows:
        print(
            f"{row.name}: denominator={row.denominator} terms={row.terms} "
            f"conjugate_bound={row.conjugate_bound} log2_bound={row.log2_bound:.6f}"
        )
    print("first obstruction E4 cleared formula:")
    print(first_obstruction_formula())
    print(f"max low-key conjugate bound: {max_low_bound}")
    print("per fixed nonzero key, prime-divisor bound for p>=n^2:")
    for s, value in official_samples.items():
        print(f"  n=2^{s}: <= {value} activating row primes")
    print("H5_X83_TRIANGULAR_NORM_GATE_PASS")


if __name__ == "__main__":
    main()
