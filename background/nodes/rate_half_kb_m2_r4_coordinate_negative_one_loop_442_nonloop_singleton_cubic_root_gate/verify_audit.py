#!/usr/bin/env python3
"""Independent F_41 witness audit for the cubic-root gate."""


PRIME = 41


def determinant(matrix):
    matrix = [[value % PRIME for value in row] for row in matrix]
    output = 1
    for column in range(4):
        pivot = next((index for index in range(column, 4)
                      if matrix[index][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            output = -output
        value = matrix[column][column]
        output = output*value % PRIME
        inverse = pow(value, -1, PRIME)
        for row in range(column+1, 4):
            scale = matrix[row][column]*inverse % PRIME
            for index in range(column, 4):
                matrix[row][index] = (
                    matrix[row][index]-scale*matrix[column][index]
                ) % PRIME
    return output % PRIME


def main():
    i, b, c, r, t = 9, 10, 5, 12, 30
    if i*i % PRIME != PRIME-1:
        raise RuntimeError("fourth root")
    labels = (1, -1, r*r, t*t, -r*r)
    products = (-b*b, b, -b, c, -c)
    labels = tuple(value % PRIME for value in labels)
    products = tuple(value % PRIME for value in products)
    if len(set(labels)) != 5 or len(set(products)) != 5:
        raise RuntimeError("common guards")
    if len({1, b*b % PRIME, c*c % PRIME}) != 3:
        raise RuntimeError("target guards")

    rows = [[-p, -p*s, 1, s] for p, s in zip(products, labels)]
    for fourth in (3, 4):
        if determinant([rows[index] for index in (0, 1, 2, fourth)]):
            raise RuntimeError("product minor")

    roots = (1, i, r, t, i*r % PRIME)
    q_values = tuple(root*edge_sum % PRIME for root, edge_sum in zip(
        roots, (0, 1+b, 1-b, 1+c, 1-c)
    ))
    differences = tuple((products[0]-value) % PRIME for value in products)
    for third in (3, 4):
        left, right = 1, 2
        weld = (
            q_values[left]*differences[right]*differences[third]
            *(labels[third]-labels[right])
            + q_values[right]*differences[left]*differences[third]
            *(labels[left]-labels[third])
            + q_values[third]*differences[left]*differences[right]
            *(labels[right]-labels[left])
        ) % PRIME
        if weld:
            raise RuntimeError("q weld")
    cubic = r**3+(2+i)*r**2+(-1-2*i)*r-i
    if cubic % PRIME:
        raise RuntimeError("cubic")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_CUBIC_AUDIT_PASS "
        "field=41 witness=guarded_common"
    )


if __name__ == "__main__":
    main()
