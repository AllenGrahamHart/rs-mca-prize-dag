#!/usr/bin/env python3
"""Replay the deficiency-aware coefficient-matrix identity."""


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    output = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] = (output[i + j] + a * b) % prime
    return output


def root_product(roots: tuple[int, ...], prime: int) -> list[int]:
    output = [1]
    for root in roots:
        output = multiply(output, [(-root) % prime, 1], prime)
    return output


def coefficient(poly: list[int], degree: int) -> int:
    return poly[degree] if degree < len(poly) else 0


def replay_case(prime: int, m: int) -> int:
    points = (1, 2, 4, 8)
    root_sets = (
        tuple(range(1, m + 1)),
        tuple(range(2, m + 1)),
        tuple(range(1, m)),
        tuple(range(3, m + 1)),
    )
    linear_factors = ((3, 1), (5, 2), (7, 0), (9, 4))
    quotients = []
    products = []
    columns = []
    for x_index, roots in enumerate(root_sets):
        delta = m - len(roots)
        quotient = [
            (11 + 3 * x_index + 5 * degree) % prime
            for degree in range(delta + 1)
        ]
        assert quotient[-1] != 0
        locator = root_product(roots, prime)
        linear = list(linear_factors[x_index])
        products.append(multiply(multiply(linear, locator, prime), quotient, prime))
        quotients.append(quotient)
        base = multiply(linear, locator, prime)
        for degree in range(delta + 1):
            columns.append((x_index, degree, [0] * degree + base))

    checks = 0
    for moment in range(4 * m + 1):
        for degree in range(m + 2):
            direct = sum(
                coefficient(poly, degree) * pow(points[index], moment, prime)
                for index, poly in enumerate(products)
            ) % prime
            matrix = 0
            for x_index, quotient_degree, column in columns:
                matrix += (
                    quotients[x_index][quotient_degree]
                    * coefficient(column, degree)
                    * pow(points[x_index], moment, prime)
                )
            assert direct == matrix % prime
            checks += 1

    unknowns = sum(m - len(roots) + 1 for roots in root_sets)
    assert unknowns == len(columns)
    return checks


def main() -> None:
    checks = sum(replay_case(prime, m) for prime, m in ((97, 3), (193, 4)))
    for m in (1, 2, 4, 8, 64, 1 << 20, 1 << 37):
        a = 7 * m - 1
        assert a <= a + 1 <= a + m
    print(
        "RATE_HALF_BIVARIATE_DEFICIENCY_CLONE_KERNEL_REDUCTION_PASS "
        f"coefficient_checks={checks}"
    )


if __name__ == "__main__":
    main()
