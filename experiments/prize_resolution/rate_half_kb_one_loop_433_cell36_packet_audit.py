#!/usr/bin/env python3
"""Independent replay of the sixteen deployed one-loop 433 packets."""

import itertools


P = 2130706433
IOTA = 16711679
B_ROOTS = (1375161449, 477266026)
C_ROOTS = {
    1375161449: 1621120540,
    477266026: 1039843884,
}
R_ROWS = {
    (1, 1): 669515297,
    (1, -1): 1125500162,
    (-1, 1): 1461191136,
    (-1, -1): 1005206271,
}
T_ROWS = {
    (1, 1): 639982870,
    (1, -1): 1732861855,
    (-1, 1): 1490723563,
    (-1, -1): 397844578,
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def determinant(matrix):
    work = [[value % P for value in row] for row in matrix]
    output = 1
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work))
             if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            output = -output
        pivot_value = work[column][column]
        output = output*pivot_value % P
        inverse = pow(pivot_value, -1, P)
        for row in range(column+1, len(work)):
            multiplier = work[row][column]*inverse % P
            for index in range(column, len(work)):
                work[row][index] = (
                    work[row][index]-multiplier*work[column][index]
                ) % P
    return output % P


def weld(labels, products, q_values, third):
    left, right = 1, 2
    d_left = (products[0]-products[left]) % P
    d_right = (products[0]-products[right]) % P
    d_third = (products[0]-products[third]) % P
    return (
        q_values[left]*d_right*d_third*(labels[third]-labels[right])
        +q_values[right]*d_left*d_third*(labels[left]-labels[third])
        +q_values[third]*d_left*d_right*(labels[right]-labels[left])
    ) % P


def check_packet(roots, products):
    labels = tuple(root*root % P for root in roots)
    require(0 not in labels and len(set(labels)) == 5, "label guard")
    require(0 not in products and len(set(products)) == 5, "product guard")
    sums = (0, 1+products[1], 1+products[2],
            products[1]+products[2], products[1]-products[2])
    q_values = tuple(
        root*edge_sum % P for root, edge_sum in zip(roots, sums)
    )
    rows = [
        (-product % P, -product*label % P, 1, label)
        for product, label in zip(products, labels)
    ]
    for third in (3, 4):
        require(
            determinant([rows[0], rows[1], rows[2], rows[third]]) == 0,
            "product minor",
        )
        require(weld(labels, products, q_values, third) == 0, "q weld")


def main():
    require(IOTA*IOTA % P == P-1, "fourth root")
    count = 0
    seen = set()
    for epsilon_1, epsilon_2 in itertools.product((1, -1), repeat=2):
        r = R_ROWS[(epsilon_1, epsilon_2)]
        t = T_ROWS[(epsilon_1, epsilon_2)]
        for b in B_ROOTS:
            c = C_ROOTS[b]
            require((b*b+278278958*b+1) % P == 0, "b polynomial")

            roots3 = (
                1, t, epsilon_1*IOTA % P,
                r, epsilon_2*IOTA*r % P,
            )
            products3 = (P-1, b, c, b*c % P, -b*c % P)
            check_packet(roots3, products3)
            seen.add((3, epsilon_1, epsilon_2, b, c, r, t))
            count += 1

            roots6 = (
                1, epsilon_1*IOTA % P, t,
                r, -epsilon_2*IOTA*r % P,
            )
            products6 = (P-1, c, b, b*c % P, -b*c % P)
            check_packet(roots6, products6)
            seen.add((6, epsilon_1, -epsilon_2, c, b, r, t))
            count += 1

    require(count == 16 and len(seen) == 16, "packet count")
    print(
        "RATE_HALF_KB_ONE_LOOP_433_CELL36_PACKET_AUDIT_PASS "
        "cell3=8 cell6=8 total=16"
    )


if __name__ == "__main__":
    main()
