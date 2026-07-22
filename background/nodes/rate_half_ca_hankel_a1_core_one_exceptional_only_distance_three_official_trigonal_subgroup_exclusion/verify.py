#!/usr/bin/env python3
"""Exact checks for the official trigonal subgroup exclusion."""

from __future__ import annotations

from math import gcd


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def curve_coefficients(
    b0: int,
    b1: int,
    b2: int,
    r0: int,
    r1: int,
    r2: int,
    prime: int,
) -> list[list[int]]:
    return [
        [(b1 * r0 - b0 * r1) % prime, (b2 * r0 - b0 * r2) % prime, r0 % prime],
        [(b2 * r0 - b0 * r2) % prime, (r0 + b2 * r1 - b1 * r2) % prime, r1 % prime],
        [r0 % prime, r1 % prime, r2 % prime],
    ]


def evaluate_curve(coefficients: list[list[int]], x: int, y: int, prime: int) -> int:
    return sum(
        coefficient * pow(x, i, prime) * pow(y, j, prime)
        for i, row in enumerate(coefficients)
        for j, coefficient in enumerate(row)
    ) % prime


def has_admissible_corner(coefficients: list[list[int]]) -> bool:
    # Rows here are x exponents. Inspect y=0 and y=2 boundary rows.
    for y_degree in (0, 2):
        boundary = [coefficients[x_degree][y_degree] for x_degree in range(3)]
        for x_degree in (0, 2):
            if boundary[x_degree] and any(
                boundary[other] for other in range(3) if other != x_degree
            ):
                return True
    return False


def primitive_root(prime: int) -> int:
    factors = []
    value = prime - 1
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    for candidate in range(2, prime):
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError("primitive root not found")


def main() -> None:
    n_value = 1 << 41
    e_value = (1 << 38) - 1

    # The worst transformed bidegree is (m,n)=(2,3).
    need(n_value * n_value > 100**2 * 6**3, "lower subgroup threshold failed")
    need((3 * n_value) ** 4 < (1 << 167) ** 3, "field-size threshold failed")
    need(1440**3 * n_value**2 < (2 * e_value) ** 3, "irreducible bound failed")
    need(32**3 * n_value**2 < e_value**3, "Mobius graph bound failed")
    need(gcd(3, n_value) == 1, "official subgroup unexpectedly has 3-torsion")

    # Check the displayed coefficient identity on deterministic inputs.
    prime = 101
    samples = 0
    for seed in range(1, 24):
        b0 = (3 * seed + 1) % prime or 1
        b1 = (5 * seed + 2) % prime
        b2 = (7 * seed + 3) % prime
        r0 = (11 * seed + 4) % prime
        r1 = (13 * seed + 5) % prime
        r2 = (17 * seed + 6) % prime
        coefficients = curve_coefficients(b0, b1, b2, r0, r1, r2, prime)
        for x, y in ((2, 3), (5, 9), (17, 41)):
            b_x = (x**3 + b2 * x**2 + b1 * x + b0) % prime
            b_y = (y**3 + b2 * y**2 + b1 * y + b0) % prime
            r_x = (r2 * x**2 + r1 * x + r0) % prime
            r_y = (r2 * y**2 + r1 * y + r0) % prime
            need(
                (x - y) * evaluate_curve(coefficients, x, y, prime)
                % prime
                == (b_x * r_y - b_y * r_x) % prime,
                "coincidence coefficient identity failed",
            )
            samples += 1

    # Exhaust the corner-failure classification over a small odd field.
    corner_prime = 7
    ordinary = cyclotomic = linear_pole = double_pole = 0
    for b0 in range(1, corner_prime):
        for b1 in range(corner_prime):
            for b2 in range(corner_prime):
                for r0 in range(corner_prime):
                    for r1 in range(corner_prime):
                        for r2 in range(corner_prime):
                            if r0 == r1 == r2 == 0:
                                continue
                            coeffs = curve_coefficients(
                                b0, b1, b2, r0, r1, r2, corner_prime
                            )
                            if has_admissible_corner(coeffs):
                                ordinary += 1
                            elif r0:
                                need(
                                    coeffs
                                    == [
                                        [0, 0, r0],
                                        [0, r0, 0],
                                        [r0, 0, 0],
                                    ],
                                    "unclassified nonzero-r0 corner failure",
                                )
                                cyclotomic += 1
                            elif r1 and not r2:
                                linear_pole += 1
                            elif r2 and not r1:
                                double_pole += 1
                            else:
                                raise AssertionError("unclassified zero-r0 corner failure")

    # Replay both exceptional determinant-one torus transformations.
    for b0, b1, b2 in ((3, 7, 11), (5, 13, 17)):
        for x, y in ((2, 3), (7, 19), (23, 41)):
            x %= prime
            y %= prime
            u = x * x * y % prime
            v = pow(x, prime - 2, prime)
            original = (x * y * (x + y + b2) - b0) % prime
            transformed = (u * u * v**3 + b2 * u * v + u - b0) % prime
            need(original == transformed, "R=x torus transform failed")

            u = y * pow(x, prime - 2, prime) % prime
            v = x
            original = (x * x * y * y - b1 * x * y - b0 * (x + y)) % prime
            transformed = v * (u * u * v**3 - b1 * u * v - b0 * (1 + u))
            need(original == transformed % prime, "R=x^2 torus transform failed")

    # Exhaust the coefficient case split for a general Mobius graph.
    graph_prime = 7
    admissible_graphs = inversion_graphs = scaling_graphs = 0
    for a in range(graph_prime):
        for b in range(graph_prime):
            for c in range(graph_prime):
                for d in range(graph_prime):
                    if (a * d - b * c) % graph_prime == 0:
                        continue
                    if b and a:
                        admissible_graphs += 1
                    elif b and d:
                        admissible_graphs += 1
                    elif b:
                        need(a == d == 0 and c, "bad inversion graph classification")
                        inversion_graphs += 1
                    else:
                        need(a and d, "singular b=0 graph escaped")
                        if c:
                            admissible_graphs += 1
                        else:
                            scaling_graphs += 1

    # A toy 2-power subgroup has no nontrivial order-three scaling graph.
    toy_prime = 97
    generator = primitive_root(toy_prime)
    subgroup = {
        pow(generator, 3 * index, toy_prime)
        for index in range(32)
    }
    omega = pow(generator, 32, toy_prime)
    need(pow(omega, 3, toy_prime) == 1 and omega != 1, "toy cube root failed")
    need(omega not in subgroup, "order-three scalar entered 2-group")
    need(
        not any(omega * x % toy_prime in subgroup for x in subgroup),
        "order-three graph met toy subgroup square",
    )

    print(
        "RATE_HALF_DISTANCE_THREE_OFFICIAL_TRIGONAL_SUBGROUP_EXCLUSION_PASS "
        f"coefficient_samples={samples} corner_cases="
        f"{ordinary}/{cyclotomic}/{linear_pole}/{double_pole} "
        f"graphs={admissible_graphs}/{inversion_graphs}/{scaling_graphs} "
        "irreducible_constant=1440 mobius_constant=32"
    )


if __name__ == "__main__":
    main()
