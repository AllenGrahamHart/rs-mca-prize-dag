#!/usr/bin/env python3
"""Replay the exact e=7 degree-ledger rank fence over F_211."""

P = 211
GENERATOR = 2


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def multiply(left, right):
    product = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] = (product[i + j] + a * b) % P
    return product


def root_polynomial(roots):
    polynomial = [1]
    for root in roots:
        polynomial = multiply(polynomial, [-root % P, 1])
    return polynomial


def rank(rows):
    pivots = {}
    for source in rows:
        row = source[:]
        for column, pivot in pivots.items():
            if row[column]:
                scale = row[column]
                row = [
                    (left - scale * right) % P
                    for left, right in zip(row, pivot)
                ]
        for column, value in enumerate(row):
            if value:
                inverse = pow(value, P - 2, P)
                pivots[column] = [entry * inverse % P for entry in row]
                break
    return len(pivots)


def fixture():
    require(pow(GENERATOR, 210, P) == 1, "F_211 order")
    require(
        all(pow(GENERATOR, 210 // prime, P) != 1 for prime in (2, 3, 5, 7)),
        "primitive generator",
    )
    values = {pow(GENERATOR, 35 * index, P) for index in range(4)}
    domain = [x for x in range(1, P) if pow(x, 7, P) in values]
    slopes = [0] + [
        delta for delta in range(1, P) if pow(delta, 5, P) in values
    ]
    incidence = [
        {
            index
            for index, delta in enumerate(slopes)
            if pow(delta, 5, P) == pow(x, 7, P)
        }
        for x in domain
    ]
    require(len(values) == 4, "four common values")
    require(len(domain) == 28 and len(slopes) == 21, "grid sizes")
    require({len(row) for row in incidence} == {5}, "row degree five")
    column_degrees = [
        sum(column in row for row in incidence)
        for column in range(len(slopes))
    ]
    require(column_degrees == [0] + [7] * 20, "fiber root degrees")
    return domain, slopes, incidence


def matrix_and_kernel(domain, slopes, incidence):
    excesses = [
        7 - sum(column in row for row in incidence)
        for column in range(len(slopes))
    ]
    require(excesses == [7] + [0] * 20, "excess profile")
    require(sum(excesses) == 7, "total excess")

    slope_weights = []
    for index, slope in enumerate(slopes):
        derivative = 1
        for other_index, other in enumerate(slopes):
            if index != other_index:
                derivative = derivative * (slope - other) % P
        slope_weights.append(pow(derivative, P - 2, P))

    known = []
    columns = []
    kernel = []
    for delta_index, excess in enumerate(excesses):
        roots = [
            domain[row]
            for row in range(len(domain))
            if delta_index in incidence[row]
        ]
        polynomial = root_polynomial(roots)
        require(len(polynomial) - 1 == 7 - excess, "known degree")
        known.append(polynomial)
        for residual_degree in range(excess + 1):
            columns.append((delta_index, residual_degree))
            kernel.append(
                -1 % P
                if (delta_index == 0 and residual_degree == 7)
                or (delta_index != 0 and residual_degree == 0)
                else 0
            )
    require(len(columns) == 28, "4e columns")

    rows = []
    for coefficient in range(8):
        for power in range(15):
            row = []
            for delta_index, residual_degree in columns:
                known_degree = coefficient - residual_degree
                known_coefficient = (
                    known[delta_index][known_degree]
                    if 0 <= known_degree < len(known[delta_index])
                    else 0
                )
                row.append(
                    known_coefficient
                    * pow(slopes[delta_index], power, P)
                    * slope_weights[delta_index]
                    % P
                )
            rows.append(row)
    require(len(rows) == 120, "parity rows")
    return rows, columns, kernel


def replay(mutation=None):
    domain, slopes, incidence = fixture()
    rows, columns, kernel = matrix_and_kernel(domain, slopes, incidence)
    if mutation == "kernel":
        kernel[0] = 1
    elif mutation == "fiber":
        kernel[-1] = 0
    require(
        all(
            sum(left * right for left, right in zip(row, kernel)) % P == 0
            for row in rows
        ),
        "displayed kernel",
    )
    require(rank(rows) == 27, "exact rank 27")
    block_starts = [0] + list(range(8, 28))
    block_widths = [8] + [1] * 20
    require(
        all(
            any(kernel[start : start + width])
            for start, width in zip(block_starts, block_widths)
        ),
        "every polynomial block nonzero",
    )
    for delta_index, delta in enumerate(slopes):
        for x in domain:
            value = (pow(delta, 5, P) - pow(x, 7, P)) % P
            if delta_index == 0:
                reconstructed = -pow(x, 7, P) % P
            else:
                reconstructed = (
                    -(pow(x, 7, P) - pow(delta, 5, P))
                ) % P
            require(value == reconstructed, "fiber factorization")
    return len(rows), len(columns)


def tamper_selftest():
    rejected = 0
    for mutation in ("kernel", "fiber"):
        try:
            replay(mutation)
        except AssertionError:
            rejected += 1
    require(rejected == 2, "hostile mutations")
    return rejected


if __name__ == "__main__":
    row_count, column_count = replay()
    mutations = tamper_selftest()
    print(
        "RATE_HALF_SHAPE_A_ALL_EXCESS_DEGREE_LEDGER_RANK_FENCE_PASS "
        f"matrix={row_count}x{column_count} rank=27 "
        f"blocks=21/21 mutations={mutations}/2"
    )
