#!/usr/bin/env python3
"""Exact controls for the dihedral quotient external-product ledger."""

from __future__ import annotations

from itertools import combinations


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return out


def power(poly: list[int], exponent: int, prime: int) -> list[int]:
    out = [1]
    for _ in range(exponent):
        out = multiply(out, poly, prime)
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


def check_orbit_product() -> None:
    prime = 97
    e = 2

    # Rows are the 15 edges of K_6; block v contains the five edges at v.
    rows = list(combinations(range(6), 2))
    blocks = [
        {index for index, edge in enumerate(rows) if vertex in edge}
        for vertex in range(6)
    ]
    require(all(len(block) == 2 * e + 1 for block in blocks), "wrong block size")
    require(
        all(sum(index in block for block in blocks) == e for index in range(len(rows))),
        "wrong row replication",
    )

    # Pair disjoint K_6 edges, so paired row-incidence sets have codegree zero.
    paired_rows = [(0, 9), (1, 7), (2, 10), (3, 8), (4, 6), (5, 13), (11, 12)]
    singleton_row = 14
    orbit_coordinate = {singleton_row: 31}
    double_coordinates = []
    for coordinate, pair in zip(range(2, 9), paired_rows, strict=True):
        double_coordinates.append(coordinate)
        for row in pair:
            orbit_coordinate[row] = coordinate

    descended = []
    simple_mass = 0
    double_mass = 0
    for block in blocks:
        roots = [orbit_coordinate[row] for row in sorted(block)]
        descended.append(locator(roots, prime))
        counts = {root: roots.count(root) for root in set(roots)}
        simple_mass += sum(multiplicity == 1 for multiplicity in counts.values())
        double_mass += sum(multiplicity == 2 for multiplicity in counts.values())
        require(all(multiplicity in (1, 2) for multiplicity in counts.values()), "bad multiplicity")

    left = [1]
    for poly in descended:
        left = multiply(left, poly, prime)
    c_two = locator(double_coordinates, prime)
    c_one = locator([orbit_coordinate[singleton_row]], prime)
    right = multiply(power(c_two, 2 * e, prime), power(c_one, e, prime), prime)
    require(left == right, "orbit external-product identity failed")

    codegrees = [sum(set(pair) <= block for block in blocks) for pair in paired_rows]
    ledger_mass = e + 2 * sum(e - codegree for codegree in codegrees)
    require(simple_mass == ledger_mass, "simple-root ledger failed")
    require(all(codegree == 0 for codegree in codegrees), "paired rows are not disjoint")
    require(simple_mass == 3 * e * (2 * e + 1), "no-exception simple-root total failed")
    require(double_mass == 0, "no-exception design has a double root")
    require(2 * double_mass + simple_mass == len(blocks) * (2 * e + 1), "degree ledger failed")


def check_identical_row_exceptions() -> None:
    prime = 97
    n = 24
    generator = pow(5, 4, prime)
    subgroup = sorted({pow(generator, index, prime) for index in range(n)})
    triple = subgroup[:3]
    b_poly = locator(triple, prime)
    sigma_1 = -b_poly[2] % prime
    sigma_2 = b_poly[1]
    sigma_3 = -b_poly[0] % prime

    antipodal_orbits = {
        tuple(sorted((value, -value % prime))) for value in subgroup
    }
    antipodal_exceptions = []
    for left, right in antipodal_orbits:
        u = left * left % prime
        difference = (evaluate(b_poly, left, prime) - evaluate(b_poly, right, prime)) % prime
        predicted = 2 * left * (u + sigma_2) % prime
        require(difference == predicted, "antipodal row-difference identity failed")
        if difference == 0:
            antipodal_exceptions.append(u)
    require(len(set(antipodal_exceptions)) <= 1, "multiple antipodal identical-row orbits")

    c = pow(generator, 3, prime)
    product_orbits = {
        tuple(sorted((value, c * inverse(value, prime) % prime)))
        for value in subgroup
        if value != c * inverse(value, prime) % prime
    }
    product_exceptions = []
    for left, right in product_orbits:
        u = (left + right) % prime
        difference = (
            evaluate(b_poly, left, prime) * inverse(left, prime)
            - evaluate(b_poly, right, prime) * inverse(right, prime)
        ) % prime
        predicted = (left - right) * (u - sigma_1 + sigma_3 * inverse(c, prime)) % prime
        require(difference == predicted, "constant-product row-difference identity failed")
        if difference == 0:
            product_exceptions.append(u)
    require(len(set(product_exceptions)) <= 1, "multiple product identical-row orbits")


def check_official_arithmetic() -> None:
    e = (1 << 38) - 1
    r = 2 * e + 1
    for exceptional in (0, 1):
        simple_mass = e * (6 * e + 3 - 2 * exceptional)
        double_mass = e * exceptional
        require(
            simple_mass + 2 * double_mass == 3 * e * r,
            "official multiplicity total failed",
        )


def main() -> None:
    check_orbit_product()
    check_identical_row_exceptions()
    check_official_arithmetic()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_DISTANCE_THREE_"
        "DIHEDRAL_QUOTIENT_EXTERNAL_PRODUCT_LEDGER_PASS product=1 branches=2"
    )


if __name__ == "__main__":
    main()
