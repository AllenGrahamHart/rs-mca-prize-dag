#!/usr/bin/env python3
"""Audit the secondary-gap identity over a small prime field."""

from __future__ import annotations

from itertools import combinations


PRIME = 1009


def multiply(
    left: list[int], right: list[int], limit: int, prime: int = PRIME
) -> list[int]:
    answer = [0] * limit
    for i, a in enumerate(left[:limit]):
        for j, b in enumerate(right[:limit - i]):
            answer[i + j] = (answer[i + j] + a * b) % prime
    return answer


def inverse(poly: list[int], limit: int, prime: int = PRIME) -> list[int]:
    answer = [pow(poly[0], -1, prime)]
    for m in range(1, limit):
        total = sum(
            poly[j] * answer[m - j]
            for j in range(1, min(m, len(poly) - 1) + 1)
        )
        answer.append(-total * answer[0] % prime)
    return answer


def square_root_one(poly: list[int], limit: int, prime: int = PRIME) -> list[int]:
    answer = [1]
    inverse_two = pow(2, -1, prime)
    for m in range(1, limit):
        cross = sum(answer[j] * answer[m - j] for j in range(1, m))
        answer.append((poly[m] - cross) * inverse_two % prime)
    return answer


def multiply_full(left: list[int], right: list[int], prime: int) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % prime
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def divide_exact(numerator: list[int], denominator: list[int], prime: int) -> list[int]:
    remainder = numerator[:]
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    inverse_lead = pow(denominator[-1], -1, prime)
    for offset in range(len(quotient) - 1, -1, -1):
        coefficient = remainder[offset + len(denominator) - 1] * inverse_lead % prime
        quotient[offset] = coefficient
        for index, value in enumerate(denominator):
            remainder[offset + index] = (
                remainder[offset + index] - coefficient * value
            ) % prime
    assert all(value == 0 for value in remainder[: len(denominator) - 1])
    return quotient


def primitive_root(prime: int) -> int:
    factors: list[int] = []
    remainder = prime - 1
    divisor = 2
    while divisor * divisor <= remainder:
        if remainder % divisor == 0:
            factors.append(divisor)
            while remainder % divisor == 0:
                remainder //= divisor
        divisor += 1
    if remainder > 1:
        factors.append(remainder)
    return next(
        candidate
        for candidate in range(2, prime)
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors)
    )


def primary_coefficients(e_poly: list[int], limit: int, prime: int) -> list[int]:
    answer = [1]
    for m in range(1, limit + 1):
        numerator = sum(
            (4 * m - 3 * j) * e_poly[j] * answer[m - j]
            for j in range(1, min(4, m) + 1)
        )
        answer.append(-numerator * pow(4 * m, -1, prime) % prime)
    return answer


