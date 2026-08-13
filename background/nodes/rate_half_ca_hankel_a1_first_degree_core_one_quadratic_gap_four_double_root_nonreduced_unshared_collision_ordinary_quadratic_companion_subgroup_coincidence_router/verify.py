#!/usr/bin/env python3
"""Replay the ordinary-quadratic subgroup-coincidence router."""


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def evaluate(coefficients, value, prime):
    total = 0
    for coefficient in reversed(coefficients):
        total = (total * value + coefficient) % prime
    return total


def determinant(matrix, prime):
    work = [[entry % prime for entry in row] for row in matrix]
    value = 1
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[pivot], work[column] = work[column], work[pivot]
            value = -value
        pivot_value = work[column][column]
        value = value * pivot_value % prime
        inverse = pow(pivot_value, -1, prime)
        for row in range(column + 1, len(work)):
            multiplier = work[row][column] * inverse % prime
            for index in range(column, len(work)):
                work[row][index] = (
                    work[row][index] - multiplier * work[column][index]
                ) % prime
    return value % prime


def quadratic_resultant(first, second, prime):
    a, b, c = first
    A, B, C = second
    return determinant(
        [
            [a, b, c, 0],
            [0, a, b, c],
            [A, B, C, 0],
            [0, A, B, C],
        ],
        prime,
    )


def add_term(polynomial, monomial, value):
    polynomial[monomial] = polynomial.get(monomial, 0) + value
    if polynomial[monomial] == 0:
        del polynomial[monomial]


def divided_wedge(left, right):
    raw = {}
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            add_term(raw, (i, j), left_value * right_value)
            add_term(raw, (j, i), -left_value * right_value)

    quotient = {}
    while raw:
        maximum_x = max(i for i, _ in raw)
        leading = sorted(
            ((j, value) for (i, j), value in raw.items() if i == maximum_x),
            reverse=True,
        )
        if maximum_x == 0:
            require(all(value == 0 for _, value in leading), "wedge remainder")
            break
        for y_degree, value in leading:
            add_term(quotient, (maximum_x - 1, y_degree), value)
            add_term(raw, (maximum_x, y_degree), -value)
            add_term(raw, (maximum_x - 1, y_degree + 1), value)
    return quotient


def multiply(left, right):
    product = {}
    for (i, j), left_value in left.items():
        for (k, ell), right_value in right.items():
            add_term(product, (i + k, j + ell), left_value * right_value)
    return product


def subtract(left, right):
    difference = dict(left)
    for monomial, value in right.items():
        add_term(difference, monomial, -value)
    return difference


N = 2**41
e = (2**39 + 1) // 3
gamma_size = 3 * e
R = (9 * e - 7) // 2
incidences = 2 * R
defect = 3 * gamma_size - incidences
full_fibers = gamma_size - defect
pair_floor = 3 * full_fibers

require(3 * e == 2**39 + 1, "first-degree row")
require(R == 824633720830, "classified-row count")
require(incidences == 9 * e - 7, "incidence total")
require(defect == 7, "vertical defect")
require(full_fibers == 2**39 - 6, "full-fiber floor")
require(pair_floor == 1649267441646, "off-diagonal pair floor")

s3_constant = 16 * 4 * 4**2 * (4 + 4)
c3_constant = 16 * 2 * 2**2 * (2 + 2)
require(s3_constant == 8192, "S3 subgroup constant")
require(c3_constant == 512, "C3 subgroup constant")
require(s3_constant**3 * N**2 < pair_floor**3, "S3 strict margin")
require(c3_constant**3 * N**2 < (pair_floor // 2) ** 3, "C3 strict margin")
require(10000 * (4 * 4) ** 3 < N**2, "lower subgroup-size hypothesis")
require((3 * N) ** 4 < (2**167) ** 3, "upper subgroup-size hypothesis")
require(2 * R > 3, "geometric split intersection contradiction")
require(pair_floor // 2 > 8, "Frobenius exchange contradiction")

fixtures = (
    ((1, 2, 0, 1), (3, 1, 4, 1), (2, 0, 5, 2)),
    ((2, 1, 3, 2), (1, 4, 0, 3), (5, 2, 1, 1)),
    ((4, 0, 2, 1), (2, 3, 1, 2), (1, 5, 2, 3)),
)

checks = 18
hostile_difference = False
for coefficient_fixture in fixtures:
    a_coefficients, b_coefficients, c_coefficients = coefficient_fixture
    A_poly = divided_wedge(a_coefficients, b_coefficients)
    B_poly = divided_wedge(a_coefficients, c_coefficients)
    C_poly = divided_wedge(b_coefficients, c_coefficients)
    K_poly = subtract(multiply(B_poly, B_poly), multiply(A_poly, C_poly))
    K_hostile = subtract(multiply(B_poly, B_poly), {
        monomial: -value for monomial, value in multiply(A_poly, C_poly).items()
    })
    require(max(i for i, _ in A_poly) <= 2, "A X-degree")
    require(max(j for _, j in A_poly) <= 2, "A Y-degree")
    require(max(i for i, _ in B_poly) <= 2, "B X-degree")
    require(max(j for _, j in B_poly) <= 2, "B Y-degree")
    require(max(i for i, _ in C_poly) <= 2, "C X-degree")
    require(max(j for _, j in C_poly) <= 2, "C Y-degree")
    require(max(i for i, _ in K_poly) <= 4, "K X-degree")
    require(max(j for _, j in K_poly) <= 4, "K Y-degree")
    hostile_difference |= K_poly != K_hostile
    checks += 9

    for prime in (101, 127):
        for x_value in range(1, 12):
            for y_value in range(13, 24):
                first = tuple(
                    evaluate(coefficients, x_value, prime)
                    for coefficients in coefficient_fixture
                )
                second = tuple(
                    evaluate(coefficients, y_value, prime)
                    for coefficients in coefficient_fixture
                )
                raw_resultant = quadratic_resultant(first, second, prime)
                delta = (x_value - y_value) % prime
                raw_ab = (first[0] * second[1] - second[0] * first[1]) % prime
                raw_ac = (first[0] * second[2] - second[0] * first[2]) % prime
                raw_bc = (first[1] * second[2] - second[1] * first[2]) % prime
                divided_resultant = (
                    (raw_ac * pow(delta, -1, prime)) ** 2
                    - (raw_ab * pow(delta, -1, prime))
                    * (raw_bc * pow(delta, -1, prime))
                ) % prime
                require(
                    raw_resultant == delta**2 * divided_resultant % prime,
                    "divided quadratic resultant",
                )
                common_root = any(
                    (first[0] * t * t + first[1] * t + first[2]) % prime == 0
                    and (second[0] * t * t + second[1] * t + second[2]) % prime == 0
                    for t in range(prime)
                )
                require((raw_resultant == 0) == common_root, "common-root test")
                checks += 2

require(hostile_difference, "hostile resultant sign mutation")
checks += 1

print(f"RATE_HALF_QUADRATIC_SUBGROUP_COINCIDENCE_PASS checks={checks}")
