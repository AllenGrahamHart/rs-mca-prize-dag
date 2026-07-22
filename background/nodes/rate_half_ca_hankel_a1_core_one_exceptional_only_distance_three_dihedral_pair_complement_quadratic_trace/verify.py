#!/usr/bin/env python3
"""Exact controls for the dihedral pair-complement quadratic trace."""

from __future__ import annotations


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    size = max(len(left), len(right))
    out = [0] * size
    for index in range(size):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def scale(poly: list[int], scalar: int, prime: int) -> list[int]:
    return [scalar * coefficient % prime for coefficient in poly]


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return out


def locator(roots: list[int], prime: int) -> list[int]:
    out = [1]
    for root in roots:
        out = multiply(out, [(-root) % prime, 1], prime)
    return out


def evaluate(poly: list[int], point: int, prime: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % prime
    return value


def inverse(value: int, prime: int) -> int:
    require(value % prime != 0, "attempted to invert zero")
    return pow(value, prime - 2, prime)


def lagrange_basis(points: list[int], index: int, prime: int) -> list[int]:
    others = [point for j, point in enumerate(points) if j != index]
    denominator = 1
    for point in others:
        denominator = denominator * (points[index] - point) % prime
    return scale(locator(others, prime), inverse(denominator, prime), prime)


def rank(matrix: list[list[int]], prime: int) -> int:
    work = [row[:] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next((index for index in range(row, len(work)) if work[index][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        factor = inverse(work[row][column], prime)
        work[row] = [value * factor % prime for value in work[row]]
        for index in range(len(work)):
            if index == row or work[index][column] == 0:
                continue
            factor = work[index][column]
            work[index] = [
                (value - factor * pivot_value) % prime
                for value, pivot_value in zip(work[index], work[row], strict=True)
            ]
        row += 1
        if row == len(work):
            break
    return row


def proportional(left: list[int], right: list[int], prime: int) -> bool:
    size = max(len(left), len(right))
    padded_left = left + [0] * (size - len(left))
    padded_right = right + [0] * (size - len(right))
    scale_value = None
    for a, b in zip(padded_left, padded_right, strict=True):
        if b:
            scale_value = a * inverse(b, prime) % prime
            break
        if a:
            return False
    if scale_value is None:
        return True
    return all((a - scale_value * b) % prime == 0 for a, b in zip(padded_left, padded_right, strict=True))


def check_quadratic_trace() -> None:
    prime = 97
    internal = [2, 3, 5, 7]
    orbit_roots = [11, 13, 17, 19]
    lambdas = [23, 29, 31, 37]
    triple = [41, 43, 47]
    external = [value for value in range(50, 97)][: 3 * len(internal)]

    i_poly = locator(internal, prime)
    e_poly = locator(orbit_roots, prime)
    p_z = locator(external, prime)
    lagrange = [lagrange_basis(internal, index, prime) for index in range(len(internal))]
    mu = [
        evaluate(p_z, point, prime) * inverse(lambdas[index] ** 2, prime) % prime
        for index, point in enumerate(internal)
    ]

    moments = []
    for exponent in range(3):
        polynomial = [0]
        for index, basis in enumerate(lagrange):
            coefficient = mu[index] * pow(orbit_roots[index], exponent, prime) % prime
            polynomial = add(polynomial, scale(basis, coefficient, prime), prime)
        moments.append(polynomial)

    width = len(i_poly)
    basis_matrix = [poly + [0] * (width - len(poly)) for poly in [i_poly, *moments]]
    require(rank(basis_matrix, prime) == 4, "complement trace space is not four-dimensional")

    candidates = [53, 59, 61, 67, 71, 73]
    complements = []
    for u in candidates:
        product_value = 1
        for point in triple:
            product_value = product_value * (u - point * point) % prime
        denominator = evaluate(e_poly, u, prime) ** 2 * product_value % prime
        chi = -inverse(denominator, prime) % prime
        lower = [0]
        lower = add(lower, scale(moments[0], chi * u * u, prime), prime)
        lower = add(lower, scale(moments[1], -2 * chi * u, prime), prime)
        lower = add(lower, scale(moments[2], chi, prime), prime)
        leading = (u + 9) % prime
        complement = add(scale(i_poly, leading, prime), lower, prime)
        require(len(complement) == len(internal) + 1, "complement has wrong degree")

        for index, point in enumerate(internal):
            expected = chi * mu[index] * (u - orbit_roots[index]) ** 2 % prime
            require(evaluate(complement, point, prime) == expected, "interpolation trace failed")

        coordinates = [leading, chi * u * u % prime, -2 * chi * u % prime, chi]
        require(coordinates[2] ** 2 % prime == 4 * coordinates[1] * coordinates[3] % prime, "cone equation failed")
        complements.append(complement)

    require(
        all(
            not proportional(left, right, prime)
            for index, left in enumerate(complements)
            for right in complements[index + 1 :]
        ),
        "distinct orbit coordinates gave proportional complements",
    )


def check_official_counts() -> None:
    e = (1 << 38) - 1
    require(3 * e - 2 > 0, "antipodal divisor count is not positive")
    require(3 * e - 3 > 0, "constant-product divisor count is not positive")
    for fixed_points in (0, 2):
        maximum_singletons = 5 + fixed_points
        minimum_pairs = (6 * e + 3 - maximum_singletons) // 2
        expected = 3 * e - 1 if fixed_points == 0 else 3 * e - 2
        require(minimum_pairs == expected, "orbit count failed")


def main() -> None:
    check_quadratic_trace()
    check_official_counts()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_DISTANCE_THREE_"
        "DIHEDRAL_PAIR_COMPLEMENT_QUADRATIC_TRACE_PASS dimension=4 cone=1"
    )


if __name__ == "__main__":
    main()
