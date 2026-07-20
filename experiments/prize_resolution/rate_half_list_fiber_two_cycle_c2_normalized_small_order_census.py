#!/usr/bin/env python3
"""Small-order census for the exact normalized c=2 gap/span interface."""

from __future__ import annotations

from itertools import combinations


PRIMES = (2017, 12097)
PRIME = PRIMES[0]
HEIGHTS = (3, 4, 7, 8, 10)
EXTRA_ROWS = ((97, 7), (113, 8), (257, 9), (641, 9))


def primitive_root() -> int:
    for candidate in range(2, PRIME):
        if all(
            pow(candidate, (PRIME - 1) // factor, PRIME) != 1
            for factor in (2, 3, 7)
        ):
            return candidate
    raise AssertionError("primitive root not found")


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % PRIME == 0:
        poly.pop()
    return [value % PRIME for value in poly]


def add(left: list[int], right: list[int], scale: int = 1) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + scale * (right[index] if index < len(right) else 0)
        ) % PRIME
    return trim(out)


def multiply(
    left: list[int], right: list[int], limit: int | None = None
) -> list[int]:
    size = len(left) + len(right) - 1
    if limit is not None:
        size = min(size, limit)
    out = [0] * size
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j >= size:
                break
            out[i + j] = (out[i + j] + a * b) % PRIME
    return trim(out)


def power(poly: list[int], exponent: int, limit: int | None = None) -> list[int]:
    out = [1]
    base = poly
    while exponent:
        if exponent & 1:
            out = multiply(out, base, limit)
        exponent >>= 1
        if exponent:
            base = multiply(base, base, limit)
    return out


def divide(numerator: list[int], denominator: list[int]) -> tuple[list[int], list[int]]:
    numerator = trim(numerator[:])
    denominator = trim(denominator[:])
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    leading_inverse = pow(denominator[-1], -1, PRIME)
    while len(numerator) >= len(denominator) and numerator != [0]:
        shift = len(numerator) - len(denominator)
        coefficient = numerator[-1] * leading_inverse % PRIME
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            numerator[shift + index] = (
                numerator[shift + index] - coefficient * value
            ) % PRIME
        numerator = trim(numerator)
    return trim(quotient), numerator


def gcd(left: list[int], right: list[int]) -> list[int]:
    while trim(right[:]) != [0]:
        _, remainder = divide(left, right)
        left, right = right, remainder
    left = trim(left)
    inverse = pow(left[-1], -1, PRIME)
    return [value * inverse % PRIME for value in left]


def denominator(roots: tuple[int, int, int, int]) -> list[int]:
    out = [1]
    for root in roots:
        out = multiply(out, [1, -root % PRIME])
    return out


def fourth_root_coefficients(poly: list[int], maximum: int) -> list[int]:
    coefficients = [1]
    for n in range(1, maximum + 1):
        value = sum(
            (4 * n - 3 * j) * poly[j] * coefficients[n - j]
            for j in range(1, min(4, n) + 1)
        )
        coefficients.append(-value * pow(4 * n, -1, PRIME) % PRIME)
    return coefficients


def inverse_series(poly: list[int], length: int) -> list[int]:
    leading_inverse = pow(poly[0], -1, PRIME)
    out = [leading_inverse]
    for n in range(1, length):
        value = sum(
            poly[index] * out[n - index]
            for index in range(1, min(n, len(poly) - 1) + 1)
        )
        out.append(-leading_inverse * value % PRIME)
    return out


def square_root_series(poly: list[int], length: int) -> list[int]:
    assert poly[0] == 1
    out = [1]
    inverse_two = pow(2, -1, PRIME)
    for n in range(1, length):
        cross = sum(out[index] * out[n - index] for index in range(1, n))
        out.append((poly[n] - cross) * inverse_two % PRIME)
    return out


def shifted(poly: list[int], amount: int) -> list[int]:
    return [0] * amount + poly