def subgroup_gap_scan() -> tuple[int, int, int]:
    expected = {
        8: (2, 2, 2),
        16: (0, 0, 0),
        32: (192, 0, 0),
    }
    totals = [0, 0, 0]
    for order, prime in ((8, 97), (16, 193), (32, 193)):
        generator = primitive_root(prime)
        zeta = pow(generator, (prime - 1) // order, prime)
        roots = [pow(zeta, exponent, prime) for exponent in range(order)]
        quarter = order // 4
        single = double = coset_double = 0
        for exponents in combinations(range(order), 4):
            e_poly = [1]
            for exponent in exponents:
                factor = [1, -roots[exponent] % prime]
                product_poly = [0] * (len(e_poly) + 1)
                for i, left in enumerate(e_poly):
                    for j, right in enumerate(factor):
                        product_poly[i + j] = (
                            product_poly[i + j] + left * right
                        ) % prime
                e_poly = product_poly
            coefficients = primary_coefficients(e_poly, quarter + 1, prime)
            if coefficients[quarter] == 0:
                single += 1
                if coefficients[quarter + 1] == 0:
                    double += 1
                    is_coset = any(
                        set(exponents)
                        == {
                            start % order,
                            (start + quarter) % order,
                            (start + 2 * quarter) % order,
                            (start + 3 * quarter) % order,
                        }
                        for start in exponents
                    )
                    coset_double += int(is_coset)
        assert (single, double, coset_double) == expected[order]
        totals[0] += single
        totals[1] += double
        totals[2] += coset_double
    return tuple(totals)


def order64_primary_route_fence() -> tuple[int, int, int, tuple[int, int, int]]:
    prime = 193
    order = 64
    quarter = 16
    generator = primitive_root(prime)
    zeta = pow(generator, (prime - 1) // order, prime)
    exponents = (0, 1, 3, 62)
    roots = [pow(zeta, exponent, prime) for exponent in exponents]

    e_poly = [1]
    for root in roots:
        e_poly = multiply_full(e_poly, [1, -root % prime], prime)
    coefficients = primary_coefficients(e_poly, quarter + 2, prime)
    assert coefficients[quarter : quarter + 3] == [0, 0, 94]

    cosets = {
        tuple(sorted((start + step * quarter) % order for step in range(4)))
        for start in range(quarter)
    }
    assert tuple(sorted(exponents)) not in cosets
    orbit = {
        tuple(sorted((exponent + shift) % order for exponent in exponents))
        for shift in range(order)
    }
    assert len(orbit) == order

    r = quarter - 1
    h = quarter // 2 + 1
    b_poly = coefficients[: r + 1]
    quotient = divide_exact([1] + [0] * (order - 1) + [prime - 1], e_poly, prime)
    b2 = multiply_full(b_poly, b_poly, prime)
    b4 = multiply_full(b2, b2, prime)
    residual = [
        ((quotient[index] if index < len(quotient) else 0)
         - (b4[index] if index < len(b4) else 0))
        % prime
        for index in range(max(len(quotient), len(b4)))
    ]
    first = next(index for index, value in enumerate(residual) if value)
    assert first == 2 * h
    rbar = residual[2 * h :]
    alpha = rbar[0]
    normalized = multiply(rbar, inverse(b2, h, prime), h, prime)
    normalized = [value * pow(alpha, -1, prime) % prime for value in normalized]
    secondary = square_root_one(normalized, h, prime)
    assert secondary[h - 2 : h] == [102, 24]

    # The same exponent pattern does not survive at the first order-64 prime
    # above the deliberately strong p>=d^2 threshold.
    square_prime = 4289
    square_generator = primitive_root(square_prime)
    square_zeta = pow(
        square_generator, (square_prime - 1) // order, square_prime
    )
    square_roots = [
        pow(square_zeta, exponent, square_prime) for exponent in exponents
    ]
    square_e = [1]
    for root in square_roots:
        square_e = multiply_full(
            square_e, [1, -root % square_prime], square_prime
        )
    square_coefficients = primary_coefficients(
        square_e, quarter + 2, square_prime
    )
    square_triple = tuple(square_coefficients[quarter : quarter + 3])
    assert square_triple == (2769, 3151, 2930)
    return len(orbit), secondary[h - 2], secondary[h - 1], square_triple


def main() -> None:
    cases = 0
    for h in range(3, 65):
        c_poly = [3] + [((7 * m + h) % 13) - 6 for m in range(1, h - 2)]
        c2 = multiply(c_poly, c_poly, h)
        j0 = 5 * c_poly[0] * c_poly[0] % PRIME
        normalized = [value * 5 * pow(j0, -1, PRIME) % PRIME for value in c2]
        p_series = square_root_one(normalized, h)
        expected = [value * pow(c_poly[0], -1, PRIME) % PRIME for value in c_poly]
        expected += [0] * (h - len(expected))
        assert p_series == expected
        assert p_series[h - 2] == p_series[h - 1] == 0

        mutated = c_poly + [1]
        mutated2 = multiply(mutated, mutated, h)
        mutated_normalized = [
            value * pow(mutated[0] * mutated[0], -1, PRIME) % PRIME
            for value in mutated2
        ]
        mutated_root = square_root_one(mutated_normalized, h)
        assert mutated_root[h - 2] != 0
        cases += 1

    primary_single, primary_double, coset_double = subgroup_gap_scan()
    orbit64, secondary_7, secondary_8, square_triple = order64_primary_route_fence()

    print(
        "AUDIT_RATE_HALF_ANTIPODAL_GENERIC_SECONDARY_GAP_PASS "
        f"prime={PRIME} degree_profiles={cases} terminal_mutations={cases} "
        f"orders=8,16,32 primary_single={primary_single} "
        f"primary_double={primary_double} coset_double={coset_double} "
        f"order64_noncoset_orbit={orbit64} secondary={secondary_7},{secondary_8} "
        f"square_threshold_pattern={square_triple}"
    )


if __name__ == "__main__":
    main()
