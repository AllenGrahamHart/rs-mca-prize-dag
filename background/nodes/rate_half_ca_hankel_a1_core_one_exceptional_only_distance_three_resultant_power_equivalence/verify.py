#!/usr/bin/env python3
"""Replay the distance-three resultant perfect-power equivalence at e=1."""

from __future__ import annotations


P = 17


def trim(poly: list[int]) -> list[int]:
    out = [value % P for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def inv(value: int) -> int:
    return pow(value % P, P - 2, P)


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)
        for i in range(size)
    ])


def mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % P
    return trim(out)


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value for value in poly])


def divmod_poly(dividend: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    work = trim(dividend)
    divisor = trim(divisor)
    assert divisor != [0]
    if len(work) < len(divisor):
        return [0], work
    quotient = [0] * (len(work) - len(divisor) + 1)
    lead_inv = inv(divisor[-1])
    while work != [0] and len(work) >= len(divisor):
        degree = len(work) - len(divisor)
        coefficient = work[-1] * lead_inv % P
        quotient[degree] = coefficient
        for index, value in enumerate(divisor):
            work[index + degree] = (work[index + degree] - coefficient * value) % P
        work = trim(work)
    return trim(quotient), work


def monic(poly: list[int]) -> list[int]:
    poly = trim(poly)
    assert poly != [0]
    return scale(poly, inv(poly[-1]))


def gcd_poly(left: list[int], right: list[int]) -> list[int]:
    left = trim(left)
    right = trim(right)
    while right != [0]:
        _, remainder = divmod_poly(left, right)
        left, right = right, remainder
    return monic(left)


def derivative(poly: list[int]) -> list[int]:
    if len(poly) == 1:
        return [0]
    return trim([index * poly[index] for index in range(1, len(poly))])


def poly_pow(poly: list[int], exponent: int) -> list[int]:
    out = [1]
    base = trim(poly)
    while exponent:
        if exponent & 1:
            out = mul(out, base)
        base = mul(base, base)
        exponent //= 2
    return out


def locator(roots: tuple[int, ...]) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % P, 1])
    return out


def evaluate(poly: list[int], value: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * value + coefficient) % P
    return out


def row_norm(
    active: tuple[int, ...], a_poly: list[int], q_1: list[int]
) -> tuple[list[int], int]:
    norm = [1]
    leading = 1
    for x in active:
        row = [evaluate(a_poly, x), evaluate(q_1, x)]
        norm = mul(norm, row)
        leading = leading * row[1] % P
    return norm, leading


def main() -> None:
    roots_a = (2, 5)
    triple = (3, 13, 15)
    active = (4, 9, 11, 6, 7, 10, 8, 12, 16)
    external = (15, 2, 4)

    a_poly = locator(roots_a) + [0]
    b_poly = locator(triple)
    q_1 = add(b_poly, scale(a_poly, -1))
    c_poly = locator(active)

    # For e=1, the row resultant Delta is q_1 itself.
    assert gcd_poly(c_poly, q_1) == [1]
    norm, leading = row_norm(active, a_poly, q_1)
    p_z = locator(external)
    assert norm == scale(poly_pow(p_z, 3), leading)

    norm_gcd = gcd_poly(norm, derivative(norm))
    quotient, remainder = divmod_poly(norm, norm_gcd)
    assert remainder == [0]
    assert monic(quotient) == p_z
    assert gcd_poly(p_z, derivative(p_z)) == [1]

    incidence = {}
    for gamma in external:
        roots = tuple(x for x in active if (evaluate(a_poly, x) + gamma * evaluate(q_1, x)) % P == 0)
        assert len(roots) == 3
        incidence[gamma] = roots
    assert incidence == {15: (4, 9, 11), 2: (6, 7, 10), 4: (8, 12, 16)}

    # Adding the omitted row makes one row lose parameter degree.
    assert evaluate(q_1, 14) == 0

    # Replacing one active row by a triple point preserves row degree but
    # destroys the exact cube, so the two gates are genuinely independent.
    mutated = (*active[:-1], 13)
    mutated_norm, mutated_leading = row_norm(mutated, a_poly, q_1)
    mutated_gcd = gcd_poly(mutated_norm, derivative(mutated_norm))
    mutated_radical, mutated_remainder = divmod_poly(mutated_norm, mutated_gcd)
    assert mutated_remainder == [0]
    mutated_radical = monic(mutated_radical)
    assert mutated_norm != scale(poly_pow(mutated_radical, 3), mutated_leading)

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "DISTANCE_THREE_RESULTANT_POWER_EQUIVALENCE_PASS "
        f"field={P} norm_degree={len(norm)-1} radical_degree={len(p_z)-1} "
        f"incidence={incidence}"
    )


if __name__ == "__main__":
    main()