def canonical_packet(
    roots: tuple[int, int, int, int], height: int
) -> tuple[str, tuple[int, int, int] | None]:
    order = 8 * height - 8
    degree = 2 * height - 3
    e_poly = denominator(roots)
    coefficients = fourth_root_coefficients(e_poly, 3 * height - 1)
    if coefficients[2 * height - 2] or coefficients[2 * height - 1]:
        return "primary", None
    leading = coefficients[2 * height]
    if leading == 0:
        return "primary_nondegenerate", None

    numerator = [1] + [0] * (order - 1) + [-1 % PRIME]
    quotient, remainder = divide(numerator, e_poly)
    assert remainder == [0]
    b_poly = coefficients[: degree + 1]
    residual = add(quotient, power(b_poly, 4), scale=-1)
    assert residual[: 2 * height] == [0] * (2 * height)
    residual_bar = residual[2 * height :]
    alpha = residual_bar[0]
    assert alpha == 4 * leading % PRIME

    b_squared = multiply(b_poly, b_poly, height)
    normalized = [
        value * pow(alpha, -1, PRIME) % PRIME for value in residual_bar[:height]
    ]
    canonical_square = multiply(
        normalized, inverse_series(b_squared, height), height
    )
    canonical_square += [0] * (height - len(canonical_square))
    c_full = square_root_series(canonical_square, height)
    if c_full[height - 2] or c_full[height - 1]:
        return "secondary", None
    c_poly = trim(c_full[: height - 2])

    sigma = add(
        residual_bar,
        multiply(
            [alpha], multiply(power(b_poly, 2), power(c_poly, 2))
        ),
        scale=-1,
    )
    x_poly = shifted(multiply(b_poly, power(c_poly, 3)), height)
    y_poly = shifted(power(c_poly, 4), 2 * height)
    beta = sigma[height] if height < len(sigma) else 0
    after_beta = add(sigma, x_poly, scale=-beta)
    gamma = after_beta[2 * height] if 2 * height < len(after_beta) else 0
    if add(after_beta, y_poly, scale=-gamma) != [0]:
        return "span", None

    invariant_i = (alpha * alpha + 12 * gamma) % PRIME
    invariant_j = (
        72 * alpha * gamma - 27 * beta * beta - 2 * alpha**3
    ) % PRIME
    outer = [gamma, beta, alpha, 0, 1]
    derivative = [beta, 2 * alpha, 0, 4]
    if len(gcd(outer, derivative)) != 1:
        return "outer_separable", None
    outer_roots = [
        value
        for value in range(PRIME)
        if sum(coefficient * pow(value, index, PRIME) for index, coefficient in enumerate(outer))
        % PRIME
        == 0
    ]
    if len(outer_roots) != 4:
        return "outer_split", None
    return "canonical", (invariant_i, invariant_j, len(outer_roots))


def pair_couples(t: int, invariant_i: int, invariant_j: int) -> bool:
    trace = (1 + t) ** 2 * pow(t, -1, PRIME) % PRIME
    return (
        4 * invariant_i**3 * trace * (trace - 36) ** 2
        - invariant_j**2 * (trace + 12) ** 3
    ) % PRIME == 0


def run_row(prime: int, height: int) -> None:
    global PRIME
    PRIME = prime
    generator = primitive_root()
    order = 8 * height - 8
    assert (PRIME - 1) % (2 * order) == 0
    subgroup = [
        pow(generator, (PRIME - 1) // order * exponent, PRIME)
        for exponent in range(order)
    ]
    counts = {
        "sets": 0,
        "primary": 0,
        "primary_nondegenerate": 0,
        "secondary": 0,
        "span": 0,
        "outer_separable": 0,
        "outer_split": 0,
        "canonical": 0,
        "coupled_pairs": 0,
    }
    witnesses: list[tuple[tuple[int, int, int, int], int]] = []
    stage_witnesses: dict[str, tuple[int, int, int, int]] = {}
    for tail in combinations(subgroup[1:], 3):
        roots = (1,) + tail
        counts["sets"] += 1
        status, invariants = canonical_packet(roots, height)
        counts[status] += 1
        if status != "primary" and status not in stage_witnesses:
            stage_witnesses[status] = roots
        if status != "canonical" or invariants is None:
            continue
        invariant_i, invariant_j, _ = invariants
        for t in tail:
            if pair_couples(t, invariant_i, invariant_j):
                counts["coupled_pairs"] += 1
                if len(witnesses) < 3:
                    witnesses.append((roots, t))
    print(
        "C2_SMALL_CENSUS "
        f"p={PRIME} H={height} N={order} counts={counts} "
        f"stage_witnesses={stage_witnesses} coupled_witnesses={witnesses}",
        flush=True,
    )


def main() -> None:
    rows = [(prime, height) for prime in PRIMES for height in HEIGHTS]
    rows.extend(EXTRA_ROWS)
    for prime, height in rows:
        run_row(prime, height)


if __name__ == "__main__":
    main()
