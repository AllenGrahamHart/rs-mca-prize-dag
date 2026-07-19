#!/usr/bin/env python3
"""Audit the intermediate Hensel gate over a small prime field."""

from __future__ import annotations


PRIME = 1009


def multiply(left: list[int], right: list[int], limit: int) -> list[int]:
    answer = [0] * limit
    for i, a in enumerate(left[:limit]):
        for j, b in enumerate(right[:limit - i]):
            answer[i + j] = (answer[i + j] + a * b) % PRIME
    return answer


def power(poly: list[int], exponent: int, limit: int) -> list[int]:
    answer = [1]
    for _ in range(exponent):
        answer = multiply(answer, poly, limit)
    return (answer + [0] * limit)[:limit]


def inverse(poly: list[int], limit: int) -> list[int]:
    answer = [pow(poly[0], -1, PRIME)]
    for m in range(1, limit):
        total = sum(
            poly[j] * answer[m - j]
            for j in range(1, min(m, len(poly) - 1) + 1)
        )
        answer.append(-total * answer[0] % PRIME)
    return answer


def cube_root_one(poly: list[int], limit: int) -> list[int]:
    answer = [1]
    inverse_three = pow(3, -1, PRIME)
    for m in range(1, limit):
        trial = (answer + [0])[:m + 1]
        known = power(trial, 3, m + 1)[m]
        answer.append((poly[m] - known) * inverse_three % PRIME)
    return answer


def hensel_solution(h_series: list[int], b_poly: list[int], u: int, h: int, limit: int) -> list[int]:
    inv_b = inverse(b_poly, limit)
    inverse_three = pow(3, -1, PRIME)
    answer = [1]
    for m in range(1, limit):
        trial = (answer + [0])[:m + 1]
        known = power(trial, 3, m + 1)[m]
        if m >= h:
            quartic = multiply(power(trial, 4, m + 1), inv_b, m + 1)
            known += u * quartic[m - h]
        answer.append((h_series[m] - known) * inverse_three % PRIME)
    return answer


def main() -> None:
    cases = nondegenerate = 0
    for h in range(3, 33):
        limit = 3 * h + 2
        b_poly = [1] + [((3 * index + h) % 13) - 6 for index in range(1, 8)]
        c_poly = [1] + [((5 * index + h) % 17) - 8 for index in range(1, 2 * h - 1)]
        u = (7 * h + 5) % PRIME
        c3 = power(c_poly, 3, limit)
        c4_over_b = multiply(power(c_poly, 4, limit), inverse(b_poly, limit), limit)
        h_series = c3[:]
        for index, value in enumerate(c4_over_b[:limit - h]):
            h_series[index + h] = (h_series[index + h] + u * value) % PRIME

        c_star = cube_root_one(h_series, limit)
        quotient = multiply(power(c_star, 2, limit), inverse(b_poly, limit), limit)
        delta = quotient[h - 1]
        kappa = c_star[2 * h - 1]
        assert (3 * kappa - u * delta) % PRIME == 0
        solved = hensel_solution(h_series, b_poly, u, h, limit)
        expected = (c_poly + [0] * limit)[:limit]
        assert solved == [value % PRIME for value in expected]
        if delta:
            assert 3 * kappa * pow(delta, -1, PRIME) % PRIME == u
            nondegenerate += 1
        cases += 1

    print(
        "AUDIT_RATE_HALF_ANTIPODAL_INTERMEDIATE_HENSEL_PASS "
        f"prime={PRIME} exact_profiles={cases} nondegenerate={nondegenerate}"
    )


if __name__ == "__main__":
    main()
