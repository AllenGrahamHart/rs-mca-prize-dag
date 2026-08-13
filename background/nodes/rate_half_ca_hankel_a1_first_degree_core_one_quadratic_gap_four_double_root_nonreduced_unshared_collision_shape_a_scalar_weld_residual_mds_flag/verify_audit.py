#!/usr/bin/env python3
"""Independent interpolation audit of the residual-MDS flag over F_127."""


def invert_matrix(matrix, right, prime):
    size = len(matrix)
    work = [
        [entry % prime for entry in row] + [value % prime]
        for row, value in zip(matrix, right)
    ]
    for column in range(size):
        pivot = next(
            row for row in range(column, size) if work[row][column]
        )
        work[column], work[pivot] = work[pivot], work[column]
        inverse = pow(work[column][column], prime - 2, prime)
        work[column] = [entry * inverse % prime for entry in work[column]]
        for row in range(size):
            if row == column or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [
                (left - scale * pivot_entry) % prime
                for left, pivot_entry in zip(work[row], work[column])
            ]
    return [work[index][-1] for index in range(size)]


def replay():
    prime = 127
    source = list(range(1, 11))
    incidence = source[:3]
    complement = source[3:]
    excess = 2
    padding_degree = 1
    generic_degree = len(incidence) + excess + padding_degree
    row_surplus = len(source) - generic_degree
    parity_start = row_surplus + padding_degree - 1
    assert generic_degree == 6 and parity_start == 4

    degrees = []
    first_parities = []
    for drop in range(excess + 1):
        degree = excess - drop
        values = [pow(point - 40, degree, prime) for point in complement]
        vandermonde = [
            [pow(point, power, prime) for power in range(len(complement))]
            for point in complement
        ]
        coefficients = invert_matrix(vandermonde, values, prime)
        recovered_degree = max(
            index for index, coefficient in enumerate(coefficients)
            if coefficient
        )
        assert recovered_degree == degree
        degrees.append(recovered_degree)

        parities = []
        for power in range(parity_start + drop + 1):
            total = 0
            for index, point in enumerate(complement):
                derivative = 1
                for other in complement:
                    if other != point:
                        derivative = derivative * (point - other) % prime
                total += (
                    values[index]
                    * pow(point, power, prime)
                    * pow(derivative, prime - 2, prime)
                )
            parities.append(total % prime)
        assert parities[:parity_start + drop] == [0] * (
            parity_start + drop
        )
        assert parities[parity_start + drop] == 1
        first_parities.append(parities[parity_start + drop])

    assert degrees == [2, 1, 0]
    assert first_parities == [1, 1, 1]
    return degrees, first_parities


if __name__ == "__main__":
    degrees, first = replay()
    print(
        "RATE_HALF_SHAPE_A_SCALAR_WELD_RESIDUAL_MDS_FLAG_AUDIT_PASS "
        f"degrees={degrees} first={first}"
    )
