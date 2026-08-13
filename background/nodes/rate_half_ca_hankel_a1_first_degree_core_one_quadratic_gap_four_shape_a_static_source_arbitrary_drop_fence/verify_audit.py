#!/usr/bin/env python3
"""Independent residue-form audit of the arbitrary-drop construction."""


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def poly_product(roots, prime):
    coefficients = [1]
    for root in roots:
        next_coefficients = [0] * (len(coefficients) + 1)
        for index, coefficient in enumerate(coefficients):
            next_coefficients[index] = (
                next_coefficients[index] - root * coefficient
            ) % prime
            next_coefficients[index + 1] = (
                next_coefficients[index + 1] + coefficient
            ) % prime
        coefficients = next_coefficients
    return coefficients


def poly_value(coefficients, point, prime):
    total = 0
    power = 1
    for coefficient in coefficients:
        total = (total + coefficient * power) % prime
        power = power * point % prime
    return total


def matrix_rank(matrix, prime):
    reduced = [[entry % prime for entry in row] for row in matrix]
    rank = 0
    for column in range(len(reduced[0])):
        pivot = None
        for row in range(rank, len(reduced)):
            if reduced[row][column]:
                pivot = row
                break
        if pivot is None:
            continue
        reduced[rank], reduced[pivot] = reduced[pivot], reduced[rank]
        inverse = pow(reduced[rank][column], prime - 2, prime)
        for index in range(column, len(reduced[rank])):
            reduced[rank][index] = (
                reduced[rank][index] * inverse
            ) % prime
        for row in range(len(reduced)):
            if row == rank:
                continue
            scale = reduced[row][column]
            if not scale:
                continue
            for index in range(column, len(reduced[row])):
                reduced[row][index] = (
                    reduced[row][index]
                    - scale * reduced[rank][index]
                ) % prime
        rank += 1
    return rank


def determinant(matrix, prime):
    reduced = [[entry % prime for entry in row] for row in matrix]
    value = 1
    for column in range(len(reduced)):
        pivot = None
        for row in range(column, len(reduced)):
            if reduced[row][column]:
                pivot = row
                break
        if pivot is None:
            return 0
        if pivot != column:
            reduced[column], reduced[pivot] = reduced[pivot], reduced[column]
            value = -value
        pivot_value = reduced[column][column]
        value = value * pivot_value % prime
        inverse = pow(pivot_value, prime - 2, prime)
        for row in range(column + 1, len(reduced)):
            scale = reduced[row][column] * inverse % prime
            for index in range(column, len(reduced)):
                reduced[row][index] = (
                    reduced[row][index]
                    - scale * reduced[column][index]
                ) % prime
    return value % prime


def main():
    prime = 127
    d = 4
    n = 2
    source = list(range(2, 10))
    roots = [30, 31, 32, 33]
    auxiliary = 50
    require(len(source) == d + n + 2, "audit source count")

    locator = poly_product(roots, prime)
    source_locator = poly_product(source, prime)
    cases = 0
    pairing_determinants = []

    for drop in range(n + 1):
        residual = poly_product([auxiliary] * (n - drop), prime)
        weights = []
        for point in source:
            l_derivative = 1
            for other in source:
                if other != point:
                    l_derivative = l_derivative * (point - other) % prime
            denominator = (
                poly_value(locator, point, prime) * l_derivative
            ) % prime
            weights.append(
                poly_value(residual, point, prime)
                * pow(denominator, prime - 2, prime)
                % prime
            )
        require(all(weights), "audit nonzero source weights")

        moments = [
            sum(
                weight * pow(point, exponent, prime)
                for point, weight in zip(source, weights)
            ) % prime
            for exponent in range(2 * d + n + 2)
        ]
        middle = [
            [moments[row + column] for column in range(d + 1)]
            for row in range(d + 1)
        ]
        require(matrix_rank(middle, prime) == d, "audit exact corank")

        kernel_values = [
            sum(
                middle[row][column] * locator[column]
                for column in range(d + 1)
            ) % prime
            for row in range(d + 1)
        ]
        require(kernel_values == [0] * (d + 1), "audit kernel")

        defects = []
        for offset in range(drop + 1):
            index = d + 1 + offset
            defects.append(
                sum(
                    locator[column] * moments[index + column]
                    for column in range(d + 1)
                ) % prime
            )
        require(defects[:-1] == [0] * drop, "audit zero run")
        require(defects[-1] == 1, "audit first nonzero")

        residue_matrix = []
        for left in range(d):
            row = []
            for right in range(d):
                value = 0
                for root in roots:
                    q_derivative = 1
                    for other in roots:
                        if other != root:
                            q_derivative = (
                                q_derivative * (root - other)
                            ) % prime
                    denominator = (
                        q_derivative
                        * poly_value(source_locator, root, prime)
                    ) % prime
                    value = (
                        value
                        - poly_value(residual, root, prime)
                        * pow(denominator, prime - 2, prime)
                        * pow(root, left + right, prime)
                    ) % prime
                require(value == moments[left + right],
                        "audit residue/source equality")
                row.append(value)
            residue_matrix.append(row)
        pairing_determinant = determinant(residue_matrix, prime)
        require(pairing_determinant != 0, "audit residue nondegeneracy")
        pairing_determinants.append(pairing_determinant)
        cases += 1

    require(cases == 3, "audit case count")
    print(
        "RATE_HALF_SHAPE_A_STATIC_ARBITRARY_DROP_FENCE_AUDIT_PASS "
        f"cases={cases} determinants={pairing_determinants}"
    )


if __name__ == "__main__":
    main()
