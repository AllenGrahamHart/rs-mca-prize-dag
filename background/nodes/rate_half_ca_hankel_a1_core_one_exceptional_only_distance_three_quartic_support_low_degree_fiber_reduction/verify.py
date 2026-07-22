#!/usr/bin/env python3
"""Exact controls for the quartic support low-degree fiber reduction."""

from __future__ import annotations


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def mul(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return trim(out)


def evaluate(poly: list[int], value: int, prime: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * value + coefficient) % prime
    return out


def locator(a: int, b: int, prime: int) -> list[int]:
    return [a * b % prime, -(a + b) % prime, 1]


def crossing_row(
    pair: tuple[int, int],
    omitted: list[int],
    h_values: dict[int, int],
    prime: int,
) -> list[int]:
    a, b = pair
    d_a = evaluate(omitted, a, prime)
    d_b = evaluate(omitted, b, prime)
    return [
        (
            h_values[b] * d_b * d_b * pow(a, degree, prime)
            + h_values[a] * d_a * d_a * pow(b, degree, prime)
        )
        % prime
        for degree in range(5)
    ]


def dot(left: list[int], right: list[int], prime: int) -> int:
    return sum(a * b for a, b in zip(left, right, strict=True)) % prime


def check_degree_two_fixture() -> int:
    prime = 101
    pairs = [(value, -value % prime) for value in range(1, 7)]
    d_polys = [locator(a, b, prime) for a, b in pairs]
    h_values = {
        row: index + 3
        for index, pair in enumerate(pairs)
        for row in pair
    }

    p_polys = [mul([0, 1], d_poly, prime) for d_poly in d_polys]
    checks = 0
    for l, p_poly in enumerate(p_polys):
        need(len(p_poly) <= 5, "fixture quartic degree exceeded")
        for k, pair in enumerate(pairs):
            if k == l:
                continue
            row = crossing_row(pair, d_polys[l], h_values, prime)
            need(dot(row, p_poly + [0] * (5 - len(p_poly)), prime) == 0,
                 "degree-two fixture crossing failed")
            need(all(evaluate(p_poly, root, prime) for root in pair),
                 "degree-two fixture lost nonvanishing")
            checks += 1

    # Here r_l=X/D_l, so f_lm=D_m/D_l and psi=X^2 identifies every pair.
    for l in range(len(pairs)):
        for m in range(l + 1, len(pairs)):
            for k, (a, b) in enumerate(pairs):
                if k in (l, m):
                    continue
                left = (
                    evaluate(d_polys[m], a, prime)
                    * pow(evaluate(d_polys[l], a, prime), -1, prime)
                ) % prime
                right = (
                    evaluate(d_polys[m], b, prime)
                    * pow(evaluate(d_polys[l], b, prime), -1, prime)
                ) % prime
                need(left == right and a * a % prime == b * b % prime,
                     "common degree-two fiber identity failed")

    need(any(
        (h_values[a] + h_values[b]) % prime
        for a, b in pairs
    ), "degree-two fixture accidentally became antiweight")
    return checks


def check_antiweight_fixture() -> int:
    prime = 101
    pairs = [(value, value + 20) for value in range(1, 7)]
    d_polys = [locator(a, b, prime) for a, b in pairs]
    h_values = {
        row: weight
        for a, b in pairs
        for row, weight in ((a, 1), (b, prime - 1))
    }
    checks = 0
    for l, d_poly in enumerate(d_polys):
        p_poly = mul(d_poly, d_poly, prime)
        for k, pair in enumerate(pairs):
            if k == l:
                continue
            row = crossing_row(pair, d_poly, h_values, prime)
            need(dot(row, p_poly, prime) == 0,
                 "antiweight constant-comparison fixture failed")
            checks += 1
    need(all((h_values[a] + h_values[b]) % prime == 0 for a, b in pairs),
         "antiweight identity lost")
    return checks


def main() -> None:
    e_value = (1 << 38) - 1
    need(2 * (e_value - 5) > 98, "official Bezout margin failed")

    fiber_floors = {}
    for degree in (2, 3, 4):
        floor = e_value - 4 - 9 * degree * degree
        need(floor >= e_value - 148, "uniform fiber floor failed")
        fiber_floors[degree] = floor

    for degree in range(5, 9):
        need(8 // degree == 1, "large-degree outer map not Mobius")
        need(
            e_value - 1 - (2 * degree - 2) >= 2,
            "Riemann-Hurwitz leaves fewer than two good indices",
        )

    degree_two_checks = check_degree_two_fixture()
    antiweight_checks = check_antiweight_fixture()
    print(
        "RATE_HALF_DISTANCE_THREE_QUARTIC_SUPPORT_LOW_DEGREE_FIBER_PASS "
        f"bezout=98 normalization_pairs=9d^2 fiber_floors={fiber_floors} "
        f"degree_two_crossings={degree_two_checks} "
        f"antiweight_crossings={antiweight_checks} degrees_5_to_8_excluded=True"
    )


if __name__ == "__main__":
    main()
